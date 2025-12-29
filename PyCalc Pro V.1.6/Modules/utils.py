"""Utility functions for asset loading and file operations."""

import sys
from pathlib import Path


def get_assets_dir():
    """Get the absolute path to the assets directory."""
    if hasattr(sys, '_MEIPASS'):
        # Running as compiled executable
        return Path(sys._MEIPASS) / 'assets'
    else:
        # Running as script, assets folder is at project root
        return Path(__file__).parent.parent.parent / 'assets'


def get_logo_path():
    """Get the path to the calculator icon."""
    assets_dir = get_assets_dir()
    logo_file = assets_dir / 'pycalcpro_v1.6_logo.ico'
    
    if logo_file.exists():
        return str(logo_file)
    
    # Fallback: check old location for backward compatibility
    old_location = Path(__file__).parent.parent.parent / 'PyCalc Pro V.1.6' / 'Src' / 'PyCalc_Pro_V1.5_Logo.ico'
    if old_location.exists():
        return str(old_location)
    
    return None


def get_data_file_path():
    """Get the path to the operations data JSON file."""
    return get_assets_dir() / 'pycalcpro_v1.6_data.json'


def load_license_text():
    """Load MIT license text from the LICENSE file at project root."""
    license_file = Path(__file__).parent.parent.parent / 'LICENSE'
    if license_file.exists():
        try:
            return license_file.read_text(encoding='utf-8')
        except Exception:
            pass
    
    # Fallback
    return "MIT License\n\nCopyright (c) 2025 LDM Dev\n\nPermission is hereby granted, free of charge..."
