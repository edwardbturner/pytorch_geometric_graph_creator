import pandas as pd
import torch
import torch_geometric.data
from torch import Tensor


# This creates the edge index and the associated weights

df_1 = pd.read_excel('excel_example.xls', sheet_name='adjacency_matrix')

start_node = []
end_node = []
weight = []

for i in range(len(df_1)):
    s = df_1[i]
    for j in range(len(df_1)):
        val = float(s[j])
        if val != 0.0:
            start_node.append(j)
            end_node.append(i)
            weight.append(val)

edge_index = torch.tensor([start_node, end_node])
edge_weight = torch.tensor(weight)


# This creates the node features

df_2 = pd.read_excel('excel_example.xls', sheet_name='node_features')

features = []

for i in range(len(df_1)):
    list = df_2[i].tolist()
    features.append(list)

x = torch.tensor(features)


# This creates the node labels

df_3 = pd.read_excel('excel_example.xls', sheet_name='node_labels')

labels = df_3['label']

y = torch.tensor(labels)


from torch_geometric.data import Data
data = Data(x=x, y=y, edge_index=edge_index, edge_weight=edge_weight, num_nodes=len(df_1))

torch.save(data, './pytorch_geometric_graph')
