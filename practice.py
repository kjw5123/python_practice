# #6001
# print('Hello')

# #6002
# print('Hello World')

# #6003
# print('Hello')
# print('World')

# #6004
# print("\'Hello\'")

# #6005
# print('\"Hello World\"')

# #6006
# print('\"!@#$%^&*()\'')

# #6007
# print('\"C:\\Download\\\'hello\'.py\"')

# #6008
# print('print("Hello\\nWorld")')

# #6009
# a = input()
# print(a)

#6010
# a = input()
# a = int(a)
# print(a)

#6011
# a = input()
# a = float(a)
# print(a)

#6012
# a = int(input())
# b = int(input())
# print(a)
# print(b)

#6013
# a = input()
# b = input()
# print(b)
# print(a)

#6014
# a = float(input())
# for i in range(3):
#     print(a)

#6015
# a, b = map(int, input().split(' '))
# print(a)
# print(b)

#6016
# a, b = map(str, input().split(' '))
# print(b, a)

#6017
# a = input()
# for i in range(3):
#     print(a, end=' ')
#또는 print(a, a, a)

#6018
# a, b = map(int, input().split(':'))
# print(a, ':', b, sep='')

#6019
# y, m, d = map(int, input().split('.'))
# print(d, m, y, sep = '-')

#6020
# a, b = input().split('-')
# print(a, b, sep='')

#6021
# a = input()
# for i in range(len(a)):
#     print(a[i])

#6022
# a=input()
# for i in range(len(a)):
#     print(a[2*i], a[2*i+1], sep='', end=' ')

#or

# a = input()
# print(a[0:2], a[2:4], a[4:6])

#6023
# a, b, c = input().split(':')
# print(b)

#6024
# a, b = input().split(' ')
# print(a + b)

#6025
# a, b = map(int, input().split(' '))
# print(a + b)

#6026
# a = float(input())
# b = float(input())
# print(a+b) 

#6027
# a = int(input())
# print('%x' %a)

#6028
# a = int(input())
# print('%X' %a)

#6029
# a= input()
# b = int(a, 16)
# print('%o' %b)

#6030
# a = ord(input())
# print(a)

#6031
# a = int(input())
# print(chr(a))

#6032
# a = int(input())
# print(-a)

#6033
# a = int(ord(input())) + 1
# print(chr(a))

#6034
# a, b = map(int, input().split(' '))
# print(a - b)

#6035
# a, b = map(float, input().split(' '))
# print(a*b)

#6036
# a, b = input().split(' ')
# b = int(b)
# print(a * b)

#6037
# a = input()
# a = int(a)
# b = input()
# print(b * a)

#6038
# a, b =  map(int, input().split(' '))
# print(a ** b)

#6039
# a, b = map(float, input().split(' '))
# print(a ** b)

#6040
# a, b = map(int, input().split(' '))
# print(a // b)

#6041
# a, b = map(int, input().split(' '))
# print(a % b)

#6042
# a= float(input())
# a = format(a, '.2f')
# print(a)

#6043
# a, b = map(float, input().split(' '))
# print(format(a / b, '.3f'))

#6044
# a, b = map(int, input().split(' '))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(format(a / b, '.2f'))

#6045
# a, b, c = map(int, input().split(' '))
# total = a + b + c
# average = format(total / 3, '.2f')

# print(total, end = ' ')
# print(average)

#6046
# a = int(input())
# print(a<<1)

#6047
# a, b = map(int, input().split(' '))
# print(a<<b)

#6048
# a, b = map(int, input().split())
# if a < b:
#     print(True)
# else:
#     print(False)

#6049
# a, b = map(int, input().split())
# if a == b:
#     print(True)
# else:
#     print(False)

#6050
# a, b = map(int, input().split(' '))
# if b >= a:
#     print(True)
# else:
#     print(False)

#6051
# a, b = map(int, input().split(' '))
# if a != b:
#     print(True)
# else:
#     print(False)

#6052
# a = int(input())
# if a == 0:
#     print(False)
# else:
#     print(True)

#6053
# a = int(input())
# print(not a)

#6054
# a, b = map(int, input().split(' '))
# if bool(a) and bool(b) == True:
#     print(True)
# else:
#     print(False)

#6055
# a, b = map(int, input().split())

# if bool(a) or bool(b) == True:
#     print(True)
# else:
#     print(False)

#6056
# a, b = map(int, input().split(' '))
# if bool(a) != bool(b):
#     print(True)
# else:
#     print(False)

#6057
# a, b = map(int, input().split(' '))
# if bool(a) == bool(b):
#     print(True)
# else:
#     print(False)

#6058
# a, b = map(int, input().split(' '))
# if (bool(a) or bool(b)) == True:
#     print(False)
# else:
#     print(True)

