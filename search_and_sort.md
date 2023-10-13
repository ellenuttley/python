# Searching & Sorting Algorithms

Below are my attempts to write various searching and sorting algorithms.

I have included a description for each one, and pseudocode bullet points for the algorithm design

# Search

### Linear Search

Linear search, aka sequential search, is the simplest search algorithm. It involves iteratating through the elements in a list one by one until the target element is found - it then returns the index position of that element. 

**Algorithm**

- Start from the leftmost element of given array and one by one compare element x with each element of array
- If x matches with any of the element, return the index value.
- If x doesn’t match with any of elements in array, return -1 or element not found.

```python
def linear_search(array, target):
    for idx in range(len(array)):
        if array[idx] == target:
            return idx
    return -1

```

---

### Binary Search

Works by dividing the array in half and comparing the target element with the middle element. If the target element is smaller, the search continues in the left half of the array; if it is larger, the search continues in the right half. This process is repeated until the target element is found or the search range becomes empty.

**Algorithm**

- Start by setting the lower bound to 0 and the upper bound to the last index of the array.
- Use binary search to find the target value in the array by continuously dividing the search range in half until the target is found or the range becomes empty.
- If the target value is not found in the array, return -1.

```python
def binary_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

```

Gif representing what is happening in the Binary Search algorithm : 

