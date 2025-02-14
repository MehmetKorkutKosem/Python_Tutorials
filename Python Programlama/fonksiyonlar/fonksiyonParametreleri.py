def degistir(a):
    a="aaaaa"
    

name="ali"
degistir(name)#degismez çünkü değişken değerini doğrudan değiştirmes

list=["blackFire","samuel"]
def degistir(n):
    n[0]=["fireSpace"] # burada doğrudan fireSpace listeye eklenir çünkü liste ve dizilerde önceki değişkene göre farklı olarake referans üzerinden işlem yapılır

degistir(list)
print(list)
def degistir(n):# burda bir önceki örnekten farklı olarak listeyi n e kopyaladığımız için kopya üzerinden işlem yapılır
    n=list[:]
    n[0]="shadowEye"
degistir(list)
print(list)

def add(a,b):
    return sum((a,b))# sum phytonun kendinde tanımlı bir fonksiyondur 
a=int(input("sayi giriniz"))
b=int(input("sayi giriniz"))
print(add(a,b))
def add(*num): # bu örnekte birden çok değeri tek tek tanımlamak yerine tek bir değer üzerinden bir çok değer atayabilirirz
    return sum((num))
a=int(input("sayi giriniz"))
b=int(input("sayi giriniz"))
c=int(input("sayi giriniz"))
d=int(input("sayi giriniz"))

print(add(a,b,c,d))

def add(*num):
    sum=0
    for x in num :
        sum=sum+x
    return sum

print(add(5,5,5))

dict=[]
for x in range(3):
   a=input("key giriniz")
   b=int(input("value giriniz" ))
   dict.append({a:b})

print(dict)

def add1(**num):# bu örnekte ise key ve value değerleri ile
    for key,value in num.items():
        print(f"key {key}: value {value}")


add1(name="a", age=2,city="istanbul")

