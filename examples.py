# -- Exercise 1
#  Memory layout:
#    Address 12 for uint16 'x'
#    Address 4 for string
x = var(12, 'uint16')
mov(33, x)
show('X is ', x)
show_memory()
readstr('Enter a name: ', 4)
show('X is ', x)
show_memory()

# -- Exercise 2
#  Memory layout:
#    Address 12 for 'password ok' integer
#    Address 4 for input password from user
passok = var(12, 'uint16')
mov(0, passok)
readstr('Enter the password: ', 4)
if equalstr(4, 's3cret'):
    print('Correct!')
    mov(1, passok)
else:
    print('Incorrect')
if not equal(passok, 0):
    print('You now have superuser privilege')
show_memory()

# -- Exercise 3
#  Memory layout:
#    Address 8 for passok variable
#    Addresses 10-19 for the input
#    Addresses 20-29 for the correct password
passok = var(8, 'uint16')
mov(0, passok)
putstr('s3cret', 20)
readstr('Enter the password: ', 10)
if equalstr(10, 20):
    print('Correct!')
    mov(1, passok)
else:
    print('Incorrect')
if not equal(passok, 0):
    print('You now have superuser privilege')
show_memory()

