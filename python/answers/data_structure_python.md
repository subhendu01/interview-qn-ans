### 1. What is the difference between a Set and a Dictionary?
     
   In Python, both sets and dictionaries are collections used to store data. 
   However, they have distinct purposes and differences in terms of structure, usage, and behavior.
  #### _1. Structure:_
   * **Set:** A set is an unordered collection of unique elements. It does not store key-value pairs; instead, it only 
     stores individual values.
     ###### Example:
     ```python
     my_set = {1, 2, 3, 4}
     ```
   * **Dictionary:** A dictionary is an unordered collection of key-value pairs. Each key is unique, and it maps to a 
     specific value.
     ###### Example:
     ```python
     my_dict = {"name": "Alice", "age": 25, "city": "New York"}
     ```
  #### _2. Usage:_
   * **Set:** Used when you need a collection of unique items, typically for membership testing, removing duplicates, or 
     performing mathematical set operations (union, intersection, etc.).
   ####
   * **Dictionary:** Used when you need to store data in pairs (key-value), such as looking up values by a key, storing 
     configurations, or mapping relationships.
  #### _3. Mutability:_
   * **Set:** Sets are mutable, meaning you can add, remove, or update elements after the set is created.
     ###### Example:
     ```python
     my_set = {1, 2, 3}
     my_set.add(4)
     print(my_set)  # Output: {1, 2, 3, 4}
     ```
   * **Dictionary:** Dictionaries are also mutable. You can add, update, or remove key-value pairs.
     ###### Example:
     ```python
     my_dict = {"name": "Alice", "age": 25}
     my_dict["city"] = "New York"
     print(my_dict)  # Output: {"name": "Alice", "age": 25, "city": "New York"}
     ```
  #### _4. Element Access:_
   * **Set:** Elements in a set are accessed through membership testing (in keyword), but direct indexing is not possible 
     because sets are unordered.
     ###### Example:
     ```python
     if 3 in my_set:
         print("3 is in the set")
     ```
   * **Dictionary:** Elements are accessed using keys, making it easy to retrieve values based on a specific key.
     ###### Example:
     ```python
     print(my_dict["name"])  # Output: Alice
     ```
  #### _5. Duplicates:_
   * **Set:** A set automatically removes duplicate elements, ensuring all elements are unique.
     ###### Example:
     ```python
     my_set = {1, 2, 2, 3}
         print(my_set)  # Output: {1, 2, 3}
     ```
   * **Dictionary:** In a dictionary, keys must be unique, but values can be duplicated.
     ###### Example:
     ```python
     my_dict = {"name": "Alice", "age": 25, "city": "New York", "age": 30}
     print(my_dict)  # Output: {"name": "Alice", "age": 30, "city": "New York"}
     ```
  #### _6. Performance:_
   * **Set:** Provides efficient membership testing, with an average time complexity of O(1) for adding, removing, and 
     checking elements.
   ####
   * **Dictionary:** Offers fast lookups, insertions, and deletions based on keys, also with an average time complexity of O(1).
  #### _7. Order Preservation:_
   * **Set:** Prior to Python 3.7, sets did not guarantee order. From Python 3.7 onwards, sets preserve insertion order, 
     but this is considered an implementation detail and should not be relied upon.
   #### 
   * **Dictionary:** Since Python 3.7, dictionaries maintain the order of insertion, making it predictable when iterating 
     over key-value pairs.

