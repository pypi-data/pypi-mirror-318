# Exploralytics

## What is it?
A Python toolkit that makes creating Plotly visualizations straightforward — focusing on common EDA plots like distributions, correlations, and other visualization. I created this to simplify my own workflow, but other data professionals might find it useful too.

## Main Features
Making subplots and visualizations less of a hassle. You can create complex layouts with a single function call — perfect for quick data exploration or when you're trying to understand your dataset's intermediate characteristics.

Here's what you can do with Exploralytics:
```python
# One line for distribution plots of all numeric columns
viz.plot_histograms(df, title='Distributions', num_cols=3)

# Quick correlation analysis
viz.plot_correlation(df, title='Correlations')

# Distribution + Box plots in one view
viz.plot_distributions(df, title='Analysis')
```

## Installation

First, make sure you have Python 3.7 or newer.

Using pip:
```bash
pip install exploralytics
```

Or install from source:
```bash
git clone https://github.com/yourusername/exploralytics.git
cd exploralytics
pip install -e .
```

## Usage Examples

Let's look at some common scenarios:

```python
from exploralytics.visualize import Visualizer
import pandas as pd

# Create your data
df = pd.DataFrame({
    'sales': [100, 150, 200, 120, 180],
    'customers': [10, 15, 20, 12, 18],
    'satisfaction': [4.5, 4.2, 4.8, 4.1, 4.6]
})

# Initialize the visualizer — you can customize colors and style
viz = Visualizer(color='#336699')  # Using a nice blue

# Create distribution plots — 2 columns
fig = viz.plot_histograms(
    df,
    title='Sales Metrics',
    num_cols=2
)
fig.show()

# Analyze correlations
fig = viz.plot_correlation(
    df,
    title='Metric Relationships'
)
fig.show()

# Create scatter matrix
fig = viz.plot_scatter_matrix(
    df,
    title='Detailed Relationships'
)
fig.show()
```

## Customization

Change the look of your plots:

```python
# Custom styling
viz = Visualizer(
    color='#FF6B6B',  # Custom color
    height=800,       # Taller plots
    width=1000        # Wider plots
)

# Update style settings
viz.update_style(
    font_size=14,
    title_x=0.5
)
```

## Development

Want to help out? Here's how:

1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/cool-new-feature
```
3. Make your changes and test them
4. Push and create a pull request

## Testing

Run the test suite:
```bash
pytest tests/
```

## License
BSD 3-Clause License

## Need Help?
Open an issue on GitHub if you run into problems or have suggestions. I check them regularly and try to help when I can.

---
Note: This is an early release — I'm using it for my own work and sharing it in case others find it helpful. Expect updates and improvements as I add features I need.