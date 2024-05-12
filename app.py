import streamlit as st 
import pandas as pd,time
# server.max
#text element
st.text("This is a text")
st.title("The title is Rhon")
st.header("The title is Rhon")
st.subheader("The title is Rhon")
st.write("The title is Rhon")


#error eleemnt
st.error("The title is Rhon",icon="🚨")
st.success("The title is Rhon")


#inout
first_name=st.text_input("Enter the name")
password=st.text_input("Enter the password",type="password")
message=st.text_area("message")
date=st.date_input("Date")
Appointment_date=st.time_input("Time")
age=st.number_input("Age",min_value=0,max_value=100)

#buttons
gender=st.radio("Gender",["Male","Female"])
enable_light=st.toggle("Enable picker")
slider=st.checkbox("Level")


#sliders
slider=st.slider('slider',0,10)
countries=st.selectbox('Country',['Uganda','Ghana','Kenya'])
continent=st.multiselect('Continent',['Europe','Asia'])
jobslider=st.select_slider('Job Level',['Junior','Intermediate','Senior','Expert'])


#dataframes

# df=pd.read_csv('/Users/mac/Downloads/people-2000000.csv').head(10)
# st.dataframe(df)

#mredia element

# st.image(path,caption=)

# audio=open(path,'rb')
# st.audio(audio)

# st.video()

if st.button("Take a photo"):
    pic=st.camera_input("Take a photo")
    with open("somepic.png",'wb') as f:
        if pic is not None:
            f.write(pic.getbuffer())
    # st.write(pic)

#download and upload
file_uploaded=st.file_uploader("upload a csv",type="csv",accept_multiple_files=True,)
st.write(file_uploaded)


# st.download_button('Donwload file','itis.csv')


#status elements:
with st.spinner('Thinking ...'):
    time.sleep(5)
    st.write('hello')

value=10
# with st.progress(0 <= value <= 100):
#     time.sleep(5)
#     st.write(f'{value}% complete........')
#     time.sleep(3)
#     with st.progress(0 <= value*5 <= 100):
#         time.sleep(5)
#         st.write(f'{value*2}% complete........')

#chat input 
prompt=st.chat_input("Ask something")
if prompt:
    with st.chat_message("ai"):
        st.write(f'You  typed {prompt}')

#layout
#tabs
Home,About=st.tabs(["Home","About"])

with Home:
    st.subheader('This is a home tab')

#columns # bases on varioables passed
col1,col2=st.columns(2)
with col1:
    st.write('Col1')

#columns can inherit
# col2.dataframe(df) This will print the df if its already there

#containers 
container=st.container(border=True) # we can pass other attributes to it border or not
with container:
    st.write("This is a container")


#explander .... 
expander=st.expander('Frequently asked Questions')
with expander:
    st.divider()
    st.write('What is a food')


#popover
