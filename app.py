import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')  # ✅ Correct

df = pd.read_csv('india.csv')
list_of_state = list(df['State'].unique())
list_of_state.insert(0,'Overall India')

st.sidebar.title('India Data  Visualization')
selected_state = st.sidebar.selectbox('Select a State',list_of_state)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('Color represent secondary parameter')

    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",size = primary,
                                color = secondary,color_continuous_scale="Plasma" ,
                                zoom=3,size_max=35, mapbox_style="open-street-map",
                                width = 1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary,
                                color=secondary, color_continuous_scale="Plasma",
                                zoom=6, size_max=35, mapbox_style="open-street-map",
                                width=1200, height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)