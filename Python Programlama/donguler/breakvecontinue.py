list=[1,7,8,9,4,5,0,2,3]
for a in list :
    if a==5:
       break # döngüyüü kırmaya yara örnegin burda beşe kadar yazdırıp sonrasında dööngü kırılır

    print(a)

for a in list :
    if a==5:
       continue # bura ise break dan farklı olarak döngü kırılmaz adımı atlanır burda beş hariç diğer elemanları yazdırır

    print(a)

sayac=0
while sayac<5 :
    sayac+=1 # bunun yerine sayacı sona atsaydık ikiden sonra devam etmiyecekti
    if sayac==3:
        continue
    print(sayac)
    