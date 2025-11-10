# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

    
#=====================================================================


# while True:
#     print("1.addition \n 2)sub \n3)multiplicatipn \n 4)division \n5)off")
#     n=int(input("Enter any option : "))
#     x=(1,2,3,4,5)
#     if n in x :
#         y=(1,2,3,4)
#         if n in y :
#              pass
#         else:
#             break
#     else:
#         print("please enter valid option")

#=====================================================================


while True:
    print("1.addition \n 2)sub \n3)multiplicatipn \n 4)division \n5)off")
    n=int(input("Enter any option : "))
    x=(1,2,3,4,5)
    if n in x :
        y=(1,2,3,4) 
        if n in y :
            if n==1:
                tn = int(input("how many numbers you want to add"))
                l=[]
                for i in range (1,tn+1):
                    value=float(input(f"enter value for {i} : "))
                    l.append(value)
                sum=0
                for i in l:
                    sum=sum+i
                print(f"sum of given values {i} is {sum}")

        else:
          break
    else:
        print("please enter valid option")
    
