import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))  # Years from 1880 to 2050
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit (using data from 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    x_pred_2000 = pd.Series(range(2000, 2051))  # Years from 2000 to 2050
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    y_pred_2000 = slope_2000 * x_pred_2000 + intercept_2000
    plt.plot(x_pred_2000, y_pred_2000, color='green', label='Best Fit Line (2000 Onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
