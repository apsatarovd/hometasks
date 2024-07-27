# first task
string=input("Введите предложение:")
print(string.upper())

print("--------------------------------------")

#second task
examination = input("Введите число: ")
try:
    examination = int(examination)
    print("Это число.")
except ValueError:
    print("Это не число.")



#third task
worlds = ["iphone", "android","nokia"]
result = ", ".join(worlds)
print (result)

print("--------------------------------------")



#fourth task
# 1 option
text = "Today is my dog's birthday and in honor of this I gave the dog a keychain"
text.replace ("dog" , "cat")

# 2 option
text = input ("Введите предложение:")
result = text.replace ("dog", "cat")
print (result)

