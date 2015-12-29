# formats variable, function, and method names to snake_case
def format_var_func_name(name):
    lowercased_name = name.lower()
    snaked_name = lowercased_name.replace(" ", "_")
    return snaked_name
