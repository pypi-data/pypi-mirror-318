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

To install the tool locally, use:

pip install .

---

## **Usage Example**

Below is an example of how to use the tool to visualize the Log-Loss function:

```python

from log_loss_tool import plot_log_loss_with_custom_input

# Visualize the Log-Loss function with a predicted probability of 0.7
plot_log_loss_with_custom_input(probability=0.7, optimal_threshold=0.5)

```

---

## **Input Parameters**
- **probability:** Predicted probability (h(x)). Must be between 0 and 1.
- **log_loss:** Log-loss value for y=1. If provided, it calculates the corresponding probability.
- **gradient:** Gradient value for y=1. If provided, it calculates the corresponding probability.
- **optimal_threshold:** The threshold used to classify the prediction into y=0 or y=1.
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
