'''
Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между 
дольками (то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
'''
n = int(input('Длина плитки шоколадки в дольках: '))
m = int(input('Ширина плитки шоколадки в дольках: '))
print('Какое кол-во долек необходимо отломить?')
k = int(input())
if k%n == 0 or k%m == 0:
    print('Yes')
else:
    print('No')    

