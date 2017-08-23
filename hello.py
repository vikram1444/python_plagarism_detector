import math
def elim(x):
    s=''
    for i in range(len(x)):
        if (ord(x[i])>96 and ord(x[i])<123) or (ord(x[i])>47 and ord(x[i])<58) or ord(x[i])==95 or ord(x[i])==32:
            s=s+x[i]
    return s
def word_count(d):
    my_string = d.replace(".", " ").replace(",", " ").split()
    my_dict = {}
    for item in my_string:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return my_dict
def sq(x):
    sum=0
    for key in x.values():
        sum=sum+(int(key)*int(key))
    return math.sqrt(sum)
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
x=word_count(d)
y=word_count(c)
p=sq(x)
q=sq(y)
hh=0
for key in x.keys():
    if key in y.keys():
         hh=hh+x[key]*y[key]
fo=hh/(p*q)
fo=fo*100
print(round(fo,2),"% plagarism detected")




