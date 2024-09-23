"""

- QR CODE NOW WORKS ON DOWNLOAD
- GNSS for 1 second
Title: SWAP Data Plotting Script
Author: Ben White
Date: 2024
Description: 
This script reads SWAP data from a CSV file, filters the data, and generates an interactive 
plot using Plotly. The plot includes markers for different TAU values, a shaded region for 
lab clocks, and a QR code for more information.
It also produces a focussed plot with a zoomed-in view of the SWAP values around 10^7 and 10^10.
it exports both plots as auto-scaled HTML files.

Usage:
- Ensure the SWAP_DATA.csv file is in the same directory as this script.
- The QRlink.png image file should also be in the same directory.
- Run the script to generate an HTML file with the plot. (can be changed to other formats such as PNG, PDF, BMP etc)

Dependencies:
- os
- plotly
- numpy
- pandas
- base64

"""


# Import necessary libraries
import os
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import numpy as np
import pandas as pd
import base64
import copy

# Import SWAP data into a pandas DataFrame
csv_file = 'SWAP_DATA.csv'
df = pd.read_csv(csv_file)

# Filter the DataFrame to include only rows where INCLUDE == 1
df = df[df['INCLUDE'] == 1]

# Filter data for rows that have valid TAU_1e3s and TAU_1e4s values
df_tau_1e3 = df[df['TAU_1e3s'] > 0]
df_tau_1e4 = df[df['TAU_1e4s'] > 0]

# Set the default plot template
pio.templates.default = "seaborn"

# Create a new Plotly figure
fig = go.Figure()

# Add a horizontal line representing GNNS:1s
gnss_1s_line = go.Scatter(
    x=[1e-3, 5e16],
    y=[4e-12, 4e-12],
    mode='lines',
    line=dict(color='black', width=1.0, dash='dot'), 
    name='GNSS:1s',
    showlegend=False,
    hoverinfo='skip'
)
fig.add_trace(gnss_1s_line)

# Add a horizontal line representing GNNS:1e3s
# gnss_1e3s_line = go.Scatter(
#     x=[1e-3, 5e16],
#     y=[1e-13, 1e-13],
#     mode='lines',
#     line=dict(color='black', width=1.0, dash='dot'), 
#     name='GNSS:1e3s',
#     showlegend=False,
#     hoverinfo='skip'
# )
# fig.add_trace(gnss_1e3s_line)

# Add a horizontal line representing GNNS:1e4s
# gnss_1e4s_line = go.Scatter(
#     x=[1e-3, 5e16],
#     y=[1e-14, 1e-14],
#     mode='lines',
#     line=dict(color='black', width=1.0, dash='dot'), 
#     name='GNSS:1e4s',
#     showlegend=False,
#     hoverinfo='skip'
# )
# fig.add_trace(gnss_1e4s_line)

# Add scatter plots for TAU_1e4s and TAU_1e3s with vertical lines
for df_temp, tau_column, symbol_shape in zip([df_tau_1e4, df_tau_1e3], ['TAU_1e4s', 'TAU_1e3s'], ['circle', 'square']):
    legend_text = 'TAU = 10,000s' if tau_column == "TAU_1e4s" else 'TAU = 1000s'
    scatter = go.Scatter(
        x=df_temp['SWAP'],
        y=df_temp[tau_column],
        mode='markers',
        name=legend_text,
        opacity=0.75,
        marker=dict(size=8, color='DarkSlateGrey', symbol=symbol_shape),
        hovertemplate='<b>CLOCK</b>: %{text}<br><b>SWaP</b> = %{x}<br><b>Tau</b> = %{y}<br>',
        text=df_temp['CLOCK']
    )
    fig.add_trace(scatter)

    # Add vertical lines to join the ADEVs for each clock
    unique_x_values = df_temp['SWAP'].unique()
    for x_value in unique_x_values:
        y1 = df[df['SWAP'] == x_value]['TAU_1s'].iloc[0]
        y2 = df_temp[df_temp['SWAP'] == x_value][tau_column].iloc[0]
        vertical_line = go.Scatter(
            x=[x_value, x_value],
            y=[y1, y2],
            mode='lines',
            line=dict(color='black', width=2),
            showlegend=False,
            opacity=0.75
        )
        fig.add_trace(vertical_line)

