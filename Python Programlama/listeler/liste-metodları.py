numbers=[1,5,7,8,0,24,98,81,31]
letters=["a","c","d","b","f","j","y","n","o","z"]
sonuc=max(numbers)
sonuc1=min(numbers)
print(sonuc)
print(sonuc1)
numbers.append(44)# sona ekler
print(numbers)
numbers.insert(2,3)#belirlenen indise ekleme
print(numbers)
numbers.insert(-1,71)
print(numbers)
numbers.pop()#sondaki elamanı siler
print(numbers)
numbers.pop(1)#indeksteki elamanı siler
print(numbers)
numbers.remove(8)#silmek istediğin elemanı girmek istediğin zaman siler
print(numbers)
letters.sort()#sayıları ve harfleri sıralar
numbers.sort()
print(numbers)
print(letters)
numbers.reverse()#tersten yazdırma
print(numbers)
print(numbers.count(0))#sayı adedini belirler