"""4. Изменение списка гостей: вы только что узнали, что один из гостей прийти не сможет,

поэтому вам придется разослать новые приглашения. Отсутствующего гостя нужно заме-
нить кем-то другим.

• Начните с программы из упражнения 3. Добавьте в конец программы команду print
для вывода имени гостя, который прийти не сможет.
• Измените список и замените имя гостя, который прийти не сможет, именем нового
приглашенного.

• Выведите новый набор сообщений с приглашениями – по одному для каждого участ-
ника, входящего в список.
"""
#список гостей 

list_ = ["adi","madi","fodi","bedi"]
message = " придет"
message_second =" не придет"
print (list_[0]+message ) 
print (list_[1]+message )
print (list_[2]+message_second ) 
print (list_[3]+message )

#замена

print ("fodi не сможет придти выберите другого человека" )

#удаление

list_.pop(2)

#новый чел

name = input()
list_.append(name) 

#вывод

print(list_[0]+" "+list_[1]+" "+list_[2]+" "+list_[3]+" ")