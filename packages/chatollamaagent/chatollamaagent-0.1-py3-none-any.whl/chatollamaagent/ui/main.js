// Global variables
let ws = null;
const statusElement = document.getElementById('status');
const nodeCategoriesElement = document.getElementById('nodeCategories');
const nodeContainer = document.getElementById('nodeContainer');
const nodeEditor = document.getElementById('nodeEditor');
let connectionsContainer = null;  // Will be initialized in setupNodeEditor
let tempConnectionsContainer = null;  // Container for temporary connections
let activeConnection = null;
const connections = new Map();
const nodes = new Map();
const selectedNodes = new Set();
let isPanning = false;
let panStartX = 0;
let panStartY = 0;
let editorTranslateX = 0;
let editorTranslateY = 0;
let editorContent = null;  // Will hold all editor content
let isSlicing = false;
let sliceStartX = 0;
let sliceStartY = 0;
let sliceLine = null;
let rightClickStartTime = 0;
let activeFlowConnection = null;

// Initialize the node editor and connections container immediately
function initializeEditor() {
    // Create a content container for all editor elements
    editorContent = document.createElement('div');
    editorContent.className = 'editor-content';
    editorContent.style.position = 'absolute';
    editorContent.style.top = '0';
    editorContent.style.left = '0';
    editorContent.style.width = '100%';
    editorContent.style.height = '100%';
    editorContent.style.transformOrigin = '0 0';
    
    // Set nodeEditor as viewport
    nodeEditor.style.position = 'relative';
    nodeEditor.style.overflow = 'hidden';
    nodeEditor.appendChild(editorContent);
    
    // Create permanent connections container - keep it fixed
    connectionsContainer = document.createElement('div');
    connectionsContainer.className = 'connections';
    connectionsContainer.style.position = 'absolute';
    connectionsContainer.style.top = '0';
    connectionsContainer.style.left = '0';
    connectionsContainer.style.width = '100%';
    connectionsContainer.style.height = '100%';
    connectionsContainer.style.pointerEvents = 'none';
    connectionsContainer.style.zIndex = '1'; // Behind nodes
    nodeEditor.appendChild(connectionsContainer); // Attach to nodeEditor instead of editorContent
    
    // Create single SVG for permanent connections
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.width = '100%';
    svg.style.height = '100%';
    svg.style.pointerEvents = 'none';
    connectionsContainer.appendChild(svg);
    
    // Create temporary connections container - keep it fixed
    tempConnectionsContainer = document.createElement('div');
    tempConnectionsContainer.className = 'temp-connections';
    tempConnectionsContainer.style.position = 'absolute';
    tempConnectionsContainer.style.top = '0';
    tempConnectionsContainer.style.left = '0';
    tempConnectionsContainer.style.width = '100%';
    tempConnectionsContainer.style.height = '100%';
    tempConnectionsContainer.style.pointerEvents = 'none';
    tempConnectionsContainer.style.zIndex = '1000'; // Above nodes
    nodeEditor.appendChild(tempConnectionsContainer); // Attach to nodeEditor instead of editorContent
    
    // Add nodeContainer to the movable content
    editorContent.appendChild(nodeContainer);
    
    // Add panning event listeners to the node editor
    nodeEditor.addEventListener('mousedown', startPanning);
    document.addEventListener('mousemove', updatePanning);
    document.addEventListener('mouseup', stopPanning);
    nodeEditor.addEventListener('mouseleave', stopPanning);
    
    // Prevent middle-click scroll behavior
    nodeEditor.addEventListener('mousedown', (e) => {
        if (e.button === 1) {
            e.preventDefault();
        }
    });
    
    // Add click handler to the node editor background
    nodeEditor.addEventListener('click', (e) => {
        console.log('Click target:', e.target);
        // Only deselect if clicking directly on the editor or grid
        if (e.target === nodeEditor || e.target === connectionsContainer) {
            console.log('Clearing node selection');
            selectedNodes.forEach(node => {
                node.classList.remove('selected');
            });
            selectedNodes.clear();
        }
    });
    
    // Setup node editor event listeners
    nodeEditor.addEventListener('dragenter', (e) => {
        e.preventDefault();
        console.log('Drag enter node editor');
        nodeEditor.classList.add('drag-over');
    });
    
    nodeEditor.addEventListener('dragleave', (e) => {
        e.preventDefault();
        if (!nodeEditor.contains(e.relatedTarget)) {
            console.log('Drag leave node editor');
            nodeEditor.classList.remove('drag-over');
        }
    });
    
    nodeEditor.addEventListener('dragover', (e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    });
    
    nodeEditor.addEventListener('drop', (e) => {
        e.preventDefault();
        e.stopPropagation();
        nodeEditor.classList.remove('drag-over');
        
        const nodeType = e.dataTransfer.getData('node-type');
        console.log('Drop event:', { nodeType, wsState: ws?.readyState });
        
        if (nodeType && ws && ws.readyState === WebSocket.OPEN) {
            const rect = nodeEditor.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const message = {
                type: 'create_node',
                node_type: nodeType,
                position: [x, y]
            };
            console.log('Sending create_node message:', message);
            ws.send(JSON.stringify(message));
        }
    });
    
    // Add right-click handling
    nodeEditor.addEventListener('contextmenu', (e) => {
        e.preventDefault(); // Prevent default context menu
    });
    
    nodeEditor.addEventListener('mousedown', startSlicing);
}