# Add the scatter plot for TAU_1s
scatter_tau1s = px.scatter(
    df, 
    x="SWAP", 
    y="TAU_1s", 
    color="CATEGORY",
    symbol='TYPE',
    hover_name='CLOCK', 
    hover_data={
        'ATOM': True,
        'GROUP': True,
        'PHYSICS': True,
        'REF_NUM': True,
        'SWAP': True,
        'TAU_1s': True,
        'CATEGORY': True,
        'TYPE': True,
        'CLOCK': False
    },
    labels={
        'CLOCK': '<b>Clock</b>',
        'CATEGORY': '<b>Category</b>',
        'TYPE': '<b>Type</b>',
        'ATOM': '<b>Atom</b>',
        'GROUP': '<b>Group</b>',
        'PHYSICS': '<b>Physics</b>',   
        'SWAP': '<b>SWaP</b>',
        'TAU_1s': '<b>τ<sub>1s</sub></b>',
        'REF_NUM': '<b>Reference Number</b>'
    },
    text='GROUP',  
    opacity=1.0,
)

# Add traces from the scatter plot to the main figure
fig.add_traces(scatter_tau1s.data)

# Update the marker size and text position for the last added traces
last_trace_index = len(fig.data) - len(scatter_tau1s.data)
for i in range(last_trace_index, len(fig.data)):
    fig.data[i].update(
        marker=dict(size=12, line=dict(width=0.5, color='DarkSlateGrey')),
        textposition='top center'
    )

# Define a shaded region for lab clocks
shaded_region = go.layout.Shape(
    type='rect',
    x0=1e-3,
    y0=1e-18,
    x1=1e16,
    y1=6.7e-17,
    fillcolor='rgba(0, 0, 255, 0.25)',
    line=dict(color='rgba(0, 0, 255, 0.1)')
)

# Add the shaded region to the figure
fig.add_shape(shaded_region)

# Define the text for the shaded region
shaded_region_text = (
    'Lab clock performance @ tau = 1s \n'
    'NIST - Yb Lattice: 6.7e-17 \n'
    'Schioppo 2017'
)

# Add a transparent scatter trace for hover box
fig.add_trace(go.Scatter(
    x=[1e-1, 1.e1, 1.e1, 1e-1, 1e-2],
    y=[1e-17, 1e-17, 2e-17, 2e-17, 1e-17],
    mode='markers',
    marker=dict(color='rgba(0, 0, 0, 0)'),
    hoverinfo='text',
    text=shaded_region_text,
    showlegend=False
))

# Disable legend item click
fig.update_layout(legend=dict(itemclick=False))

# Configure layout, axis, and other features
fig.update_layout(
    xaxis_title='Size, Weight and Power (cm³kgW)',
    yaxis_title='Fractional Frequency Stability (ADEV)',
    yaxis=dict(range=[-17.5, -8]),
    xaxis=dict(range=[-2.5, 15.5]),
    xaxis_type='log',
    yaxis_type='log',
    xaxis_tickmode='linear',
    yaxis_tickmode='linear',
    xaxis_tickformat='.1e',
    yaxis_tickformat='.1e',
    legend=dict(
        yanchor="top",
        y=1,
        xanchor="right",
        x=1,
        traceorder="reversed",
    ),
    annotations=[dict(
        x=0.5,
        y=1.09,
        xref='paper',
        yref='paper',
        text='Hover over points on the plot for more information.' +
             'Use mouse to zoom in, pan or download a PNG of the plot. <br>' +
             'Scan QR code for more information and source data.',
        showarrow=False,
        font=dict(size=12)
    )]     
)

# Add annotation for lab clocks area
fig.add_annotation(
    xref="paper", yref="y",
    x=0.01,
    y=-16.8,
    text="Lab Clock Performance",
    showarrow=False,
    align='left',
    font=dict(size=12, color='rgba(0, 0, 0, 0.8)')
)

# add annotation for author and date
fig.add_annotation(
    xref="paper", yref="paper",
    x=1.0,
    y=-0.0,
    text="B. White 2024",
    showarrow=False,
    align='right',
    font=dict(size=12, color='rgba(0, 0, 0, 0.8)')
)

# Add annotation for GNNS:1s
fig.add_annotation(
    xref="paper", yref="y",
    x=0.01,
    y=-11.6,
    text="GNSS:1s",
    showarrow=False,
    align='left',
    font=dict(size=12, color='rgba(0, 0, 0, 0.8)')
)

