import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data: remove top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]

# 1. Draw Line Plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

# 2. Draw Bar Plot
def draw_bar_plot():
    # Prepare data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group by year and month to get average page views
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plot bar chart
    fig = df_grouped.plot(kind='bar', figsize=(12,6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ])
    
    fig.savefig('bar_plot.png')
    return fig

# 3. Draw Box Plot
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name()

    # Sort months correctly
    months_order = ['January','February','March','April','May','June','July','August',
                    'September','October','November','December']

    fig, axes = plt.subplots(1,2, figsize=(15,6))

    # Year-wise box plot (trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot (seasonality)
    sns.boxplot(x='month', y='value', data=df_box, order=months_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
