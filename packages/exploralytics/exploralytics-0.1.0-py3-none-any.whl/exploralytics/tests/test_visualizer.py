# tests/test_visualizer.py

import pytest
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from exploralytics.visualize import Visualizer
from exploralytics.visualize.utils import (
    check_data,
    get_number_columns,
    calc_subplot_size,
    identify_plot_layout
)
from exploralytics.visualize.style import create_custom_style

# Fixtures
@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    np.random.seed(42)
    return pd.DataFrame({
        'numeric1': np.random.normal(0, 1, 100),
        'numeric2': np.random.uniform(0, 10, 100),
        'category': ['A', 'B'] * 50,
        'date': pd.date_range('2023-01-01', periods=100)
    })

@pytest.fixture
def visualizer():
    """Create a Visualizer instance."""
    return Visualizer()

# Test Visualizer Class
class TestVisualizer:
    def test_init_default(self):
        """Test Visualizer initialization with default values."""
        viz = Visualizer()
        assert viz.color == '#94C973'
        assert viz.height == 600
        assert viz.width == 800
        assert viz.style is not None

    def test_init_custom(self):
        """Test Visualizer initialization with custom values."""
        viz = Visualizer(color='#000000', height=400, width=600)
        assert viz.color == '#000000'
        assert viz.height == 400
        assert viz.width == 600

    def test_invalid_color(self):
        """Test initialization with invalid color."""
        with pytest.raises(ValueError):
            Visualizer(color='invalid')

    def test_plot_distributions(self, visualizer, sample_df):
        """Test distribution plot creation."""
        fig = visualizer.plot_distributions(
            sample_df,
            title='Test Distribution'
        )
        assert isinstance(fig, go.Figure)
        assert fig.layout.title.text == 'Test Distribution'

    def test_empty_dataframe(self, visualizer):
        """Test behavior with empty DataFrame."""
        empty_df = pd.DataFrame()
        with pytest.raises(ValueError):
            visualizer.plot_distributions(empty_df, title='Empty Test')

# Test Utility Functions
class TestUtils:
    def test_check_data(self, sample_df):
        """Test data validation."""
        # Should not raise error
        check_data(sample_df)
        
        # Should raise error
        with pytest.raises(ValueError):
            check_data(pd.DataFrame())

    def test_get_number_columns(self, sample_df):
        """Test numeric column identification."""
        numeric_cols = get_number_columns(sample_df)
        assert len(numeric_cols) == 2
        assert 'numeric1' in numeric_cols
        assert 'numeric2' in numeric_cols
        assert 'category' not in numeric_cols

    def test_calc_subplot_size(self):
        """Test subplot size calculations."""
        num_rows, total_height = calc_subplot_size(
            total_plots=5,
            plots_per_row=2,
            height_per_plot=300
        )
        assert num_rows == 3
        assert total_height == 750

    def test_identify_plot_layout(self):
        """Test plot layout identification."""
        # Test single plot
        rows, cols = identify_plot_layout(1)
        assert rows == 1
        assert cols == 1

        # Test multiple plots
        rows, cols = identify_plot_layout(5)
        assert rows == 2
        assert cols == 3

# Test Plot Outputs
class TestPlotOutputs:
    def test_distribution_plot_shape(self, visualizer, sample_df):
        """Test shape and structure of distribution plot."""
        fig = visualizer.plot_distributions(sample_df, title='Test')
        
        # Check basic figure properties
        assert fig.layout.height is not None
        assert fig.layout.width is not None
        assert fig.layout.title.text == 'Test'

    def test_plot_with_missing_values(self, visualizer):
        """Test plotting with missing values."""
        df_with_na = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [5, None, 7, 8]
        })
        fig = visualizer.plot_distributions(df_with_na, title='Test NA')
        assert isinstance(fig, go.Figure)

    def test_plot_with_single_column(self, visualizer, sample_df):
        """Test plotting single column."""
        fig = visualizer.plot_distributions(
            sample_df[['numeric1']],
            title='Single Column'
        )
        assert isinstance(fig, go.Figure)

# Integration Tests
class TestIntegration:
    def test_full_workflow(self, visualizer, sample_df):
        """Test complete workflow with multiple plots."""
        # Create different types of plots
        dist_fig = visualizer.plot_distributions(
            sample_df,
            title='Distributions'
        )
        assert isinstance(dist_fig, go.Figure)

        # Test style consistency
        assert dist_fig.layout.font.size == visualizer.style['font_size']
        assert dist_fig.layout.title.x == visualizer.style['title_x']

    def test_style_customization(self, sample_df):
        """Test plot creation with custom style."""
        # Create custom style using the utility function
        custom_style = create_custom_style(
            font_size=14,
            title_x=0.3
        )
        
        custom_viz = Visualizer(
            color='#000000',
            style=custom_style
        )
        fig = custom_viz.plot_distributions(sample_df, title='Custom Style')
        
        # Test style application
        assert fig.layout.font.size == 14
        assert fig.layout.title.x == 0.3