# add annotation for GNNS:1e3s
# fig.add_annotation(
#     xref="paper", yref="y",
#     x=0.01,
#     y=-13.2,
#     text="GNSS:1e3s",
#     showarrow=False,
#     align='left',
#     font=dict(size=12, color='rgba(0, 0, 0, 0.8)')
# )

# Add annotation for GNSS:1e4s
# fig.add_annotation(
#     xref="paper", yref="y",
#     x=0.01,
#     y=-14.2,
#     text="GNSS:1e4s",
#     showarrow=False,
#     align='left',
#     font=dict(size=12, color='rgba(0, 0, 0, 0.8)')
# )



# QR code image that links to source data on IPAS page
# with open("IPAS-QR.png", "rb") as image_file:
with open("IPAS-QR-bitly.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Add the QR code image to the plot
fig.add_layout_image(
    dict(
        source='data:image/png;base64,{}'.format(base64_image),
        xref="paper", yref="paper",
        x=0.0, y=1,
        sizex=0.1, sizey=0.1,
        xanchor="left", yanchor="top",
        opacity=0.9,
        layer="above"
    )
)

# Add frame around plot
fig.update_layout(
    xaxis=dict(
        showline=True,
        linewidth=0.4,
        mirror=True,
        linecolor='lightgrey'
    ),
    yaxis=dict(
        showline=True,
        linewidth=0.4,
        mirror=True,
        linecolor='lightgrey'
    ),
    margin=dict(t=70, b=50)
)

# # Save the plot as an HTML file
# fig.write_html('SWAP-PLOT-MAIN.html')


# Define the config for higher resolution PNG export, using only the scale
config = {
    'toImageButtonOptions': {
        'format': 'png',  # Export as PNG
        'filename': 'SWAP-PLOT-MAIN',  # Filename
        'scale': 5  # Scale factor for higher resolution
    }
}

# Export to an HTML file with the config
pio.write_html(fig, 'SWAP-PLOT-MAIN.html', config=config)




# Create a deep copy of the original figure for focused plot
fig2 = copy.deepcopy(fig)

# Remove the first annotation
fig2.layout.annotations = list(fig2.layout.annotations)[1:]

# Adjust the x and y axis limits
fig2.update_layout(
    xaxis=dict(range=[6.5, 10.6], fixedrange=True),  
    yaxis=dict(range=[-15.5, -10.5], fixedrange=True),
    margin=dict(t=30)
)

# Add vertical line at 10^7 for PS5 SWaP
fig2.add_trace(
    go.Scatter(
        x=[10**7, 10**7],  
        y=[10**-15.5, 10**-10.5], 
        mode='lines',
        line=dict(color='grey', width=10, dash='dot'),
        opacity=0.3,  
        showlegend=False
    )
)

# Add vertical line at 10^10 for FRIDGE SWaP
fig2.add_trace(
    go.Scatter(
        x=[10**10, 10**10],  
        y=[10**-15.5, 10**-10.5],  
        mode='lines',
        line=dict(color='grey', width=10, dash='dot'),
        opacity=0.3,  
        showlegend=False
    )
)

# Add annotations for PS5 and FRIDGE
fig2.add_annotation(
    x=7.08,
    y=-15.4,
    text="PLAYSTATION 5",
    showarrow=False,
    textangle=-90, 
    font=dict(
        size=16,
        color="grey"
    ),
    xref="x",
    yref="y",
    yanchor="bottom"
)
fig2.add_annotation(
    x=10.08,
    y=-15.4,
    text="FAMILY FRIDGE",
    showarrow=False,
    textangle=-90, 
    font=dict(
        size=16,
        color="grey"
    ),
    xref="x",
    yref="y",
    yanchor="bottom"
)


# Define the config for higher resolution PNG export, using only the scale
config2 = {
    'toImageButtonOptions': {
        'format': 'png',  # Export as PNG
        'filename': 'SWAP-PLOT-FOCUS',  # Filename
        'scale': 5  # Scale factor for higher resolution
    }
}

# Export to an HTML file with the config
# pio.write_html(fig, 'SWAP-PLOT-MAIN.html', config=config)


# write html file for focused plot
pio.write_html(fig2, 'SWAP-PLOT-FOCUS.html', config=config2)