// Call initialization immediately
initializeEditor(); 

// Add connection handling functions
function startConnection(nodeId, socketName, isInput, event) {
    if (activeConnection) return;
    
    const dot = event.target;
    const rect = dot.getBoundingClientRect();
    const editorRect = nodeEditor.getBoundingClientRect();
    
    // Calculate start position relative to editor, matching node visual position
    activeConnection = {
        nodeId,
        socketName,
        isInput,
        startX: rect.left - editorRect.left + (rect.width / 2),
        startY: rect.top - editorRect.top + (rect.height / 2),
        socketColor: dot.style.backgroundColor
    };
    
    // Create temporary SVG connection
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.width = '100%';
    svg.style.height = '100%';
    svg.style.pointerEvents = 'none';
    svg.classList.add('connection', 'active');
    
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.classList.add('connection-path');
    path.style.stroke = activeConnection.socketColor;
    svg.appendChild(path);
    
    tempConnectionsContainer.appendChild(svg);
    activeConnection.element = svg;
    
    document.addEventListener('mousemove', updateConnection);
    document.addEventListener('mouseup', cancelConnection);
}

function updateConnection(event) {
    if (!activeConnection) return;
    
    const editorRect = nodeEditor.getBoundingClientRect();
    // Calculate end position relative to editor, matching mouse visual position
    const endX = event.clientX - editorRect.left;
    const endY = event.clientY - editorRect.top;
    
    const path = activeConnection.element.querySelector('path');
    const dx = endX - activeConnection.startX;
    const bezierX = Math.abs(dx) * 0.5;
    
    const d = `M ${activeConnection.startX} ${activeConnection.startY} 
               C ${activeConnection.startX + bezierX} ${activeConnection.startY},
                 ${endX - bezierX} ${endY},
                 ${endX} ${endY}`;
    
    path.setAttribute('d', d);
}

function cancelConnection(event) {
    // Only cancel if we're not over a socket dot
    if (!event.target.classList.contains('socket-dot')) {
        console.log('Cancelling connection');
        if (activeConnection && activeConnection.element) {
            activeConnection.element.remove();
        }
        document.removeEventListener('mousemove', updateConnection);
        document.removeEventListener('mouseup', cancelConnection);
        activeConnection = null;
        
        // Remove connecting class from all dots
        document.querySelectorAll('.socket-dot').forEach(dot => {
            dot.classList.remove('connecting');
        });
    }
}

function setupSocketDot(dot, nodeId, socketName, isInput) {
    console.log('Setting up socket dot:', { nodeId, socketName, isInput });
    
    dot.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        startConnection(nodeId, socketName, isInput, e);
    });
    
    dot.addEventListener('mouseup', (e) => {
        e.stopPropagation();
        endConnection(nodeId, socketName, isInput);
    });
    
    dot.addEventListener('mouseenter', (e) => {
        if (activeConnection && activeConnection.isInput !== isInput) {
            dot.classList.add('connecting');
        }
    });
    
    dot.addEventListener('mouseleave', (e) => {
        dot.classList.remove('connecting');
    });
}

// Add this function to create SVG paths for connections
function createConnection(fromNodeId, fromSocket, toNodeId, toSocket, isFlow = false) {
    const connectionId = `${fromNodeId}-${fromSocket}-${toNodeId}-${toSocket}`;
    
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.classList.add('connection-path');
    if (isFlow) {
        path.classList.add('flow');
    }
    
    // Use the existing SVG in connectionsContainer
    const svg = connectionsContainer.querySelector('svg');
    svg.appendChild(path);
    
    const connection = {
        fromNode: fromNodeId,
        fromSocket,
        toNode: toNodeId,
        toSocket,
        path,
        isFlow
    };
    
    connections.set(connectionId, connection);
    updateConnectionPath(connection);
    
    return connection;
}

