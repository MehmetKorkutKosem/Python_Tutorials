#string concat
ad="yilmaz"
soyad="turan"
yas=40
all="ad"+ad+" soyad"+soyad+" yas"+str(yas)
print(all)
#string format
all="ad:{} soyad:{} yas:{}".format(ad,soyad,yas)
print(all)
#f-string
all=f"ad:{ad} soyad:{soyad} yas:{yas}"
print(all)