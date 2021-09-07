# Repository to create a PyTorch Geometric graph from scratch

## Requirements
```
(Anaconda) Python 3.6
pandas
torch
torch_geometric
Excel
```
## Instructions
This is a simple code to transform a graph (with adjacency matrix) from an excel sheet to a PyTorch Geometric graph object. The graph may be weighted, directed and have self loops. I created this as there seems to be a real lack of literature on creating your own PyTorch Geometric graphs online.

The ```excel_example.xls``` file is included to show the necessary excel layout, simply download and edit it to fit your graph. Note for the adjacency matrix of a weighted graph the (i, j) entry is the edge from node i to node j.

If this is found to be helpful in your work consider refrencing/linking the repository.