function createNodeElement(nodeId, nodeData) {
    console.log('Creating node element with data:', { nodeId, nodeData });
    const node = document.createElement('div');
    node.id = nodeId;
    node.className = 'node';
    node.style.left = `${nodeData.position[0]}px`;
    node.style.top = `${nodeData.position[1]}px`;
    node.style.zIndex = '100';
    
    // Create node header
    const header = document.createElement('div');
    header.className = 'node-header';
    header.innerHTML = `<h3 class="node-title">${nodeData.type}</h3>`;
    node.appendChild(header);
    
    // Create node content
    const content = document.createElement('div');
    content.className = 'node-content';
    
    // Create flow connection points container
    const flowContainer = document.createElement('div');
    flowContainer.className = 'flow-connections';
    
    // Add flow input
    const flowInput = document.createElement('div');
    flowInput.className = 'flow-dot input';
    flowContainer.appendChild(flowInput);
    
    // Add flow output
    const flowOutput = document.createElement('div');
    flowOutput.className = 'flow-dot output';
    flowContainer.appendChild(flowOutput);
    
    content.appendChild(flowContainer);
    
    // Create sockets container
    const socketsContainer = document.createElement('div');
    socketsContainer.className = 'node-sockets';
    
    // Add input sockets
    Object.entries(nodeData.inputs).forEach(([name, socket]) => {
        const socketEl = createSocketElement(name, true, socket);
        socketsContainer.appendChild(socketEl);
    });
    
    // Add output sockets
    Object.entries(nodeData.outputs).forEach(([name, socket]) => {
        const socketEl = createSocketElement(name, false, socket);
        socketsContainer.appendChild(socketEl);
    });
    
    content.appendChild(socketsContainer);
    node.appendChild(content);
    
    // Setup flow connection handlers
    setupFlowDot(flowInput, nodeId, true);
    setupFlowDot(flowOutput, nodeId, false);
    
    // Make node draggable
    makeNodeDraggable(node);
    
    // Setup socket connections
    setTimeout(() => {
        node.querySelectorAll('.socket-dot').forEach(dot => {
            const isInput = dot.parentElement.classList.contains('input');
            setupSocketDot(dot, nodeId, dot.dataset.socketName, isInput);
        });
    }, 0);
    
    return node;
}

function setupFlowDot(dot, nodeId, isInput) {
    dot.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        startFlowConnection(nodeId, isInput, e);
    });
    
    dot.addEventListener('mouseup', (e) => {
        e.stopPropagation();
        endFlowConnection(nodeId, isInput);
    });
    
    dot.addEventListener('mouseenter', (e) => {
        if (activeFlowConnection && activeFlowConnection.isInput !== isInput) {
            dot.classList.add('connecting');
        }
    });
    
    dot.addEventListener('mouseleave', (e) => {
        dot.classList.remove('connecting');
    });
}

function handleNodeCreated(nodeId, nodeData) {
    console.log('Creating node element:', { nodeId, nodeData });
    const nodeElement = createNodeElement(nodeId, nodeData);
    console.log('Created node element:', nodeElement);
    nodeContainer.appendChild(nodeElement);  // Changed from nodeEditor to nodeContainer
    nodes.set(nodeId, nodeData);
    console.log('Current nodes:', nodes);
}

function handleConnectionMade(fromNode, fromSocket, toNode, toSocket) {
    console.log('=== Creating New Connection ===');
    console.log('Connection details:', { fromNode, fromSocket, toNode, toSocket });
    
    const connectionId = `${fromNode}:${fromSocket}-${toNode}:${toSocket}`;
    
    // Check if we already have this connection (from endConnection)
    let connection = connections.get(connectionId);
    if (connection) {
        console.log('Connection already exists, updating it');
        updateConnectionLine(connectionId);
        return;
    }
    
    // If we don't have the connection yet, create it
    const svg = connectionsContainer.querySelector('svg');
    if (!svg) {
        console.error('SVG container not found!');
        return;
    }
    
    // Create path for this connection
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.classList.add('connection-path');
    
    // Get socket color from the output socket
    const fromNodeEl = document.getElementById(fromNode);
    const outputDot = fromNodeEl?.querySelector(`[data-socket-name="${fromSocket}"]`);
    const socketColor = outputDot?.style.backgroundColor || '#4CAF50';
    
    // Set initial path styles
    path.style.stroke = socketColor;
    path.style.strokeWidth = '2px';
    path.style.fill = 'none';
    
    svg.appendChild(path);
    
    // Store connection data
    connections.set(connectionId, {
        path,
        fromNode,
        fromSocket,
        toNode,
        toSocket,
        color: socketColor
    });
    
    // Initial update of the connection line
    updateConnectionLine(connectionId);
    
    // Verify the connection was created properly
    console.log('Connection created:', {
        exists: connections.has(connectionId),
        pathInDom: path.parentNode === svg,
        connectionData: connections.get(connectionId)
    });
}

