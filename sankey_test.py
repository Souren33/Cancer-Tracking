"""
File title: sankey
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Description: The sankey library containing the make_sankey function and multi_layer_sankey function
Date: 2024/10/10
"""

# This file is made to only construct the two_layer_sankey(), three_layer_sankey(), and four_layer_sankey() functions,
# so no main() function is constructed or called at the end. This file only serves as a library so that files from
# future work can import this library and call the three functions within, in order to make the sankey diagrams

import pandas as pd
import plotly.graph_objects as go


def multi_layer_sankey(cancer_df, *args, **kwargs):
    if len(args) < 2:
        raise ValueError("At least two layers (source and target) are required.")

    all_columns = pd.concat([cancer_df[col] for col in args])
    label = list(all_columns.unique())

    indices = [cancer_df[col].apply(lambda x: label.index(x)) for col in args]

    source = pd.concat(indices[:-1])
    target = pd.concat(indices[1:])

    # Change this line:
    value = pd.concat([cancer_df["Patient_count"]] * (len(args) - 1))

    link = {"source": source, "target": target, "value": value}
    node = {"pad": 50, "thickness": 50, "label": label}

    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)

    width = kwargs.get("width", 1500)
    height = kwargs.get("height", 800)
    fig.update_layout(autosize=False, width=width, height=height)

    return fig