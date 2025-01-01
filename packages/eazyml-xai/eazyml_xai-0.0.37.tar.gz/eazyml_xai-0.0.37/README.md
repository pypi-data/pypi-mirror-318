## Eazyml Explainable AI
![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)  ![PyPI package](https://img.shields.io/badge/pypi%20package-0.0.33-brightgreen) ![Code Style](https://img.shields.io/badge/code%20style-black-black)

It provides explanations for a model's prediction, based on provided train and test data files.

### Features
- It provides explanations for a model's prediction, based on provided train and test data files.
### APIs
It provides following apis :

1. scikit_feature_selection
    ```python
    ez_explain(
            mode='classification',
            outcome='target',
            train_file_path='train.csv',
            test_file_path='test.csv',
            model=my_model,
            data_type_dict=data_type_dict,
            selected_features_list=lis_of_derived_features,
            options={"data_source": "parquet", "record_number": [1, 2, 3]})