function updateConnectionLine(connectionId) {
    const connection = connections.get(connectionId);
    if (!connection) return;
    
    const fromNode = document.getElementById(connection.fromNode);
    const toNode = document.getElementById(connection.toNode);
    if (!fromNode || !toNode) return;
    
    const outputDot = fromNode.querySelector(`[data-socket-name="${connection.fromSocket}"]`);
    const inputDot = toNode.querySelector(`[data-socket-name="${connection.toSocket}"]`);
    if (!outputDot || !inputDot) return;
    
    const editorRect = nodeEditor.getBoundingClientRect();
    const fromRect = outputDot.getBoundingClientRect();
    const toRect = inputDot.getBoundingClientRect();
    
    // Calculate positions relative to the editor
    // Since SVG container is fixed, we need to add the translation to match node positions
    const x1 = fromRect.left - editorRect.left + (fromRect.width / 2);
    const y1 = fromRect.top - editorRect.top + (fromRect.height / 2);
    const x2 = toRect.left - editorRect.left + (toRect.width / 2);
    const y2 = toRect.top - editorRect.top + (toRect.height / 2);
    
    const dx = x2 - x1;
    const bezierX = Math.abs(dx) * 0.5;
    
    const d = `M ${x1} ${y1} C ${x1 + bezierX} ${y1}, ${x2 - bezierX} ${y2}, ${x2} ${y2}`;
    connection.path.setAttribute('d', d);
}

function createSocketElement(name, isInput, socketData) {
    console.log('Creating socket element:', { name, isInput, socketData });
    const socket = document.createElement('div');
    socket.className = `socket ${isInput ? 'input' : 'output'}`;
    
    const dot = document.createElement('div');
    dot.className = 'socket-dot';
    dot.dataset.socketName = name;
    dot.dataset.socketType = socketData.type;
    
    // Apply socket color
    const socketColor = socketData.type === 'FloatSocket' ? '#4CAF50' : '#666666';
    console.log('Setting socket color:', socketColor);
    dot.style.setProperty('--socket-color', socketColor);
    dot.style.backgroundColor = socketColor;
    dot.style.borderColor = socketColor;
    
    const label = document.createElement('span');
    label.className = 'socket-label';
    label.textContent = name;
    
    if (isInput) {
        socket.appendChild(dot);
        socket.appendChild(label);
    } else {
        socket.appendChild(label);
        socket.appendChild(dot);
    }
    
    return socket;
}

function makeNodeDraggable(nodeElement) {
    console.log('Setting up draggable behavior for node:', nodeElement.id);
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    let isDragging = false;
    const header = nodeElement.querySelector('.node-header');
    
    // Add click handler for selection
    nodeElement.addEventListener('mousedown', (e) => {
        if (!e.target.classList.contains('socket-dot')) {
            selectNode(nodeElement, e.shiftKey);
        }
    });
    
    header.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e.preventDefault();
        console.log('Mouse down on node:', nodeElement.id);
        
        // If clicking an unselected node without shift, select only this node
        if (!nodeElement.classList.contains('selected')) {
            selectNode(nodeElement, e.shiftKey);
        }
        
        // Get initial positions for all selected nodes
        selectedNodes.forEach(node => {
            node.initialX = node.offsetLeft;
            node.initialY = node.offsetTop;
        });
        
        // Get mouse position at startup
        pos3 = e.clientX;
        pos4 = e.clientY;
        isDragging = true;
        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        if (!isDragging) return;
        e.preventDefault();
        
        // Calculate movement delta
        const dx = e.clientX - pos3;
        const dy = e.clientY - pos4;
        
        console.log('=== Node Drag Event ===');
        console.log('Movement delta:', { dx, dy });
        
        // Move all selected nodes
        selectedNodes.forEach(node => {
            const newLeft = node.initialX + dx;
            const newTop = node.initialY + dy;
            console.log('Moving node:', { id: node.id, newLeft, newTop });
            node.style.left = newLeft + "px";
            node.style.top = newTop + "px";
            
            // Update connections for this node
            connections.forEach((conn, id) => {
                if (conn.fromNode === node.id || conn.toNode === node.id) {
                    console.log('Updating connection for moved node:', {
                        connectionId: id,
                        nodeId: node.id,
                        isSource: conn.fromNode === node.id,
                        isTarget: conn.toNode === node.id
                    });
                    updateConnectionLine(id);
                }
            });
        });
        
        // Force a repaint of the connections container
        connectionsContainer.style.display = 'none';
        connectionsContainer.offsetHeight; // Force reflow
        connectionsContainer.style.display = 'block';
    }

    function closeDragElement() {
        if (!isDragging) return;
        console.log('Finished dragging selected nodes');
        isDragging = false;
        document.onmouseup = null;
        document.onmousemove = null;
        
        // Send position updates for all selected nodes
        if (ws && ws.readyState === WebSocket.OPEN) {
            selectedNodes.forEach(node => {
                const position = [node.offsetLeft, node.offsetTop];
                console.log('Sending position update:', { nodeId: node.id, position });
                ws.send(JSON.stringify({
                    type: 'update_node_position',
                    node_id: node.id,
                    position: position
                }));
            });
        }
    }
}

