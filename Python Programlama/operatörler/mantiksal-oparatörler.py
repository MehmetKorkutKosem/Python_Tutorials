x=int(input("sayi giriniz"))
result=5<x<10
print(result)
# and iki tarafında doğru olması gerekir sonucun true olmasi için
result= x>5 and x<10
# or iki taraftan birinin doğru olması sonucun doğru olması için yeterli
y=int(input("sayi giriniz"))
result2= y==0 or y==3
print(result2)
# not oparatörü tersler 
a=5
print(a==5)
result3=not a==5
print(result3)

