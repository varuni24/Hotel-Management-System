print(" WELCOME TO HOLIDAY INN")
print("")
print ("We have the following rooms types:-")
print ("1.Ultra Royal: Dhs 1000 ")
print ("2.Royal      : Dhs 800")
print ("3.Elite      : Dhs 600")
print ("4.Budget     : Dhs 400")
print("")

d=[]

while(True):

     print("1. Book a Room!")
     print("2. Calculate Room Bill")
     print("3. Order Food and Calculate Bill")
     print("4. Get Customer Details")
     print("5. EXIT")
     print("")
     n=int(input("Enter Choice: "))
     

     if n==1:
          print("Enter the following details:-")
          name=input("Name        : ")
          phn=input("Phone Number: ")
          email=input("E-Mail      : ")
          room=int(input("Room Type   : "))
          nights=int(input("Nights      : "))

          tuple=(name,phn,email,room,nights)
          d.insert(1,tuple)

          print("Room Booked!")
          print()
         
     elif n==2:
          s=input("Enter Name : ")
          p=input("Enter phone number : ")
          t = [item for item in d
               if item[0]==s and item[1]==p] 
          if len(t)==0:
               print("No such customer found in database \n")
          else:
               room=t[0][3]
               night=t[0][4]
               if (room==1):
                    price=1000*night
               elif (room==2):
                    price=800*night
               elif (room==3):
                    price=600*night
               elif (room==4):
                    price=400*night
          print("Bill Amount: ",price)
          print()
          
              
     elif n==3:
          print("Menu:-")
          print("1. Sandwich  : Dhs 4")
          print("2. Pasta     : Dhs 16")
          print("3. Soup      : Dhs 12")
          print("4. Fruits    : Dhs 8")
          print("5. ComboMeal : Dhs 20")
          print("Enter 0 to stop ordering or any other number to order items")
          
          menu={"1":4,"2":16,"3":12,"4":8,"5":20}
          quant={"1":0,"2":0,"3":0,"4":0,"5":0}
          print()
          n=int(input("Enter 0 or any other number: "))
          
          while(n):
               i = input("Enter Item Number: ")
               q = int(input("Enter Quantity   : "))
               quant[i]=q
               print()
               n=int(input("Enter 0 or any other number: "))

          price = menu["1"]*quant["1"]+menu["2"]*quant["2"]+menu["3"]*quant["3"]+menu["4"]*quant["4"]+menu["5"]*quant["5"]
          print("Order amount: ",price)
          print()
     
     elif n==4:
          s=input("Enter Name : ")
          p=input("Enter phone number : ")
          t = [item for item in d
               if item[0]==s and item[1]==p] 
          if len(t)==0:
               print("No such customer found in database \n")
          else:
               print("Name        : ",t[0][0])
               print("Phone Number: ",t[0][1])
               print("Email       : ",t[0][2])
               print()
               
     elif n==5:
         print("\n THANK YOU !! DO VISIT AGAIN")
         break;

                                                       
                                                                    
