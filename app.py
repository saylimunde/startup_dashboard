import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],format='mixed',errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')

    #total invested amount
    total = round(df['amount'].sum())

    #max amount infused in a startup
    max_funding = df.groupby('startups')['amount'].max().sort_values(ascending=False).head(1).values[0]

    #avg funding in a startup
    avg_funding = round(df.groupby('startups')['amount'].sum().mean())

    #total funded startups
    total_funded_startups = df['startups'].nunique()

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Maximum Funding', str(max_funding) + ' Cr')
    with col3:
        st.metric('Average Funding', str(avg_funding) + ' Cr')
    with col4:
        st.metric('Total Funded Startups', str(total_funded_startups))

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':

        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()


    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    # fig5, ax5 = plt.subplots()
    # temp_df[['amount', 'x_axis']]
    st.line_chart(data=temp_df,x='x_axis',y='amount')

    # st.pyplot(fig5)





def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[
        ['date', 'startups', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    #big investements
    col1,col2 = st.columns(2)
    with col1:
        big_series = (df[df['investors'].str.contains(investor)].groupby('startups')
                  ['amount'].sum().sort_values(ascending=False)).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.dataframe(big_series)

        st.pyplot(fig)
    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct='%1.1f%%')
        ax1.axis('equal')

        st.pyplot(fig1)
    col3,col4 = st.columns(2)
    with col3:
        big_round = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Invested Round')
        fig2, ax2 = plt.subplots()
        ax2.pie(big_round, labels=big_round.index, autopct='%1.1f%%')
        ax2.axis('equal')
        st.pyplot(fig2)

    #big city
    with col4:
        big_city = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('Biggest City Invested In')
        fig3, ax3 = plt.subplots()
        ax3.pie(big_city, labels=big_city.index, autopct='%1.1f%%')
        ax3.axis('equal')
        st.pyplot(fig3)

    print(df.info())

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')


    st.line_chart(data=year_series,x_label='year',y_label='amount')


# df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
# st.dataframe(df)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':

    # btn0 = st.sidebar.button('Show Overall Analysis')
    # if btn0:
        load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startups'].unique().tolist()))
    btn1  = st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2  = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)

    # st.title('Investor Analysis')

