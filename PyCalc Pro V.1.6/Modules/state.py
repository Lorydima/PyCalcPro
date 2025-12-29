"""Calculator state management and history."""

import json
from pathlib import Path


class CalculatorState:
    """Manages calculator state and operation history."""
    
    def __init__(self, data_file):
        """
        Initialize calculator state.
        
        Args:
            data_file: Path to the JSON data file
        """
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
    
    def save_operation(self, operation):
        """Save an operation to history."""
        try:
            if self.data_file.exists():
                try:
                    data = json.loads(self.data_file.read_text())
                except (json.JSONDecodeError, IOError):
                    data = {"operations": []}
            else:
                data = {"operations": []}
            
            data["operations"].append(operation)
            # Keep only last 10 operations
            data["operations"] = data["operations"][-10:]
            
            self.data_file.write_text(json.dumps(data, indent=4))
        except Exception as e:
            print(f"Error saving operation: {e}")
    
    def get_operations(self):
        """Retrieve operation history."""
        try:
            if self.data_file.exists():
                try:
                    data = json.loads(self.data_file.read_text())
                    return data.get("operations", [])
                except json.JSONDecodeError:
                    return []
            return []
        except Exception as e:
            print(f"Error reading operations: {e}")
            return []
