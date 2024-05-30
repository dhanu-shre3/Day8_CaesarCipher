# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello")
#     print("How are you doing")
#     print("My name is Dhanu")

# greet()    
#parameter is the name of the data that's passed in
#argument is the actual data
#function that allows input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print("How are you doing")
#     print("My name is Dhanu")

# greet_with_name("Anna")    

#function with more than 1 input

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is the weather in {location}")    

# greet_with("Jack", "London")    

def prime_checker(number):
  is_prime =  True
  for num in range(2, number):
     if number % num == 0:
       is_prime = False
       
  if is_prime:
     print("It's a prime number.")   
  else:
      print("It's not a prime number.")   