# Just codes


<br> <br>


### Variable printing
```python
name = "Foo"
print (name)
```

output:
```
Foo
```

---
<br> <br>

### Finding type
```python
name = "Foo"
print (type(name == str))
```

output:
```
<class 'bool'>
```

---
<br> <br>

### Checking of Data type
```python
name = "Foo"
print (isinstance(name, str))
```

output:
```
True
```

---
<br> <br>

### Datatype

```python
complex 
bool 
list 
tuple 
range 
dict 
set 
```

---
<br> <br>

### Arithmetic Operators

```python
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
4 // 2 #2
```

---
<br> <br>


### String Concatenate

```
+ is also used to concatenate String values:
```

```python
name = "foo"
name += " and bar"
print(name)
```


output:
```
foo and bar
```


```python
print("foo is " + str(8) + " years old") #Roger is
```


### Type Casting

```python
age = int("20")
print(age)

fraction = 0.1
intFraction = int(fraction)

print(intFraction)
```

output:
```
20
0
```

---
<br> <br>

### walrus operator

```python
age = 8
age += 1

print (age)
```

output:
```
9
```


---
<br> <br>

### Comparison Operators

```python
==
!=
>
<
>=
<=
```


```python
a = 1
b = 2
print (a == b) #False
print (a != b) #True
print (a > b )#False
print (a <= b) #True
```

output:
```
False
True
False
True
```

---
<br> <br>


### Boolean Operators


```python
not
and
or
```

```python

# or
print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print('hi' or 'hey') ## 'hi'
print([] or False) ## 'False'
print(False or []) ## '[]'

# and
print(0 and 1) ## 0
print(1 and 0) ## 0
print(False and 'hey') ## False
print('hi' and 'hey') ## 'hey'
print([] and False ) ## []
print(False and [] ) ## False

```

---
<br> <br>


### Bitwise Operators

```python
& : performs binary AND
| : performs binary OR
^ : performs a binary XOR operation
~ : performs a binary NOT operation
<< : shift left operation
>> : shift right operation
```


---
<br> <br>

### `is` and `in`

`is` is called the identity operator

`in` is called the membership operator


---
<br> <br>


### multiline

```python
print ("""
This is 
a multiline
checking.
""")
```

output:
```

This is 
a multiline
checking.

```


```python
print ('''
This is 
a multiline
checking.
''')
```

Same output:
```

This is 
a multiline
checking.

```


---
<br> <br>

### string build-in methods

```

isalpha()       --> to check if a string contains only
characters and is not empty

isalnum()       --> to check if a string contains
characters or digits and is not empty

isdecimal()       --> to check if a string contains digits
and is not empty

lower()       --> to get a lowercase version of a string
islower()       --> to check if a string is lowercase
upper()       --> to get an uppercase version of a string
isupper()       --> to check if a string is uppercase
title()       --> to get a capitalized version of a string

startsswith()    -->  to check if the string starts with a
specific substring

endswith()   --> to check if the string ends with a
specific substring
replace()    --> to replace a part of a string
split()    --> to split a string on a specific character
separator
strip()    --> to trim the whitespace from a string
join()    --> to append new letters to a string
find()    --> to find the position of a substring

and much more...
```

### Few string methods

```python
name = "Foo"
print(name.lower()) #"foo"
print(name) #"Foo"
```


```python
name = "foo"
print(len(name)) #3
```

```python
name = "Amit"
print("mit" in name) #True
```

```Python
name = "Amit"
name[0] #'A'
name[1] #'m'
name[2] #'i'
name[-1] #'t'
```

```python
name = "Roger"
name[0:2] #"Ro"
name[:2] #"Ro"
name[2:] #"ger"
```


### Escape Character

```python
name = "Am\"it" #Am"it
```