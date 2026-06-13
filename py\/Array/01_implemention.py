import array as myarray

array01 = myarray.array('i', [0,1,2,3,4,5])

print(array01.typecode)
print(array01)
print(len(array01))

for i in range (0,len(array01)):
    print(array01[i], end = "" )

print("\n")