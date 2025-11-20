# l = list(range (1,10))
# x=iter(l)
# # print(x)
# # print(next(x))
# # print("Hellow")
# # print(next(x))

# for i in range(15):
#     print(next(x))


##===========================================================================================================================


l = list(range (1,10))
x=iter(l)


for i in range(15):
    try:
         print(next(x))
    except StopIteration:
        print("iterator is empty")
        break