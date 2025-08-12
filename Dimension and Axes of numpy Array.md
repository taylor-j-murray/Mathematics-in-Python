
** Warning: This is a rough draft and still needs some cleaning up **

# Dimension and Axes of numpy Arrays

## What is a numpy Array

The numpy object numpy.array is similar to an array object in the native python language with two exceptions
1. A numpy.array must be homogenous, meaning that the type of all elements of the array must be the same.
2. A numpy.array stores the data in the array much more efficiently than its native python counterpart. 

One way in which we can create a numpy.array is by feeding in an array-like object e.g a python list or python array into the function 
numpy.array(). For example

```python
import numpy as np
A = [[1,2,3],[4,5,6]]
A = np.array(A)
```
```output
[[1 2 3]
 [4 5 6]]
```

You will notice that I have imported numpy with the alias `np`; this convention will be kept through out this document.
Here are a few other ways to create an np.array

```python
np.zeros((2,4),dtype = int)
```
```output
[[0 0 0 0]
 [0 0 0 0]]
```

```python
np.ones((2,2,3), dtype = int)
```
```output
[[[1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]]]
```
## The Dimension and Axes of a np.array
Roughly speaking (we will make this rigorous below with mathematics) the **dimension** of an np.array is how many nested brackets an np.array has. One can find
the dimension of a given np.array by calling for its attribute `ndim`. For example:

```python
A = np.array([])
B = np.array([1])
C = np.array([[]])
D = np.array([[[1]][[2]])
A.ndim
B.ndim
C.ndim
D.ndim
```
```output
1
1
2
3
```

The axes of a np.array is, roughly speaking, are the `dimensions` of the array. For example an np.array `[[1,2,1],[3,3,2]]` has and has dimension 2 and shape `(2,3)`
where there are two elements in the 0-axis and 3 elements in the 1-axis. This description of the dimension and axes of an np.array is not satisfying, at least 
to the author, which leads us into the next section.

## A Mathematical Description of the Dimension and Axes of an np.array




### The Depth and Levels of a Set

Our goal for this section is to study the notion of `depth` in set theory (a branch of mathematics) and define an analogous notion to lists/arrays to help describe dimension and axes. 

The `depth` of a set is roughly how deep a set is. Precisely, the `depth` of a set is defined recursively, as follows:
* The depth of the empty set {} is 0
* The depth of any object which is itself not a set is 0. E.g the depth of 1,2,3... are all zero.
* The depth of a set S is 1 plus the maximum depth among all the elements of S

Example 1: The depth of {{}} is 1 since {} has depth 0.

Example 2: The depth of {1} is 1 since 1 has depth 0.

Example 3: The depth of {1,{{}}} is 2 since the depth of {{}} is 1.

These examples illuminate the connection between the depth of a set and the dimension of an np.array, albeit with a few small caveats:
* The depth of the empty set {} is 0, whereas the dimension of the empty np.array is 1. 
* Sets cannot have duplicated elements, unlike arrays.
* Sets are not ordered, unlike arrays.

To fix these disparities, we introduce the notion of `refined depth` of a list/array. The `refined depth` of a list/array is defined recursively as follows
* the refined depth of anything that is itself not a list/array is 0.
* the refined depth of [] is 1.
* the refined depth of a list/array S is the maximal refined depth among the elements of S.

Taking our examples above and computing the refined depth we obtain:

Refined Example 1: The refined depth of [[]] is 2 since [] has refined depth 1.

Refined Example 2: The refined depth of [1] is 1 since 1 has refined depth 0.

Refined Example 3: The refined depth of [1,[[]]] is 3 since the depth of [[]] is 2.

The upshot of refined depth is that it is lines up exactly to the notion of dimension of np.arrays, which is what we are after. 

Our next goal is to use refined depth to describe the axes of an np.array. To this end, we define the notion of the `i-level`
for a list/array S. For a set S of refined depth n>0 and i a non-negative integer with i < n, we define the `i-level` of S, denoted `S_i`, recursively as follows:
* The 0-level of S is S_0 = [S]
* The 1-level of S is defined as S.
* Given S_i, we define S_(i+1) = [x in T | T is in S_i]

Example 4: Let S =[[1,2],[3,4]]. Then
* S_0 = [S]
* S_1 = [[1,2],[3,4]]

With this new terminology in hand, we are ready to describe what the dimension and axes of an np.array are.

## From Math to CS

* Given an np.array, call it A, we define the `dimension` of A to be the refined depth of A.
* Given an np.array, call it A with dim(A)>0, and j a positive integer less than dim(A), we define the `j-th` axis of A as the `j-th`-level of A.

Why is the proposed definition of an axis of an np.array a good one? We will convince the reader of this through an example

Example 5: Consider the np.arrays `A = [[[1,2]],[[3,4]]]` and `B = [[[0,0]],[[1,1]]]`. We have

* `A_0 = [A]` and `B_0 = [B]`
* `A_1 = A` and `B_1 = B`
* `A_2 = [[1,2]],[[3,4]]` and `B_2 =[[0,0]],[[1,1]]`

Now, 

* `concatenate([A,B], axis = 0) = [[[1,2]],[[3,4]],[[0 0]],[[1,1]]]`

* `concatenate([A,B], axis = 1) = [[[1,2],[0,0]], [[3,4],[1,1]]]`

* `concatenate([A,B], axis = 2) = [[[1,2,0,0]],[[3,4,1,1]]]`


We then see that `concatenate([A,B], axis = i)` is obtained by 'indexing' along A_j and B_j simultaneously. Using the methods of python lists, this can be described  rigorously as follows:
* First, we define a function J_i on lists for i recursively, as follows: let J_0(L) =L, and given J_k define J_(k+1)(L) = [J_k(L)]. 
* For i = 0, we have that `concatenate([A,B], axis = 0)` is simply `A.append(B)` (again, viewing these as lists!)
* For i > 0, we have that `concatenate([A,B], axis = i)` is precisely (as lists) `J_i([A[j],B[j] for j in range(len(A_i))])`.











