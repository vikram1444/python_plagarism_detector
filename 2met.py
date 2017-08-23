def elim(x):
    s=''
    for i in range(len(x)):
        if (ord(x[i])>96 and ord(x[i])<123) or (ord(x[i])>47 and ord(x[i])<58) or ord(x[i])==95 or ord(x[i])==32:
            s=s+x[i]
    return s.replace(".", " ").replace(",", " ")
f1=open("3.txt","r")
f2=open("4.txt","r")
d1=f1.read().lower()
c1=f2.read().lower()
print(d1)
print(c1)
d=elim(d1)
c=elim(c1)
print(d)
print(c)