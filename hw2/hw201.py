def oddOrEven(n):
        print("Поскільки ділення ",n," на 2 дає в остатку ",n%2)
        if ((n%2)==0):print("Число ",n," є парним")
        else:print("Число",n," є непарним")
try:
    num=int(input("Введи ціле число "))
    oddOrEven(num)
except ValueError:print("Треба ввести тільки число і тільки ціле")