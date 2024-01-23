modules = dict()

def register(module_name, json=False):
    def decorate_action(func):
        module = {"func": func, "json": json}
        if module_name in modules:
            modules[module_name][func.__name__] = module
        else:
            modules[module_name] = dict()
            modules[module_name][func.__name__] = module
        
        return func

    return decorate_action
