# ürünlerin adedinin ve fiyatının ayrı tutulduğu toplam satış ve ürün fiyatının başka bir class da belirlendiği bir örnek
class market:
    sonuc=0
    def __init__(self,adet,fiyat):
        self.adet=adet
        self.fiyat=fiyat
    
    def calculate(self):
        sonuc=self.adet*self.fiyat
        return sonuc
    
class total:
    sonuc=0
    def __init__(self,list):
        self.list=list

    def add(self,item):
        self.list.append(item)
    
    def display(self):
        for x in self.list:
            print(f"{x.fiyat},{x.adet}")

        if self.list==[]:
            print("bos")

    def calculate(self):
        return sum([item.calculate() for item in self.list])
    
    def remove(self,item1):
        self.liste=[item for item in self.list if item!=item1]

    def clear(self):
        self.list=[]
        

i=market(2,500)
i1=market(3,400)
i1.calculate()
i.calculate()
a=total(list=[])
a.add(i)
a.add(i1)
a.display()

print(a.calculate())
a.remove(i)
a.display()
a.clear()
a.display()