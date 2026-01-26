"""
PyCalc Pro - Storage Module

This module handles saving and loading calculator operations history.
"""

import json
import os
import sys


def get_operations_file_path():
    """Get the path to the operations history file."""
    filename = "DATA.json"
    if hasattr(sys, 'frozen'):
        app_dir = os.path.dirname(sys.executable)
    else:
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(app_dir, filename)


operations_file_path = get_operations_file_path()


def save_operation(operation):
    """Save a calculation operation to the history file."""
    try:
        if os.path.exists(operations_file_path):
            with open(operations_file_path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"operations": []}
        else:
            data = {"operations": []}

        data["operations"].append(operation)
        data["operations"] = data["operations"][-10:]

        with open(operations_file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving operation: {e}")


def get_operations():
    """Retrieve the last 10 operations from history."""
    try:
        if os.path.exists(operations_file_path):
            with open(operations_file_path, "r") as file:
                try:
                    data = json.load(file)
                    return data.get("operations", [])
                except json.JSONDecodeError:
                    return []
        return []
    except Exception as e:
        print(f"Error reading operations: {e}")
        return []
