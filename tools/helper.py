def read_input(name):
    with open(name, "r") as i:
        inputdata = i.read().splitlines()
    return inputdata


def read_inputline(name):
    with open(name, "r") as i:
        inputdata = i.read()
    return inputdata
