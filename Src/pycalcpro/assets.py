"""
PyCalc Pro - Assets Module

This module handles asset paths and resources.
"""

import os
import sys


def get_logo_path():
    """Get the path to the application logo."""
    filename = 'PyCalc_Pro_Logo.ico'
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.path.dirname(__file__), filename)


logo_path = get_logo_path()

# Fallback: prefer the logo filename
if not os.path.exists(logo_path):
    logo_path = "PyCalc_Pro_Logo.ico"
