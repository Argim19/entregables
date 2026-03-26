#Request product name and text-only verification

while True:
   name = input("enter the name:")
   if name.isalpha():
      break
   else:
      print("enter text")

#Request the price and  verify that only numbers are entered     
      
while True:
   try:
      price = float(input("enter the price:"))
      if price <=0:
         print("enter a price greater than 0")
      else:   
         break
   except ValueError:
      print("error")

#Request the price and  verify that only numbers are entered          

while True:
   try:
      quantity = int(input("enter the quantity:"))
      if quantity <=0:
         print("enter a quantity greater than 0")
      else:   
         break
   except ValueError:
      print("error")      
    

total_cost = price * quantity

print("name the product:",name)
print("unit price:",price)
print("quantity:",quantity)
print("total:",total_cost)




    


#while price <= 0:
#   price = float(input("enter again the price:"))

#while not quantity.isdigit():
#   quantity = input("enter again the quantity:")
#quantity = int(quantity)   