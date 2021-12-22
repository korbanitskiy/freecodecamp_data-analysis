import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def _calculate_sea_levels(df, min_year=None, max_year=2051):
    min_year = min_year or df.Year.min()
    df = df[df.Year >= min_year]
    lr = linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    years = pd.RangeIndex(df.Year.min(), max_year)
    levels = lr.slope * years + lr.intercept
    return pd.Series(data=levels, index=years)


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    plt.plot(_calculate_sea_levels(df))

    # Create second line of best fit
    plt.plot(_calculate_sea_levels(df, min_year=2000))

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
