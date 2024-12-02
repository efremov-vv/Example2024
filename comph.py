"""print()
print([i / j for i in range(1, 4) for j in range(4, 7)])
str1 = [str(i) + '^2=' + str(i ** 2) for i in range(1, 10)]
print('\n'.join(str1))
print(' '.join(input().split()[2::3]))
print('\n'.join(str(i ** 2) for i in range(int(input()))))
print()"""
print(' '.join([str(int(i) ** 2) for i in input().split() if int(i) % 2 != 0 and i[-1] != '9']))

name = "аркадий"
age = 14
print(f"меня зовут {name} мне {age} лет.")
print("меня зовут " + name + " мне " + str(age) + " лет.")
print("меня зовут", name, "мне", age, "лет.")

s = "зелёный клён"
s = s.strip()
s = s.lower()
s = s.replace('ё','е')
print(s)

s = "зелёный клён"
print(s.strip().lower().replace('ё','е'))