### 2. How the time complexity works for operations on sets and dictionaries?
    The average time complexity of O(1) for sets and dictionaries is due to the use of hash tables, which allow direct 
    indexing based on computed hash values. The efficiency of these operations makes sets and dictionaries powerful 
    data structures for quick lookups, insertions, and deletions.

   #### _1. Set Example:_
     Sets in Python are implemented using hash tables, allowing operations like insertion, deletion, and membership 
     testing to be done in constant time on average.
   ###### Example:
   ```python
   my_set = {1, 2, 3, 4, 5}

   # Membership test: O(1) average time complexity
   print(3 in my_set)  # Output: True

   # Adding an element: O(1) average time complexity
   my_set.add(6)
   print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

   # Removing an element: O(1) average time complexity
   my_set.remove(4)
   print(my_set)  # Output: {1, 2, 3, 5, 6}
   ```
   ###### Why is it O(1)?:
   * **Hashing:** Sets use hash tables, where each element is hashed into an index in the underlying array.
   ####
   * **Direct Access:** Once the hash is computed, Python can directly access the index corresponding to the element, 
     making operations like membership checks, additions, and deletions efficient.

   #### _2. Dictionary Example:_
    Dictionaries in Python are also implemented using hash tables, where keys are hashed to quickly find their 
    associated values.
    
   ###### Example:
   ```python
   my_dict = {"a": 1, "b": 2, "c": 3}

   # Lookup by key: O(1) average time complexity
   print(my_dict["b"])  # Output: 2

   # Insertion of a key-value pair: O(1) average time complexity
   my_dict["d"] = 4
   print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

   # Deletion of a key-value pair: O(1) average time complexity
   del my_dict["a"]
   print(my_dict)  # Output: {'b': 2, 'c': 3, 'd': 4}
   ```
   ###### Why is it O(1)?:
   * **Hashing:** Like sets, dictionaries hash the keys, allowing direct access to the value associated with that key.
   ####
   * **Efficient Indexing:** The hash table provides an efficient mechanism to look up, add, or delete entries without 
     needing to scan through all items.

 ###### **Understanding Hashing and Time Complexity:**
 * **Hashing Function:** When you add a key to a dictionary or an element to a set, Python computes a hash value using a 
   hashing function. This hash value determines where the object is stored in the underlying array.
 ##### 
 * **Collision Handling:** In some cases, two different keys may hash to the same index (a collision). Python handles 
   this using techniques like open addressing or chaining. Although collisions can lead to slower lookups, they are 
   relatively rare, so the average time complexity remains O(1).
 #####
 * **Worst Case:** In the worst-case scenario (e.g., too many collisions), the time complexity can degrade to O(n), but 
   this is uncommon.

### 3. Is Tuple Comprehension? If yes, how, and if not why?
    No, there is no tuple comprehension in Python in the same way that there is list comprehension. However, there is a 
    workaround that might look similar to a tuple comprehension but is actually a generator expression.
    
    If you want a tuple from a comprehension-like process, you need to explicitly convert the generator to a tuple 
    using the tuple() function.
  ###### Why Is There No Tuple Comprehension?
   * Python uses specific syntax for list comprehension ([]) and set comprehension ({}). 
     For tuples, using parentheses () does not define a comprehension—it creates a generator instead.
   ####
   * If Python allowed tuple comprehension, it would conflict with the existing generator expression syntax, 
     which also uses parentheses.
  ###### Example Comparison:
  1. List Comprehension (Creates a List):
     ```python
     my_list = [x * 2 for x in range(5)]
     print(my_list)  # Output: [0, 2, 4, 6, 8]
     ```
  2. Generator Expression (Looks Like a Tuple Comprehension):
     ```python
     my_gen = (x * 2 for x in range(5))
     print(my_gen)  # Output: <generator object <genexpr> at 0x...>
     print(tuple(my_gen))  # Output: (0, 2, 4, 6, 8)
     ```
     In this expression (x * 2 for x in range(5)) is not a tuple comprehension. It’s a generator expression, 
     which can be converted to a tuple using tuple().
  ###### Why Does This Happen?
   * Parentheses are used for both grouping expressions and defining generator expressions. Allowing tuple comprehension
     would cause ambiguity in the syntax.
   ####
   * Python designers opted to keep tuple comprehensions out to avoid confusion and maintain clear, distinct syntax for 
     generators.
  ###### How to Simulate Tuple Comprehension?
   Although there isn’t a direct tuple comprehension, you can achieve a similar result by converting a generator 
   expression into a tuple:
   ```python
    my_tuple = tuple(x * 2 for x in range(5))
    print(my_tuple)  # Output: (0, 2, 4, 6, 8)
   ```