function selectNode(nodeElement, addToSelection = false) {
    if (!addToSelection) {
        // Clear other selections if not adding to selection
        selectedNodes.forEach(node => {
            node.classList.remove('selected');
        });
        selectedNodes.clear();
    }
    
    nodeElement.classList.add('selected');
    selectedNodes.add(nodeElement);
    console.log('Selected nodes:', selectedNodes);
} 

function connectWebSocket() {
    ws = new WebSocket('ws://localhost:8765');

    ws.onopen = () => {
        updateStatus('Connected', 'connected');
    };

    ws.onclose = () => {
        updateStatus('Disconnected', 'disconnected');
    };

    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        updateStatus('Error connecting', 'error');
    };

    ws.onmessage = (event) => {
        const message = JSON.parse(event.data);
        console.log('Received message:', message);
        
        switch (message.type) {
            case 'node_registry':
                handleNodeRegistry(message.nodes);
                break;
            case 'node_created':
                handleNodeCreated(message.node_id, message.node_data);
                break;
            case 'node_removed':
                handleNodeRemoved(message.node_id);
                break;
            case 'connection_made':
                // Fix parameter order to match server response
                handleConnectionMade(
                    message.from_node,  // Changed from message.node_id
                    message.from_socket, // Changed from message.socket1
                    message.to_node,    // Added
                    message.to_socket   // Changed from message.socket2
                );
                break;
            case 'connection_removed':
                handleConnectionRemoved(message.node_id, message.socket);
                break;
            case 'node_executed':
                handleNodeExecuted(message.node_id, message.outputs);
                break;
        }
    };
}

function updateStatus(message, type) {
    statusElement.textContent = `Status: ${message}`;
    statusElement.className = 'alert';
    
    switch(type) {
        case 'connected':
            statusElement.classList.add('alert-success');
            break;
        case 'disconnected':
            statusElement.classList.add('alert-danger');
            break;
        case 'error':
            statusElement.classList.add('alert-danger');
            break;
        default:
            statusElement.classList.add('alert-info');
    }
}

function handleNodeRegistry(nodeTypes) {
    console.log('Received node registry:', nodeTypes);
    // Update node palette with available node types
    const palette = document.getElementById('nodeCategories');
    palette.innerHTML = ''; // Clear existing content
    
    // Group nodes by category
    const categories = {};
    nodeTypes.forEach(node => {
        console.log('Processing node:', node);
        const category = node.category || 'General';
        if (!categories[category]) {
            categories[category] = [];
        }
        categories[category].push(node);
    });
    
    console.log('Categorized nodes:', categories);
    
    // Create category sections
    Object.entries(categories).forEach(([category, nodes]) => {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'node-category';
        
        const titleDiv = document.createElement('div');
        titleDiv.className = 'node-category-title';
        titleDiv.textContent = category;
        categoryDiv.appendChild(titleDiv);
        
        const nodesDiv = document.createElement('div');
        nodesDiv.className = 'node-category-items';
        
        nodes.forEach(node => {
            console.log('Creating node item:', node);
            const nodeItem = document.createElement('div');
            nodeItem.className = 'node-item';
            nodeItem.draggable = true;
            nodeItem.dataset.nodeType = node.type;
            nodeItem.textContent = node.title || node.type;
            nodeItem.addEventListener('dragstart', handleDragStart);
            nodesDiv.appendChild(nodeItem);
        });
        
        categoryDiv.appendChild(nodesDiv);
        palette.appendChild(categoryDiv);
    });
}

function handleNodeRemoved(nodeId) {
    const nodeElement = document.getElementById(nodeId);
    if (nodeElement) {
        nodeElement.remove();
        nodes.delete(nodeId);
    }
}

function handleConnectionRemoved(nodeId, socket) {
    // TODO: Implement connection removal visualization
}

function handleNodeExecuted(nodeId, outputs) {
    // TODO: Update node output displays
}

