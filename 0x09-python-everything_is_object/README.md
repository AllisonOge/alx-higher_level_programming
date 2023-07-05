python everything is object readme

Answers to the following questions
- What is the function to get the type of an object? (Ans: `0-answer.txt`)
- What is the function to get the unique variable identifier-the memory address in a the CPython implementation? (Ans: `1-answer.txt`)
- Do the variables `a` and `b` in the following code point to the same object? (Ans: `2-answer.txt`)
```python
>>> a = 89
>>> b = 100
```
- Do the variables `a` and `b` in the following code point to the same object? (Ans: `3-answer.txt`)
```python
>>> a = 89
>>> b = 89
```
- Do the variables `a` and `b` in the following code point to the same object? (Ans: `4-answer.txt`)
```python
>>> a = 89
>>> b = a
```
- Do the variables `a` and `b` in the following code point to the same object? (Ans: `5-answer.txt`)
```python
>>> a = 89
>>> b = a + 1
```
- What do the lines in the following code print? (Ans: `6-answer.txt`)
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
- What do the lines in the following code print? (Ans: `7-answer.txt`)
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
- What do the lines in the following code print? (Ans: `8-answer.txt`)
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
- What do the lines in the following code print? (Ans: `9-answer.txt`)
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
- What do the lines in the following code print? (Ans: `10-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
- What do the lines in the following code print? (Ans: `11-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```
- What do the lines in the following code print? (Ans: `12-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
- What do the lines in the following code print? (Ans: `13-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
- What do the lines in the following code print? (Ans: `14-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
```
- What do the lines in the following code print? (Ans: `15-answer.txt`)
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)
```
- What does the following script print? (Ans: `16-answer.txt`)
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
- What does the following script print? (Ans: `17-answer.txt`)
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
- What does the following script print? (Ans: `18-answer.txt`)
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
- Is `a` a tuple in the following code? (Ans: `20-answer.txt`)
```python
a = ()
```
- Is `a` a tuple in the following code? (Ans: `21-answer.txt`)
```python
a = (1, 2)
```
- Is `a` a tuple in the following code? (Ans: `22-answer.txt`)
```python
a = (1)
```
- Is `a` a tuple in the following code? (Ans: `23-answer.txt`)
```python
a = (1, )
```
- What does the following script print? (Ans: `24-answer.txt`)
```python
a = (1)
b = (1)
a is b
```
- What does the following script print? (Ans: `25-answer.txt`)
```python
a = (1, 2)
b = (1, 2)
a is b
```
- What does the following script print? (Ans: `26-answer.txt`)
```python
a = ()
b = ()
a is b
```
- Will the last line of the following script print 139926795932424? (Ans: `27-answer.txt`)
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
- Will the last line of the following script print 139926795932424? (Ans: `28-answer.txt`)
```python
>>> a
[1, 2, 3]
>>> id(a)
139926795932424
>>> a += [4]
>>> id(a)
```
