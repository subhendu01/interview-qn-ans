x = 10  # Global namespace


def outer():
   x = 20  # Enclosing (nonlocal) namespace
   def inner():
       x = 30  # Local namespace
       print("Inner x:", x)

   inner()
   print("Outer x:", x)

outer()
print("Global x:", x)