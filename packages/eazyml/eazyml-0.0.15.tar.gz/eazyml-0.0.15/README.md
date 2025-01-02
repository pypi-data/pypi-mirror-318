## Eazyml Modeling
![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)  ![PyPI package](https://img.shields.io/badge/pypi%20package-0.0.9-brightgreen) ![Code Style](https://img.shields.io/badge/code%20style-black-black)

This API allows users to build machine learning models.

### Features
- Build model and predict on test data for given model.
- Provides utils function which can be used to beautify dataframe, dict or markdown format data.

### APIs
It provides following apis :

1. ez_init_model :
Initialize and build a predictive model based on the provided dataset and options.

    ```python
    ez_init_model(
            df='train_dataframe'
            options={
                "model_type": "predictive",
                "accelerate": "yes",
                "outcome": "target",
                "remove_dependent": "no",
                "derive_numeric": "yes",
                "derive_text": "no",
                "phrases": {"*": []},
                "text_types": {"*": ["sentiments"]},
                "expressions": []
            }
    )

2. ez_predict :
Perform prediction on the given test data based on model options and validate the input dataset.

    ```python
    ez_predict(
            test_data ='test_dataframe'
            options={
                "extra_info": {

                },
                "model": "Specified model to be used for prediction",
                "outcome": "target",
            }
    )

