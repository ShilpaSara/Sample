print("Hello")
#Sample code
a, b, c = 10, "Hello", 200.9
print(a)
print(b)
print(c)
print("{} {} {}".format("Value is", a, b))
data2 = "Data2"
print("Data1 \t"+data2)
values=[2,"python",200.9]
print(values[2])
values.insert(2,"is easy")
print(values[:-1])
print(values[2])
values.append("End")
print(values)
values[2]="Hello"
print(values)
del values[2]
print(values)
print(type(values))

#Tuple
val=(1,2,"shilpa",4.9)
print(type(val))
print(val)
#val[2]="SHILPA"

#Dictionary
a={1: "Firstname", 2: "Lastname"}
dic={"1":12, "c":"S"}
print(a)
print(type(a))
print(dic["c"])
#print(dic[2])
dic={}
print(dic)
dic["Firstname"]="Shilpa"
dic["Lastname"]="Sarath"
print(dic)