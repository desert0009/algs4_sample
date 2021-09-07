# Algs4 in Python3

- Algorithm and Data structure theories
- Practices code in Python3


## Python
- Mutable vs Immutable Objects
  - Mutable Objects
    * list, dict, set
  - Immutable Objects
    * bool, int, float, str, tuple
- Usage for Decorator
  - Useful as they allow the extension of an existing function, without any modification to the original function source code
  - Ex: Analysis of memory consumption for python programs (@profile)
- Deep Copy vs Shallow Copy
  - Deep Copy
    * Completely independent of the original object
  - Shallow Copy
    * “one-level-deep” copy.

 
  ```
  import copy

  l1 = [1, 2, [3, 5], 4]
  # deep copy sample
  # l3 = copy.deepcopy(l1)

  # shallow copy sample
  # l2 = l1[:] 
  # l2 = copy.copy(l1)

  l2 = copy.copy(l1)
  l3 = copy.deepcopy(l1)

  l1[2][0] = 7
  print(l2) # [1, 2, [7, 5], 4]
  print(l3) # [1, 2, [3, 5], 4]
  ```

## Algorithm and Data structure

#### Hash Table (dict())
- Save items in a key-indexed table
- O(1) search time

#### Queue and Stack
- Queue (FIFO) and BFS
  - **BFS** uses **Queue** data structure for finding the shortest path and do level-order traversal.
- Stack (FILO) and DFS
  - **DFS** to do pre-order, in-order and post-order traversal with **Stack** data structure.

#### Sorting
- Sorting Algorithms Summary

|             | Inplace | Stable | Worst      | Average    | Best       | Remark                                              |
|-------------|---------|-------:|------------|------------|------------|-----------------------------------------------------|
| Selection   |    Y    |        | O(N^2 / 2) | O(N^2 / 2) | O(N^2 / 2) |                     N exchanges                     |
| Insertion   |    Y    |    Y   | O(N^2 / 2) | O(N^2 / 4) |    O(N)    |         Use for small N or partially ordered        |
| Shell       |    Y    |        |            |            |    O(N)    |               Tight code, subquadratic              |
| Merge       |         |    Y   |   O(NlgN)  |   O(NlgN)  |   O(NlgN)  |              O(NlgN) guarantee, Stable              |
| Quick       |    Y    |        | O(N^2 / 2) |  O(2NlgN)  |   O(NlgN)  | O(NlgN) probabilistic guarantee. Faster in practice |
| 3-way Quick |    Y    |        | O(N^2 / 2) |  O(2NlgN)  |    O(N)    |   Improves QuickSort in presence of duplicate keys  |
| Heap        |    Y    |        |  O(2NlgN)  |  O(2NlgN)  |   O(NlgN)  |             O(NlgN) guarantee, in-place             |
| ???         |    Y    |    Y   |   O(NlgN)  |   O(NlgN)  |   O(NlgN)  |                  Holy Sorting Grail                 |

#### Graph
- Graph representation in practice - **Adjacency-list**
  - Space O(V+E). 
  - V: no. of vertices, E: no. of edges

```
[Graph]
0--1
|\
| \
2--3

[Adjacency-list]
graph = {
  0: [1,2 3],
  1: [0],
  2: [0, 3],
  3: [0, 2]
}
```


## Practices Code

- #### [Array](array)
- #### [String](string)
- #### [Stack and Queue](stack_queue)
- #### [Linked List](linkedlist)
  - [Build the Linked List from array](linkedlist/util_linkedlist.py)
- #### [Tree](tree)
  - [Encode and decode binary tree](tree/util_binary_tree.py)
- #### [Graph](graph)
- #### [Backtracking](backtracking)
- #### [Searching](search)
- #### [Sorting](sorting)
- #### [Dynamic Programming](dynamic_programming)
- #### [Design](design)
- #### [Trie](trie)
- #### [Math](math)
- #### [Union Find](union_find)


## Reference
- [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/home/)
- [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/)