# File Handling, and API Calls

Some basic code snippets that include file handling and API calls, with brief explanations 

---

### Astronaut API

Makes a call to an API endpoint to get live information about astronauts in space, then adds each astronauts name to a txt file, on a new line

```python
import requests
response = requests.get('<http://api.open-notify.org/astros.json>')

resp_dict = response.json()

with open('astronaut.txt', 'a+') as file:
    for astronaut in resp_dict['people']:
        each_astronaut = (astronaut['name'])
        file.write(each_astronaut + '\\n')

```

---

### ISS Tracking

Makes a call to the iss-now API to get the current location for the International Space Station, converts the 'timestamp' from the response into readable date and time format, and writes a log to the new file that captures time and ISS's location

```python
import requests
from datetime import datetime

endpoint = "<http://api.open-notify.org/iss-now.json>"
response = requests.get(endpoint)

if response.status_code == 200:
    data = response.json()
else:
    data = 'Error'

current_datetime = datetime.fromtimestamp(data['timestamp'])
print("Current Date / Time :", current_datetime)

msg = f"At {current_datetime} the ISS was at latitude: {data['iss_position']['latitude']} and longitude: {data['iss_position']['longitude']}"
print(msg)

with open('iss_log.txt', 'a+') as file:
    file.write(msg + '\\n')
```

---

### Pokémon Info

Prints the height and weight of a specific Pokémon, and then all that Pokémon’s moves

```python
import requests

response = requests.get('<https://pokeapi.co/api/v2/pokemon/6/>')
data = response.json()

print("Height: ", data['height'])
print("Weight: ", data['weight'])

print("Moves: ")
for move in data['moves']:
    print(move['move']['name'])

```

---

### Teenager Registration

A program to validate whether users are in fact teenagers before completing their registration. Includes functions to validate the entered age and name, and a main code block to prompt the user for input, validate it, and write the registration information to a file. Error messages are displayed for any validation or file writing errors, and a success or failure message is printed at the end

```python
def age_validation(age):
    if age < 0:
        raise ValueError("Only positive integers allowed!")
    assert 12 < age <= 19
    return True

def name_validated(name_string):
    if ',' not in name_string:
        raise ValueError("Incorrect input, please write names seperated by a comma")
    name, surname = name_string.split(",")
    if not len(name) or not len(surname):
        raise ValueError("Incorrect info, please input the missing name ")

isSuccessful = False

try:
    name = input("Please enter your first and last name, seperated by a comma : ")
    name_validated(name)
    age = int(input("Please enter your age : "))
    age_validation(age)
except ValueError as exc:
    print("Invalid input : %s" % exc)
except AssertionError:
    print("The age is not within range")
else:
    with open("registration_file.exe", "a+") as file:
        file.write(f"New member{name} and {age}. \\n")
    isSuccessful = True
finally:
    if isSuccessful:
        print("Registration Successful")
    else:
        print("Could not complete registration. Please try again")

```

---

### Simple File Reading

Reads and prints the contents of a file specified by the `file_name` parameter. The function uses the `open()` function with the 'r' mode to open the file in read-only mode and then uses the `readlines()` method to read and print all the lines in the file. If the specified file is not found, a `FileNotFoundError` is caught and an appropriate error message is displayed.

```python
def readFile(file_name):
    try:
        with open(file_name, 'r') as f:
            print(f.readlines())
    except FileNotFoundError as exc:
        print(exc)

readFile("hello.txt")
```

Reads data about trees from a file to find the shortest tree

```python
import csv

with open('trees.csv', 'r') as file:
    reader = csv.DictReader(file)
    tree_heights = [int(row['height']) for row in reader]

    print(min(tree_heights))
```

---

### Simple To-Do List Function

Reads the contents of the existing to-do items, asks the user to input a new to-do item, adds a new to-do, and saves the updated file 

```python
with open("todo.txt", "r+") as file:
    print(file.read())

new_item = input("What is your todo list item? : ")
file.write(f"\\n {new_item}")

```

---

### Simple Counting Function

Takes a word from the user and count the number of occurrences of that word in a file

```python
with open('5.3_example_one.txt', 'r') as file:
    text = file.read()

    word = input("Enter a word to count: ")

    count = text.count(word)

    print(f"The word '{word}' appears {count} times in the text.")

```

---

### Reading a CSV

This example uses `csv.reader` to read the CSV file 'example.csv' and print the data as a list of values for each row :

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

This example uses `csv.DictReader` to read the same CSV file and print the data as a dictionary for each row, with the keys being the column names in the first row of the file :

```python
with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

```

---

### Writing a CSV

This example uses `csv.writer` to write data to a CSV file row by row. It takes a list of values as input and writes them to the file as a single row :

```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerow(['Reece', '32', 'Male'])
    writer.writerow(['Robin', '7', 'Female'])
```

This example does the same as above, but with `csv.DictWriter` :

```python
import csv

field_names = ["name", "age"]
data = [
    {'name': "Jack", 'age': 32},
    {'name': "Jill", 'age': 24}
]

with open("team.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)
```

---
