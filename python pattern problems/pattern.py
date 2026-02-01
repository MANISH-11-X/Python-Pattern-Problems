# pattern 1
# n = int(input("Enter number of rows:"))

# for i in range(n): #rows
#     for j in range(n): #columns
#         print('*',end=' ')
#     print()

# pattern 2 ==
# n = int(input("Enter number of rows:"))

# for i in range(n): #rows
#     for j in range(i+1): #columns
#         print('*',end=' ')
#     print()

# pattern 3

# n = int(input("Enter number of rows:"))

# for i in range(n): #rows
#     for j in range(i,n): #columns
#         print('*',end=' ')
#     print()  #new row/line

# pattern 4

# n = int(input("Enter number of rows:"))

# for i in range(n): #rows
#     for j in range(i,n): #columns
#         print('',end=' ')
#     for j in range(i+1):
#         print('*',end='')
#     print()  #new row/line

# pattern 5

# n = int(input("Enter number of rows:"))

# for i in range(n): #rows
#     for j in range(i+1): #columns
#         print('',end=' ')
#     for j in range(i,n):
#         print('*',end='')
#     print()  #new row/line

# pattern 6
# n = int(input("Enter number of rows:"))

# for i in range(n): #rows

#     for j in range(i,n): #columns
#         print('',end=' ')

#     for j in range(i):
#         print('*',end='')

#     for j in range(i+1):
#         print('*',end='')

#     print()  #new row/line

#pattern 7

n = int(input("Enter number of rows:"))

for i in range(n): #rows

    for j in range(i+1): #columns
        print('',end=' ')

    for j in range(i,n-1):
        print('*',end='')
 
    for j in range(i,n): #columns
        print('*',end='')
    
    print()

#pattern 8

