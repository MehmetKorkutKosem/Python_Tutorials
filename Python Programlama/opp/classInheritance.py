class person:#base sınıf
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print("base sinif")
    
    def display(self):
        print(self.name,self.surname)

class student(person):#inherit durumu base sınıfın özelliklerini kullanabilir 
    def __init__(self,name,surname,lessonCount):
        super().__init__(name,surname)#super base sınıfın constructurunu inherit etmeyi sağlar
        self.lessonCount=lessonCount
    
    def display(self):
        print(self.name,self.surname,self.lessonCount)
        print("ögrenci sinifi turetildi")
  
class teacher(person):
      def __init__(self,name,surname,lessonCount,studentCount):
        super().__init__(name,surname)
        self.lessonCount=lessonCount
        self.studentCount=studentCount
      def display(self):
        print(self.name,self.surname,self.lessonCount,self.studentCount)#display base fonksiyonda biz displayi burdada kullanıyoruz ve ezmiş oluruz polimorfizim
        print("ögretmen sinifi turetildi")

p1=person("ali","çakal")
p1.display()
p2=teacher("mustafa","kara",4,54)
p2.display()
p3=student("samet","urban",4)
p3.display()

class personInformation:
    def __init__(self,adress,crimeCount):
        self.adress=adress
        self._crimeCount=crimeCount
    
    def setCrimeCount(self,value):
        if value>=0:
           self._crimeCount=value
        else:
            raise ValueError("value invalid")
    
    def getCrime(self):
        return self._crimeCount
    @property 
    def _Crime(self):#artık crime set ederken fonksiyon gibi davranmak yerine normal bir value değeri gibi değişikliğini sağlayabiliriz bu olayı property sağlar
        return self._crimeCount
    @_Crime.setter
    def _Crime(self,value):
        if value>=0:
           self._crimeCount=value
        else:
            raise ValueError("value invalid")

b=personInformation("ali",2)
b.setCrimeCount(1)
b._Crime=1
print(b._Crime)
