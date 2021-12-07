# algorithims
Random algos

##BT Weight Max
Bianry Tree Max Weight

Given a binary tree where each node represents a 'weight'
this algo finds the maximum non-adjecent nodes sum

This algo cosiders nodes on the same path as adjecent (rather than just sharing an edge), and
thus is kinda useless


##Binomial
Calculates the amount of shortest paths between two points in a 2D plane.

you can only move vertically or horizontally to the next discrete point. (0,0) -> (0,1).
This is called Binomial since the probably is really just calcualting Pascals triangle/Binomial Coeficents.

##Fib
Dynamic Programe for calcuating a certain fibonacci 

##QuickSort
Its quick sort

##Hamilton_Path
Given a complete directional graph (sometimes refered to as a tournament graph though not like the real word one), this algorithm finds a Hamiltion path.
A Hamiltion path is just a path that goes to everynode and only once.

This algorithm runs O(nlgn) and is based off a mathematical proof that for any complete directed graph, there exists a Hamiltion path. Very similar to Merg Sort

The graph is stored as a list of Node objects, where each Node object has two lists: inNodes[] & outNodes[]. These lists point to other nodes where inNodes[] are all nodes that have a directed path into Node, and outNodes[] are all the nodes that Node has a directed path too.
