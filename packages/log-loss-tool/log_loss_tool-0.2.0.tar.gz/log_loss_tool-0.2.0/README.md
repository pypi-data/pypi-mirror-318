# **Log Loss Tool**

A Python library designed to visualize and simplify the understanding of the Log-Loss function, gradients, and probabilities in binary logistic regression models.

---

## **Purpose**

This library was created to assist beginners and professionals in:
- Abstracting complex calculations behind the Log-Loss function.
- Visualizing gradients and probabilities to better understand their influence on the loss function.
- Building intuition about binary logistic regression through clear, customizable plots.

---

## **Features**
- Visualization of the Log-Loss function for both classes (y=1 and y=0).
- Gradient Behavior Analysis: Explore how gradients change with probability.- Customizable Plots: Configure colors, labels, gridlines, and more.
- Educational Support: Perfect for students, educators, and professionals who want to strengthen their understanding of logistic regression.

---

## **Installation**

To install the tool, use the following command:

```bash
pip install log_loss_tool
```

---

## **Usage Example**

Below is an example of how to use the tool to visualize the Log-Loss function:

```python
from log_loss_tool import plot_log_loss_with_custom_input

# Visualize the Log-Loss function with a predicted probability of 0.7 and a threshold of 0.5
plot_log_loss_with_custom_input(probability=0.7, threshold=0.5)

# Alternatively, use log-loss and gradient values to calculate threshold automatically
log_loss = 0.5  # log-loss calculated from training/testing
gradient = -3.0  # gradient calculated from the log-loss
plot_log_loss_with_custom_input(log_loss=log_loss, gradient=gradient)

```

---

## **Example Visualization**

Below is an example of the Log-Loss function visualization:

```python

# Plot with calculated log-loss and optimal threshold
plot_log_loss_with_custom_input(log_loss=log_loss_value, threshold=threshold_otimo)

```

![Log-Loss Graph](log_loss_example.png)


This image illustrates how the Log-Loss function behaves with the given probability and threshold. The image above is for illustrative purposes, showing the impact of different thresholds on the loss function.

---

## **Input Parameters**
- **probability:** Predicted probability (h(x)). Must be between 0 and 1.
- **log_loss:** Log-loss value for y=1. If provided, it calculates the corresponding probability.
- **gradient:** Gradient value for y=1. If provided, it calculates the corresponding probability.
- **optimal_threshold:** The `optimal_threshold` is used to classify the predicted value into class 0 or 1:

- If not provided, the function will automatically use the default value of **0.5**.
- This threshold determines the cutoff for classification, where values above it will be classified as class 1 and below it as class 0.

If you would like to calculate an optimal threshold based on the data, you can provide a value. Otherwise, the default of 0.5 will be used.
- **title, figsize, font_size, etc.:** Options to customize the plot style.

---

## **Why Use Log Loss Tool?**

Understanding machine learning models often requires digging into mathematical details. This tool provides a visual and intuitive way to:
- Grasp how probabilities influence the Log-Loss function.
- See how the gradient behaves during optimization.
- Communicate model behavior to others through visuals.

---

## **Contributing**

We welcome contributions to improve this library. To contribute:
	1.	Fork the repository.
	2.	Create a new branch.
	3.	Make your changes and add tests.
	4.	Submit a pull request.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Author**

This project was created by Rodrigo Campos.  
**Email:** rodrigocamposag90@gmail.com  
**GitHub:** RodrigoCamposDS  
**Date:** 2025-01-01  
