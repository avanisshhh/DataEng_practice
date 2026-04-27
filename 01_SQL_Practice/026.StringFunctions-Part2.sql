SELECT REPLACE('hello','e','x')

SELECT REPLACE('hello','l','x')

SELECT REPLACE('hello','e','xy')

SELECT REPLACE('hello','el','x')

SELECT REPLACE('hello','e','')

SELECT REPLACE('hello','e',' ')

SELECT REVERSE('HELLO')

SELECT REVERSE(EnglishProductName) FROM DimProduct

SELECT STUFF('hello',2,3,'x')
-- The STUFF function is used to insert a string into another string, while also deleting a specified number of characters from the original string. In this case, the function takes the string 'hello', starts at the second character (which is 'e'), deletes 3 characters ('ell'), and then inserts 'x' in place of the deleted characters. The result of this operation will be 'hxo', as 'e', 'l', and 'l' are removed and replaced with 'x'.
SELECT REPLACE('hello','l','x')

SELECT STUFF('hello',4,1,'x')