### 4. Differentiate between a List and a Tuple.
   * Lists are mutable, more versatile, and used when you need to modify the data.
   * Tuples are immutable, more memory-efficient, and used when you want to ensure data integrity and consistency.
 ###### Differences Between List and Tuple:
  * **List:**
    1. **Mutability :-** ```Mutable: You can change, add, or remove items after creation.```
    2. **Syntax :-** ```Defined using square brackets [].```
    3. **Example :-** ```my_list = [1, 2, 3]```
    4. **Use Case :-** ```Used when you need a collection of items that can change over time.```
    5. **Performance :-** ```Slower due to additional operations like insertion, deletion, and resizing.```
    6. **Methods :-** ```Supports more built-in methods like append(), remove(), sort(), etc.```
    7. **Memory Usage :-** ```Requires more memory because of the overhead for dynamic resizing.```
    8. **Iteration Speed :-** ```Slower than tuples.```
    9. **Element Addition :-** ```You can add elements using append(), insert(), or extend().```
    10. **Element Deletion :-** ```You can remove elements using remove(), pop(), or del.```
    11. **Usage in Keys :-** ```Cannot be used as dictionary keys or set elements because they are mutable.```
  ####
  * **Tuple:** 
    1. **Mutability :-** ```Immutable: Once created, the elements cannot be changed.```
    2. **Syntax :-** ```Defined using parentheses ().```
    3. **Example :-** ```my_tuple = (1, 2, 3)```
    4. **Use Case :-** ```Used when you need a constant set of values that should not be changed.```
    5. **Performance :-** ```Faster due to immutability and fixed size, with less memory overhead.```
    6. **Methods :-** ```Fewer methods are available (e.g., count(), index()); most are not applicable due to immutability.```
    7. **Memory Usage :-** ```Requires less memory because it’s static and immutable.```
    8. **Iteration Speed :-** ```Faster than lists due to immutability and fixed size.```
    9. **Element Addition :-** ```Elements cannot be added after the tuple is created.```
    10. **Element Deletion :-** ```Elements cannot be removed; however, you can delete the entire tuple.```
    11. **Usage in Keys :-** ```Can be used as dictionary keys or set elements because they are immutable and hashable.```

### 5. Why Tuples Can Be Used as Dictionary Keys?  
  * Immutability: Since tuples are immutable, their hash value remains constant throughout their lifetime. This allows 
     them to be used as dictionary keys because dictionary keys must be hashable.
  * Lists Are Not Hashable: Lists are mutable and can be changed after creation (e.g., by adding, removing, or altering
     elements). Due to this mutability, lists are not hashable, and hence cannot be used as dictionary keys.
   
    ###### Example:
    ```python
    # Using a tuple as a dictionary key (This works)
    coordinates = {
        (10, 20): "Location A",
        (15, 25): "Location B",
        (30, 40): "Location C"
    }
   
    print(coordinates[(10, 20)])  # Output: Location A
    
    # Using a list as a dictionary key (This will raise a TypeError)
    my_dict = {
        [1, 2, 3]: "This will not work"  # This will raise an error
    }
    
    # Uncommenting the line above will result in:
    # TypeError: unhashable type: 'list'
    ```
### 6. What are built-in data types in Python?
   Python provides several built-in data types that are used to store different kinds of data. These data types can be 
   broadly categorized into several groups:
   1. **Numeric Types:** 
      * ```int```: Represents integers (whole numbers), both positive and negative.
        * Example: ```x = 10```
      * ```float```: Represents floating-point numbers (decimal numbers).
        * Example: ```y = 10.5```
      * ```complex```: Represents complex numbers with a real and an imaginary part.
        * Example: ```z = 3 + 4j```

   2. **Sequence Types:**
      * ```str```: Represents a sequence of Unicode characters (text).
        * Example: ```name = "Alice"```  
      * ```list```: Represents an ordered and mutable sequence of items.
        * Example: ```fruits = ["apple", "banana", "cherry"]```
      * ```tuple```: Represents an ordered and immutable sequence of items.
        * Example: ```coordinates = (10, 20, 30)```
      * ```range```: Represents a sequence of numbers, often used in loops.
        * Example: ```numbers = range(5) '(which gives [0, 1, 2, 3, 4])'```
   3. **Mapping Type:**
      * ```dict```: Represents key-value pairs (unordered and mutable).
        * Example: ```person = {"name": "Alice", "age": 25, "city": "New York"}```
   4. **Set Types:**
      * ```set```: Represents an unordered collection of unique items.
        * Example: ```my_set = {1, 2, 3, 4}```
      * ```frozenset```: Represents an immutable version of a set.
        * Example: ```frozen = frozenset([1, 2, 3, 4])```
   5. **Boolean Type:**
      * ```bool```: Represents the truth values `True` or `False`.
        * Example: ```is_active = True```
   6. **Binary Types:**
      * ```bytes```: Represents immutable sequences of bytes (binary data).
        * Example: ```b = b'hello'```
      * ```bytearray```: Represents mutable sequences of bytes.
        * Example: ```ba = bytearray([65, 66, 67])```
      * ```memoryview```: Represents a view of a memory buffer.
        * Example: ```mv = memoryview(bytes(5))```
   7. **None Type:** 
      * ```NoneType```: Represents the absence of a value or a null value. It has a single value: `None`.
        * Example: ```value = None```

