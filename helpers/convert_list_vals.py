import data_types


# converts a list of values to proper data types
def convert_list_vals(vals):
    # (bug fix) removes first or last item if it is blank
    if vals[0] == '':
        vals.pop(0)
    if len(vals) > 0 and vals[-1] == '':
        vals.pop()
    # return empty list if there or no values in it
    if len(vals) == 0:
            return []
    # formats the values in the list
    formatted = [data_types.format_value(i) for i in vals]
    # if any of the data types is False, invalid command
    if False in formatted:
        return False
    else:
        for i in formatted:
            # converts booleans (a bug that fixed a bug)
            if str(i).lower() == "false":
                formatted[formatted.index(i)] = False
            elif str(i).lower() in ["true", "through", "tru"]:
                formatted[formatted.index(i)] = True
        # hack that formats variables and strings properly
        final = "".join([i for i in list(str(formatted)) if i != "'"])

        return final