#6059
# a = int(input())
# print(~a)

#6060
# a, b = map(int, input().split())
# print(a&b)

#6061
# a, b = map(int, input().split())
# print(a|b)

#6062
# a, b = map(int, input().split())
# print(a ^ b)

#6063
# a, b = map(int, input().split())
# if a < b:
#     print(b)
# else:
#     print(a)

# or

# a, b = map(int, input().split())
# c =a if a > b else b
# print(int(c))

#6064

# a, b, c = map(int, input().split())

# d = [a, b, c]
# print(min(d))

#6065
# a, b, c = map(int, input().split())
# d = [a, b, c]
# i = 0
# while i < len(d):
#     if d[i] % 2 != 0:
#         i += 1
#     elif d[i] % 2 == 0:
#         print(d[i])
#         i += 1

#6066
# a, b, c = map(int, input().split())
# d = [a, b, c]
# i = 0
# while i < len(d):
#     if d[i] % 2 == 0:
#         print('even')
#         i += 1
#     elif d[i] % 2 == 1:
#         print('odd')
#         i += 1

#6067
# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print('A')
#     elif a % 2 == 1:
#         print('B')
# elif a > 0:
#     if a % 2 == 0:
#         print('C')
#     elif a % 2 == 1:
#         print('D')

#6068
# a = int(input())
# if 90 <= a <= 100:
#     print('A')
# elif 70 <= a < 90:
#     print('B')
# elif 40<= a < 70:
#     print('C')
# elif 0 <= a < 40:
#     print('D')

#6069
# a = input()
# if a == 'A':
#     print('best!!!')
# elif a == 'B':
#     print('good!!')
# elif a == 'C':
#     print('run!')
# elif a == 'D':
#     print('slowly~')
# else:
#     print('what?')

#6070
# a = int(input())

# if 3<= a < 6:
#     print('spring')
# elif 6 <= a < 9:
#     print('summer')
# elif 9 <= a < 12:
#     print('fall')
# elif a == 12 or 1 or 2:
#     print('winter')

#6071
# i = int(input())
# while i != 0:
#     print(i)
#     i = int(input())

#6072
# i = int(input())
#
# while i != 0:
#     print(i)
#     i -= 1

#6073
# i = int(input())
# while i > 0:
#     i -= 1
#     print(i)

#6074
# some = ord(input())
# a = ord('a')
#
# while a <= some:
#     print(chr(a))
#     a += 1

#6075
# a = int(input())
# b = 0
# while b <= a:
#     print(b)
#     b += 1

#6076
# a = int(input())
# for i in range(a + 1):
#     print(i)

#6077
# a = int(input())
# b = 0
# for i in range(a + 1):
#     if i % 2 == 0:
#         b += i
# print(b)

#6078
# a = input()
# while a != 'q':
#     if a != 'q':
#         print(a)
#         a = input()
# print(a)

#6079
#당연히 while로도 가능하지만 다시 작성하기 귀찮다.
# a = int(input())
# b = 0
# for i in range(10000):
#     b += i
#     if b >= a:
#         print(i)
#         break

#6080
# a, b = map(int, input().split())
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)

#6081
# a = input()
# X_a = int(a, 16)
# for i in range(1, 16): #이 놈들이 16진수를 자꾸 문자열로 인식함
#     result = '{0:X}'.format(X_a*i) # 이거 앵간하면 문자로 표현 됨
#     X_i = '{0:X}'.format(i)
#     print('%s*%s=' %(a, X_i), result, sep = '')

#6082       
# a = int(input())
# for i in range(1, a+1):
#     i_a = i % 10
#     if i_a != 0:
#         i_b = i_a % 3
#     else:
#         i_b = 1
#     if i_b == 0:
#         print('X', end = ' ')
#     else:
#         print(i, end = ' ')

# 6083
# r, g, b = map(int, input().split())

# a = 0

# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             a += 1
# print(a)

# 6084
# h, b, c, s = map(int, input().split())
# memory = h*b*c*s/8/1024/1024
# print(format(memory, '.1f'), 'MB')

#6085
# w, h, b = map(int, input().split())
# memory = format(w*h*b/8/1024/1024, '.2f')
# print(memory, 'MB')

#6086
# a = int(input())
# i = 1
# total = 0
# while total < a:
#     total += i
#     i += 1
#     if total >= a:
#         print(total)
#         break

#6087
# a = int(input())

# for i in range(1, a + 1):
#     if i % 3 != 0:
#         print(i, end = ' ')
#     else:
#         continue

#6088
# a, d, n = map(int, input().split())
# num = a
# print(a + d*(n -1))

#6089
# a, r, n = map(int, input().split())
# num = a
# for i in range(2, n+1):
#     num *= r
# print(num)

#6090
# a, m, d, n = map(int, input().split())

