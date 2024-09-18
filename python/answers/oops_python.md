### 1. What is __init__() in Python?
   
    In Python, __init__() is a special method known as a constructor. It is automatically called when an instance 
    (object) of a class is created. The primary purpose of __init__() is to initialize the newly created object by 
    setting the initial state of the object (e.g., assigning values to object attributes) or performing any setup 
    required.
  ###### Key Characteristics of `__init__()`:
  1. **Automatic Invocation:** The `__init__()` method is automatically invoked when you create a new instance of 
     a class using the class name.
  2. **Self Parameter:** The first parameter of `__init__()` is always self, which refers to the instance being created. 
     Through self, you can access and modify the attributes and methods of the instance. 
  3. Not a Constructor in the Traditional Sense: Unlike constructors in other languages like C++ or Java, 
     `__init__()` is not technically the constructor of the class. The actual object creation is handled by `__new__()`. 
     `__init__()` is more like an initializer. 
  ###### Example:
  ```python
    class Person:
        def __init__(self, name, age):
            # Initialize instance attributes
            self.name = name
            self.age = age
    
        def greet(self):
            print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Create an instance of the Person class
    person1 = Person("Alice", 30)
    
    # Access attributes and methods of the object
    print(person1.name)  # Output: Alice
    print(person1.age)   # Output: 30
    
    # Call the greet method
    person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
  ```
  ###### Explanation:
  * `__init__()` Method:
    * The `__init__()` method in the `Person` class takes three arguments: `self`, `name`, and `age`. 
    * `self.name = name` assigns the value of the `name` argument to the `name` attribute of the instance.
    * Similarly, `self.age = age` assigns the value of the `age` argument to the `age` attribute of the instance.
  * Creating an Instance:
    * When `person1 = Person("Alice", 30)` is executed, Python creates a new instance of `Person`, and the 
      `__init__()` method is automatically called with `"Alice"` and `30` as arguments.
    * As a result, `person1.name` is set to `"Alice"`, and `person1.age` is set to `30`.
  * Accessing Methods and Attributes:
    * After the object is created, you can access its attributes (`name` and `age`) and call its methods (like `greet()`).
  
### 2. Explain how inheritance works in Python with an example.
### 3. How will you check if a class is a child of another class?
### 4. What is Polymorphism in Python?
### 5. Define encapsulation in Python.
### 6. How do you achieve data abstraction in Python?
### 7. What are global, protected, and private attributes in Python?
### 8. What is monkey patching in Python?
### 9. What are Access Specifiers in Python?
### 10. Is it possible to call a parent class without its instance creation?
### 11. How do you access parent members in the child class?
### 12. What are modules and packages in Python?
### 13. How do you create a class in Python?
### 14. How is an empty class created in Python?
### 15. What is the init method in Python?
### 16. Differentiate between new and override modifiers.