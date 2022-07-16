def transformStr(txt):
         shrttxt=txt[:5]
         print("Новий текст з довжиною в -",len(shrttxt),"символів","\n"+"-"*10)
         if (txt[0]=='l' or txt[0]=='L'):print(shrttxt.lower())
         elif (txt[0]=='u' or txt[0]=='U'):print(shrttxt.upper())
         else:print(shrttxt+"...")
         print("-"*10)
str=input("Введи текст не менше п'яти символів ")
print("Ваш текст",str,"має довжину-",len(str),"і починається на літеру-",str[0])
if ((len(str)>=5) and (str.isalpha())):transformStr(str)
else:print("-"*10,"\nТреба було ввести тільки літери і не менше п'ятьох\n","-"*10)