// Add this function near the top with other event handlers
function handleDragStart(event) {
    console.log('Drag started:', event.target.dataset.nodeType);
    event.dataTransfer.setData('node-type', event.target.dataset.nodeType);
    event.dataTransfer.effectAllowed = 'move';
}

function endConnection(nodeId, socketName, isInput) {
    if (!activeConnection) return;
    
    if (activeConnection.isInput !== isInput && 
        activeConnection.nodeId !== nodeId) {
        // Valid connection, send to server
        const fromNode = isInput ? activeConnection.nodeId : nodeId;
        const fromSocket = isInput ? activeConnection.socketName : socketName;
        const toNode = isInput ? nodeId : activeConnection.nodeId;
        const toSocket = isInput ? socketName : activeConnection.socketName;
        
        console.log('Making connection:', {
            from_node: fromNode,
            from_socket: fromSocket,
            to_node: toNode,
            to_socket: toSocket
        });
        
        // Keep reference to the temporary path
        const tempPath = activeConnection.element.querySelector('path');
        tempPath.classList.add('connection-path');
        
        // Store connection data immediately with the existing path
        const connectionId = `${fromNode}:${fromSocket}-${toNode}:${toSocket}`;
        connections.set(connectionId, {
            path: tempPath,
            fromNode,
            fromSocket,
            toNode,
            toSocket,
            color: activeConnection.socketColor
        });
        
        // Move the path to the main SVG
        const mainSvg = connectionsContainer.querySelector('svg');
        mainSvg.appendChild(tempPath);
        
        // Remove the temporary SVG container but keep the path
        activeConnection.element.remove();
        
        ws.send(JSON.stringify({
            type: 'connect_nodes',
            from_node: fromNode,
            from_socket: fromSocket,
            to_node: toNode,
            to_socket: toSocket
        }));
        
        // Update the connection line immediately
        updateConnectionLine(connectionId);
    } else {
        // Invalid connection, remove temporary connection
        if (activeConnection.element) {
            activeConnection.element.remove();
        }
    }
    
    document.removeEventListener('mousemove', updateConnection);
    document.removeEventListener('mouseup', cancelConnection);
    activeConnection = null;
    
    // Remove connecting class from all dots
    document.querySelectorAll('.socket-dot').forEach(dot => {
        dot.classList.remove('connecting');
    });
}

// Initial connection
connectWebSocket();

// Handle page unload
window.addEventListener('beforeunload', () => {
    if (ws) {
        ws.close();
    }
}); 

// Add a function to dump connection state for debugging
function dumpConnectionState() {
    console.log('Current connections:', {
        size: connections.size,
        connections: Array.from(connections.entries()).map(([id, conn]) => ({
            id,
            fromNode: conn.fromNode,
            fromSocket: conn.fromSocket,
            toNode: conn.toNode,
            toSocket: conn.toSocket
        }))
    });
} 

// Add these functions after initializeEditor
function startPanning(e) {
    // Middle mouse button (button 1)
    if (e.button === 1) {
        e.preventDefault();
        isPanning = true;
        panStartX = e.clientX - editorTranslateX;
        panStartY = e.clientY - editorTranslateY;
        nodeEditor.style.cursor = 'grabbing';
    }
}

function updatePanning(e) {
    if (!isPanning) return;
    e.preventDefault();
    
    editorTranslateX = e.clientX - panStartX;
    editorTranslateY = e.clientY - panStartY;
    
    // Update the transform of the content container
    editorContent.style.transform = `translate(${editorTranslateX}px, ${editorTranslateY}px)`;
    
    // Update all connection positions
    connections.forEach((_, id) => updateConnectionLine(id));
}

function stopPanning(e) {
    if (isPanning) {
        isPanning = false;
        nodeEditor.style.cursor = 'default';
    }
} 

function startSlicing(e) {
    if (e.button === 2) { // Right mouse button
        e.preventDefault();
        rightClickStartTime = Date.now();
        
        const editorRect = nodeEditor.getBoundingClientRect();
        // Calculate slice position relative to editor, matching visual position
        sliceStartX = e.clientX - editorRect.left;
        sliceStartY = e.clientY - editorRect.top;
        
        // Create slice line
        sliceLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        sliceLine.setAttribute('x1', sliceStartX);
        sliceLine.setAttribute('y1', sliceStartY);
        sliceLine.setAttribute('x2', sliceStartX);
        sliceLine.setAttribute('y2', sliceStartY);
        sliceLine.style.stroke = '#ff0000';
        sliceLine.style.strokeWidth = '2';
        
        const svg = tempConnectionsContainer.querySelector('svg') || 
                   document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.style.position = 'absolute';
        svg.style.top = '0';
        svg.style.left = '0';
        svg.style.width = '100%';
        svg.style.height = '100%';
        svg.style.pointerEvents = 'none';
        
        if (!svg.parentNode) {
            tempConnectionsContainer.appendChild(svg);
        }
        svg.appendChild(sliceLine);
        
        isSlicing = true;
        document.addEventListener('mousemove', updateSliceLine);
        document.addEventListener('mouseup', endSlicing);
    }
}

