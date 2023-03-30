from enum import unique
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(page_title="Calls KPI Dashboard", page_icon=':scales:', layout="wide")

dataFrameSerialization = "legacy"
df = pd.read_excel(
    io='front_desk_calls_consolidated.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    skiprows=0,
    usecols='B:R',
    nrows=1000)

#df['Date'] = pd.to_datetime(df['Date (MM/DD/YYYY)'] + ' ' + df['Incoming Time'])

#st.dataframe(df)

# Sidebar 

st.sidebar.header("Filter By:")
destination = st.sidebar.multiselect(
    "Select Destination:",
    options=df["Destination"].unique(),
    default=df["Destination"].unique()
)

notes = st.sidebar.multiselect(
    "Notes on PP?",
    options=df["Note_on_PP"].unique(),
    default=df["Note_on_PP"].unique()
) 

transfer_successful = st.sidebar.multiselect(
    "Transfer Successful?",
    options=df["Transferred"].unique(),
    default=df["Transferred"].unique()

) 
df_selection = df.query(
    "Destination == @destination & Transferred == @transfer_successful & Note_on_PP == @notes"
       
)

#st.dataframe(df_selection)

#--- MAIN PAGE --- 

st.title(":bar_chart: Call Performance Indicators")
st.markdown("##")
#indicators for calls that were picked up
successful_calls = df_selection[df_selection["Transferred"]=="Yes"].shape[0]
unsuccessful_calls = df_selection[df_selection["Transferred"]=="No"].shape[0]
total_calls = df_selection["Transferred"].shape[0]
average_successful_calls = round((successful_calls / total_calls), 2) 
average_for_ratings = int(round(average_successful_calls * 10 /2,0))
rating = ":star:" * average_for_ratings
left_column, mid_column,  right_column = st.columns(3)







with left_column:
    st.subheader("Total Calls:")
    st.subheader(f'{total_calls}')
with mid_column:
    st.subheader("Rating:")
    st.subheader(f"{average_successful_calls * 100}%")
    
   
    #st.subheader(f"{rating}")

with right_column:
    st.subheader("Successful Calls:")
    st.subheader(f"{successful_calls}")


st.markdown("----")

# TOP 5 CALLERS

left_col, right_col  = st.columns(2)
team_member_calls = df['Destination']
team_member_calls_count = df['Destination'].value_counts()
team_member_calls_dict = team_member_calls_count.to_dict()
calls_dict = {k: v for k,v in team_member_calls_dict.items() if v > 20}

calls_for_graph = pd.DataFrame(list(calls_dict.items()),columns=['Destination', 'Number of Calls'])
fig = px.pie(calls_for_graph, values='Number of Calls', names='Destination', title='<b>Most Calls Received<b>')

#Waiting Time Graphic

average_waiting_time = df['Hang up Time (MIN)'].value_counts()
average_waiting_time_dict = average_waiting_time.to_dict()
graph_df = pd.DataFrame(list(average_waiting_time_dict.items()), columns=['Hang up Time (MIN)', 'Frequency'])
other_fig = px.bar(graph_df, y='Frequency', x='Hang up Time (MIN)', title='<b>Waiting Times<b>')

#specific team member waiting time

average_selective_waiting_time = df_selection['Hang up Time (MIN)'].value_counts()
average_select_wt_dict = average_selective_waiting_time.to_dict()
graph_awt = pd.DataFrame(list(average_select_wt_dict.items()), columns=['Hang up Time (MIN)', 'Frequency'])
awt_fig = px.bar(graph_awt, y='Frequency', x='Hang up Time (MIN)', title='<b>Waiting Times - Specific Team Member <b>')


#making a graphic for a specific team member

relative_member_calls = df_selection['Destination']
team_member_calls_count = df_selection['Destination'].value_counts()
relative_calls_dict = team_member_calls_count.to_dict()
relative_calls_dict = {k: v for k,v in relative_calls_dict.items()}

relative_calls_graph = pd.DataFrame(list(relative_calls_dict.items()), columns=['Destination', 'Number of Calls'])
relative_graph_fig = px.pie(relative_calls_graph, values='Number of Calls', names='Destination', title='Calls per Selected Team Members')

# making a graphic to show the overall percentage of successfully transferred calls vs filtered calls

overall_calls = df["Transferred"].count()
successful_vs_unsuccessful_calls = df["Transferred"].value_counts()

svu_calls = successful_vs_unsuccessful_calls.to_dict()
svu_calls_graph = pd.DataFrame(list(svu_calls.items()), columns=['Transferred', 'Number of Calls'])
svu_fig = px.bar(svu_calls_graph, y='Number of Calls', x='Transferred', title='Calls Transferred vs Not Transferred')

# this graphic shows the percentage of FILTERED successfully trasferred vs filtered calls

svu_relative_calls = df_selection['Transferred'].count()
relative_svu_calls = df_selection["Transferred"].value_counts()

relative_svu_calls_dict = relative_svu_calls.to_dict()
rel_svu_calls_graph = pd.DataFrame(list(relative_svu_calls_dict.items()), columns=['Transferred', 'Number of Calls'])
relsvu_fig = px.bar(rel_svu_calls_graph, y='Number of Calls', x='Transferred', title='Calls Transferred vs Not Transferred - Filtered')
#Duration - to know the mean time of call durations
#df['Hang up Time (MIN)'] = (pd.to_datetime(df['Hang up Time (MIN)'],format='%H:%M:%S')) -> this is NOT needed and will cause problems

#the below works for duration
df['Hang up Time (MIN)'] = (pd.to_timedelta(df['Hang up Time (MIN)'].astype(str).map(lambda x: x[-1:] + x[:x.find("-")])))

mean_wait_time = df['Hang up Time (MIN)'].dt.seconds/60
calculate_mean_time = mean_wait_time.mean()
minute = 0
mt_printout = str
calculate_mean_time = calculate_mean_time*60
while calculate_mean_time > 60:
    calculate_mean_time = int(round(calculate_mean_time - 60,0))
    minute += 1
mt_printout = f'{minute}:{calculate_mean_time}'

df_selection['Hang up Time (MIN)'] = (pd.to_timedelta(df['Hang up Time (MIN)'].astype(str).map(lambda x: x[-1:] + x[:x.find("-")])))

select_mwt = df_selection['Hang up Time (MIN)'].dt.seconds/60
calculate_mwt = select_mwt.mean()
select_min = 0
smt_printout = str
calculate_mwt = calculate_mwt*60
while calculate_mwt > 60:
    calculate_mwt = int(round(calculate_mwt - 60,0))
    minute += 1
smt_printout = f'{select_min}:{calculate_mwt}'




with left_col: 
    st.subheader("Average Wait Time:")
    st.subheader(f'{mt_printout}')
    st.plotly_chart(fig)
    st.plotly_chart(relative_graph_fig)
    
with right_col:
    st.subheader("Average Team Member(s) Call Wait Time:")
    st.subheader(f'{smt_printout}')
    st.plotly_chart(other_fig)
    st.plotly_chart(awt_fig)
   
    

st.markdown('----')

graph_col_one, graph_col_two = st.columns(2)

with graph_col_one:
    st.plotly_chart(relsvu_fig)
with graph_col_two:
    st.plotly_chart(svu_fig)