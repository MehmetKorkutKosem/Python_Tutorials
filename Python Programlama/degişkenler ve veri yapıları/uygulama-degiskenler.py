customerInformation1 = input("Customer Name: ")
customerInformation2 = input("Customer Number: ")
customerInformation3 = input("Customer Email Address: ")

productInformation1 = input("Product Name: ")
productInformation2 = int(input("Product Price: "))
productInformation3 = input("Product Name: ")
productInformation4 = int(input("Product Price: "))
productInformation5 = input("Product Name: ")
productInformation6 = int(input("Product Price: "))

kdv = 0.18

totalPrice = productInformation2 + productInformation4 + productInformation6
totalPrice = totalPrice + (totalPrice * kdv)

print("Name: " + customerInformation1 + "\nNumber: " + customerInformation2 + "\nEmail: " + customerInformation3)
print("Product Name: " + productInformation1 + " Product Price: " + str(productInformation2))
print("Product Name: " + productInformation3 + " Product Price: " + str(productInformation4))
print("Product Name: " + productInformation5 + " Product Price: " + str(productInformation6))
print("Total Price: " + str(totalPrice))
