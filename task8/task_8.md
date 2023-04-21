# Create a new collection binary tree bag

One of the first data structures discussed in Sedgewick's Algorithms is the Bag. A Bag is a data structure, which holds an unordered collection. We say unordered because it is in contrast to ordered collections like conventional arrays. Because we are not concerned with order, we can store the elements in any way we want.

Createa binary tree structure that will keep the elements in proper order. It will be mutable structure. Basic structure will be MutableSet.

Note that:
* A binary tree doesn't fit well with some sequence features. Notably, we
don't often use an integer index with a binary tree. We most often refer to
elements in a search tree by their key. While we can impose an integer
* index without too much difficulty, it will involve O(n) tree traversals.
A tree could be used for the keys of a mapping; this would keep the keys in
a sorted order at a relatively low cost.