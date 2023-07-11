# def summaMatric(someMatrica1, someMatrica2,someInt):
#     for i in range(someInt):
#         for j in range(someInt):
#             print(someMatrica1[i][j], end=' ')
#         print()
#     print()
#     for i in range(someInt):
#         for j in range(someInt):
#             print(someMatrica2[i][j], end=' ')
#         print()
#     print('\/ Сумма матрицы равна \/ \n')
#     for i in range(someInt):
#         for j in range(someInt):
#             print(someMatrica1[i][j] + someMatrica2[i][j], end=' ')
#         print()


#
# def printWords(someStrings, someStrings1):
#     someString1 = ''
#     someString3 = ''
#     for i in someStrings:
#         if i.isalpha() or i == " ":
#             someString1 += i.lower()
#     for i in someStrings1:
#         if i.isalpha() or i == " ":
#             someString3 += i.lower()
#     someMatric = someString1.split()
#     someMatric1 = someString3.split()
#     for i in someMatric:
#         if someMatric1.count(i) == 1:
#             print(i)


# def printWords2(someStrings, someStrings1):
#     someString1 = ''
#     someString3 = ''
#     for i in someStrings:
#         if i.isalpha() or i == " ":
#             someString1 += i.lower()
#     for i in someStrings1:
#         if i.isalpha() or i == " ":
#             someString3 += i.lower()
#     someMatric = someString1.split()
#     someMatric1 = someString3.split()
#     for i in someMatric:
#         if someMatric1.count(i) != 1:
#             print(i)