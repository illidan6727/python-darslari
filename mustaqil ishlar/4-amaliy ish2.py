# LIST=["lola","diyora","diyora","diyora","diyora"]
# print(LIST[::2]) //qadam tashlash

# print(LIST[::-1]) orqa tomonga chiqarish
# print(LIST[3:6])

# print("diyora" in LIST )

# for index in  range(len(LIST)):
#     print(f"index = {index}, value= {LIST}")



# LIST.append("rayhon")
# # print(LIST)
# LIST.insert(2,"maftuna")
# print(LIST)
# LIST.pop() //Listdan index bo'yicha o'chiradi
# print(LIST)
# LIST.remove("diyora") Listdan nomi bo'yicha o'chiradi
# print(LIST)

# del LIST  o'zgaruvchini o'chirib yuboradi\
# LIST.sort(reverse=True) teskari tartiblash

# print(LIST)

# LIST [2]="bunyod"
# # print(LIST)
#
# # print(LIST.count("azizbek"))
#
#
#
# LIST=["lola","diyora","diyora","diyora","diyora"]
# cars=["mers","sonata","audi"]
# # print(LIST.index("diyora"))
# LIST.extend(cars) #listlarni bir biriga qo'shadi
# # print(LIST)
#
# LIST.extend(["damas","malibu"])
# # print(LIST)
#
# list_elementlari_soni=len(LIST)
#
# for index in range(list_elementlari_soni):
#     print(f"index={index}, car={LIST[index]}")


# numbers=[1,2,3,4,5,6,7,8,9,10]
# #
# # newlist=[]
# # for i in numbers:
# #     if i%2==0:
# #         newlist.append(i**2)
# # print(newlist)
#
# son=numbers.copy()
# son.remove(4)
# print(son)
# print(numbers)
u=0
r=0
x='stop'
n=int(input("nechta son kiritmoqchisiz="))
for i in range(0,n):
    r=int(input("qo'shiladigan sonni kiriting="))
    if r==x:
        continue
    else:
        u=u+r

print("jami sonlar yig'indisi",u)

