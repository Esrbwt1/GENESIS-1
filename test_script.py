# test_script.py
print("Starting the test script...\n")

# Basic arithmetic
result = 2 + 3
print(f"1. Basic arithmetic test: 2 + 3 = {result}")

# List operations
my_list = [1, 2, 3]
print(f"\n2. List test - Original list: {my_list}")
my_list.append(4)
my_list.reverse()
print(f"   After appending '4' and reversing: {my_list}")

# String manipulation
str1 = "Hello"
str2 = "World!"
combined = f"{str1} {str2}"
print(f"\n3. String test: {combined}")
print(f"   Sliced string: {combined[:5]}")

# Conditional check
num = 10
print(f"\n4. Conditional test:")
if num % 2 == 0:
    print(f"   {num} is even")
else:
    print(f"   {num} is odd")

# Loop test
print("\n5. Loop test:")
for i in range(5):
    print(f"   Iteration {i}", end=", ")

# Dictionary test
print("\n\n6. Dictionary test:")
my_dict = {"key1": "value1", "key2": 42}
for key, value in my_dict.items():
    print(f"   {key}: {value}")

print("\nTest script completed successfully!")