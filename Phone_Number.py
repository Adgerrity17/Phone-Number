
#Finding patterns in text without regular expressions

def isPhoneNumber(text):
    if len(text) != 12: #if the lenght doesn't equal 12 break
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #if the 4th value isn't a dash break the code
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print ('415-555-4242 is a phone number')
print (isPhoneNumber('415-555-4242'))
print ('Hideo Notsu is a phone number')
print (isPhoneNumber('Hideo Notsu'))

