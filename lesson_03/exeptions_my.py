#обход ошибок с их указанием но код продолжает рботать
try:# этот блок даёт знать об ошибке но код продолжает рботать
    res=10/0
    print("Res is", res)
except ZeroDivisionError:
    print("Division by zero")



input_str="avf"
input_str1="67"

try:
    number=int(input_str)
    print(number)
except ValueError:
    print("Only integers")

print("Hi")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError:
        print("Type error")

print(divide(1, 2))
divide(1, 0)
divide(1, "0")

print("==========================================================")

#number=[1,2,3]
#print(number[4])#IndexError: list index out of range

try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print(e)
    print(type(e).__name__)

def divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(e)
divide(1, "python")
print("=========================================================")

#data={"name":"John","age":22}
#print(data["email"])#KeyError: 'email'

try:

     data={"name":"John","age":22}
     print(data["email"])
except KeyError:# ожидаемую ошибку ставят первой
    print("Key error")
except Exception:
    print("Unexpected error")

print("=========================================================")
try:
    number = int("456")
except ValueError:
    print("Only integer")
else:# если не попали в ошибку кад выполняется
    print("Success, it is a number: ", number)
print("=========================================================")

try:
    print("Try part")
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:#этот блок выполнится в любом случаи
    print("Always finished")
print("=========================================================")

def type_age(age):
    try:
        age = int(age)
    except (TypeError, ValueError):
        print("Type error or Value Error")
    else:
        print("Success, it is a number: ", age)
    finally:
        print("Type age")

type_age("25")
type_age("hundred")

