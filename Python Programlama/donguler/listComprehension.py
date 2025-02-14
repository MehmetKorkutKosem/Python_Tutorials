numbers=[ x for x in range(0,50)] # bu yöntemle 0 - 50 ye kadar olan sayılar listeye yerleştirilir
print(numbers)
numbers=[ x**2 for x in range(0,10)] # bu yöntemle 0 - 10 a kadar olan sayıların karesini almış oluruz
print(numbers)
numbers=[ x**2  for x in range(0,10) if x%3==0 ] # bu yöntemle şart eklemiş oluruz
print(numbers)

mylist=[a for a in "Bir Ənvər ölür, min Ənvər doğular"]# listeye string ifadenin indislerindeki karakterleri sırayla ekler
print(mylist)

years=[1978,1979,1989,1999,1985]
age=[2024-year for year in years ]
print(age)
numbers1=[  x if x%2==0 else "tek" for x in range(0,10)  ] # bu yöntemle şart eklemiş oluruz
print(numbers1)
sayilar=[ (x,y ) for x in range(0,10) for y in range(0,10) ]
print(sayilar)