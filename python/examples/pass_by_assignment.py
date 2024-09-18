"""
Two ways we can pass the data to a function
1. Pass the data directly
print(1, ['a', 'b'])

2. Pass the data via Variable
i = 1
l = ['a', 'b']
print(i, l)

The difference between two methods of passing data to a function  is that the second one allows you to access the data
even after you have passed  it to a function, so we can still access 'l' and even we can change l here.

l.pop() # output: 'b'

On primitive data such as Int, bool, float or string or immutable data such as Tuple is passed to a function in python
all the values contained in that data are copied over into that function. That means if the data is changed inside the
function the data won't change outside the function, this is called pass by value.

When mutable data type such as List, Set or Dict are passed to a function in python the data isn't copied over.
Only a reference to the data is pass to that function and this is called pass by reference. When the data is then
changed in the function it also changes outside of that function.
"""


def func(x, y):
    x = x - 1
    y.pop()


if __name__ == "__main__":
    i = 1  # Immutable and passed by value, the value will not change outside the function.
    lst = ['a', 'b']  # Mutable and passed by reference, the value will change outside the function.
    func(i, lst)
    print(i, lst)  # 1, ['a']


# If you don't want to the list value should not change then you can do the follow
def func1(x, y):
    x = x - 1
    y.pop()


if __name__ == "__main__":
    i = 1  # Immutable and passed by value
    lst = ['a', 'b']  # Mutable and passed by reference
    func1(i, lst.copy())
    print(i, lst)  # 1, ['a']


# Example with an Integer:
def modify_int(x):
    print("Initial ID of x:", id(x))
    x += 10  # This creates a new integer object
    print("ID of x after modification:", id(x))


a = 5
print("ID of a before function call:", id(a))
modify_int(a)
print("ID of a after function call:", id(a))


# Example with a String:
def modify_string(s):
    print("Initial ID of s:", id(s))
    s += " World"  # This creates a new string object
    print("ID of s after modification:", id(s))


text = "Hello"
print("ID of text before function call:", id(text))
modify_string(text)
print("ID of text after function call:", id(text))


# Example with a List:
def modify_list(lst):
    print("Initial ID of lst:", id(lst))
    lst.append(4)  # Modifies the original list
    print("ID of lst after modification:", id(lst))


my_list = [1, 2, 3]
print("ID of my_list before function call:", id(my_list))
modify_list(my_list)
print("ID of my_list after function call:", id(my_list))


# Example with a Dictionary:
def modify_dict(d):
    print("Initial ID of d:", id(d))
    d["new_key"] = "new_value"  # Modifies the original dictionary
    print("ID of d after modification:", id(d))


my_dict = {"key": "value"}
print("ID of my_dict before function call:", id(my_dict))
modify_dict(my_dict)
print("ID of my_dict after function call:", id(my_dict))


# Example with a Tuple:
def modify_tuple(t):
    print("Initial ID of t:", id(t))
    t += (4, 5)  # This creates a new tuple object
    print("ID of t after modification:", id(t))


my_tuple = (1, 2, 3)
print("ID of my_tuple before function call:", id(my_tuple))
modify_tuple(my_tuple)
print("ID of my_tuple after function call:", id(my_tuple))


def modify_tuple_with_list(t):
    print("Initial ID of t:", id(t))
    print("Initial ID of t[1]:", id(t[1]))  # ID of the list inside the tuple

    t[1].append(4)  # Modifying the list inside the tuple

    print("ID of t after modifying the list:", id(t))  # Tuple ID remains unchanged
    print("ID of t[1] after modification:", id(t[1]))  # List ID remains unchanged


my_tuple = (1, [2, 3])  # A tuple containing a list
print("ID of my_tuple before function call:", id(my_tuple))
modify_tuple_with_list(my_tuple)
print("ID of my_tuple after function call:", id(my_tuple))
print("Modified tuple:", my_tuple)





