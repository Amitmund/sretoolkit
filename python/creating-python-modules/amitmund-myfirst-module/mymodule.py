import os
import platform

class OperatingSystemIdentifier:
    def __init__(self):
        pass

    def identify(self):
        # Use platform, sys, or os modules to determine the OS
        if platform.system() == "Windows":
            return "Windows"
        elif platform.system() == "Darwin":
            return "macOS"
        elif platform.system() == "Linux":
            return "Linux"
        else:
            return "Unknown"

    def __str__(self):
        return f"Operating System: {self.identify()}"
    

identifier = OperatingSystemIdentifier()
print(identifier.identify())