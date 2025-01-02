
"""
Exploralytics Visualization Module
--------------------------------

Create data visualizations with minimal code.

Examples:
    # Initialize visualizer
    from exploralytics.visualize import Visualizer
    viz = Visualizer()

    # Distribution plots
    viz.plot_histograms(
        df,
        title='Feature Distributions',
        plots_per_row=2
    )

    # Correlation analysis
    viz.plot_correlation(
        df,
        title='Feature Relationships'
    )

    # Time series analysis
    viz.plot_time_series(
        df,
        date_column='date',
        value_column='value'
    )
"""

from .visualizer import Visualizer
from .utils import check_data, get_number_columns, calc_subplot_size

__all__ = [
    'Visualizer',
    'check_data',
    'get_number_columns',
    'calc_subplot_size'
]