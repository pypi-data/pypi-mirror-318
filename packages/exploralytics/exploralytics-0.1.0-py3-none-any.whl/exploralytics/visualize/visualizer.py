"""
Core visualization module for creating interactive plots with Plotly.
Provides a unified interface for data visualization tasks.
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import List, Optional, Union, Dict

from .utils import (
    check_data,
    get_number_columns,
    calc_subplot_size,
    identify_plot_layout,
    suggest_bin_count,
    validate_color
)
from .style import (
    DEFAULT_STYLE,
    apply_style,
    get_color_palette,
    create_custom_style
)


class Visualizer:
    """
    Create interactive data visualizations using Plotly.

    This class provides methods for common data visualization tasks,
    maintaining consistent styling while allowing customization.

    Attributes:
        color: Main color used in plots
        height: Default height for plots in pixels
        width: Default width for plots in pixels
        style: Dictionary of plot styling settings
    """

    def __init__(
        self,
        color: str = '#94C973',
        height: int = 600,
        width: int = 800,
        style: Optional[Dict] = None
    ):
        """Initialize the visualization tool."""
        if not validate_color(color):
            raise ValueError(
                "Color must be a valid hex code (e.g., '#94C973')"
            )
        
        self.color = color
        self.height = height
        self.width = width
        self.style = style or DEFAULT_STYLE.copy()

    def plot_histograms(
        self,
        data: pd.DataFrame,
        title: str,
        columns: List[str] = [],
        num_cols: int = 1,
        subtitle: str = ' '
    ) -> go.Figure:
        """Create histogram plots for numerical columns."""
        if len(columns) >= 1:
            numerical_columns = data.select_dtypes(
                include=np.number
            ).columns.tolist()
            plot_height = (len(numerical_columns) * 400) / num_cols
        else:
            numerical_columns = data.select_dtypes(
                include=np.number
            ).columns.tolist()
            plot_height = (len(numerical_columns) * 400) / num_cols

        num_rows = (len(numerical_columns) + num_cols - 1) // num_cols

        fig = make_subplots(
            rows=num_rows,
            cols=num_cols,
            subplot_titles=numerical_columns
        )

        for index, col_name in enumerate(numerical_columns):
            row = index // num_cols + 1
            col = index % num_cols + 1

            fig.add_trace(
                go.Histogram(
                    x=data[col_name],
                    autobinx=True,
                    name=col_name,
                    marker_color=self.color
                ),
                row=row,
                col=col
            )

        fig.update_annotations(font_size=12)
        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>",
            showlegend=False,
            height=plot_height,
            title_x=0.5
        )

        return fig

    def plot_boxplots(
        self,
        data: pd.DataFrame,
        title: str,
        columns: List[str] = [],
        num_cols: int = 1,
        subtitle: str = ' '
    ) -> go.Figure:
        """Create box plots for numerical columns."""
        if len(columns) >= 1:
            numerical_columns = [
                col for col in columns 
                if data[col].dtype in ['int64', 'float64']
            ]
            plot_height = (len(numerical_columns) * 400) / num_cols
        else:
            numerical_columns = data.select_dtypes(
                include=np.number
            ).columns.tolist()
            plot_height = (len(numerical_columns) * 400) / num_cols

        num_rows = (len(numerical_columns) + num_cols - 1) // num_cols

        fig = make_subplots(
            rows=num_rows,
            cols=num_cols,
            subplot_titles=numerical_columns
        )

        for index, col_name in enumerate(numerical_columns):
            row = index // num_cols + 1
            col = index % num_cols + 1

            fig.add_trace(
                go.Box(
                    y=data[col_name],
                    name=col_name,
                    marker_color=self.color
                ),
                row=row,
                col=col
            )

        fig.update_annotations(font_size=12)
        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>",
            showlegend=False,
            height=plot_height,
            title_x=0.5
        )

        return fig

    def plot_correlation(
        self,
        data: pd.DataFrame,
        title: str,
        columns: List[str] = [],
        subtitle: str = ' '
    ) -> go.Figure:
        """Create correlation heatmap."""
        if len(columns) >= 1:
            numerical_columns = [
                col for col in columns 
                if data[col].dtype in ['int64', 'float64']
            ]
        else:
            numerical_columns = data.select_dtypes(
                include=np.number
            ).columns.tolist()

        correlation = data[numerical_columns].corr()

        fig = go.Figure(data=go.Heatmap(
            z=correlation,
            x=numerical_columns,
            y=numerical_columns,
            colorscale='RdBu',
            zmin=-1,
            zmax=1
        ))

        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>",
            height=700,
            width=700,
            title_x=0.5
        )

        return fig

    def plot_scatter_matrix(
        self,
        data: pd.DataFrame,
        title: str,
        columns: List[str] = [],
        subtitle: str = ' '
    ) -> go.Figure:
        """Create scatter plot matrix."""
        if len(columns) >= 1:
            numerical_columns = [
                col for col in columns 
                if data[col].dtype in ['int64', 'float64']
            ]
        else:
            numerical_columns = data.select_dtypes(
                include=np.number
            ).columns.tolist()

        fig = px.scatter_matrix(
            data,
            dimensions=numerical_columns,
            color_discrete_sequence=[self.color]
        )

        fig.update_layout(
            title_text=f"{title}<br><sup>{subtitle}</sup>",
            height=800,
            width=800,
            title_x=0.5
        )

        return fig

    def update_style(self, **kwargs) -> None:
        """Update plot styling settings."""
        self.style.update(kwargs)