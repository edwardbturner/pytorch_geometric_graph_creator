# Repository to create a PyTorch Geometric graph from scratch

## Requirements
```
(Anaconda) Python 3.6
pandas
torch
torch_geometric
Excel
```

## PyTorch Geometric
This will be used for implementing the netowrk into GCNs.

```ntx_to_pyg.py``` is included purely for interest, I have already saved it's ouput (the PyToch Geometric version of the graph with node features) as ```pyg_featured_71_node_occurrence_graph```. The only possible issue I can see with the code is the ouputs type is "torch_geometric.data.data.Data" rather than the normal "torch_geometric.data.Data".

```pyg_loader.py``` is included just to demonstrate loading of the saved PyTorch Geometric graph and gives some features of the graph.

Note this graph has 250 features associated to each node which can be viewed in ```pvCLCL_features_as_percentages.xls```. Unforunately the node labels have to be removed for PyTorch Geometric and are instead labelled 0, ..., 70. To see the correspondence between the NetworkX node labels (tickers) and the PyTorch Geometric numeric labels see ```node_list.xlsx``` (it isn't alphabetical!).
