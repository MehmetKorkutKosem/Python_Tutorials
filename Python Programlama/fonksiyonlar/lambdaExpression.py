def square(num):
    return num**2
list1=[1,2,3,4,5,6,7,8,9,10]
result=map(square,list1)
result1=list(result)
print(result) # bu şekilde yaparsak bize adres veriri sadece
print(result1) # bu şekilde yaparsak sonuçları liste içerisinde görebiliriz
print(list(map(square,list1))) # map pythonun yapısal bir fonksiyonudur

for x in map(square,list1):# bu yöntemle liste yerine her bir sonucu tek tek ekrana yazdırabiliriz
    print(x)
for x in result1:
    print(x)

print(list(map(lambda num :num**2,list1)))# lambda metodunu kullanarak isimsiz bir fonksiyon kullanarakta aynı işlemi gerçekleştirebiliriz
square=lambda num :num**2 # bura da lambda fonksiyonunu bir değişkene atayarak kullanabiliriz
print(list(map(square,list1))) 
result =square(5)# normal fonksiyon şeklindede kullanabiliriz
print(result)

def check(num):
    return num%2==0
result=list(filter(check,list1))# filter fonksiyonu ile belirli bir koşulu sağlayan değerleri listeleyebiliriz
print(result)
print(list(filter(lambda num:num%2==0,list1)))# aynı sonuca lamda tanımını kullandığımız farklı bir örnek ilede ulaşabiliriz
