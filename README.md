*This project has been created as part of the 42 curriculum by humontas*

# ft_linear_regression — Car Price Prediction

A Python application that predicts car prices based on mileage using a linear regression model.

The project provides both a command-line interface and a graphical interface to train the model, make predictions, and evaluate its accuracy.

## Description

ft_linear_regression implements a complete prediction workflow:

* Train a model from a dataset
* Predict a car price from a given mileage
* Evaluate the model accuracy using R² score
* Visualize the regression results
* Keep track of previous predictions

The graphical interface provides an easier way to interact with the model without using the command line.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Train the model

```bash
python3 sources/train.py
```

The training parameters can be modified in `config.json`.

### Predict a price

```bash
python3 sources/predict.py
```

Example:

```
Enter the mileage: 150000

Estimated price: 7850.42
```

### Evaluate the model

```bash
python3 sources/precision.py
```

Example:

```
Model precision (R²): 73.30%
```

The R² score indicates how well the model fits the dataset.

## Graphical interface

```bash
python3 sources/gui.py
```

The GUI allows you to:

* Train the model
* Predict prices
* Display the model precision
* View prediction history
* Reset the model
* Access generated files

## Configuration

All training and visualization parameters are configurable via `config.json`.

| Parameter          | Description                             | Example |
| ------------------ | --------------------------------------- | ------- |
| `learning_rate`    | Controls the size of each training step | `0.1`   |
| `iterations`       | Number of training iterations           | `10000` |
| `verbose`          | Display training progress               | `false` |
| `show_line`        | Display regression line                 | `true`  |
| `show_predictions` | Display prediction history on graph     | `true`  |

Increasing the number of iterations does not always improve the model.
A very high value can increase training time significantly while providing little or no improvement.

The optimal values depend on the dataset and learning rate.

## Bonus features

The project goes beyond the original requirements by adding:

* Graphical user interface
* Prediction history
* Model evaluation with R² score
* External configuration system
* Multi-platform file opening support
* Reset functionality
