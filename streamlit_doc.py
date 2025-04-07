import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning streamlit')
st.subheader('Sayli Munde!')

st.write('This is a normal text')
st.markdown('''
### My favourite movies
- Race
- Deol
- Don
''')

st.code("""
def foo(input):
    return foo*2

x = foo(2)

""")

st.latex('x^2 + y^2 = 2')

df = pd.DataFrame({'name':['Vinita','Namita','Anupam'],
                  'marks':[40,50,60],
                    'package':[10,12,13]
                   })
st.dataframe(df)

st.metric('Revenue','Rs 3L','3%')

st.json({'name':['Vinita','Namita','Anupam'],
                  'marks':[40,50,60],
                    'package':[10,12,13]
                   })
st.image('pencils.jpg')

st.sidebar.title('sidebar ka title')

col1,col2 = st.columns(2)

with col1:
    st.image('pencils.jpg')

with col2:
    st.image('pencils.jpg')

st.error('Login Failed')
st.success('Login Successfull')
st.info('Login Successfull')
st.warning('Login Successfull')

bar = st.progress(0)

for i in range(1,101):
    # time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter Email:')
number = st.number_input('Enter number:')
st.date_input('enter regs date')

file = st.file_uploader('upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])

btn = st.button('Login karo')

# #if the button is clicked
if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        st.balloons()
        st.write(gender)
    else:
        st.error('Login failed')
#
file = st.file_uploader('upload a csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())