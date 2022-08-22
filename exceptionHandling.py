def index_of(val, lista):
    if val in lista:
        success(lista.index(val))
        return

    failure(ValueError('TEST'))
    return

def success(val):
    print("success")

def failure(exc):
    print("failure")