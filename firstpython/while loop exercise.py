#print square up to limit

def printsqu(limit):
    i=1
    while i*i < limit:
        print(i*i, end=" ")
        i = i+1

#printsqu(60)

#print cubes

def printcub(limit):
    i=1
    while i*i*i < limit:
        print(i*i*i, end=" ")
        i = i+1

printcub(67)
