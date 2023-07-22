def printAccount(i):
    print("Ваш баланс: " + str(i))

def verificationAdd(i):
    if i % cratnost == 0:
        return True
    else:
        return False

def nalog():
    global summa
    if summa > limit:
        summa -= summa * wealthTax

def percentageForWithdrawal(i):
    temp = i * 0.015
    if temp < minPop:
        return minPop
    elif temp > maxPop:
        return maxPop
    else:
        return temp
    
def Procent():
    global summa, count
    count += 1
    if count == countSize:
        summa += summa * procent
        count = 0

summa = 0
minPop = 30
maxPop = 600
cratnost = 50
procent = 0.03
count = 0
countSize = 3
limit = 5000000
wealthTax = 0.1
while True:
    print("1 - Внести деньги\n2 - Снять деньги\n3 - Выход")
    action = int(input("Выберите операцию: "))
    if action == 1:
        while True:
            add = int(input("На какую сумму вы хотите пополнить: "))
            nalog()
            if verificationAdd(add):
                summa += add
                Procent()
                printAccount(summa)                
                break
            else:
                print("Вводимая вами сумма должна быть кратна {!s}\nПопробуйте ещё раз".format(cratnost))
    elif action == 2:
        while True:
            pop = int(input("Какую сумму вы хотите снять: "))
            nalog()
            if pop +  percentageForWithdrawal(pop) > summa:
                print("Запрашиваемая вами сумма превышает сумму на счете\nПопробуйте ещё раз")
            else:
                summa -= pop +  percentageForWithdrawal(pop)
                Procent()
                printAccount(summa)
                break
    elif action == 3:
        nalog()
        printAccount(summa)
        break

print("Досвидание")