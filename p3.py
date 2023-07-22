from fractions import Fraction

separator = "/"
arr = input("Введите первую дробь: ").split(separator)
arrA = [int(arr[0]), int(arr[1])]
a = Fraction(arrA[0], arrA[1])

arr = input("Введите вторую дробь: ").split(separator)
arrB = [int(arr[0]), int(arr[1])]
b = Fraction(arrB[0], arrB[1])

c = a+b
print("Сумма: " + str(c))
result = [(arrA[0] * arrB[1] + arrB[0] * arrA[1]), arrA[1]*arrB[1]]
print(str(result[0]) + "/" + str(result[1]))

c = a * b
print("Произведение: " + str(c))
result = [arrA[0] * arrB[0], arrA[1] * arrB[1]]
print(str(result[0]) + "/" + str(result[1]))