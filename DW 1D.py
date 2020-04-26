# def decompose(n,dic):
#     print(n)
#     if n == 0:
#         return dic
#     if n == 1:
#         dic['1'] += 1
#         return dic
#     if n >= 200:
#         if not dic:
#             dic['200'] = 1
#             return decompose(n-200,dic)
#         dic['200'] += 1
#         return decompose(n-200,dic)
#     if n >= 100:
#         if not dic:
#             dic['100'] = 1
#             return decompose(n-100,dic)
#         dic['100'] += 1
#         return decompose(n-100,dic)
#     if n >= 50:
#         if not dic:
#             dic['50'] = 1
#             return decompose(n-50,dic)
#         dic['50'] += 1
#         return decompose(n-50,dic)
#     if n >= 20:
#         if not dic:
#             dic['20'] = 1
#             return decompose(n-20,dic)
#         dic['20'] += 1
#         return decompose(n-20,dic)
#     if n >= 10:
#         if not dic:
#             dic['10'] = 1
#             return decompose(n-10,dic)
#         dic['10'] += 1
#         return decompose(n-10,dic)
#     if n >= 5:
#         print(dic)
#         if not dic:
#             print(dic)
#             dic['5'] = 1
#             print(dic)
#             return decompose(n-5,dic)
#         dic['5'] += 1
#         return decompose(n-5,dic)
#     if n >= 2:
#         print(n,dic)
#         if not dic or not '2' in dic.keys():
#             print(n, dic,'hi')
#             dic['2'] = 1
#             print(dic)
#             return decompose(n-2,dic)
#         dic['2'] += 1
#         return decompose(n-2,dic)
# 
# 
# def tester(n,minus):
# 
# 
#     return n
# 
# def decompose2(n, lst   ):
#     print('start', n)
#     if n == 1:
#         print(1)
#         decompose2(n-1)
#     if n == 0:
#         print('end')
#         return
#     while n > 1:
#         if n >= 200:
#             print(200)
#             decompose2(n-200)
#         if n >= 100:
#             print(100)
#             decompose2(n - 100)
#             pass
#         if n >= 50:
#             print(50)
#             decompose2(n - 50)
#             pass
#         if n >= 20:
#             print(20)
#             decompose2(n - 20)
#             pass
#         if n >= 10:
#             print(10)
#             decompose2(n - 10)
#             pass
#         if n >= 5:
#             print(5)
#             decompose2(n - 5)
#             pass
#         if n >= 2:
#             print(2)
#             return decompose2(n - 2)
# 
# 
# 
# 
# print(decompose2(7))
# 
# 
# lst = ['3','2']
# lst2 = lst[0]
# lst3 = ['3']
# 
# print(id(lst),id(lst2))

import numpy as np

years = [int(i**2) for i in range(4,10)]

A = [[1.0]*len(years),years]
A = np.transpose(A)
B = [65.0,71.0,73.0,74.5,77.5,79.0]



ATA = np.matmul(np.transpose(A),A)
print(ATA,'ATA')
ATA_inv = np.linalg.inv(ATA)

print(ATA_inv,'ATA_inv')

c = np.matmul(np.matmul(ATA,np.transpose(A)),B)


print(c,'c')

import matplotlib

import numpy as np

years = [int(i**2) for i in range(4,10)]

new_years =  [int(i**3) for i in range(4,10)]
A = [[1.0]*len(years),years,new_years]
A = np.transpose(A)
B = [65.0,71.0,73.0,74.5,77.5,79.0]



ATA = np.matmul(np.transpose(A),A)
print(ATA,'ATA')
ATA_inv = np.linalg.inv(ATA)

print(ATA_inv,'ATA_inv')

c = np.matmul(np.matmul(ATA,np.transpose(A)),B)


print(c,'c')

import math
import matplotlib

years = [math.log(i) for i in range(4,10)]

new_years =  [int(i**3) for i in range(4,10)]
A = [[1.0]*len(years),years]
A = np.transpose(A)
print(A)
B = [65.0,71.0,73.0,74.5,77.5,79.0]
B = [math.log(i) for i in B]
print(B)


ATA = np.matmul(np.transpose(A),A)
print(ATA,'ATA')
ATA_inv = np.linalg.inv(ATA)

print(ATA_inv,'ATA_inv')

c = np.matmul(np.matmul(ATA,np.transpose(A)),B)


print(c,'c')

import matplotlib