#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install dash


# In[3]:


from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv('master_dataset.csv')  

data1 = data.loc[data['ASGS_remoteness']!='Not Defined',['ASGS_remoteness', 'Indigenous_pct','LBOTE_pct','ICSEA_value']]
dropdown_options = sorted(data1['ASGS_remoteness'].unique())

dropdown_options_list = [{'label': option, 'value': option} for option in dropdown_options]
app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='region',
        options=dropdown_options,
        value=dropdown_options[1],
        clearable=False,
        multi=True
    ),

    dcc.Dropdown(
        id='column',
        options=[
            'Indigenous %',
            'LBOTE %',
            'ICSEA Score'
        ],
        value='Indigenous %',
        clearable=False,
        multi=False
    ),

    dcc.RadioItems(
        id='statistic',
        options=[
            'Mean',
            'Median',
            'Maximum'
        ],
        value='Mean',
        inline=True
    ),

    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value'),
    Input('column', 'value'),
    Input('statistic', 'value')
)
def update_graph(selected_regions, selected_column, selected_statistic):
    if not selected_regions:
        return None
    else:
        if selected_column == 'Indigenous %':
            column_name = 'Indigenous_pct'
        elif selected_column == 'LBOTE %':
            column_name = 'LBOTE_pct'
        else:
            column_name = 'ICSEA_value'
        
        newdata = data.loc[data['ASGS_remoteness'].isin(selected_regions), ['ASGS_remoteness', column_name]]
        newdata[column_name] = pd.to_numeric(newdata[column_name], errors='coerce')
        
       
        if selected_column == 'Indigenous %':
            fig_title = 'Indigenous %'
        elif selected_column == 'LBOTE %':
            fig_title = 'LBOTE %'
        else:
            fig_title = 'ICSEA Score'
        
        if selected_statistic == 'Mean':
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[column_name].mean().reset_index(),
                         x='ASGS_remoteness', y=column_name, title=f'Mean {fig_title} by Region of NSW')
        elif selected_statistic == 'Median':
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[column_name].median().reset_index(),
                         x='ASGS_remoteness', y=metric_column, title=f'Median {fig_title} by Region of NSW')
        else:
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[column_name].max().reset_index(),
                         x='ASGS_remoteness', y=metric_column, title=f'Maximum {fig_title} by Region of NSW')
        
        fig.update_layout(xaxis_title='Region', yaxis_title=fig_title)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:


from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv('master_dataset.csv')  

data1 = data.loc[data['ASGS_remoteness']!='Not Defined',['ASGS_remoteness', 'Indigenous_pct','LBOTE_pct','ICSEA_value']]
dropdown_options = sorted(data1['ASGS_remoteness'].unique())

dropdown_options_list = [{'label': option, 'value': option} for option in dropdown_options]
app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='region',
        options=dropdown_options,
        value=dropdown_options[1],
        clearable=False,
        multi=True
    ),

    dcc.Dropdown(
        id='column',
        options=[
            'Indigenous %',
            'LBOTE %',
            'ICSEA Score'
        ],
        value='Indigenous %',
        clearable=False,
        multi=False
    ),

    dcc.RadioItems(
        id='statistic',
        options=[
            'Mean',
            'Median',
            'Maximum'
        ],
        value='Mean',
        inline=True
    ),

    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value'),
    Input('column', 'value'),
    Input('statistic', 'value')
)
def update_graph(selected_regions, selected_metric, selected_statistic):
    if not selected_regions:
        return None
    else:
        if selected_metric == 'Indigenous %':
            metric_column = 'Indigenous_pct'
        elif selected_metric == 'LBOTE %':
            metric_column = 'LBOTE_pct'
        else:
            metric_column = 'ICSEA_value'
        
        newdata = data.loc[data['ASGS_remoteness'].isin(selected_regions), ['ASGS_remoteness', metric_column]]
        newdata[metric_column] = pd.to_numeric(newdata[metric_column], errors='coerce')
        
       
        if selected_metric == 'Indigenous %':
            metric_title = 'Indigenous %'
        elif selected_metric == 'LBOTE %':
            metric_title = 'LBOTE %'
        else:
            metric_title = 'ICSEA Score'
        
        if selected_statistic == 'Mean':
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[metric_column].mean().reset_index(),
                         x='ASGS_remoteness', y=metric_column, title=f'Mean {metric_title} by Region of NSW')
        elif selected_statistic == 'Median':
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[metric_column].median().reset_index(),
                         x='ASGS_remoteness', y=metric_column, title=f'Median {metric_title} by Region of NSW')
        else:
            fig = px.bar(data_frame=newdata.groupby('ASGS_remoteness')[metric_column].max().reset_index(),
                         x='ASGS_remoteness', y=metric_column, title=f'Maximum {metric_title} by Region of NSW')
        
        fig.update_layout(xaxis_title='Region', yaxis_title=metric_title)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




