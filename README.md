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
```Python
from tensorsc import sc_multi_omics

data = np.array([expression_data, methylation_data])

sc_model = sc_multi_omics(K1=30, K2=30, K3=30)
predict_data = sc_model.fit(data, opt="Adam", dist="negative_bionomial", n_epochs=260, lambda_C_regularizer=0.01, lambda_G_regularizer=0.01, lambda_O_regularizer=[0.01, 0.01], lambda_OC_regularizer=[1, 1], lambda_OG_regularizer=[1, 1], batch_size=256, device="cpu")
```

The example data can be downloaded from [Google Drive](https://drive.google.com/drive/folders/1F_WBwNsHggjTqgFfTm6IugNKpb0xJTje?usp=sharing).






## Parameters


