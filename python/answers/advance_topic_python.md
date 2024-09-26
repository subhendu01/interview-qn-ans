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
    Namespaces help organize and structure the names used in a Python program, ensuring no conflicts occur between 
    variables, functions, and other identifiers.
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
    ```python
    x = 10  # Global variable

    def my_function():
        print(x)  # Access global variable
    
    my_function()  # Output: 10
    ```
  * #### Local Namespace
    * This contains names defined within a function or method. These are created when the function is called and are 
      destroyed once the function finishes executing.
    * Variables inside a local namespace are not accessible outside the function.
  ```python
   def my_function():
       y = 5  # Local variable
       print(y)
   my_function()  # Output: 5
   # print(y)  # Error: 'y' is not defined outside the function
  ```
  * #### Enclosing Namespace
    * This namespace comes into play when you have nested functions. It refers to the scope of the outer (enclosing) 
      function that surrounds a nested function.
    * Variables in the enclosing namespace can be accessed by the inner function, and can be modified 
      using the `nonlocal` keyword.
  ```python
      def outer_function():
        z = 20  # Enclosing variable
    
        def inner_function():
            print(z)  # Access enclosing variable
    
        inner_function()  # Output: 20
    
      outer_function()
   ```
   ###### Accessing Enclosing Variables Using nonlocal
   When working with nested functions, you can modify variables in the enclosing (nonlocal) scope using the nonlocal keyword.
   ```python
   def outer_function():
        y = 10  # Enclosing scope
    
        def inner_function():
            nonlocal y  # Refers to the enclosing scope variable
            y = 20  # Modifies enclosing 'y'
    
        inner_function()
        print(y)  # Output: 20
    
   outer_function()
   ```

   ###### Namespace Lifetimes
   * Built-in Namespace: This lasts as long as the Python interpreter is running.
   * Global Namespace: This lasts for the duration of the module or script. Once the script finishes, the global namespace is cleaned up.
   * Local Namespace: This is created when a function is called and is destroyed once the function completes.

### 3. What is Scope Resolution in Python?
   * Scope resolution in Python follows the LEGB rule, starting from the Local scope, then checking the Enclosing scope, 
     Global scope, and finally the Built-in scope.
   * Python searches for variable names based on this hierarchy, and if a name isn't found in any scope, 
     it raises a `NameError`.

### 4. What is the Global Interpreter Lock (GIL)?
    The Global Interpreter Lock (GIL) is a mutex (mutual exclusion lock) used in Python, to ensure that only one thread 
    executes Python bytecode at a time, even in a multi-threaded program. This means that Python threads are not fully 
    concurrent when executing Python code, as only one thread can execute at a time due to the GIL.
    
    * The Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time in CPython.
    * It simplifies memory management but restricts true parallelism in multi-threaded, CPU-bound programs.
    * For I/O-bound tasks, the GIL has less of an impact because Python threads can be switched while waiting for I/O operations.
    * For CPU-bound tasks, the GIL can be a significant bottleneck, and multiprocessing is recommended to bypass the GIL for parallelism.
    * The GIL is specific to CPython, and alternative Python implementations do not have it.
  ###### Why Does Python Have a GIL?
  The GIL exists because CPython's memory management, specifically reference counting for garbage collection, 
  is not thread-safe. Reference counting is used to keep track of the number of references to an object in memory, 
  and when the count drops to zero, the object can be safely deallocated. The GIL ensures that multiple threads do not 
  interfere with reference counting and other critical internal operations, preventing race conditions and corruption 
  of memory.
  
  ###### How Does the GIL Affect Python Programs?
  * Multithreading in CPU-bound Tasks:
    * For programs that are CPU-bound (tasks that heavily use the CPU, such as complex calculations or data processing), 
      the GIL can significantly reduce performance when using threads.
    * Even though Python supports threading, the GIL ensures that only one thread is actively executing Python code at 
      any given time, which limits the benefits of multithreading in CPU-bound tasks.
    ####
    Example: In CPU-intensive tasks like matrix multiplication or cryptography, using multiple threads will not speed 
    up the program since the GIL allows only one thread to execute at a time.
  * Multithreading in I/O-bound Tasks:
    * In I/O-bound tasks (e.g., reading/writing files, network requests), the GIL is less of a bottleneck. 
      This is because when a thread is waiting for I/O operations, the GIL is released, allowing other threads to run.
    * In this case, multithreading can still provide performance improvements, as multiple threads can wait for 
      I/O operations in parallel.
    ####
    Example: Web scraping, downloading files, or handling multiple client requests on a server can benefit from 
    multithreading since I/O waits release the GIL.
  * Multiprocessing as an Alternative:
    * To overcome the GIL's limitations in CPU-bound tasks, Python provides the multiprocessing module, which creates 
      separate processes, each with its own memory space and Python interpreter instance.
    * Since each process has its own GIL, true parallelism can be achieved in CPU-bound programs.
    ```python
    from multiprocessing import Process

    def task():
        # CPU-bound task
        pass
    
    processes = [Process(target=task) for _ in range(4)]
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    ```
  * Third-Party Libraries:
    * Many third-party libraries, especially those written in C or using C extensions (e.g., `NumPy`, `SciPy`), 
      can release the GIL during their execution. This allows these libraries to achieve real parallelism for 
      performance-critical operations, even with threading.
 ###### GIL and CPython vs. Other Implementations
  * The GIL is specific to CPython, the default and most widely used implementation of Python. Other implementations 
    of Python, such as Jython (Python for Java) and IronPython (Python for .NET), do not have a GIL and allow true 
    multithreading.
  * **PyPy**, an alternative Python interpreter, also has a GIL, but its just-in-time (JIT) compilation optimizations often 
    help to mitigate performance issues.
 ###### GIL and Performance Bottlenecks
  While the GIL simplifies the implementation of CPython, it introduces performance bottlenecks in CPU-bound programs, 
  particularly for multithreaded applications. The GIL is one of the reasons Python is not always the best choice for programs that require heavy parallelism across multiple CPU cores.
  
