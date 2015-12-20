import data_types

def convert_list_vals(vals):
    if vals[0] == '':
        vals.pop(0)
        if len(vals) == 0:
            return []
    formatted = [data_types.format_value(i) for i in vals]
    if False in formatted:
        return False
    else:
        for i in formatted:
            if str(i).lower() == "false":
                formatted[formatted.index(i)] = False
            elif str(i).lower() in ["true", "through", "tru"]:
                formatted[formatted.index(i)] = True
        final = "".join([i for i in list(str(formatted)) if i != "'"])
        return final
