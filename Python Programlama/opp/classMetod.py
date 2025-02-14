class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self): #display person sınıfına ait bir metoddur class içinde tanımlanmış fonksiyonlara metod denir
        print(f"name={self.name} age={self.age}")

    def  yaz(self):# ilk durumu yaz()
        print("hello "+self.name)

    def  calculate(self):
        return 2024-self.age

p1=person("ali",33)
p1.display()
p1.yaz()#hata verir çünkü yaz metodunun self parametresi yoktur self objeyi temsil eder referansıdır
print(p1.calculate())


class circle:
    pi=3.14# class variable tanımlanır ve class içindeki tüm metodlar tarafından kullanılabilir eğer olmasaydı ve init içinde tanımlansaydı her nesne oluşturulduğunda tekrar tanımlanacaktı
    def __init__(self,radius=1):# default değer ataması yapılır
        self.radius=radius
    def area(self):
        return self.pi*self.radius**2
    
    def perimeter(self):
        return 2*self.pi*self.radius

c1=circle(5)
print(c1.area())
print(c1.perimeter())
c2=circle() # default değer ataması yapıldığı için radius=1 olur
print(c2.area())
print(c2.perimeter())

class price:
    __indirimOrani=0.8#bu tanım private olma durumunu gösterir
    respawn=0
    @classmethod# sınıf üyesi bir metod haline getirdik displayi
    def display(cls):
      print(cls.__indirimOrani)#cls.__indirimOrani yerine doğrudan class isminide yazabiliriz değişken gibi düşünülebilir
    def __init__(self,urun,alim):
        self.urun=urun
        self.alim=alim
        price.respawn+=1
    def calculate(self):
        result=(self.urun-self.alim)*price.__indirimOrani#"__indirimOrani bir sınıf özelliği olduğu için sınıf adı ile çağrılır"
        print(result)

    
p1= price(1000,500)
p2=price(1200,300)
p1.calculate()
price.display()
#print(p1.__indirimOrani)# yazdırmaz private
print(price.__dict__)#special attiribüte dir
print(p1.__dict__)
print(price.respawn)
class identity:
    @classmethod
    def create(cls,giris_str):
        name,surname=giris_str.split(",")
        print(name,surname)
        return cls(name,surname)
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    
    def info(self):
         print(f"ismi:{self.name},soyismi:{self.surname}")
      
 
    
identity.create("mustaf,cemal")
p1=identity("ali","fuat")
print(identity.__dict__)
print(p1.name)