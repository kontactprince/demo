t1=("apple","cherry","banana","cherry")
print(t1)
t2=("apple","cherry","banana","cherry")
print(len(t2))

t3=("apple","cherry","banana","cherry")
print(type(t3))

t4=("apple","cherry","banana","cherry")
print(t4[1])

#range
t5=("apple","cherry","banana","cherry")
print(t5[1:3])

#add item
t6=("apple","cherry","banana","cherry")
y=list(t6)
y.append("orange")
t6=tuple(y)
print(t6)

#remove item
t7=("apple","cherry","banana","cherry")
y=list(t7)
y.remove("apple")
t7=tuple(y)
print(t7)

#loop through a tuple
t8=("apple","cherry","banana","cherry")
for x in t8:
    print(x)

    