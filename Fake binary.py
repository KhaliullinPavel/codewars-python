
a = '45385593107843568'

def fake_bin(x):
    l = list(x)
    for i,v in enumerate(l):
        if int(v) < 5:
            l[i]=0
        else:
            l[i]=1
    s = ''.join(str(n) for n in l)
    return s

res = fake_bin(a)
print(res)
print(type(res))
