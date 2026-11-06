# --- PART 1: VARIABLES & TYPES ---
a = 5                  # Creates a variable holding a single whole number
print(a)               # Output: 5 (shows the single value stored inside a)

type(a)                # Finds the data type silently in memory (shows nothing on screen)
print(type(a))         # Output: <class 'int'> (prints the formal type of variable a)
print(type(a).__name__)# Output: int (prints just the clean name without <class ' '>)

a2 = "50"              # This is a string (text) because it is inside quotes " "
print(type(a2))        # Output: <class 'str'> (str stands for string/text)


# --- PART 2: DICTIONARIES ---
# dict1 is a filing cabinet storing multiple related data items using 'Key: Value' pairs
dict1 = {"name": "aman", "age": 20, "city": "delhi"}

print(dict1)           # Output: {'name': 'aman', ...} (prints the entire cabinet at once)
print(dict1["name"])   # Output: aman (looks up the 'name' label to grab its specific value)
print(dict1["city"])   # Output: delhi (looks up the 'city' label to grab its specific value)
print(type(dict1))     # Output: <class 'dict'> (verifies this container is a dictionary)


# --- PART 3: OPERATORS ---
print(5 + 3)           # Output: 8 (standard addition)
print(5 ** 3)          # Output: 125 (** means power, so 5 * 5 * 5)
print(5 // 2)          # Output: 2 (// is floor division, gives whole quotient without decimal)
