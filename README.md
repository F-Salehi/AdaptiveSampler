
# TreeSampler

TreeSampler is a tree data structure, which is efficient for sampling from an unnormalized categorical distribution (with $n$ categories) and updating the sampling weight of 1 of the categories. Sampling and updating can be done in $O(\log n)$. The code is used in "[Stochastic Optimization with Bandit Sampling](https://arxiv.org/abs/1708.02544) ", F. Salehi, P. Thiran, and E. Celis, 2017.

The code is 200 times faster compared to the implementation with numy.choice (see the notebook below).

Each node in the tree has attributes: 
* pointer to the left child, 
* pointer to the right child, 
* pointer to the parent node,
*  node id (node id of the leaves start from 0 to $n$)
* node value 

## Methods

* Adding a node to the tree with value v, parent node par, and node id n_id.
```
add(self, val, par, n_id)
```
* Getting the root of tree.
```
getRoot(self)
```
* Finding the node of the tree with a specific id.
```
find_id(self,n_id)
```
* Sampling according to the unnormalized distribution of the leaves.
```
sample(self)
``` 
* Initializing the values of the leaves of the tree with value_list.
```
initialize(self, value_list)
``` 
* Updating the value of a node.
```
update(self, node, value_new)
``` 
* In-order traversal of the tree.
```
printTree(self)
``` 


To start, you might want to look at the notebook

* "[TreeSampler Example Code](https://github.com/F-Salehi/AdaptiveSampler/blob/master/example.ipynb)"

