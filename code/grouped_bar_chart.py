import matplotlib.pyplot as plt
import seaborn as sns

def grouped_bar_chart(df,
                      series_x_main,
                      series_x_sub,
                      series_y,
                      series_x_sub_palette,
                      width=15,
                      height=5,
                      fontsize_bar=10,
                      graph_title='Graph Title',
                      legend_title='Legend Title',
                      legend_loc='upper center',
                      axis_x_label='axis x name',
                      axis_y_label='axis y name',
                      min_axis_y=None,
                      max_axis_y=None,
                      save_name=None):
    
    # Set the figure size
    plt.figure(figsize=(width, height))
    
    # Set the theme for the plot
    sns.set_theme(style='white')
    
    # Create the bar plot
    ax = sns.barplot(data=df, 
                     x=series_x_main, 
                     y=series_y, 
                     hue=series_x_sub, 
                     palette=series_x_sub_palette)
    
    # Add bar labels
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f', fontsize=fontsize_bar)
    
    # Set the title and labels
    plt.title(graph_title)
    plt.xlabel(axis_x_label)
    plt.ylabel(axis_y_label)
    
    # Set y-axis limits if specified
    plt.ylim(min_axis_y, max_axis_y)
    
    # Configure the legend
    plt.legend(title=legend_title, loc=legend_loc, ncol=len(df[series_x_sub].unique()))
    
    # Save the plot if a filename is provided
    if save_name is not None:
        plt.savefig('./figure/' + save_name + '.png', format='png', dpi=300)
    
    # Show the plot
    plt.show()
