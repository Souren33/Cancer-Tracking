"""
File title: Cancer_explore
Description: The backend program that calls the API functions and connects to the panel dashboard
Author: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar
Date: 2024/10/10
"""

"""
File title: Cancer_explore

Description: The backend program that calls the API functions and connects to the panel dashboard

Author: Souren Prakash, Kuan Chun Chiu, Atharva Nilapwar

Date: 2024/10/10
"""

import pandas as pd
from Cancer_API import CANAPI
from sankey_test import multi_layer_sankey
import panel as pn

# Loads javascript dependencies and configure panel
pn.extension()

# Initialize the API object
file_name = "CTDC_Participants_download 2024-10-04 12-59-58.csv"
can_api = CANAPI()

# Load the cancer file
can_df = can_api.load_can(file_name)
can_df = can_api.clean_can()
can_df = can_api.create_age_ranges()

print(can_df.head(15))

# Search widgets
min_patient_count = pn.widgets.IntSlider(name="Min patient count", start=1, end=5, value=1)
checkbox_group = pn.widgets.CheckBoxGroup(name="Sankey layer checkbox",
                                          value=["Age", "Gender"],
                                          options=["Age", "Gender"], inline=True)

# Plot widgets
width = pn.widgets.IntSlider(name="Diagram width", start=250, end=2000, step=125, value=1500)
height = pn.widgets.IntSlider(name="Diagram height", start=200, end=2500, step=100, value=800)


# menu widget


def grab_selection(selected_val):
    if selected_val:
        selection = can_api.get_unique_vals(selected_val)
        return selection
    return []


def update_values_dropdown(selected_column = None):

    if selected_column == "Remove Filter":
        values_dropdown.options = []
    else:
        options = grab_selection(selected_column)  # Get unique values from the selected column
        values_dropdown.options = options

"""
menu_items = [('Diagnosis', 'Diagnosis'), ('Age', 'Age'), ('Sex', 'Sex'), ('Treatment', 'Treatment')]
menu_button = pn.widgets.MenuButton(name='Sorting Categories', items=menu_items, button_type='primary')
menu_button_2 = pn.widgets.MenuButton(name = 'Item' )
pn.Column(menu_button, height=200)
"""


#menu_items =
columns_dropdown = pn.widgets.Select(name='Select Column', options=["Remove Filter"] + list(can_df.columns))
values_dropdown = pn.widgets.Select(name = 'Select Value', options = [])
# Callback functions:
def get_plot(min_patient_count, checkbox_group, width, height, selected_column, selected_val):
    if selected_column == "Remove Filter":
        filtered_df = can_df

    elif selected_column and selected_val:
     #first want to grab the filtering based on drop down
        filtered_df = can_df[can_df[selected_column] == selected_val]
    else:
        filtered_df = can_df

    layers = ["Diagnosis"] + checkbox_group + ["Therapy"]
    group_list = layers

    cancer_df = can_api.group_df(group_list, min_patient_count, df=filtered_df)

    fig = multi_layer_sankey(cancer_df, *layers, width=width, height=height)
    return fig

def get_catalog():
    pass

# Callback bindings
plot = pn.bind(get_plot, min_patient_count, checkbox_group, width, height,
               columns_dropdown.param.value, values_dropdown.param.value)

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
"""

Focus on menu drop down, main drop down lets the partition carry to any of the nodes 
the second drop down allows the different unique values used in the sankey to sort by those items
"""
menu_card = pn.Card(
    pn.Column(
    columns_dropdown,#first dropdown
    pn.bind(update_values_dropdown, columns_dropdown.param.value),
        values_dropdown),
    title= "Dropdown", width=card_width, collapsed=True
)
# Dashboard layout
layout = pn.template.FastListTemplate(
    title="The Diagnosis & Therapy Linkage Dashboard",
    sidebar=[
        search_card,
        plot_card,
        menu_card
    ],
    theme_toggle=False,
    main=[
        pn.Tabs(
            ("Network", plot),
            ("Associations", None),
            active=0
        )
    ],
    header_background='#a93226'
)

layout.servable()
layout.show()