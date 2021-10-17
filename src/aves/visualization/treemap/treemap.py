import matplotlib.pyplot as plt
import squarify
import pandas as pd

def treemap(df: pd.DataFrame, groupByColumn: str, aggregatedColumn: str, aggregatedFunction):
    res = df.groupby(by=groupByColumn).agg(
        d_max=pd.NamedAgg(column=aggregatedColumn, aggfunc=aggregatedFunction)
    ).reset_index(drop=True)

    squarify.plot(res['d_max'].tolist())
    plt.show()

