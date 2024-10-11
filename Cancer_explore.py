"""
File title: Cancer_explore
Description: The backend program that calls the API functions and connects to the panel dashboard
Author: Souren Prakash, Kuan Chun Chiu, Atharva
Date: 2024/10/10
"""

import panel as pn
from Cancer_API import CANAPI
import sankey as sk

# Loads javascript dependencies and configure panel
pn.extension()

# Initialize the API object
file_name = "CTDC_Participants_download 2024-10-04 12-59-58.csv"
can_api = CANAPI()

# Load the cancer file
can_df = can_api.load_can(file_name)
can_df = can_api.clean_can()
can_df = can_api.create_age_ranges()

print (can_df.head(15))

# Search widgets
min_patient_count = pn.widgets.IntSlider(name="Min patient count", start=1, end=5, value=1)
checkbox_group = pn.widgets.CheckBoxGroup(name="Sankey layer checkbox", value=["Age", "Gender"],
                                          options=["Age", "Gender"], inline=True)

# Plot widgets
width = pn.widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
height = pn.widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)

# Callback functions:
def get_plot(min_patient_count, checkbox_group, width, height):
    inter_layers = checkbox_group
    if len(inter_layers) == 0:
        group_list = ["Diagnosis", "Therapy"]
        cancer_df = can_api.group_df(group_list, min_patient_count)
        fig = sk.two_layer_sankey(cancer_df, "Diagnosis", "Therapy", width=width, height=height)
    if len(inter_layers) == 1:
        group_list = ["Diagnosis", inter_layers[0], "Therapy"]
        cancer_df = can_api.group_df(group_list, min_patient_count)
        fig = sk.three_layer_sankey(cancer_df, "Diagnosis", inter_layers[0], "Therapy",
                                    width=width, height=height)
    if len(inter_layers) == 2:
        group_list = ["Diagnosis", inter_layers[0], inter_layers[1], "Therapy"]
        cancer_df = can_api.group_df(group_list, min_patient_count)
        fig = sk.four_layer_sankey(cancer_df, "Diagnosis", inter_layers[0], inter_layers[1], "Therapy",
                                   width=width, height=height)
    return fig

def get_catalog():
    pass



# Callback bindings
plot = pn.bind(get_plot, min_patient_count, checkbox_group, width, height)
# catalog = pn.bind(get_catalog)

# Dashboard widgets card
card_width = 320
search_card = pn.Card(
    pn.Column(
        min_patient_count,
        checkbox_group
    ),
    title="Search", width=card_width, collapsed=True
)

plot_card = pn.Card(
    pn.Column(
        width,
        height
    ),
    title="Plot", width=card_width, collapsed=True
)

# Dashboard layout
layout = pn.template.FastListTemplate(
    title="The Diagnosis & Therapy Linkage Dashboard",
    sidebar=[
        search_card,
        plot_card,
    ],
    theme_toggle=False,
    main=[
        pn.Tabs(
            ("Network", plot),  # Replace None with callback binding
            ("Associations", None),  # Replace None with callback binding
            active=0   # Which tab is active by default?
        )
    ],
    header_background='#a93226'
).servable()

layout.show()