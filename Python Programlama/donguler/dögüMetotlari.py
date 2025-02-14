for x in range(5):# range belirlediğiniz aralıktaki tur sayisi kadar forun çalismasini saglar
    if x==1 :         # range(0,5,2) eger bu sekilde range tanımlamış olsaydık sadece 2 ve  4 ün çıktısını alacaktık çünkü son tanımladığımız iki artma miktarı
      print("   *")   
    elif x==2:
       print("  * *")
    elif x==3:
       print(" * * *")
    elif x==4:
       print("* * * *")

for x in range(50,100,2):# bu şekildeki tanımlama 50 ile 100 arasında artım miktarı 2 olan bir sıralama yapabiliriz
   print(x)

print(list(range(50,100,2)))# bu şekilde listeye dönüştürmüş oluruz
index=0
for a in "Enver Paşa":
   print(a)
   print(f"index {index}={a}")
   index+=1
y="Enver Paşa"   
for index,b in enumerate("Enver Paşa"):# çıktı önceki örnek ile aynı olur çünkü enumerate indexler
    print(f"index {index}={b}")

list1=[1,2,3,4,5,6,7]
list2=["a","b","c","d","e","f","g"]
list3=[8,9,10,11,12,13,14]
print(list(zip(list1,list2,list3)))# zip metodu listelerin elemanlarını eşleştirir

   