![https://blog.penjee.com/wp-content/uploads/2015/12/optimal-binary-search-tree-from-sorted-array.gif](https://blog.penjee.com/wp-content/uploads/2015/12/optimal-binary-search-tree-from-sorted-array.gif)

---

# Sort

### Bubble Sort

Bubble Sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 

**Algorithm**

- Start by stepping through the list and compare adjacent pairs of elements.
- Swapped the elements if they are in the wrong order.
- Repeat passing through the unsorted portion of the list until the list is sorted.

```python
def bubble_sort(array):
    length = len(array)
    for idx in range(length):
        for idx_2 in range(0, length-idx-1):
            if array[idx_2] > array[idx_2+1] :
                array[idx_2], array[idx_2+1] = array[idx_2+1], array[idx_2]

```

---

### Selection Sort

Works by dividing the input array into two parts: the sorted part and the unsorted part. It iterates through the unsorted part swapping the first element with the smallest element - putting the smallest element in the first position, before moving on to the next element in the list. This process continues until the entire array is sorted.

**Algorithm**

- Divide input array into two parts: items already sorted and items remaining to be sorted (they make up the rest of the list).
- First find the smallest element in the unsorted sublist and place it at the end of the sorted sublist.
- Continuously grab the smallest unsorted element and place it in sorted order in the sorted sublist.
- Continue this process iteratively until the list is fully sorted.

```python
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

```

---

### Insertion Sort

The array is split into a sorted and an unsorted part, then values from the unsorted part are picked and placed at the correct position in the sorted part. 

**Algorithm**

- Sort the array, and iterate over it
- Compare the current element (key) to its predecessor.
- If the key element is smaller than its predecessor, compare it to the elements before.
- Move the greater elements one position up to make space for the swapped element.

```python
def insertion_sort(array):
    for idx in range(1, len(array)):
        key = array[idx]
        last = idx-1
        while last >= 0 and key < array[last]:
                array[last+1] = array[last]
                last -= 1
        array[last+1] = key

```

---

### Merge Sort

Famous “divide-and-conquer” sorting algorithm. The unsorted list is ****divided**** into smaller sublists until they only contain one element each, these sublists are then merged together in the correct order.

**Algorithm**

**(divide)**

- Continuously divide the unsorted list until you have a sublist containing 1 item, for each item in the original array

**(conquer)**

- Merge (conquer) the sublists together 2 at a time to produce new sorted sublists until all elements have been fully merged into a single sorted array.

```python
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        idx_l = idx_r = idx_a = 0  # indexes for the left, right, and original arrays
        while idx_l < len(left) and idx_r < len(right):
            if left[idx_l] < right[idx_r]:
                array[idx_a] = left[idx_l]
                idx_l += 1
            else:
                array[idx_a] = right[idx_r]
                idx_r += 1
            idx_a += 1
        while idx_l < len(left):
            array[idx_a] = left[idx_l]
            idx_l += 1
            idx_a += 1
        while idx_r < len(right):
            array[idx_a] = right[idx_r]
            idx_r += 1
            idx_a += 1
}

```

---

### Quick Sort

Works by selecting a pivot element from the array and dividing the other elements into two sub-arrays based on whether they are smaller or larger than the pivot. The sub-arrays are then sorted recursively using the same process until the whole array is sorted. 

**Algorithm**

- Divide the collection in two (roughly) equal parts and use that index as the pivot
- Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.
- This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

```python
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [num for num in array if num < pivot]
    middle = [num for num in array if num == pivot]
    right = [num for num in array if num > pivot]
    return quick_sort(left) + middle + quick_sort(right)

```

---

### Shell Sort

Shell Sort is a variation of the Insertion Sort algorithm that uses a gap sequence to sort the elements. It starts by dividing the input array into smaller subarrays and performing Insertion Sort on each subarray. The gap sequence determines the size of the subarrays and is gradually reduced until the array is fully sorted.

**Algorithm** 

- Divide the array into subarrays by choosing a gap sequence.
- Sort each subarray using Insertion Sort.
- Repeat the process with a smaller gap sequence until the array is fully sorted.

```python
def shell_sort(array):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for idx in range(gap, length):
            temp = array[idx]
            idx_2 = idx
            while idx_2 >= gap and array[idx_2 - gap] > temp:
                array[idx_2] = array[idx_2 - gap]
                idx_2 -= gap
            array[idx_2] = temp
        gap //= 2

```

---

### Heap Sort

Uses a binary heap data structure. Builds a max heap from the input array, then repeatedly extracts the maximum element (root of the heap) and places it at the end of the sorted portion of the array. The remaining heap is then “re-heapified” to maintain the heap property, and the process continues until the array is fully sorted.

**Algorithm** 

- Build a max heap from the input array.
- Extract the maximum element (root of the heap) and place it at the end of the sorted portion of the array.
- “Re-heapify” the remaining heap.
- Repeat the extraction and “re-heapification” steps until the array is fully sorted.

```python
def heapify(array, heap, node):
    largest = node
    idx_l = 2 * node + 1
    idx_r = 2 * node + 2
    if idx_l < heap and array[node] < array[idx_l]:
        largest = idx_l
    if idx_r < heap and array[largest] < array[idx_r]:
        largest = idx_r
    if largest != node:
        array[node],array[largest] = array[largest],array[node]
        heapify(array, heap, largest)

def heap_sort(array):
    heap = len(array)
    for node in range(heap // 2 - 1, -1, -1):
        heapify(array, heap, node)
    for node in range(heap-1, 0, -1):
        array[node], array[0] = array[0], array[node]
        heapify(array, node, 0)

```

---

### Counting Sort

A non-comparison-based sorting algorithm that works by determining, for each element in the input array, the number of elements that are smaller than it. It then uses this information to determine the correct position of each element in the output array. *Counting Sort assumes that the input consists of integers with a relatively small range.*

**Algorithm** 

- Create a count array to store the count of each element in the input array.
- Modify the count array to contain the actual position of each element in the output array.
- Build the output array by placing each element in its correct position based on the count array.

```python
def counting_sort(array):
    max_num = max(array)
    count_array = [0] * (max_num + 1)
    sorted_array = [0] * len(array)
    for num in array:
        count_array[num] += 1
    for idx in range(1, len(count_array)):
        count_array[idx] += count_array[idx-1]
    for num in array:
        sorted_array[count_array[num]-1] = num
        count_array[num] -= 1
    return sorted_array
```

---

### Bucket Sort

A distribution-based sorting algorithm that works by dividing the input array into a number of equal-sized “buckets”. Each bucket is then sorted individually, either using another sorting algorithm or recursively applying Bucket Sort. Finally, the sorted elements from all the buckets are concatenated to obtain the fully sorted array.

**Algorithm** 

- Create a fixed number of buckets.
- Distribute the elements of the input array into the buckets based on their values.
- Sort each bucket individually, either using another sorting algorithm or recursively applying Bucket Sort.
- Concatenate the sorted elements from all the buckets to obtain the fully sorted array.

```python
def bucket_sort(array):
    bucket_size = 10
    min_value, max_value = min(array), max(array)
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in array:
        buckets[(num - min_value) // bucket_size].append(num)
    sorted_array = []
    for bucket in buckets:
        sorted_array += sorted(bucket)
    return sorted_array
```

---

### Radix Sort

Radix Sort is a non-comparison-based sorting algorithm that operates by sorting elements based on their digits by iterating through each digit position, and dividing elements into appropriate “buckets”. The term "radix" refers to the base or number system being used to represent the digits of the elements being sorted. It determines the number of buckets or partitions needed during each iteration. 

*In my example I am working with decimal numbers (base 10), so the radix is 10, and I use 10 buckets (0 to 9) to sort the elements based on their digits.* 

**Algorithm** 

- Iterate through each digit position, creating a ‘bucket’ for each.
- Sort each bucket individually using a stable sorting algorithm, using a temp element to store elements during the sorting process
- Concatenate the sorted buckets to obtain the partially sorted array.
- Repeat the above steps for each digit position, until the array is fully sorted

```python
def radix_sort(array):
    radix = 10
    max_len = False
    digit = 1
    while not max_len:
        max_len = True
        buckets = [[] for _ in range(radix)]
        for num in array:
            temp = num // digit
            buckets[temp % radix].append(num)
            if max_len and temp > 0:
                max_len = False
        idx = 0
        for bucket in buckets:
            for num in bucket:
                array[idx] = num
                idx += 1
        digit *= radix
    return array

```

---

### Cubesort

A non-comparison-based sorting algorithm that works by counting the occurrence of each element in the input array and then using those counts to order them.

**Algorithm** 

- Count the occurrence of each element in the input array.
- Reconstruct the sorted array based on the count information.

```python
def cubesort(array):
    max_num = max(array)
    length = len(array)
    count_array = [0] * (max_num + 1)
    for num in array:
        count_array[num] += 1
    sorted_array = []
    for idx in range(length):
        sorted_array.append(0)
    for idx in range(max_num, -1, -1):
        while count_array[idx]:
            sorted_array[length - count_array[idx]] = idx
            count_array[idx] -= 1
    return sorted_array

```

---
