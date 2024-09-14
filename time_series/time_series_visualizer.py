import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Import and clean data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data by filtering the top and bottom 2.5% page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Function to draw the line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# Function to draw the bar plot
def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Define the correct order for months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views by Month and Year')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Set legend using the correct month order
    ax.legend(title='Months', labels=months_order)

    fig.savefig('bar_plot.png')
    return fig


# Function to draw the box plot
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    try:
        sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    except AttributeError:
        print("Error with the year-wise box plot. Check for numpy version issues.")
    
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    try:
        sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    except AttributeError:
        print("Error with the month-wise box plot. Check for numpy version issues.")
    
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
