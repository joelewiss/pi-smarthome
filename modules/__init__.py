import os

modules = []

for file in os.listdir("modules/"):
    if ".py" in file and "_" not in file:
        module = file[0:file.index(".py")]
        modules.append(module) 

__all__ = modules
