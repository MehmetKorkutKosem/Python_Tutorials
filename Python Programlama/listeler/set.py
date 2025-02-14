furuits={"muz","elma","portakal"}
#print(furuits[0])#hata verir çünkü indekslenemez
for x in furuits:
    print(x)
furuits.update(["narenciye","nektar"])  
for x in furuits:
    print(x)  
furuits.update(["apple"])  #aynı elemanı bir deha eklersek tekrarlanma olmaz
for x in furuits:
    print(x)  
furuits.discard("apple")   
for x in furuits:
    print(x)  