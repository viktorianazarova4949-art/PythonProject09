#for перебор

fruits2=['apple','banana','cherry']
for fruit in fruits2:#перебирает лист
    print("I like",fruit)

for letter in "banana":
    print(letter)# перебрал буквы
print("================================================================")
for i in range(5):
    print(i)
print("================================================================")
for i in range(1,5): #от и до
    print(i)
print("================================================================")

for i in range(1,10,2):# шагом
    print(i)
print("================================================================")

#While работаеи пока выполняет условия (Try)
count=1
while count < 5:
    print(count)
    count += 1#увеличим на 1 до
print("================================================================")

n=5
while n > 1:
    print(n)
    n -= 1# уменьшает на 1

print("================================================================")

cash=0 # Накапливает 10 раз
while cash < 100:
    cash += 10
    print("My cash -->", cash)
print("================================================================")

for num in [2,5,6,9,0,3]:
    if num==9:
        print("I found 9")
        break  # закончил когда дошол до 9
    print(num)

print("================================================================")

for number in range(1,11):# чётнын вывести не чётные
    if number % 2 ==0:
        continue
    print("Нечётные:",number)

print("================================================================")

for number in range(1,21):#числа / на 3
    if number % 3 == 0:
        print("divided into 3-->",number)

print("================================================================")
def add(a,b):
    return a+b # функция возврашает результат
res=add(1,2)
print("Sum is -->",add(1,2))
print("================================================================")

def is_even(a):
    return a%2==0# функция с is = True tai Folse

print(is_even(2))
print(is_even(5))

print("================================================================")

def min_max(numbers):
    return min(numbers), max(numbers)
low, high = min_max([7,0,3,15])
print(f"low={low}, high={high}")

print("================================================================")
def sum_list(numbers):
    sum=0
    for num in numbers:
        sum += num
    return sum
print(sum_list([1,2,3,4,5]))# sum lista

print("================================================================")

def avg(numbers):#средние значение
    return sum_list(numbers)/len(numbers)
print(avg([10,20,30]))

my_list = ["dog","cat","mouse","rabbit","house","field"]

def count_words_longer_three_chars(words):#слова больше 3 символов
    counter=0
    for word in words:
        if len(word)>3:
            counter += 1
    return counter
print("Count is -->",count_words_longer_three_chars(my_list))

print("================================================================")

#(a,e,i,o,u) PrivEt

def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():#(text.lower()), чтобы учитывать все гласные независимо от регистра.
        if char in vowels: # Если буква гласная можно так "aeiou"
            count += 1 # Увеличиваем счётчик
    return count#После проверки всех букв возвращаем итоговое количество гласных.

# Пример использования:
text = "PrivEt"
print(count_vowels(text))  # Выведет: 2
print(count_vowels("Python"))








