"""
TALDTool: A Python package for detecting suspicious script patterns.

This package provides:
- Predefined regex patterns for identifying potentially dangerous or malicious commands.
- Utility functions for script analysis.

Author: Mohamed Rayan Ettaldi
GitHub: https://github.com/ettaldi/TALDTool
Version: 2.0.0
"""

from .TALDCommands import TALDCommands

# Package metadata
__version__ = "2.0.0"
__author__ = "Mohamed Rayan Ettaldi"
__email__ = "taldtool06@gmail.com"  # Replace with your actual email

# Optional utility function to access patterns
def get_patterns():
    """
    Returns the dictionary of suspicious patterns.

    Returns:
        dict: A dictionary of suspicious patterns categorized by type.
    """
    return TALDCommands