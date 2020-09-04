

a = "abc"
b = "def"
c = a + b
print(c)

if a.startswith('a'):
    print('start with a')
else:
    print ('not start with a')

for char in a:
    print(char)

i = 0
while i <= 5:
    print(a)
    i = i + 1

print(a.upper())
print(a.find('b'))


print('He said, "What\'s there?"')

print(2 + 3)
print('2' + '3')

mystring = "abcdefg"
print(mystring[2:])
print(mystring[:2])
print(mystring[1:3])
print(mystring[::])
print(mystring[::2])
print(mystring[::-1])
print(mystring.upper())


print('The {} {} {}'.format('fox','brown','quick'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

result=100/777
print(result)
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))

name= "Jose"
print(f'Hello, his name is {name}')

print("add a line")