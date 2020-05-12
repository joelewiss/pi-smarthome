modules = dict()

def register(module_name):
    def decorate_action(func):
        if module_name in modules:
            modules[module_name][func.__name__] = func
        else:
            modules[module_name] = dict()
            modules[module_name][func.__name__] = func
        
        return func

    return decorate_action
