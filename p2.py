table = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
result = "0x"

def isInt(text):
    try:
        i = int(text)
    except:
        return False
    return True

def Result(i):
    if i < 10:
        return str(i)
    else:
        return table[i]


a = input("Введите число: ")
if isInt(a):
    i = int(a)
    print("i in hex = " + hex(i))
    while True:
        temp1 = i // 16
        temp2 = i % 16
        if temp1 != 0:
            i = temp1
            result = result + Result(temp2)
        else:
            result = result + Result(temp2)
            break
    
    print(result)
else:
    print("Это не целое число")