### 7. What is slicing in Python?
    Slicing in Python is a technique used to extract a portion (or slice) of a sequence such as a list, tuple, string, 
    or range. Slicing allows you to access a subsequence of elements from the original sequence based on specified 
    start, stop, and step values.
   ###### Syntax:
   ```python 
   sequence[start:stop:step]
   ```
   ###### Explanation:
   * `start:` The index where the slice starts (inclusive). If omitted, slicing starts from the beginning of the 
      sequence (index 0).
   * `stop:` The index where the slice ends (exclusive). If omitted, slicing goes up to the end of the sequence.
   * `step:` The interval or step size between each element in the slice. If omitted, the default step size is 1.
   ###### Example:  [CODE RUN](..%2Fexamples%2Fslicing_ex.py)
   ###### Key Points:
   * **Inclusive Start, Exclusive Stop:** The start index is included, but the stop index is not.
   ####
   * **Default Values:** If start is omitted, it defaults to 0. If stop is omitted, it defaults to the length of the 
     sequence. If step is omitted, it defaults to 1.
   #### 
   * **Negative Indices:** You can use negative indices to slice from the end of the sequence.
   ####
   * **Reverse Slicing:** Using a negative step value ([::-1]) allows you to reverse the sequence.

### 8. What are negative indexes and why are they used?
   * **Convenience:** Negative indexing provides an intuitive way to access elements from the end of a sequence without 
     having to calculate the length.
     * Example: `my_list[-1]` is more readable than `my_list[len(my_list) - 1]`. 
   ####
   * Flexibility: When working with sequences of varying lengths, negative indexing allows you to consistently access 
     elements from the end regardless of the sequence size.
   ####
   * Simplified Code: Negative indexing can reduce the need for complicated calculations, especially in cases where 
     you want to slice a sequence or work with the last few elements.
   ###### Example
   ```python
   my_string = "Python Programming"

   # Slice the last 3 characters
   print(my_string[-3:])  # Output: "ing"
   
   # Slice from the third last to the second last character
   print(my_string[-3:-1])  # Output: "in"
   
   my_string = "Python Programming"

   # Slice the last 3 characters
   print(my_string[-3:])  # Output: "ing"

   # Slice from the third last to the second last character
   print(my_string[-3:-1])  # Output: "in"
   ```
