user_name = input('your Name : \n')
user_age = input('Your Age : \n')
user_street = input('Street: \n')
user_city = input('City : \n')
user_addrees = input ('Addrees : \n')

msg = f''' "Name:{user_name }"\n "Age:{user_age}"\n" city:{user_city}"\t
"addrees:{user_addrees}"
"Street:{user_street}\n\n"'''
print(msg)

name = 'Ali'
age = 17
address= 147
city = 'Gaza'

Country = 'palestine'
msg2 = f'''"Hello{name}"\t "Your age is {age}"\tYour is {address,city,Country} "
 '''
print(msg2)
print(type(msg2))

msg3 = f'''"Hello 'ali' , How are yoy "+'your age is '+
 'and your country is:
  'palestaine'\n '''
print(msg3.upper())

msg4 = f'''msg4 = \"\"\"Hello 'Ali' How Are You?
Your Age Is 17
And Your City Is: Gaza
\"\"\"
'''
print(msg4)
name = 'Doaa Reem'
print(name[0],name[3],name[8])
print(name[6:9], name[0:4],name[: :-5])
print(name.replace('a','A'),name.replace('e','E'),)
name2 ='$&$&Mohammed$&$&'
print(name2.strip('$&'))
msg5 = "I%7 python And Although I %7 GSG with Zakria "
print(msg5.replace('%7','love'))

msg6 = 'hello world'
new_msg6 = msg6.title()
print(new_msg6)
msg7= 'hello world'
new_msg7 =msg7.capitalize()
print(new_msg7)



















