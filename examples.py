# -- Exercise 1
#  Memory layout:
#    Address 12 for uint16 'x'
#    Address 4 for string
x = var(12, 'uint16')
name = var(4, 'str')
mov(33, x)
show('X is ', x)
show_memory()
readstr('Enter a name: ', name)
show('X is ', x)
show_memory()

# -- Exercise 2
#  Memory layout:
#    Address 12 for 'password ok' integer
#    Address 4 for input password from user
passok = var(12, 'uint16')
password = var(4, 'str')
mov(0, passok)
readstr('Enter the password: ', password)
if equal(password, 's3cret'):
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
password = var(10, 'str')
real = var(20, 'str')
mov(0, passok)
mov('s3cret', real)
readstr('Enter the password: ', password)
if equal(password, real):
    print('Correct!')
    mov(1, passok)
else:
    print('Incorrect')
if not equal(passok, 0):
    print('You now have superuser privilege')
show_memory()

