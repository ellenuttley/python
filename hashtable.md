# Hash Table
My attempt at a basic hash table, that is set up to handle collisions. 

When there is no collisions, the insert method makes a new node object using the original_key and the value - this is then inserted into the hash table. The index that it is inserted at is decided by the has_index method. 

The hash_index method takes the original_key and turns it into a hashed_key by iterating through the letters and turning them to ASCII using ord(), it then multiplies the ascii by seven (a prime number), before using the 
modulo operator of 31 (another prime number) on the total to assign the index to one of the 31 spots in the hash table. The use of prime numbers should make collisions less likely. 

If there is no collision, as in there is no Node / linked list currently at the hashed_index, then when it gets to that hashed_index a new linked list will be created with the inserted value as the root node.

If there is a collision, when the hashed_index is reached the code will carry on until it has reached the end of the last child node / the leaf node,
the value will then be inserted there. During this process, the chain between each node is defined using node.next - essentially
providing a link between each list item as well as defining the order that they appear in the linked list. 

```python

# defines a node : 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# defines the table : 
class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, original_key, value):
        index = self.hash_index(original_key)
        if index in self.table:                  
            node = self.table[index]               
            while node.next:                       
                node = node.next                   
            node.next = Node(original_key, value)  
        else:
            self.table[index] = Node(original_key, value)  
            return f"Inserted : {original_key}:{value} at index : {index}"

    def search(self, original_key):
        index = self.hash_index(original_key)
        if index in self.table:
            node = self.table[index]             
            while node:                          
                if node.key == original_key:     
                    return f"Found : {original_key}:{node.value}"
                node = node.next                  
        return f"{original_key} not in the hash table"

    def delete(self, original_key):
        index = self.hash_index(original_key)
        if index in self.table:
            node = self.table[index]         
            if node.key == original_key:     
                del self.table[index]
                return f"Deleted : {original_key}:{node.value}"
            else:
                while node.next:                            
                    if node.next.key == original_key:       
                        value = node.next.value             
                        node.next = node.next.next          
                        return f"Deleted : {original_key}:{value}"
                    node = node.next
        return f"{original_key} not in the hash table"

    @staticmethod
    def hash_index(original_key):
        hashed_key = 0
        for i in original_key:
            hashed_key += ord(i) * 7
        return hashed_key % 31    # prime numbers are less likely to collide
```
