import importlib
import ovito.gui

# Note: Using importlib.import_module() to import modules, because human-readable Python script names in this directory may contain whitespaces.
MyFirstUtility = importlib.import_module(".MyFirstUtility", __name__).MyFirstUtility
