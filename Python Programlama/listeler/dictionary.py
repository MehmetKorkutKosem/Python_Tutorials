# key-value
mevsimler={"ocak":1,"şubat":2,"mart":3}
print(mevsimler["ocak"])
mevsimler["nisan"]=4#kendini güncelleyerek yeni bilgiyi ekler
print(mevsimler)
mevsimler["ocak"]=2
print(mevsimler)
cars={"bmw":{
"color":"black",
"model":["a","b"],
"price":12977
},
"ferrari":{
    "color":"red",
    "price":239304
}
}
print(cars["bmw"]["color"])
print(cars["ferrari"]["price"])