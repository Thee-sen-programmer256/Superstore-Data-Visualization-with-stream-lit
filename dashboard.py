import pandas as pd
import streamlit as st
import os,xlrd
import plotly.express as px
import matplotlib
#set the page
st.set_page_config(page_title='SuperStore!!!',page_icon=":bar_chart:",layout="wide")
st.title(':bar_chart: Superstore EDA')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# allow user to upload a file 
if st.button('Upload a file'):
    file=st.file_uploader(":file_folder: Upload a file ",type=(['csv','txt','xlsx']))
    if file is not None:
        df=pd.read_csv(file.name)
else:
    df=pd.read_excel('./Superstore.xls')

    col1,col2=st.columns(2)
    #get the dates :
    df['Order Date']=pd.to_datetime(df['Order Date'])
    #define the  start and end 
    start_date=df['Order Date'].min()
    end_date=df['Order Date'].max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", start_date))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", end_date))

    #filter the dataframe basing on the date selected 
    df=df[df['Order Date'].between(date1,date2)]


    #create the side bar 
    st.sidebar.title('Choose Filter')

    #create filters 

    # Create for Region
    region = st.sidebar.multiselect("Region", df["Region"].unique())
    if not region:
        df2 = df.copy()
    else:
        df2 = df[df["Region"].isin(region)]

    # Create for State
    state = st.sidebar.multiselect("State", df2["State"].unique())
    if not state:
        df3 = df2.copy()
    else:
        df3 = df2[df2["State"].isin(state)]

    # Create for City
    city = st.sidebar.multiselect("City",df3["City"].unique())
    


# Filter the data based on Region, State and City

    if not region and not state and not city:
        filtered_df = df
    elif not state and not city:
        filtered_df = df[df["Region"].isin(region)]
    elif not region and not city:
        filtered_df = df[df["State"].isin(state)]
    elif state and city:
        filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
    elif region and city:
        filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]
    elif region and state:
        filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]
    elif city:
        filtered_df = df3[df3["City"].isin(city)]
    else:
        filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]


    category_df=filtered_df.groupby("Category",as_index=False).agg({'Sales':"sum"})

    with col1:
        st.subheader('Category wise sales')
        fig=px.bar(category_df,x="Category",y="Sales",text=['${:,.2f}'.format(x) for x  in category_df['Sales']],template='seaborn',color="Category" )
        st.plotly_chart(fig,use_container_width=True,height=200)

    with col2:
        st.subheader('Region wise sales')
        fig=px.pie(filtered_df,values="Sales",names="Region",hole=0.6)
        fig.update_traces(text=filtered_df.Region,textposition="outside")
        st.plotly_chart(fig,use_container_width=True,height=200)

cl1,cl2=st.columns(2)
with cl1:
    with st.expander('Total Sales by Category'):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv=category_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download File",data=csv,file_name="category.csv")

with cl2:
    regiondf=filtered_df.groupby("Region",as_index=False).agg({'Sales':"sum"})
    with st.expander('Total Sales by Region'):
        st.write(regiondf.style.background_gradient(cmap="YlOrRd"))
        csv=regiondf.to_csv(index=False).encode('utf-8')
        st.download_button("Download File",data=csv,file_name="region.csv")

filtered_df['month_year']=filtered_df['Order Date'].dt.to_period('M')
yearly_sales=pd.DataFrame(filtered_df.groupby(filtered_df['month_year'].dt.strftime('%Y : %B'))["Sales"].sum()).reset_index()
st.subheader('Time Series Analysis')
fig=px.line(yearly_sales, x = "month_year", y="Sales",labels={"Sales":"Amount"},height=500,width=1000,template="gridon")
st.plotly_chart(fig,use_container_width=True)


# filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
# st.subheader('Time Series Analysis')

# linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
# fig2 = px.line(linechart, x = "month_year", y="Sales", labels = {"Sales": "Amount"},height=500, width = 1000,template="gridon")
# st.plotly_chart(fig2,use_container_width=True)



    