function updateSliceLine(e) {
    if (!isSlicing) return;
    e.preventDefault();
    
    const editorRect = nodeEditor.getBoundingClientRect();
    // Use the same coordinate space as the wire positions
    const currentX = e.clientX - editorRect.left;
    const currentY = e.clientY - editorRect.top;
    
    sliceLine.setAttribute('x2', currentX);
    sliceLine.setAttribute('y2', currentY);
    
    // Check for intersections with wires
    connections.forEach((conn, id) => {
        const path = conn.path;
        if (doesLineIntersectPath(
            sliceStartX, sliceStartY, 
            currentX, currentY, 
            path
        )) {
            path.style.stroke = '#ff0000'; // Highlight intersected wires
        } else {
            path.style.stroke = conn.color;
        }
    });
}

function endSlicing(e) {
    if (!isSlicing) return;
    if (e.button !== 2) return; // Only end on right mouse button
    
    const dragDuration = Date.now() - rightClickStartTime;
    
    if (dragDuration < 150) {
        // Short right-click, show context menu
        console.log('Show context menu');
        // TODO: Implement context menu
    } else {
        // Dragged right-click, cut wires
        const editorRect = nodeEditor.getBoundingClientRect();
        // Use the same coordinate space as the wire positions
        const endX = e.clientX - editorRect.left;
        const endY = e.clientY - editorRect.top;
        
        // Find and remove intersected connections
        connections.forEach((conn, id) => {
            if (doesLineIntersectPath(
                sliceStartX, sliceStartY,
                endX, endY,
                conn.path
            )) {
                // Send disconnect message to server
                ws.send(JSON.stringify({
                    type: 'disconnect_nodes',
                    from_node: conn.fromNode,
                    from_socket: conn.fromSocket,
                    to_node: conn.toNode,
                    to_socket: conn.toSocket
                }));
                
                // Remove connection visually
                conn.path.remove();
                connections.delete(id);
            }
        });
    }
    
    // Clean up
    if (sliceLine) {
        sliceLine.remove();
        sliceLine = null;
    }
    isSlicing = false;
    document.removeEventListener('mousemove', updateSliceLine);
    document.removeEventListener('mouseup', endSlicing);
    
    // Reset wire colors
    connections.forEach(conn => {
        conn.path.style.stroke = conn.color;
    });
}

function doesLineIntersectPath(x1, y1, x2, y2, path) {
    // Get path segments
    const pathLength = path.getTotalLength();
    const segments = 20; // Number of segments to check
    const points = [];
    
    // Sample points along the path
    for (let i = 0; i <= segments; i++) {
        const point = path.getPointAtLength(pathLength * i / segments);
        // The points from the path are already in SVG coordinates
        points.push([point.x, point.y]);
    }
    
    // Check each segment for intersection
    for (let i = 0; i < points.length - 1; i++) {
        if (doLinesIntersect(
            x1, y1, x2, y2,
            points[i][0], points[i][1],
            points[i + 1][0], points[i + 1][1]
        )) {
            return true;
        }
    }
    return false;
}

function doLinesIntersect(x1, y1, x2, y2, x3, y3, x4, y4) {
    // Calculate denominator
    const den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
    if (den === 0) return false;
    
    // Calculate intersection point parameters
    const t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
    const u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
    
    // Check if intersection occurs within both line segments
    return t >= 0 && t <= 1 && u >= 0 && u <= 1;
} 

function startFlowConnection(nodeId, isInput, event) {
    console.log('Starting flow connection:', { nodeId, isInput });
    if (isSlicing) return;
    
    const dot = event.target;
    const rect = dot.getBoundingClientRect();
    const editorRect = nodeEditor.getBoundingClientRect();
    const scale = parseFloat(editorContent.style.transform.match(/scale\((.*?)\)/)?.[1] || 1);
    
    activeFlowConnection = {
        nodeId,
        isInput,
        startX: (rect.left + rect.width / 2 - editorRect.left - editorTranslateX) / scale,
        startY: (rect.top + rect.height / 2 - editorRect.top - editorTranslateY) / scale,
        svg: null,
        path: null
    };
    console.log('Flow connection start position:', { x: activeFlowConnection.startX, y: activeFlowConnection.startY });
    
    // Create temporary connection line
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.style.position = 'absolute';
    svg.style.top = '0';
    svg.style.left = '0';
    svg.style.width = '100%';
    svg.style.height = '100%';
    svg.style.pointerEvents = 'none';
    svg.style.zIndex = '1000';  // Make sure it's visible above other elements
    
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.classList.add('connection-path', 'flow', 'active');
    svg.appendChild(path);
    
    activeFlowConnection.svg = svg;
    activeFlowConnection.path = path;
    tempConnectionsContainer.appendChild(svg);
    
    // Add event listeners for movement and completion
    document.addEventListener('mousemove', updateFlowConnection);
    document.addEventListener('mouseup', endFlowConnection);
}

