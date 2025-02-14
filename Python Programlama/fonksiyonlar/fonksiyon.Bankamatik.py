samuelWalter={

    "name":"samuel Walter",
    "hesap no":" 123456789",
    "bakiye":10000,
    "ek hesap":5000
}

LeoWalter={

    "name":"Leo Walter",
    "hesap no":" 987654321",
    "bakiye":20000,
    "ek hesap":10000

}
islemGecmisi=[]
islemGecmisi1=[]
def paracek(hesap):
    print(f"merhaba {hesap["name"]}")
    miktar=int(input(f"{hesap["name"]} çekmek istediğiniz miktari giriniz"))
    sinir=hesap["bakiye"]+hesap["ek hesap"]
    if sinir>=miktar:
        if hesap["bakiye"]>=miktar:
            hesap["bakiye"]=hesap["bakiye"]-miktar
            geçmiş=-miktar
            islemGecmisi.append(geçmiş)
        else:
            geçmiş=-miktar
            islemGecmisi.append(geçmiş)
            miktar=miktar-hesap["bakiye"]
            hesap["bakiye"]=0
            
            hesap["ek hesap"]=hesap["ek hesap"]-miktar
            
    else:
        print("bakiye yetersiz")
def parayatir(hesap):
    print(f"merhaba {hesap["name"]}")
    miktar=int(input(f"{hesap["name"]} yatirmak istediğiniz miktari giriniz"))
    secim=input("hangi hesabınıza yatırmak istersiniz e/a")
    if secim.lower()=="e":
        hesap["ek hesap"]=hesap["ek hesap"]+miktar
        geçmiş=miktar
        islemGecmisi.append(geçmiş)
    if secim.lower()=="a":
        hesap["bakiye"]=hesap["bakiye"]+miktar
        geçmiş=miktar
        islemGecmisi.append(geçmiş)

def paraGonder(hesap,hesap1):
    print(f"merhaba {hesap["name"]}")
    miktar=int(input(f"{hesap["name"]} göndermek istediğiniz miktari giriniz"))
    secim=input("hangi hesaptan göndermek istersiniz e/a")
    if secim.lower()=="e":
        if hesap["ek hesap"]>=miktar:
            hesap["ek hesap"]=hesap["ek hesap"]-miktar
            geçmiş=-miktar
            islemGecmisi.append(geçmiş)
            hesap1["bakiye"]=hesap1["bakiye"]+miktar
            geçmiş=miktar
            islemGecmisi1.append(geçmiş)
        else:
            print("bakiye yetersiz")
    if secim.lower()=="a":
        if hesap["bakiye"]>=miktar:
            hesap["bakiye"]=hesap["bakiye"]-miktar
            geçmiş=-miktar
            islemGecmisi.append(geçmiş)
            hesap1["bakiye"]=hesap1["bakiye"]+miktar
            geçmiş=miktar
            islemGecmisi1.append(geçmiş)
        else:
            print("bakiye yetersiz")




paracek(samuelWalter)
print(samuelWalter)
print(islemGecmisi)
parayatir(samuelWalter)
print(samuelWalter)
print(islemGecmisi)
paraGonder(samuelWalter,LeoWalter)
print(samuelWalter)
print(LeoWalter)
print(islemGecmisi)
print(islemGecmisi1)