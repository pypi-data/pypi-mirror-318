import numpy as np
import matplotlib.pyplot as plt

def plot_log_loss_with_custom_input(
    probability=None,
    log_loss=None,
    gradient=None,
    threshold=None,  # Renomeado de optimal_threshold para threshold
    title="Logarithmic Loss Function (Log-Loss)",
    figsize=(15, 10),
    font_size=12,
    color_y1="red",
    color_y0="black",
    scatter_size=100,
    show_grid=True,
):
    """
    Plot the Log-Loss function with tangent lines for y=1 and y=0 based on custom inputs.

    The function calculates the missing values (probability, log-loss, or gradient) 
    automatically if at least one is provided. It also highlights the predicted class 
    based on the threshold.

    Author: Rodrigo Campos
    Email: rodrigocamposag90@gmail.com
    GitHub:https://github.com/RodrigoCamposDS
    LinkedIn: https://www.linkedin.com/in/rodrigo-barcelos-campos/
    Date: 2025-01-01
    Description: This file contains the implementation of the plot_log_loss_with_custom_input function,
             which visualizes the Log-Loss function for binary logistic regression.

    Parameters
    ----------
    probability : float, optional
        Predicted probability (h(x)). Must be between 0 and 1.
    log_loss : float, optional
        Log-loss value for y=1. If provided, it will be used to calculate the probability.
    gradient : float, optional
        Gradient for y=1. If provided, it will be used to calculate the probability.
    threshold : float, optional, default=None
        The threshold used to classify the predicted value into class 0 or 1. If not provided, the function will calculate it automatically.
    title : str, default="Logarithmic Loss Function (Log-Loss)"
        Title of the plot.
    figsize : tuple, default=(15, 10)
        Figure size of the plot.
    font_size : int, default=12
        Font size for labels and title.
    color_y1 : str, default="red"
        Color of the -log(h(x)) curve for y=1.
    color_y0 : str, default="black"
        Color of the -log(1-h(x)) curve for y=0.
    scatter_size : int, default=100
        Size of the scatter points for log-loss values.
    show_grid : bool, default=True
        Whether to display a grid in the plot.

    Raises
    ------
    ValueError
        If none of `probability`, `log_loss`, or `gradient` is provided.
        If `probability` is not between 0 and 1.
        If `log_loss` is not positive.
        If `gradient` is zero.

    Examples
    --------
    >>> plot_log_loss_with_custom_input(probability=0.7, threshold=0.5)
    >>> plot_log_loss_with_custom_input(log_loss=0.5, threshold=0.5)
    >>> plot_log_loss_with_custom_input(gradient=-3.0, threshold=0.5)

    In the above examples, the **threshold** parameter determines how the predicted class is classified. 
    - **log_loss** could be a log-loss value calculated based on model predictions, 
    - **gradient** is the gradient of the log-loss, 
    - and **threshold** is the value for classification (default is 0.5).
    """
    # Validation of inputs
    if probability is not None:
        if not (0 < probability < 1):
            raise ValueError("Probability must be between 0 and 1.")
        h_x_real = probability
        log_loss_y1 = -np.log(h_x_real)  # Calculate log-loss based on the probability
        best_gradient_y1 = -1 / h_x_real  # Calculate gradient based on the probability
    elif log_loss is not None:
        if log_loss <= 0:
            raise ValueError("Log-loss must be positive.")
        log_loss_y1 = log_loss
        h_x_real = np.exp(-log_loss_y1)  # Calculate probability based on the log-loss
        best_gradient_y1 = -1 / h_x_real  # Calculate gradient based on the probability
    elif gradient is not None:
        if gradient == 0:
            raise ValueError("Gradient cannot be zero.")
        best_gradient_y1 = gradient
        h_x_real = -1 / best_gradient_y1  # Calculate probability based on the gradient
        log_loss_y1 = -np.log(h_x_real)  # Calculate log-loss based on the probability
    else:
        raise ValueError("You need to provide at least one input: probability, log-loss, or gradient.")

    # Calculations for y=0
    log_loss_y0 = -np.log(1 - h_x_real)
    best_gradient_y0 = 1 / (1 - h_x_real)

    # Automatically calculate threshold if not provided
    if threshold is None:
        threshold = 0.5  # Default value
        print(f"Threshold was not provided. Using default value: {threshold}")

    # Determine the class based on the threshold
    predicted_class = 1 if h_x_real >= threshold else 0

    # Coordinates for tangent lines
    h_x = np.linspace(0.01, 0.99, 500)
    tangent_x = h_x
    tangent_y_y1 = best_gradient_y1 * (tangent_x - h_x_real) + log_loss_y1
    tangent_y_y0 = best_gradient_y0 * (tangent_x - h_x_real) + log_loss_y0

    # Adjust label for threshold
    threshold_label = f"Threshold = {threshold:.3f}"

    # Plot the graph
    plt.figure(figsize=figsize)
    plt.plot(h_x, -np.log(h_x), label="-log(h(x)) (y=1)", color=color_y1)
    plt.plot(h_x, -np.log(1 - h_x), label="-log(1-h(x)) (y=0)", color=color_y0)
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.axvline(h_x_real, color="blue", linestyle="--", linewidth=0.8, label=f"h(x) = {h_x_real:.4f}")
    plt.axvline(threshold, color="purple", linestyle="--", linewidth=0.8, label=threshold_label)

    # Tangents and scatter points
    plt.scatter([h_x_real], [log_loss_y1], color="green", zorder=5, label=f"Log-Loss (y=1) = {log_loss_y1:.4f}", s=scatter_size)
    plt.plot(tangent_x, tangent_y_y1, color="green", linestyle="--", label=f"Tangent (y=1, Gradient = {best_gradient_y1:.4f})")
    plt.scatter([h_x_real], [log_loss_y0], color="blue", zorder=5, label=f"Log-Loss (y=0) = {log_loss_y0:.4f}", s=scatter_size)
    plt.plot(tangent_x, tangent_y_y0, color="blue", linestyle="--", label=f"Tangent (y=0, Gradient = {best_gradient_y0:.4f})")

    # Predicted class annotation
    plt.text(0.5, 4.5, f"Predicted class: {predicted_class} (Threshold = {threshold:.3f})", 
             fontsize=font_size, color="purple", bbox=dict(facecolor='white', alpha=0.8))

    # Final adjustments
    plt.title(title, fontsize=font_size)
    plt.xlabel("h(x) (Predicted Probability)", fontsize=font_size)
    plt.ylabel("Loss", fontsize=font_size)
    plt.legend(fontsize=font_size)
    if show_grid:
        plt.grid(alpha=0.3)
    plt.show()