function updateFlowConnection(e) {
    console.log('Updating flow connection');
    if (!activeFlowConnection) return;
    
    const editorRect = nodeEditor.getBoundingClientRect();
    const scale = parseFloat(editorContent.style.transform.match(/scale\((.*?)\)/)?.[1] || 1);
    const endX = (e.clientX - editorRect.left - editorTranslateX) / scale;
    const endY = (e.clientY - editorRect.top - editorTranslateY) / scale;
    
    // Create bezier curve
    const dx = Math.abs(endX - activeFlowConnection.startX);
    const path = `M ${activeFlowConnection.startX} ${activeFlowConnection.startY} 
                C ${activeFlowConnection.startX + dx/2} ${activeFlowConnection.startY},
                  ${endX - dx/2} ${endY},
                  ${endX} ${endY}`;
    
    console.log('Setting path:', path);
    activeFlowConnection.path.setAttribute('d', path);
}

function endFlowConnection(e) {
    console.log('Ending flow connection');
    if (!activeFlowConnection) return;
    
    const dot = document.elementFromPoint(e.clientX, e.clientY);
    console.log('Target element:', dot);
    if (dot && dot.classList.contains('flow-dot')) {
        const targetNodeId = dot.closest('.node').id;
        const isTargetInput = dot.classList.contains('input');
        console.log('Found valid target:', { targetNodeId, isTargetInput });
        
        // Only connect if one is input and other is output
        if (isTargetInput !== activeFlowConnection.isInput) {
            const fromNodeId = activeFlowConnection.isInput ? targetNodeId : activeFlowConnection.nodeId;
            const toNodeId = activeFlowConnection.isInput ? activeFlowConnection.nodeId : targetNodeId;
            
            // Check for existing output connections if this is an output
            if (!activeFlowConnection.isInput) {
                const existingConnection = Array.from(connections.values()).find(
                    conn => conn.isFlow && conn.fromNode === fromNodeId
                );
                if (existingConnection) {
                    // Disconnect existing connection first
                    const oldConnectionId = `${existingConnection.fromNode}-flow-${existingConnection.toNode}-flow`;
                    connections.delete(oldConnectionId);
                    existingConnection.path.remove();
                }
            }
            
            // Create the new connection
            createConnection(fromNodeId, 'flow', toNodeId, 'flow', true);
        }
    }
    
    // Clean up
    if (activeFlowConnection.svg) {
        activeFlowConnection.svg.remove();
    }
    activeFlowConnection = null;
    document.removeEventListener('mousemove', updateFlowConnection);
    document.removeEventListener('mouseup', endFlowConnection);
}

// Modify the slicing function to handle flow connections
function doesLineIntersectPath(x1, y1, x2, y2, path) {
    // Get path segments
    const pathLength = path.getTotalLength();
    const segments = 20; // Number of segments to check
    const points = [];
    
    // Sample points along the path
    for (let i = 0; i <= segments; i++) {
        const point = path.getPointAtLength(pathLength * i / segments);
        points.push([point.x, point.y]);
    }
    
    // Check each segment for intersection
    for (let i = 0; i < points.length - 1; i++) {
        if (doLinesIntersect(
            x1, y1, x2, y2,
            points[i][0], points[i][1],
            points[i + 1][0], points[i + 1][1]
        )) {
            return true;
        }
    }
    return false;
}

// Update the connection creation to handle flow connections
function createConnection(fromNodeId, fromSocket, toNodeId, toSocket, isFlow = false) {
    const connectionId = `${fromNodeId}-${fromSocket}-${toNodeId}-${toSocket}`;
    
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.classList.add('connection-path');
    if (isFlow) {
        path.classList.add('flow');
    }
    
    // Use the existing SVG in connectionsContainer
    const svg = connectionsContainer.querySelector('svg');
    svg.appendChild(path);
    
    const connection = {
        fromNode: fromNodeId,
        fromSocket,
        toNode: toNodeId,
        toSocket,
        path,
        isFlow
    };
    
    connections.set(connectionId, connection);
    updateConnectionPath(connection);
    
    return connection;
} 