# num = a
# for i in range(2, n+1):
#     num *= m
#     num += d
# print(num)

#6091
# a, b, c = map(int, input().split())

# d = 1 
# while d % a != 0 or d % b != 0 or d % c != 0:
#     d += 1

# print(d)

#6092
# a = int(input())
# b = []
# for i in range(1, 24):
#     b.append(0)

# c = map(int, input().split())
# c = list(c)

# for j in c
#     b[j-1] += 1
# for k in b:
#     print(k, end = ' ')

#6093
# a = int(input())
# c = a
# b = map(int, input().split())
# b = list(b)
# for i in range(a, 0, -1):
#     c -= 1
#     print(b[c], end = ' ')

#6094
# a = int(input())
# b = map(int, input().split())
# b = list(b)
# print(min(b))

#6095
# n = int(input())
# a = []
  
# for i in range(n):
#     a.append(list(map(int, input().split())))

# for i in range(1, 20):
#     for j in range(1, 20):
#             if [i, j] in a:
#                 print(1, end = ' ')
#             else:
#                 print(0, end = ' ')
#     print('')

#6096
bdp = [] #바둑판
for i in range(19):
    bdp.append(list(map(int, input().split())))

n = int(input())

for i in range(n):
    z = list(map(int, input().split()))
    z[0] -= 1
    z[1] -= 1
    for j in range(19):
        for k in range(19):
            if k == z[1] and j == z[0]:
                for g in range(19):
                    if bdp[j][g] == 1:
                        bdp[j][g] = 0
                    else:
                        bdp[j][g] = 1
                for g in range(19):
                    if bdp[g][k] == 1:
                       bdp[g][k] = 0
                    else:
                       bdp[g][k] = 1

for i in range(19):
    for k in range(19):
        print(bdp[i][k], end = ' ')
    print()

#6097
# a, b = map(int, input().split())
# play = int(input())
# pan = [] #설탕뽑기 판때기
# for i in range(a):s
#     pan.append([])
#     for j in range(b):
#          pan[i].append(0)

# i = 0

# while i < play:
#     l, d, x, y = map(int, input().split())
#     if d == 0:
#         for j in range(l):
#             pan[x-1][y-1+j] = 1
#     elif d == 1:
#         for k in range(l):
#             pan[x-1+k][y-1] = 1
#     i += 1

# for i in range(a):
#     for j in range(b):
#         print(pan[i][j], end = ' ')
#     print()

# 대망의 6098
house = []
for i in range(10):
    house.append(list(map(int, input().split())))

house[1][1] = 9

sample = True

for i in range(10):
    for j in range(10):
        if house[8][8] == 9:
            sample = False
            break
        if 1<= i <= 8 and 1<= j <= 8:
            if house[i][j] == 9:
                if house[i+1][j] == 2 and house[i][j+1] != 0:
                    house[i+1][j] = 9
                    sample = False
                    break
                if house[i][j+1] == 2:
                    house[i][j+1] = 9
                    sample = False
                    break
                if house[i][j+1] == 0:
                    house[i][j+1] = 9
                if house[i][j+1] == 1:
                    house[i+1][j] = 9
                    break
    if (sample == False):
        break



        
for i in range(10):
    for j in range(10):
        print(house[i][j], end = ' ')
    print()


        # if 1 <= i <= 8:
        #     if house[i][j] == 0:
        #             for k in range(1, i+1): # 9 검사 for 문
        #                 if house[k][j] == 9: # 위에 9가 있다?
        #                     house[i][j] = 0
        #                     break # 9 있으면 그냥 바로 0 맥이고 9 검사 for문 끝내버림
        #                 if house[k][j] != 9:
        #                     if house[i][j+1] == 1:
        #                         house[i][j] = 9
        #                         if house[i+1][j] == 0:
        #                             house[i+1][j] = 9
        #                             break
        #     if house[i][j] == 9:
        #         if house[i][j+1] == 0:
        #             house[i][j+1] = 9
        #         if house[i][j+1] == 1:
        #             if house[i+1][j] == 0:
        #                 house[i+1][j] = 9
        #         if house[i+1][j] == 2:
        #             house[i+1][j] = 9
        #             break
        #         if house[i][j+1] == 2:
        #             house[i][j+1] = 9
        #             break
                


            
# for i in range(10):
#     for j in range(10):
#         if house[i][j] == 2:
#             house[i][j] = 9
#             break
#         if house[i][j] == 0:
#             for k in range(i):
#                 if house[k][j] == 9:
#                     if house[i][j] == 9:
#                         break
#                     else:
#                         house[i][j] = 0
#                         break
#                 else:
#                     house[i][j] = 9
#             if house[i][j+1] == 1: #오른 쪽이 1로 막혔을  때
#                 house[i+1][j] = 9
#                 break

