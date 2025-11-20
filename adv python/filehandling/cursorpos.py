#tell( ) - it shows current position of cursor
#  and seek( ) - through this we moves our cursor to get required position

#tell( ) 
#append mode
# with open("c1.txt","a+") as f :
#     print(f.tell())

#read mode
# with open("c1.txt","r+") as f :
#     print(f.tell())

# with open("c1.txt","r+") as f :
#     print(f.tell())
#     data = f.read(10)
#     print(data)
#     print(f.tell())

#==================================================================================================================
#seek( )
#syntax: ("no of moved bits" , "from whuch position")
# with open("p1.txt","ab+") as f:
#     print(f.tell())
#     data=b'this is python'
#     f.write(data)
#     print(f.tell())
#     data1= f.read()
#     print(data1)
#     f.seek(0,0)
#     print(f.tell())


# with open("p1.txt","rb+") as f:
#     print(f.tell())
#     f.read(10)
#     print(f.tell())
#     f.seek(-5,1)
#     print(f.tell())




