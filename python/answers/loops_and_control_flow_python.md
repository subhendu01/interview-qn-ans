### 1. What is the difference between a for loop and a while loop in Python?
   In Python, both `for` and `while` loops are used for iterating over a block of code multiple times. 
   However, they differ in how they control the flow of the loop.
   1. **For Loop**

    A for loop is generally used when you know in advance how many times you want to execute a statement or 
    a block of statements. It iterates over a sequence (such as a list, tuple, string, or range) and executes 
    the loop's body once for each element in the sequence.
   ###### Key Characteristics:
   * Iterates over a sequence.
   * The number of iterations is determined by the length of the sequence.
   * More commonly used when the number of iterations is known or when iterating over a collection of elements.
   ###### Example:
   ```python
   # Iterate over a list using a for loop
   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```
   ###### Output:
   ```output
   apple
   banana
   cherry
   ```
   2. **While Loop**
   
    A while loop is used when the number of iterations is not known in advance and depends on a condition 
    that is evaluated before each iteration. The loop continues to execute as long as the condition is True. 
    If the condition becomes False, the loop stops.
  ###### Key Characteristics:
  * Iterates based on a condition.
  * The loop can potentially run indefinitely if the condition never becomes `False`.
  * More commonly used when the number of iterations is not predetermined.
  ###### Example:
  ```output
  0
  1
  2
  3
  4
  ```
  ###### Key Differences:
  1. **Control Mechanism:**
     * **For Loop:** Iterates over a sequence or range. The number of iterations is fixed and based on the length of 
       the sequence or range.
     * **While Loop:** Continues until a condition becomes False. The number of iterations is not fixed and is 
       controlled by the loop condition.
  2. **Use Case:**
     * **For Loop:** Best used when you know the number of iterations beforehand, such as iterating through elements 
       in a list, tuple, dictionary, or string.
     * **While Loop:** Best used when the number of iterations is unknown and depends on dynamic conditions, 
       such as reading data until a certain condition is met.
  3. **Potential for Infinite Loop:**
     * **For Loop:** Less prone to infinite loops since it usually runs for a specific number of iterations.
     * **While Loop:** More prone to infinite loops if the condition never becomes False (e.g., a logical error in 
       the loop condition).

### 2. What is the difference between break, continue, and pass in Python?
 
    In Python, break, continue, and pass are control flow statements used within loops or conditional structures to 
    alter the flow of execution. Each serves a different purpose.
 
  1. `break` Statement

   The `break` statement is used to immediately exit a loop, regardless of the loop's condition. 
   When `break` is encountered, the loop terminates, and control is transferred to the first statement following the loop.
   #####
   **Use Case:**
   * When you want to exit a loop as soon as a specific condition is met.
   **Example:**
   ```python
    for i in range(10):
        if i == 5:
            break  # Exit the loop when i equals 5
        print(i)
   ```
   **Output:**
         
    0
    1
    2
    3
    4
  2. `continue` Statement
  
  The `continue` statement skips the current iteration of the loop and moves to the next iteration. When `continue` is 
  encountered, the rest of the code inside the loop is skipped for the current iteration, and the loop continues with 
  the next iteration.
  #####
   **Use Case:**
   * When you want to skip certain iterations based on a condition without terminating the entire loop.
   **Example:**
   ```python
    for i in range(10):
        if i % 2 == 0:
            continue  # Skip the iteration when i is even
        print(i)
   ```
   **Output:**
         
    1
    3
    5
    7
    9

  3. `pass` Statement

  The `pass` statement is a null operation; it does nothing when executed. It is used as a placeholder for future code. 
  `pass` is often used in situations where syntactically some code is required but you don't want to perform any action.
  
  #####
   **Use Case:**
   * When you're writing code and haven't decided what to do in a loop, function, or conditional block but want to 
     avoid syntax errors.
   * As a placeholder in a class or function definition.
   **Example:**
   ```python
    for i in range(10):
        if i < 5:
            pass  # Placeholder for future code
        else:
            print(i)
   ```

   **Output:**
         
    5
    6
    7
    8
    9

### 3. What is the difference between / and // in Python?
    
   In Python, `/` and `//` are both division operators, but they behave differently in terms of the result they produce.

  1. `/` Operator: True Division
     ####
     The `/` operator performs true division (also known as floating-point division). It returns a floating-point 
     number (a decimal) as the result, regardless of whether the operands are integers or floats.
     ###### Example:
     ```python
      result = 7 / 2
      print(result)
      print(10.0 / 3)
     ```
     ###### Output:
     ```output
      3.5
      3.3333333333333335
     ```
  2. `//` Operator: Floor Division 
     ####
     The `//` operator performs floor division (also known as integer division). It returns the largest integer that 
     is less than or equal to the division result. If both operands are integers, the result will also be an integer. 
     If either operand is a float, the result will be a float, but still representing the floor of the division.
     
     ###### Example:
     ```python
      result = 7 // 2
      print(result)
      print(10.0 // 3)
     ```
     ###### Output:
     ```output
      3
      3.0
     ```

  