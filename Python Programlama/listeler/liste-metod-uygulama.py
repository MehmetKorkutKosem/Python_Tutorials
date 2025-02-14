names=['ali','hakan','yagmur','deniz'] 
years=[1998,200,1998,1987]
# 1
names.insert(4,"cenk")
print(names)
# 2
names.insert(0,"sema")
print(names)
# 3
names.pop(4)
print(names)
names.insert(4,"deniz")
# 4
print(names.index("deniz"))
# 5
x="ali"in names
print(x)
# 6
names .reverse()
print(names)
# 7
names.sort()
print(names)
# 8
years.sort()
print(years)
# 9
str="chevrollet,dacia"
z1=str.split(",")
print(z1)
# 10
f=max(years)
y=min(years)
print(f)
print(y)
# 11
sayi=years.count(1998)
print(sayi)
# 12
years.clear()
print(years)
# 13
marka=[]
num=0
while num<3:
    a=input("marka giriniz")
    marka.append(a)
    num=num+1
print(marka)   