### 9. Python Functions and Arguments.
    In Python, functions are blocks of reusable code that perform a specific task. They can take inputs (arguments), 
    perform operations, and return outputs. Understanding how functions and arguments work is key to writing clean, 
    efficient, and modular code.
 #### 1. Defining a Function:
   A Python function is defined using the def keyword, followed by the function name, a pair of parentheses (), 
   and a colon :. The function body is indented.
   ```python
   def function_name(parameters):
       # Function body
       # Code to be executed
       return result  # Optional
   ```
   ###### Example:
   ```python
   def greet(name):
       return f"Hello, {name}!"

   print(greet("Alice"))  # Output: Hello, Alice!
   ``` 
 #### 2. Function Arguments:
   Arguments are values passed to a function when it is called. Python functions can take different types of arguments:
   ###### Types of Arguments:
   1. **Positional Arguments:** The most common way of passing arguments. The order matters.
      ```python
      def add(a, b):
          return a + b

      print(add(3, 5))  # Output: 8
      ```
   2. **Keyword Arguments:** You can specify arguments by name when calling the function. The order doesn’t matter.
      ```python
      def greet(name, message):
          return f"{message}, {name}!"
      
      print(greet(name="Alice", message="Good morning"))  # Output: Good morning, Alice!
      print(greet(message="Good morning", name="Alice"))  # Output: Good morning, Alice! 
      ```
   3. **Default Arguments:** You can set default values for parameters, which are used if no argument is provided during
      the function call.
      ```python
      def greet(name, message="Hello"):
          return f"{message}, {name}!"
      
      print(greet("Alice"))  # Output: Hello, Alice!
      print(greet("Bob", "Good evening"))  # Output: Good evening, Bob!
      ```
   4. **Variable-Length Arguments:** Sometimes, you may want a function to accept a variable number of arguments. 
      Python provides two ways to achieve this:
      * `*args` (Non-keyword variable-length arguments): Allows a function to accept any number of positional arguments.
      ####
      * `**kwargs` (Keyword variable-length arguments): Allows a function to accept any number of keyword arguments.
      ```python
      def my_function(*args, **kwargs):
          print("Positional arguments:", args)
          print("Keyword arguments:", kwargs)
      
      my_function(1, 2, 3, name="Alice", age=25)
      # Output:
      # Positional arguments: (1, 2, 3)
      # Keyword arguments: {'name': 'Alice', 'age': 25}
      ```
 #### 3. Returning Values from a Function:
   Functions can return a value using the `return` statement. If no `return` statement is used, 
   the function returns `None` by default.
   ```python
   def multiply(a, b):
       return a * b

   result = multiply(4, 5)
   print(result)  # Output: 20
   ``` 
 #### 4. Function Scope:
   Variables defined inside a function are local to that function and cannot be accessed outside of it.
   ```python
    def my_function():
        x = 10  # Local variable
        return x

    print(my_function())  # Output: 10
    # print(x)  # Error: NameError because 'x' is not defined outside the function
   ```
 #### 5. Lambda Functions (Anonymous Functions):
   Lambda functions are small, anonymous functions defined using the `lambda` keyword. They are typically used for short, 
   simple operations.
   ```python
    # Syntax: lambda arguments: expression
    multiply = lambda a, b: a * b
    print(multiply(4, 5))  # Output: 20
   ```

### 10. What is List Comprehension? Give an example.
    List comprehension is a powerful Python feature that allows you to create lists efficiently and concisely. 
    It's particularly useful for generating new lists by applying transformations and filters to existing iterables.
   ###### Here are all the possible ways you can use list comprehensions, ranging from simple to more complex examples:
   #### 1. Basic List Comprehension
   Create a new list by applying an expression to each item in an iterable.
   ```python
   # Square of numbers from 0 to 4
   squares = [x**2 for x in range(5)]
   # Output: [0, 1, 4, 9, 16]
   ```
   #### 2. List Comprehension with a Condition (Filtering)
   Include an `if` statement to filter elements.
   ```python
    # Even numbers from 0 to 9
    evens = [x for x in range(10) if x % 2 == 0]
    # Output: [0, 2, 4, 6, 8]
   ```
   #### 3. List Comprehension with Multiple Conditions
   You can use multiple conditions in the comprehension.
   ```python
    # Numbers divisible by both 2 and 3 from 0 to 19
    div_by_2_and_3 = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
    # Output: [0, 6, 12, 18]
   ```
   #### 4. List Comprehension with `else`
   To include an `else` condition, you need to place it before the for statement (this is a conditional expression or 
   ternary operator in Python).
   ```python
    # Label numbers as even or odd
    labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
    # Output: ['even', 'odd', 'even', 'odd', 'even']
   ```
   #### 5. Nested List Comprehension
   List comprehension within another list comprehension, often used for 2D lists or matrices.
   ```python
    # 3x3 matrix filled with zeros
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
   ```
   #### 6. List Comprehension with Nested Loops
   You can use multiple `for` loops inside a list comprehension.
   ```python
    # Cartesian product of two lists
    cartesian_product = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
    # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
   ```
   #### 7. Flattening a Nested List
   Flatten a 2D list (or a list of lists) into a 1D list.
   ```python
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened = [item for sublist in nested_list for item in sublist]
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```
   #### 8. List Comprehension with Function Calls
   Apply a function to each item in the iterable.
   ```python
    # Apply the abs() function to a list of numbers
    numbers = [-1, -2, 3, -4, 5]
    absolute_values = [abs(x) for x in numbers]
    # Output: [1, 2, 3, 4, 5]
   ```
   #### 9. List Comprehension with Enumerate
   Use `enumerate()` to access both the index and value during iteration.
   ```python
    # Create a list of tuples containing index and value
    indexed_values = [(i, x) for i, x in enumerate(['a', 'b', 'c'])]
    # Output: [(0, 'a'), (1, 'b'), (2, 'c')]
   ```
   #### 10. Using List Comprehension with `zip()`
   Combining multiple iterables element-wise.
   ```python
    # Combine two lists into tuples
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    zipped = [(x, y) for x, y in zip(list1, list2)]
    # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
   ```

