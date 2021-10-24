import matplotlib.pyplot as plt
import matplotlib
import squarify
import pandas as pd

def drawTreeMapSumAggr( #
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):
    drawTreemap(df, group_by_column, aggregated_column, "sum", axis, pad, legend_class, x_size, y_size, color_blues, title)

def drawTreeMapAvgAggr( #
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):
    drawTreemap(df, group_by_column, aggregated_column, "mean", axis, pad, legend_class, x_size, y_size, color_blues, title)

def drawTreeMapMaxAggr( #
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):
    drawTreemap(df, group_by_column, aggregated_column, "max", axis, pad, legend_class, x_size, y_size, color_blues, title)

def drawTreeMapMinAggr(
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):
    drawTreemap(df, group_by_column, aggregated_column, "min", axis, pad, legend_class, x_size, y_size, color_blues, title)

def drawTreeSizeAggr(
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):
    drawTreemap(df, group_by_column, aggregated_column, "size", axis, pad, legend_class, x_size, y_size, color_blues, title)

def drawTreemap(
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    aggregated_function: str,
    axis: bool,
    pad: bool,
    legend_class: str,
    x_size: int,
    y_size: int,
    color_blues: bool,
    title: dict):

    fig = plt.gcf()
    fig.add_subplot()
    fig.set_size_inches(x_size, y_size)

    res = df.groupby(by=group_by_column).agg(
        param=pd.NamedAgg(column=aggregated_column, aggfunc=aggregated_function)
    ).reset_index().sort_values(by=['param'])

    plot_legend(res, group_by_column, legend_class)

    if bool(title):
        plt.title(title['title'], fontsize = title['fontsize'], fontweight = title['fontweight'])


    squarify.plot(
        sizes = res['param'],
        label=  res['label'],
        alpha = 0.6,
        pad = pad,
        color = normalize_colors(df, aggregated_column) if color_blues else None
    )

    if not axis:
        plt.axis('off')

    plt.show()
    return res

def plot_legend(df: pd.DataFrame, group_by_column: str, legend_class: str) :
    if legend_class == "legend_class_aggr":
        df['label'] = df[group_by_column].astype(str) + "\n(" + df['param'].round(2).astype(str) + ")"
    elif legend_class == "legend_class" :
        df['label'] = df[group_by_column].astype(str)
    else :
        df['label'] = ""

def normalize_colors(df: pd.DataFrame, column: str) :
    norm = matplotlib.colors.LogNorm(
        vmin=min(df[column]),
        vmax=max(df[column])
    )
    return [matplotlib.cm.Greens(norm(value)) for value in df[column]]
