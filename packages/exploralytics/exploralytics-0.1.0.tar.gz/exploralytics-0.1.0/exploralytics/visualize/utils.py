"""
Utility functions for the Exploralytics visualization module.

This module contains helper functions for:
1. Data validation and processing
2. Layout calculations
3. Column type identification
"""

from typing import List, Tuple, Union
import pandas as pd
import numpy as np


def check_data(df: pd.DataFrame) -> None:
    """
    Validate if DataFrame is not empty.

    Args:
        df: DataFrame to check

    Raises:
        ValueError: If DataFrame is empty
        TypeError: If input is not a pandas DataFrame
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    if df.empty:
        raise ValueError("DataFrame is empty")


def get_number_columns(
    df: pd.DataFrame,
    columns: List[str] = None
) -> List[str]:
    """
    Get list of numeric columns from DataFrame.

    Args:
        df: DataFrame to analyze
        columns: Specific columns to check (default: None, checks all columns)

    Returns:
        List of column names containing numeric data

    Raises:
        ValueError: If no numeric columns found
    """
    if columns:
        number_cols = [
            col for col in columns 
            if df[col].dtype in ['int64', 'float64']
        ]
    else:
        number_cols = df.select_dtypes(
            include=['int64', 'float64']
        ).columns.tolist()
    
    if not number_cols:
        raise ValueError("No numeric columns found")
        
    return number_cols


def calc_subplot_size(
    total_plots: int,
    plots_per_row: int,
    height_per_plot: int
) -> Tuple[int, float]:
    """
    Calculate subplot layout dimensions.

    Args:
        total_plots: Total number of plots needed
        plots_per_row: Number of plots to put in each row
        height_per_plot: Height in pixels for each individual plot

    Returns:
        Tuple containing:
        - Number of rows needed
        - Total height for all plots

    Examples:
        >>> num_rows, total_height = calc_subplot_size(5, 2, 300)
        >>> print(num_rows)  # 3 rows needed
        >>> print(total_height)  # 750 pixels total height
    """
    # Calculate number of rows needed
    num_rows = (total_plots + plots_per_row - 1) // plots_per_row
    
    # Calculate total height needed
    total_height = (total_plots * height_per_plot) / plots_per_row
    
    return num_rows, total_height


def identify_plot_layout(
    num_plots: int,
    max_cols: int = 3
) -> Tuple[int, int]:
    """
    Determine optimal number of rows and columns for subplots.

    Creates a balanced layout that's visually appealing.

    Args:
        num_plots: Number of plots to arrange
        max_cols: Maximum number of columns allowed (default: 3)

    Returns:
        Tuple containing:
        - Number of rows
        - Number of columns

    Examples:
        >>> rows, cols = identify_plot_layout(5)
        >>> print(f"{rows} rows, {cols} columns")  # "2 rows, 3 columns"
    """
    # For single plot, return 1x1 layout
    if num_plots == 1:
        return 1, 1
    
    # For 2 plots, return 1x2 layout
    if num_plots == 2:
        return 1, 2
    
    # For other cases, calculate optimal layout
    cols = min(num_plots, max_cols)
    rows = (num_plots + cols - 1) // cols
    
    return rows, cols


def validate_color(color: str) -> bool:
    """
    Check if color string is valid hex code.

    Args:
        color: Color string to validate (e.g., '#FF0000')

    Returns:
        True if valid hex color, False otherwise

    Examples:
        >>> validate_color('#FF0000')  # True
        >>> validate_color('invalid')  # False
    """
    if not isinstance(color, str):
        return False
    
    # Check if string starts with # and has 6 hex digits
    if len(color) == 7 and color.startswith('#'):
        try:
            # Try converting hex color to integer
            int(color[1:], 16)
            return True
        except ValueError:
            return False
    
    return False


def suggest_bin_count(
    data: Union[pd.Series, np.ndarray],
    min_bins: int = 10,
    max_bins: int = 50
) -> int:
    """
    Suggest number of bins for histogram based on data.

    Uses Freedman-Diaconis rule with limits.

    Args:
        data: Data series to analyze
        min_bins: Minimum number of bins (default: 10)
        max_bins: Maximum number of bins (default: 50)

    Returns:
        Suggested number of bins

    Examples:
        >>> data = np.random.normal(0, 1, 1000)
        >>> bins = suggest_bin_count(data)
    """
    # Convert to numpy array if needed
    if isinstance(data, pd.Series):
        data = data.dropna().values
    
    # Use Freedman-Diaconis rule
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    bin_width = 2 * iqr * (len(data) ** (-1/3))
    
    if bin_width == 0:
        return min_bins
    
    # Calculate number of bins
    data_range = np.ptp(data)
    num_bins = int(np.ceil(data_range / bin_width))
    
    # Apply limits
    return np.clip(num_bins, min_bins, max_bins)