### 11. What is Dictionary Comprehension? Give an example.
    Dictionary comprehension in Python is a concise way to create dictionaries. Similar to list comprehension, 
    it allows you to generate a dictionary by iterating over an iterable and applying an expression to each item. 
    This method is often more readable and efficient than using a traditional for loop.

   ###### Syntax:
   ```python
    {key_expression: value_expression for item in iterable if condition}
   ```
   ###### Example 1: Basic Dictionary Comprehension
   ```python
    squares = {x: x**2 for x in range(1, 6)}
    print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
   ```
   ###### Example 2: Dictionary Comprehension with a Condition
   ```python
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
   ```
   ###### Example 3: Swapping Keys and Values
   ```python
    original = {'a': 1, 'b': 2, 'c': 3}
    swapped = {v: k for k, v in original.items()}
    print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}
   ```
   ###### Example 4: Dictionary Comprehension with `zip()`
   ```python
    keys = ['name', 'age', 'city']
    values = ['Alice', 25, 'New York']
    info = {k: v for k, v in zip(keys, values)}
    print(info)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
   ```
   ###### Example 5: Nested Dictionary Comprehension
   ```python
    nested_dict = {x: {'square': x**2, 'cube': x**3} for x in range(1, 4)}
    print(nested_dict)
    # Output: {1: {'square': 1, 'cube': 1}, 2: {'square': 4, 'cube': 8}, 3: {'square': 9, 'cube': 27}}
   ```

### 12. What is Set Comprehension? Give an example.
    Set comprehension in Python is a concise way to create sets, similar to list and dictionary comprehensions.

  ###### Syntax:
   ```python
    {expression for item in iterable if condition}
   ```
  ###### Example 1: Basic Set Comprehension
   ```python
    squares = {x**2 for x in range(1, 6)}
    print(squares)  # Output: {1, 4, 9, 16, 25}
   ```
  ###### Example 2: Set Comprehension with a Condition
   ```python
    evens = {x for x in range(10) if x % 2 == 0}
    print(evens)  # Output: {0, 2, 4, 6, 8}
   ```
  ###### Example 3: Removing Duplicates with Set Comprehension
   ```python
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = {x for x in numbers}
    print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
   ```
  ###### Example 4: Set Comprehension with Complex Expressions
   ```python
    sentence = "Set comprehension is a powerful feature in Python"
    word_lengths = {len(word) for word in sentence.split()}
    print(word_lengths)  # Output: {1, 2, 5, 6, 7, 8}
   ```

### 13. What is lambda in Python? Why is it used?
    A lambda function in Python is a small, anonymous function defined with the lambda keyword. Unlike regular functions
    defined with `def`, a lambda function is a single-line expression that returns a value. Lambda functions are often 
    used for short, simple operations that are needed temporarily and are typically passed as arguments to higher-order 
    functions.
  ###### Syntax:
   ```python
    lambda arguments: expression
   ```
   * `arguments`: The input parameters for the lambda function (comma-separated if there are multiple).
   * `expression`: The single expression that is evaluated and returned.
  ###### Characteristics of Lambda Functions:
   1. **Anonymous:** Lambda functions don't have a name (though they can be assigned to a variable).
   2. **Single Expression:** They contain a single expression, and the result of this expression is automatically returned.
   3. **No Statements:** Lambda functions can't contain statements or annotations; they are limited to simple expressions.
  
  ###### Characteristics of Lambda Functions:
  Lambda functions are used when you need a simple function for a short period of time, especially as arguments to other
  functions like `map()`, `filter()`, and `sorted()`. They are concise, making the code more readable and reducing the 
  need to define a full function using `def`.
  
  ###### Example 1: Basic Lambda Function
  ```python
   add_ten = lambda x: x + 10
   print(add_ten(5))  # Output: 15
  ```  
  ###### Example 2: Lambda with Multiple Arguments
  ```python
   multiply = lambda x, y: x * y
   print(multiply(2, 3))  # Output: 6
  ```  
  
  ###### Example 3: Lambda in `map()`
  ```python
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x**2, numbers))
   print(squared)  # Output: [1, 4, 9, 16, 25]
  ```  
  ###### Example 4: Lambda in filter()
  ```python
   numbers = [1, 2, 3, 4, 5, 6]
   odds = list(filter(lambda x: x % 2 != 0, numbers))
   print(odds)  # Output: [1, 3, 5]
  ```  
  ###### Example 5: Lambda in `sorted()`
  ```python
   pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
   sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
   print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
  ```  

