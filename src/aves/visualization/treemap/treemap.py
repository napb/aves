import matplotlib.pyplot as plt
import squarify
import pandas as pd

def drawTreeMapSumAggr(df: pd.DataFrame, group_by_column: str, aggregated_column: str, axis: bool, legend_class: str):
    drawTreemap(df, group_by_column, aggregated_column, "sum", axis, legend_class)

def drawTreemap(
    df: pd.DataFrame,
    group_by_column: str,
    aggregated_column: str,
    aggregated_function: str,
    axis: bool,
    legend_class: str):
    res = df.groupby(by=group_by_column).agg(
        param=pd.NamedAgg(column=aggregated_column, aggfunc=aggregated_function)
    ).reset_index()

    plot_legend(res, group_by_column, legend_class)

    squarify.plot(
        sizes = res['param'],
        label=  res['label'],
        alpha = 0.6,
        pad = True)

    if not axis:
        plt.axis('off')

    plt.show()

def plot_legend(df: pd.DataFrame, group_by_column: str, legend_class: str) :
    if legend_class == "legend_class_aggr":
        df['label'] = df[group_by_column].astype(str) + "(" + df['param'].astype(str) + ")"
    elif legend_class == "legend_class" :
        df['label'] = df[group_by_column].astype(str)
    else :
        df['label'] = ""
