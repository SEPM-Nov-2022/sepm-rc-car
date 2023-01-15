"""
The purpose of this file is to maintain utility-based functions used
throughout the application.
"""

from pathlib import Path


def get_project_root() -> Path:
    """
    Get the project's root directory.
    Returns:
        the path of the project's root directory.
    """
    return Path(__file__).parent.parent