### 14. What are *args and kwargs?
    In Python, *args and **kwargs are used in function definitions to allow the function to accept an arbitrary number 
    of arguments. They are a flexible way to handle variable numbers of input arguments and keyword arguments.

   #### 1. *args:
   * `*args` allows a function to accept any number of positional arguments.
   * The `*` symbol before `args` indicates that the function can take multiple arguments, which will be passed as a tuple.
   * The name `args` is a convention, but you can use any name preceded by `*`.
   ###### Example of `*args`:
   ```python
    def my_function(*args):
        for arg in args:
            print(arg)
    my_function(1, 2, 3, 4)
   ```
   ###### Output:
     1
     2
     3
     4
   
   #### 2. **kwargs:
   * `**kwargs` allows a function to accept any number of keyword arguments.
   * The `**` symbol before `kwargs` indicates that the function can take multiple keyword arguments, which will be 
     passed as a dictionary.
   * The name `kwargs` is a convention, but you can use any name preceded by `**`.
   ###### Example of `**kwargs`:
   ```python
    def my_function(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    my_function(name="Alice", age=25, city="New York")
   ```
  ###### Output:
    name: Alice
    age: 25
    city: New York
  #### Combining *args and **kwargs:
  You can use both `*args` and `**kwargs` in the same function definition, allowing the function to accept both 
  positional and keyword arguments.
  ```python
    def my_function(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
    my_function(1, 2, 3, name="Alice", age=25)
  ```
  ###### Output:
    Positional arguments: (1, 2, 3)
    Keyword arguments: {'name': 'Alice', 'age': 25}

### 15. Can we pass a function as an argument in Python?
    Yes, you can pass a function as an argument to another function in Python. This is a common practice in Python and 
    is a feature of higher-order functions, which are functions that can take other functions as arguments or return 
    them as results.
 #### Why Pass a Function as an Argument?
  Passing functions as arguments is useful for various reasons:
   * **Customization:** You can pass different functions to customize the behavior of a higher-order function.
   * **Code Reusability:** You can write generic functions that can perform actions on a wide range of inputs.
   * **Callbacks:** Functions can be passed as callbacks, which are executed after an event or action is completed.
  ###### Example 1: Basic Example
  Let's pass a function that doubles a number as an argument to another function.
  ```python
    def double(x):
        return x * 2
    
    def apply_function(func, value):
        return func(value)
    
    result = apply_function(double, 5)
    print(result)  # Output: 10
  ```
  ###### Example 1: Basic Example
  You can also pass lambda functions as arguments, which is often more concise.
  ```python
    def apply_function(func, value):
        return func(value)
    
    result = apply_function(lambda x: x**2, 4)
    print(result)  # Output: 16
  ```
  ###### Example 3: Using Functions as Filters
  Pass a function as an argument to filter elements from a list.
  ```python
    def is_even(x):
        return x % 2 == 0
    
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(is_even, numbers))
    print(even_numbers)  # Output: [2, 4, 6]
  ```
  ###### Example 3: Using Functions as Filters
  Pass a function to customize the sorting behavior.
  ```python
    def get_second_element(item):
        return item[1]
    
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    sorted_pairs = sorted(pairs, key=get_second_element)
    print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
  ```

