print([i / j for i in range(1, 4) for j in range(4, 7)])

#Комментарий
str1 = [str(i) + '^2=' + str(i ** 2) for i in range(1, 10)]
print('\n'.join(str1))


print('\n'.join(str(i ** 2) for i in range(int(input()))))
