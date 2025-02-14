x,y,z=2,5,107
numbers=1,5,7,10,6
#kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı nedir
a=int(input("lutfen  iki sayi giriniz "))
b=int(input("lutfen  iki sayi giriniz "))
sonuc=(a*b)-(x*y*z)
print(sonuc)
#y nin x e kalansız bölümünü hesaplayiniz
y//=x
print(y)
#x,y,z nin toplamının mod üçü nedir
x+=y
z+=x
z%=4
print(z)
#y nin x inci kuvvetini hesaplayınız.
y**=x
print(x)
# x,*y,z=numbers işlemine göre z'nin küpü kaçtır
x,*y,z=numbers
z**=3
print(z)
#x,*y,z=numbers işlemine göre y nin değerleri toplamı nedir
top=0
for i in range(2):
    top+=y[i]
print(top)    