### 16. What are Function Annotations in Python?
    Function annotations in Python are a way to attach metadata to the parameters of a function and its return value. 
    They are completely optional and do not affect the actual execution of the function. Annotations are often used for 
    type hints, documentation, or other metadata purposes.
  #### Syntax of Function Annotations:
   The syntax for function annotations is straightforward:
   * Annotations for function parameters are defined by adding a colon (`:`) after the parameter name, followed by the annotation.
   * An annotation for the return value is defined by adding an arrow (`->`) after the closing parenthesis of the 
     parameter list, followed by the annotation.

   #### Example of Function Annotations
   ```python
     def greet(name: str, age: int) -> str:
        return f"Hello, {name}! You are {age} years old."
   ```
   #### Accessing Annotations
   Function annotations are stored in the `__annotations__` attribute of the function as a dictionary.
   ##### Example:
   ```Python
   print(greet.__annotations__)
   ```
   ##### Output:
   ```python
   {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
   ```
   ###### Usage of Function Annotations
   1. **Type Hints:** The most common use of function annotations is for type hints, which help with code readability, 
      understanding, and tooling (like IDEs and linters). They do not enforce type checking at runtime but can be used 
      with external tools like `mypy` for static type checking. 
   2. **Documentation:** Annotations can also be used to provide additional context or documentation for the function 
      parameters and return value. 
   3. **Custom Metadata:** Although less common, annotations can store any metadata associated with function parameters 
      or the return value. 
   ###### Important Points
   * **Optional:** Annotations are completely optional and do not affect how the function is executed.
   * **No Enforcement:** Python does not enforce the types specified in annotations. They are merely hints or guidelines.
   * **Flexible:** You can annotate with any expression, not just types. For example, you could use strings, lists, or custom objects.
   ###### Example of Annotations with Non-Type Metadata
   ```python
    def example(x: 'input integer', y: 'input float') -> 'output float':
        return x * y
   ```

### 17. What is the use of self in Python?
 `self` is a reference to the current instance of the class.
  
    In Python, self is a conventionally used name for the first parameter in instance methods of a class. 
    It refers to the instance of the class itself. When you create an object of a class and call one of its methods, 
    self is automatically passed to the method to give you access to the instance's attributes and methods.

 #### Key Points About `self`:
 1. **Refers to the Instance:**
    * `self` refers to the specific instance of the class that is calling the method. It allows you to access and 
    * modify the instance’s attributes and call other methods on that instance.
 2. **Required in Instance Methods:**
    * In instance methods (i.e., methods that are called on an instance of a class), the first parameter must be `self`
      (though it can be named differently, `self` is the convention). This parameter allows the method to refer to the 
      calling instance.
 3. **Not Automatically Provided:**
    * When defining methods within a class, Python does not automatically include `self`. 
      You must explicitly define it as the first parameter in your method definitions.
    
 ###### Example of `self` in a Class:
 ```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # self.name refers to the instance attribute 'name'
        self.age = age    # self.age refers to the instance attribute 'age'
        
    def bark(self):
        return f"{self.name} is barking."
    
    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Calling instance methods
print(my_dog.bark())      # Output: Buddy is barking.
print(my_dog.get_age())   # Output: Buddy is 3 years old.
```
 ###### Explanation:
 * **`__init__(self, name, age)`:** The `__init__` method is the constructor that initializes 
   the attributes `name` and `age` for each instance of the class. `self.name` and `self.age` refer to the instance's 
   attributes.
 * **`bark(self)` and `get_age(self)`:** These are instance methods that operate on the instance attributes `self.name` and `self.age`.
 * **Accessing attributes and methods:** When you create an instance of the `Dog` class (`my_dog = Dog("Buddy", 3)`), 
   `self` in the methods refers to `my_dog`. Thus, calling `my_dog.bark()` makes `self.name` refer to `"Buddy"`.
 
 ###### Why is self Important?
  * **Distinguishing Instance Attributes:** Using `self` allows you to distinguish between instance attributes and 
    local variables or parameters within methods.
  * **Accessing Instance Methods:** With `self`, you can call other methods on the same instance or modify 
    the instance’s attributes.
  * **Consistency Across Instances:** Each instance of a class has its own set of attributes and methods, 
    and `self` ensures that each method operates on the correct instance.