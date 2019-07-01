def caller(fun):
    return(fun())

print(caller(lambda: 33 + 55 ))

# The lambda works like the following method:

def adding():
    return(33 + 55)

print(caller(adding))
