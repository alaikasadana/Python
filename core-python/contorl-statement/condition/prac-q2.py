age = int(input("Enter Your Age :"))
if(0<age<18):
  print(f"You're child")

elif(17<age<61):
   print(f"You're Adult")

elif(60<age):
    print(f"You're senior citizen")

else:
   print("Invalid!")