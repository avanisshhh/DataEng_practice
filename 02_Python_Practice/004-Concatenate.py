
x = "hello"  + " world"
print(x)
#OP: hello world

10 + 10
#OP: 20

10 + "10"
#OP: TypeError: unsupported operand type(s) for +: 'int' and 'str'

10 + int("10")
#OP: 20
  

int("a")
#OP: ValueError: invalid literal for int() with base 10: 'a'

str(10) + "10"
#OP: 1010

