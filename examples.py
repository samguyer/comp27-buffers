# -- Exercise 1
#  Memory layout:
#    Address 4 for string
#    Address 12 for uint16 'x'
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
#    Address 4 for input password from user
#    Address 12 for 'password ok' integer
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


# -- Exercise 4
#  Memory layout:
#  Addresses 4,6,8 for values
#  Address 12 for payload
#  Address 20+ for other data
size = var(4, 'uint16')
p = var(6, 'uint16')
val = var(8, 'uint8')
payload = var(12, 'str')
otherdata = var(20, 'str')
mov('Secret', otherdata)
read('Size: ', size)
readstr('Payload: ', payload)
mov(10, p)
while not equal(size, 0):
    load(p, 'uint8', val)
    show('', val)
    add(1, p)
    sub(size, 1)
show_memory()
