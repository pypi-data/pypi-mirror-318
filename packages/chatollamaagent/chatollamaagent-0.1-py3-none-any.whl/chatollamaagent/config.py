import json
import os
from typing import Any

class Config:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        self._ensure_config_exists()

    def _ensure_config_exists(self) -> None:
        """Ensure the config file exists and is properly formatted."""
        try:
            if not os.path.exists(self.config_path):
                with open(self.config_path, 'w') as f:
                    json.dump({}, f, indent=4)
                return

            # Check if file is readable and properly formatted
            with open(self.config_path, 'r') as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, dict):
                        raise ValueError("Config must be a JSON object")
                except (json.JSONDecodeError, ValueError):
                    # If file is corrupted or improperly formatted, reset it
                    with open(self.config_path, 'w') as f:
                        json.dump({}, f, indent=4)
        except Exception as e:
            print(f"Error handling config file: {e}")
            # If all else fails, ensure we at least have an empty config
            with open(self.config_path, 'w') as f:
                json.dump({}, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value from the config file.
        If the key doesn't exist, returns the default value.
        """
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
                return data.get(key, default)
        except Exception as e:
            print(f"Error reading config: {e}")
            return default

    def set(self, key: str, value: Any) -> bool:
        """
        Set a value in the config file.
        Returns True if successful, False otherwise.
        """
        try:
            # Ensure config exists and is valid
            self._ensure_config_exists()
            
            # Read current config
            with open(self.config_path, 'r') as f:
                data = json.load(f)
            
            # Update value
            data[key] = value
            
            # Write back to file
            with open(self.config_path, 'w') as f:
                json.dump(data, f, indent=4)
            
            return True
        except Exception as e:
            print(f"Error writing to config: {e}")
            return False

# Create a global instance for easy import
config = Config() 