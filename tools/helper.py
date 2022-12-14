def read_input(name):
    with open(name, "r") as i:
        inputdata = i.read()
    return inputdata


def read_inputlines(name):
    with open(name, "r") as i:
        inputdata = i.read().splitlines()
    return inputdata
