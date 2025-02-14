student={
    567:{
        "name":"samuel",
        "surname":"wolter",
        "phone number":56034902058
    },
    540:{
        "name":"black",
        "surname":"fire",
        "phone number":54300203038
    },
    430:{
        "name":"black",
        "surname":"fury",
        "phone number":58522985805
    }
}
number = int(input("Öğrenci ID'sini girin: "))  
student[number ] = {}
for i in range(3):
   if(i==0):
     student[number]["name"] = input("Yeni adi girin: ")
   if(i==1):
     student[number]["surname"] = input("Yeni soyadi girin: ")
   if(i==2):
        student[number]["phone number"] = int(input("Yeni telefon numarasini girin: ")),

 
print(student)
ogrenciid=int(input())
print(student[ogrenciid])