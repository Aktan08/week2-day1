#список гостей 
list_ = ["adi","madi","fodi","alisa","malisa"]
message3 = " ОТПРАВЛЕНО ПРИГЛАШЕНИЕ:"
print (list_[0]+message3 ) 
print (list_[1]+message3 )
print (list_[2]+message3 ) 
print (list_[3]+message3 )


message = " ПРИДЕТ"
message_second =" НЕ ПРИДЕТ"
print("")
print ("СПИСОК ГОСТЕЙ:")
print("")
print (list_[0]+message ) 
print (list_[1]+message )
print (list_[2]+message_second ) 
print (list_[3]+message )

#замена
print("")
print ("FODI НЕ СМОЖЕТ ПРИДТИ ВЫБЕРИТЕ ДРУГОГО ЧЕЛОВЕКА :" )
print("")
#удаление

list_.pop(2)

#новый чел

name = input()
list_.append(name) 


#рассширение списка гостей
print("")
print("РАСШИРЕНИЕ ПОЗВЕМ ЕЩЕ ТРЕХ ЧЕЛОВЕК :")
print("")

print ("ВЫБЕРИТЕ ГОСТЯ :" )
name_1 = input()
print ("ВЫБЕРИТЕ ЕЩЕ ОДНОГО ГОСТЯ :" )
name_2 = input()
print ("ВЫБЕРИТЕ ЕЩЕ ОДНОГО ГОСТЯ :" )
name_3 = input()

list_.insert(0,name_1)
list_.insert(3,name_2)
list_.append(name_3)

print("")
print(list_[0]+" "+list_[1]+" "+list_[2]+" "+list_[3]+" "+list_[4]+" "+list_[5]+" "+list_[6]+" "+list_[7])
print("")
#сокращение списка гостей 
# for element in range(len(list_)):
#     if element == list_[1]:
#         list_.pop(-1)
#     break
list_.pop(-1)
print("SEND MESSAGE:МНЕ ОЧЕНЬ ЖАЛЬ ЧТО Я НЕ МОГУ ВАС ПОЗВАТЬ, "+list_[-1])
list_.pop(-1)
print("SEND MESSAGE:МНЕ ОЧЕНЬ ЖАЛЬ ЧТО Я НЕ МОГУ ВАС ПОЗВАТЬ, "+list_[-1])
list_.pop(-1)
print("SEND MESSAGE:МНЕ ОЧЕНЬ ЖАЛЬ ЧТО Я НЕ МОГУ ВАС ПОЗВАТЬ, "+list_[-1])
list_.pop(-1)
print("SEND MESSAGE:МНЕ ОЧЕНЬ ЖАЛЬ ЧТО Я НЕ МОГУ ВАС ПОЗВАТЬ, "+list_[-1])
list_.pop(-1)
print("SEND MESSAGE:МНЕ ОЧЕНЬ ЖАЛЬ ЧТО Я НЕ МОГУ ВАС ПОЗВАТЬ, "+list_[-1])
list_.pop(-1)

print("")
print("SEND MESSAGE:ПРИХОДИТЕ К 18:00, "+list_[0])
print("SEND MESSAGE:ПРИХОДИТЕ К 18:00, "+list_[1])