### 5. What is the difference between a shallow copy and a deep copy?
 * #### Shallow Copy
   A shallow copy creates a new object, but it only copies the references to the objects contained in the original 
   compound object. It means that while the outer structure is copied, the inner elements (objects or references) are 
   shared between the original and the copied object.
   * If the elements inside the compound object are immutable (like integers, strings, or tuples), both the original 
     and the shallow copy can change independently without affecting each other.
   * If the elements are mutable (like lists or dictionaries), changes to the mutable objects inside the copy will 
     reflect in the original object and vice versa because they share the same reference. 
   #### 
   ###### Example of Shallow Copy:
   ```python
    import copy

    original_list = [1, [2, 3], 4]
    shallow_copied_list = copy.copy(original_list)
    
    # Modify the nested list in the copied version
    shallow_copied_list[1][0] = 99
    
    print("Original List:", original_list)  # Output: [1, [99, 3], 4]
    print("Shallow Copy List:", shallow_copied_list)  # Output: [1, [99, 3], 4]
   ```
   In this example, modifying the nested list in `shallow_copied_list` also affects `original_list` because 
   the shallow copy only copies references to the original list’s inner objects.
 * #### Deep Copy
   A deep copy creates a new object and recursively copies all objects found within the original object. This means 
   that the deep copy duplicates not only the outer structure but also all nested objects and their references. 
   The original and the copied objects are completely independent, and changes made to one will not affect the other, 
   even for mutable objects.
  ###### Example of Deep Copy:
  ```python
    import copy

    original_list = [1, [2, 3], 4]
    deep_copied_list = copy.deepcopy(original_list)
    
    # Modify the nested list in the deep copy
    deep_copied_list[1][0] = 99
    
    print("Original List:", original_list)  # Output: [1, [2, 3], 4]
    print("Deep Copy List:", deep_copied_list)  # Output: [1, [99, 3], 4]
  ```
  In this example, modifying the nested list in `deep_copied_list` does not affect `original_list` because the deep copy 
  creates a completely independent clone, including all inner elements.
 
 ###### Key Differences
 * Object
   * **Shallow Copy:** New object with references to original’s inner objects
   * **Deep Copy:** Entirely new object with copies of all inner objects
 * Mutability
   * **Shallow Copy:** Changes to mutable inner objects affect both the original and the copy
   * **Deep Copy:** Changes in any object (including nested ones) do not affect the other
 * Performance
   * **Shallow Copy:** Faster, as it only copies references
   * **Deep Copy:** Slower, as it duplicates everything recursively
 * Usage
   * **Shallow Copy:** Suitable when you want to copy the structure but not the data inside mutable elements
   * **Deep Copy:** Suitable when you need a fully independent copy of all nested elements
### 6. What is swapcase function in Python?
### 7. What are Iterators in Python?
### 8. What are Generators in Python?
### 9. What are Decorators?
### 10. Does Python support multiple inheritance?
### 11. What is the difference between a shallow copy and a deep copy?
### 12. Which sorting technique is used by sort() and sorted() functions of python?