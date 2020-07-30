import os

modules = []

for file in os.listdir("modules/"):
    if ".py" in file and "_" not in file and file[0] != ".":
        module = file[0:file.index(".py")]
        modules.append(module) 

__all__ = modules
