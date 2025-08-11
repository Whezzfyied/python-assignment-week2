Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> my_list =[]
>>> print("After creation:", my_list)
After creation: []
>>> my_list.append(10)
>>> my_list.append(20)
>>> my_list.append(30)
>>> my_list.append(40)
>>> print("After appends:", my_list)
After appends: [10, 20, 30, 40]
>>> my_list.insert(1, 15)
>>> print("After inserting 15 at second position:", my_list)
After inserting 15 at second position: [10, 15, 20, 30, 40]
>>> my_list.extend([50, 60, 70])
>>> print("After extend:", my_list)
After extend: [10, 15, 20, 30, 40, 50, 60, 70]
>>> removed = my_list.pop()
>>> print("Removed last element:", removed)
Removed last element: 70
>>> print("List now:", my_list)
List now: [10, 15, 20, 30, 40, 50, 60]
>>> my_list.sort()
>>> print("After sorting ascending:", my_list)
After sorting ascending: [10, 15, 20, 30, 40, 50, 60]
>>> index_30 = my_list.index(30)
>>> print("Index of value30:", index_30)
Index of value30: 3
