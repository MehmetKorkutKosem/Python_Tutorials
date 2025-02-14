x="global x"

def yaz():
    x="local x"
    print(x) #fonksiyonun içinde local tanım yazılır 

yaz()
print(x) # fonksiyonun dışında global değer yazdırılır

y="ali"

def yaz():
    #y="murat" eğer murat değeride olmasaydı global sınıfı temel alırdı
    def yaz():  # bu durumda ikinci fonksiyon muratı temel alır 
        #y="hamit" ama burdaki durum olursa local değeri olan hamiti baz alır
        print("hello "+y)
    yaz()

yaz()
x=100
def changed(x):
    print(f"x: {x}")
    x=200
    print(f"x changed {x}")
changed(x)


def switch():
    global x # bu şekilde global değere doğrudan ulaşabiliriz ve değerii değiştirebiliriz
    x=3

switch()
changed(x)

