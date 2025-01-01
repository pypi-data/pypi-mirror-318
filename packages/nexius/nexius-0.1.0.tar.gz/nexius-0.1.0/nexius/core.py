"""
Core functionality for the Nexius library
"""

class NexiusBase:
    """Base class for Nexius functionality"""
    
    def __init__(self):
        self._initialized = True
    
    @property
    def is_initialized(self):
        return self._initialized

# You can add more classes and functions here later 