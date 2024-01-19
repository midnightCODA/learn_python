import math


firstname = 'mbunji'
surname = 'mbunji'

print(type(firstname))
print(type(surname))
print(type(surname))
print(isinstance(surname, str))


# concatenation

first = 'Pedri'
surname = 'Gonzalez'
fullname = first + surname
print(fullname)


# casting a number to a string
decade = str(1980)
print(type(decade))\


# lets test the famous multilines

multiline = '''
    WE WELCOME ALL THE SMOKE
    MAMA PRAY FOR ME SO I WONT FOLD

    ANXIETY
    DONT LET THAT PRESSURE GET TO YOUR HEAD
    YOU KNOW WE PLAY FOR KEEPS 
    DONT LETIT GO OVER YOUR HEAD

    STEADY
'''


multiline += "           "
print(multiline)

print(multiline.replace('DONT', 'DON\'T'))


# THE STRIP METHOD IS USED TO GET RID OF WHITE SPACES
print(len(multiline))
print(len(multiline.strip()))
print(multiline.strip())


# so you can call a string method right after the string itself like so

pythonista = "i love writing python code".upper()

print(pythonista)


menu = "menu".upper()
print(menu.center(40, '='))
print("coffee".ljust(36, '.') + "$23".rjust(4, ' '))
print("beans".ljust(36, '.') + "$3".rjust(4, ' '))
print("sugar".ljust(36, '.') + "$6".rjust(4, ' '))


# string index values

print(first[1:]) # this takes all strings to the end
print(first[1:-1]) # this takes all strings to the end except the last one i.e teh -1 is not taken


# so there are some string methods that helps with checking wether or not something starts with
# or ends with a certain letter

print(first.startswith("D"))
print(first.endswith("i"))


# for bolean dat

isMbunjiGoodOnPython = False


# Integer numbers

price =  100 #price is set into interger directly

alsoprice = int(80)

gpa = 4.10 #this is a float directly no mbambamba

alsoGpa = float(3.98)


# So why do we need to have two ways for doing this?



print(math.pi)
print(math.sqrt(9))
# print(math.)
