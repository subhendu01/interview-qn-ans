### 1. What is Scope in Python?
    In Python, scope refers to the region of a program where a particular variable is accessible and can be used. 
    It determines the visibility or lifetime of a variable or function within the code.

   ###### LEGB Rule (Scope Resolution Order):
   * When Python looks up a variable, it searches in the following order:
      * L: Local — inside the current function.
      * E: Enclosing — in any enclosing function(s), if present.
      * G: Global — in the module-level variables.
      * B: Built-in — Python’s built-in names.
     
   #### i. Local Scope
   * Variables declared inside a function are in the local scope.
   * These variables can only be accessed within that function.
   ```python
   def my_function():
       x = 10  # local variable
       print(x)
   my_function()  # Output: 10
   # print(x)  # Error: x is not defined outside the function
   ```
   #### ii. Enclosing Scope (Nonlocal Scope)
   * This refers to the scope of a nested (inner) function where the variable is not in the local or global scope 
     but is in the enclosing function's scope.
   * Variables defined in this enclosing function can be accessed and modified in the nested function using 
     the `nonlocal` keyword.
   ```python
   def outer_function():
        y = 20  # Enclosing scope
    
        def inner_function():
            nonlocal y
            y = 30  # Modifies enclosing scope variable
            print(y)
    
        inner_function()
        print(y)
    
    outer_function()  # Output: 30 (inside), 30 (outside after modification)
   ```
   #### iii. Global Scope
   * Variables declared at the top level of the script or module, outside any function, are in the global scope.
   * These variables can be accessed anywhere in the module.
   ```python
    z = 50  # Global variable
    
    def another_function():
        print(z)
    
    another_function()  # Output: 50
   ```  
   * To modify a global variable inside a function, you must use the `global` keyword.
   ```python
    a = 10

    def modify_global():
        global a
        a = 20  # Modify global variable
    
    modify_global()
    print(a)  # Output: 20
   ```
   #### iv. Built-in Scope
   * This is the outermost scope, containing all the built-in names in Python, such as `print()`, `len()`, `int()`, etc.
   * You can always access these built-in functions and constants, but you can also override them by defining 
     your own variables with the same names (though it's generally not recommended).
   ```python
   print(len([1, 2, 3]))  # Built-in function 'len' used
   ````

### 2. What is a namespace in Python?
    In Python, a namespace is a system that ensures that names (identifiers) in a program are unique to avoid conflicts.
    A namespace is essentially a mapping between names (variables, functions, etc.) and their corresponding 
    objects (values, functions, etc.). Each namespace is isolated and helps manage and resolve names used in a program 
    to avoid name collisions.
  There are three types of namespaces in Python:
  * #### Built-in Namespace
    * This contains the names of all the built-in objects, functions, and exceptions that Python provides by default. 
      These are always available for use and can be accessed anywhere in the program.
    * Example: print(), len(), int(), etc.
    ```python
     print(len([1, 2, 3]))  # 'print' and 'len' are in the built-in namespace
    ``` 
  * #### Global Namespace
    * This refers to the names defined at the top level of a Python program or module, outside of any function or class.
    * Global namespaces exist for the lifetime of the program, and global variables/functions can be accessed 
      throughout the module in which they are defined.
  * #### Local Namespace
  * #### Enclosing Namespace

### 3. What is Scope Resolution in Python?
### 4. What is the Global Interpreter Lock (GIL)?
### 5. What is the difference between a shallow copy and a deep copy?
### 6. What is swapcase function in Python?
### 7. What are Iterators in Python?
### 8. What are Generators in Python?
### 9. What are Decorators?
### 10. Does Python support multiple inheritance?
### 11. What is the difference between a shallow copy and a deep copy?
### 12. Which sorting technique is used by sort() and sorted() functions of python?