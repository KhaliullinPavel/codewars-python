def friend(x):
    return [name for name in x if len(name)==4]

r = friend( ["Ryan", "Kieran", "Mark",])
print(r)