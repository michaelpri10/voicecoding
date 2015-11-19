def exec_code(code):
    print(">>> {0}".format(code))
    try:
        exec(code)
    except Exception as e:
        print(e.__doc__)
        print(e)
