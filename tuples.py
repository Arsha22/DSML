print("containers:Tuples")
d={(x,x+1):x for x in range(10)}
print("dictionary with tuples key:")
for k,v in d.items():
    print(k,":",v)
t=(5,6)
print("tuple t:",t)
print(d[t])
print(d[1,2])
    
