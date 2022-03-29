# Tensor-SC
Tensor-SC is an implementation of a probabilistic tensor decomposition framework for single-cell multi-omics data integration. Tensor-SC accepts the input of datasets from multiple omics, with missing values allowed.

![image](https://github.com/deepomicslab/Tensor-SC/blob/main/framework.png)

# Getting started

## Prerequisite
+ numpy
+ pytorch 1.9.0

## Install
```
pip install Tensor-SC
```

## Examples
This is an example for the multiple datasets when features have corresponding information.
```Python
from tensorsc import sc_multi_omics

data = np.array([expression_data, methylation_data])
sc_model = sc_multi_omics()
predict_data = sc_model.fit(data) # the imputed data
np.savetxt("global_cell_embeddings.csv", sc_model.C, delimiter = ',') # global cell embeddings
np.savetxt("global_gene_embeddings.csv", sc_model.G, delimiter = ',') # global gene embeddings
np.savetxt("local_cell_embeddings.csv", sc_model.C, delimiter = ',') # omics-specific cell embeddings
np.savetxt("local_gene_embeddings.csv", sc_model.G, delimiter = ',') # omics-specific gene embeddings
```
When the features of different omics do not have corresponding information, please use ```fit_list``` function, which accepts the input as a list of matrices.
```Python
from tensorsc import sc_multi_omics

data = [expression_data, protein_data]
sc_model = sc_multi_omics()
predict_data = sc_model.fit_list(data)
```
If the input does not contain missing values ("NA"), we provide ```fit_complete``` and ```fit_list_complete``` functions to accelerate the optimization, since they take the advantages of matrix operations.
```Python
from tensorsc import sc_multi_omics

data = np.array([expression_data, methylation_data])
sc_model = sc_multi_omics()
predict_data = sc_model.fit_complete(data) # the imputed data
```
```Python
from tensorsc import sc_multi_omics

data = [expression_data, protein_data]
sc_model = sc_multi_omics()
predict_data = sc_model.fit_list_complete(data)
```

We put the complete scripts for analysis described in the manuscript under ```examples/``` directory, for detailed usage examples and the reproduction. The example data can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1F_WBwNsHggjTqgFfTm6IugNKpb0xJTje?usp=sharing).

## Parameters


