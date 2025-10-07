import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    line_all = intercept + slope * years_extended
    ax.plot(years_extended, line_all, 'r', label='Fit: All Data')

    # Create second line of best fit (year >=
