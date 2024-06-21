import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import pickle


#set up page configuration for streamlit
def main():
    st.set_page_config(page_title='Industrial Copper Modeling',initial_sidebar_state='expanded',
                            layout='wide',menu_items={"about":'This streamlit application for Induatrial Copper Modelling'})

    st.title(":red[ Industrial Copper Modeling ]")
    st.markdown(" ")

    #set up the sidebar with optionmenu
    selected = option_menu("Industrial Copper | Comprehensive Analysis and Predictive Modeling",
                                options=["Home","Get Prediction","Explore"],
                                icons=["house","lightbulb","bar-chart-line"],
                                default_index=1,menu_icon="globe",
                                orientation="horizontal")
    # set up the information for 'Home' menu
    if selected == 'Home':
        title_text = '''<h1 style='font-size: 30px;text-align: center; color:grey;'>INDUSTRIAL COPPER</h1>'''
        st.markdown(title_text, unsafe_allow_html=True)
        col1,col2= st.columns([2, 1.5], gap="large")
        with col1:
            st.markdown("### :red[Domain]: ")
            st.markdown('<h5> Manufacturing ',unsafe_allow_html=True)              

            st.markdown("### :red[Skills & Technologies]:")
            st.markdown('<h5> Python scripting,  Data Preprocessing,  Scikit-learn,  Machine learning,  EDA, Streamlit ',unsafe_allow_html=True)
                
            st.markdown("### :red[Overview]:")
            st.markdown('''<h4>
                                <li>Processed copper sales and pricing data using Python, <br>
                                <li>Cleaned data and handled outliers and skewness, <br>
                                <li>Analyzed pricing trends and sales predictions, <br>
                                <li>Created interactive visualizations and dynamic plots for insights. <br>
                        </h4>

                            ''', unsafe_allow_html=True)

            # Problem Statement
            st.info('''
                ### :red[Problem Statement]: ###
                Industry data on sales and pricing can be skewed, affecting manual predictions. 
                ML regression with normalization and outlier detection improves accuracy. 
                Lead classification predicts customer conversion to predict 'Status' (WON/LOST).
                     
                The solution includes data exploration, cleaning, regression, and classification model building. 
                Streamlit enables user input for price and lead status predictions.
            ''')
            st.markdown("### :red[Solution Steps]: ###")
            st.markdown("""
                - 🔍 Explore and address skewness and outliers in the dataset.
                - 🔄 Transform and clean the data.
                - 📈 Build a regression model to predict 'Selling_Price'.
                - 🎯 Build a classification model to predict 'Status' (WON/LOST).
                - 🚀 Create a Streamlit page for interactive predictions.
            """)
            st.markdown("")
            st.image("Copper.png",width=400,use_column_width=False)  

        with col2:
            st.markdown("  ")
            st.image("https://stockhead.com.au/wp-content/uploads/2022/05/slow-copper.gif",use_column_width=True)
            st.markdown("  ")
            st.write("----")
            df = pd.read_csv(r"data_description.csv")
            st.markdown("  ")
            if st.button("## :rainbow[ About Data - Click to view ]"):
                raw_data = pd.read_csv('data_description.csv')

                st.write(raw_data)


    #user input values for selectbox and encoded for respective features
    class option():
        
        country_values=[ 25.,  26.,  27.,  28.,  30.,  32.,  38.,  39.,  40.,  77.,  78., 79.,  80.,  84.,  89., 107., 113.]

        status_values=['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM','Wonderful', 'Revised',
                'Offered', 'Offerable']

        status_encoded = {'Lost':0, 'Won':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,'Wonderful':5, 'Revised':6,
                        'Offered':7, 'Offerable':8}
        
        item_type_values=['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']

        item_type_encoded = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}

        application_values=[2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 27.0, 28.0, 29.0, 38.0, 39.0, 40.0,
                    41.0, 42.0, 56.0, 58.0, 59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0]
        
        product_ref_values=[611728, 611733, 611993, 628112, 628117, 628377, 640400, 640405, 640665, 164141591, 164336407,
                    164337175, 929423819, 1282007633, 1332077137, 1665572032, 1665572374, 1665584320, 1665584642,
                    1665584662, 1668701376, 1668701698, 1668701718, 1668701725, 1670798778, 1671863738, 1671876026,
                    1690738206, 1690738219, 1693867550, 1693867563, 1721130331, 1722207579]

    #set up information for the 'get prediction' menu
    if selected == 'Get Prediction':
        title_text = '''<h2 style='font-size: 32px;text-align: center;color:grey;'>Copper Selling Price and Status Prediction</h2>'''
        st.markdown(title_text, unsafe_allow_html=True)
        
        #set up option menu for selling price and status menu
        select=option_menu('',options=["Selling Price","Status"],
                                        icons=["cash", "toggles"],
                                        orientation='horizontal',)

        if select == 'Selling Price':
            st.markdown("<h5 style=color:grey>To predict the selling price of copper, please provide the following information:",unsafe_allow_html=True)
            st.write('')

            # creted form to get the user input 
            with st.form('prediction'):
                col1,col2,col3=st.columns([6, 1, 6])
                with col1:
                    item_date=st.date_input(label='Item Date',format='DD/MM/YYYY')

                    country=st.selectbox(label='Country',options=option.country_values,index=None)

                    item_type=st.selectbox(label='Item Type',options=option.item_type_values,index=None)

                    application=st.selectbox(label='Application',options=option.application_values,index=None)

                    product_ref=st.selectbox(label='Product Ref',options=option.product_ref_values,index=None)

                    customer=st.number_input('Customer ID',min_value=12458)

                with col3:
                    delivery_date=st.date_input(label='Delivery Date',format='DD/MM/YYYY')

                    status=st.selectbox(label='Status',options=option.status_values,index=None)

                    quantity=st.number_input(label='Quantity',min_value=0.1)

                    width=st.number_input(label='Width (Min: 1.0, Max: 2990)',min_value=1.0,max_value=2990.0)

                    thickness=st.number_input(label='Thickness (Min: 0.18, Max: 400)',min_value=0.18,max_value=400.0)

                    st.markdown('<br>', unsafe_allow_html=True)
                    
                    button=st.form_submit_button('PREDICT SELLING PRICE',use_container_width=True)

                    st.markdown("""
                            <style>
                            div.stButton > button:first-child {
                                background-color: #009999;
                                color: white;
                                width: 100%;
                            }
                            </style>
                        """, unsafe_allow_html=True)

            if button:

                #check whether user fill all required fields
                if not all([item_date, delivery_date, country, item_type, application, product_ref,
                            customer, status, quantity, width, thickness]):
                    st.error("Please fill in all required fields.")

                else:
                    
                    #opened pickle model and predict the selling price with user data
                    with open('Regressor.pkl','rb') as files:
                        predict_model=pickle.load(files)

                    # customize the user data to fit the feature 
                    status=option.status_encoded[status]
                    item_type=option.item_type_encoded[item_type]

                    delivery_time_taken=abs((item_date - delivery_date).days)

                    quantity_log=np.log(quantity)
                    thickness_log=np.log(thickness)

                    #predict the selling price with regressor model
                    user_data=np.array([[customer, country, status, item_type ,application, width, product_ref,
                                        delivery_time_taken, quantity_log, thickness_log ]])
                    
                    pred=predict_model.predict(user_data)

                    selling_price=np.exp(pred[0])

                    #display the predicted selling price 
                    st.subheader(f":green[Predicted Selling Price :] {selling_price:.2f}") 
                    st.balloons()

        if select == 'Status':
            st.markdown("<h5 style=color:grey;>To predict the status of copper, please provide the following information:",unsafe_allow_html=True)
            st.write('')

            #creted form to get the user input 
            with st.form('classifier'):
                col1,col2,col3=st.columns([6, 1, 6])

                with col1:

                    item_date=st.date_input(label='Item Date',format='DD/MM/YYYY')

                    country=st.selectbox(label='Country',options=option.country_values,index=None)

                    item_type=st.selectbox(label='Item Type',options=option.item_type_values,index=None)

                    application=st.selectbox(label='Application',options=option.application_values,index=None)

                    product_ref=st.selectbox(label='Product Ref',options=option.product_ref_values,index=None)

                    customer=st.number_input('Customer ID',min_value=10000)

                with col3:

                    delivery_date=st.date_input(label='Delivery Date',format='DD/MM/YYYY')

                    quantity=st.number_input(label='Quantity',min_value=0.1)

                    width=st.number_input(label='Width (Min: 1.0, Max: 2990)',min_value=1.0)

                    thickness=st.number_input(label='Thickness (Min: 0.18, Max: 400)',min_value=0.1)

                    selling_price=st.number_input(label='Selling Price(Min: 0.1, Max: 100001015)',min_value=0.1)

                    st.markdown('<br>', unsafe_allow_html=True)
                    
                    button=st.form_submit_button('PREDICT STATUS',use_container_width=True)
                    
                    st.markdown("""
                            <style>
                            div.stButton > button:first-child {
                                background-color: #009999;
                                color: white;
                                width: 100%;
                            }
                            </style>
                        """, unsafe_allow_html=True)

            if button:

                if not all([item_date, delivery_date, country, item_type, application, product_ref,
                            customer,quantity, width, thickness,selling_price]):
                    st.error("Please fill in all required fields.")

                else:
                    #opened pickle model and predict status with user data
                    with open('Classifier.pkl','rb') as files:
                        model=pickle.load(files)

                    # customize the user data to fit the feature 
                    item_type=option.item_type_encoded[item_type]

                    delivery_time_taken=abs((item_date - delivery_date).days)

                    quantity_log=np.log(quantity)
                    thickness_log=np.log(thickness)
                    selling_price_log=np.log(selling_price)

                    #predict the status with classifier model
                    user_data=np.array([[customer, country, item_type ,application, width, product_ref,
                                        delivery_time_taken, quantity_log, thickness_log, selling_price_log ]])
                    
                    status=model.predict(user_data)

                    #display the predicted status 
                    if status==1:
                        st.subheader(f":green[Status of the copper : ] WON")
                        st.balloons()

                    else:
                        st.subheader(f":red[Status of the copper :] LOST")

#--------------------

    #set up information for 'Explore' menu 
    if selected == "Explore":
        col1,col2=st.columns([3,2])
        with col1:
            st.markdown(" ")
            st.subheader(':blue[Project Title :]')
            st.markdown('<h5> Industrial Copper Modeling',unsafe_allow_html=True)

            st.subheader(':blue[Domain :]')
            st.markdown('<h5> Manufacturing ',unsafe_allow_html=True)

            st.subheader(':blue[Process :]')
            st.markdown('<h5> Data Preprocessing,Feature Engineering, EDA, Model Building, Streamlit ',unsafe_allow_html=True)

        with col2:
            st.markdown(" ")
            st.image("https://mekascable.com/wp-content/uploads/2021/09/copper-mekas-cable.jpg",width=450)
        st.markdown("-------- ")
        col1,col2,col3=st.columns([2,1,3])
        with col1:
            st.subheader(':blue[About Copper]')
            st.info('''
                        ### What is copper?
                        Copper is a reddish-brown metal found abundantly worldwide, with top producers including Chile, Peru, and China. It was the first metal worked by humans and led to the Bronze Age when combined with tin around 3000 BC.
                        ''')
            st.link_button(':red[Explore About copper]',url='https://en.wikipedia.org/wiki/Copper')
        with col3:
            st.subheader(':blue[What is Copper Used For?]')
            st.info("""
                #### Key Facts About Copper
                - 🔌 **Electrical:** Copper is widely used in electrical wiring due to its excellent conductivity.
                - 🏗️ **Construction:** It's utilized in plumbing, roofing, and various decorative elements for its durability and aesthetic appeal.
                - 🚗 **Transportation:** Copper components are essential in automotive and aerospace industries for radiators, oil coolers, and more.
                - 🦠 **Antimicrobial:** Copper's antimicrobial properties make it ideal for healthcare settings, used in surfaces and fixtures to reduce germ spread.
                - 🎨 **Art and Jewelry:** It's a popular choice for sculptures, jewelry, cookware, and artistic designs due to its malleability and attractive appearance.
                """, icon="🔍")
            
        st.markdown("-------- ")

        col1,col2,col3=st.columns([2,1,2])  
        with col2:
                st.image("https://target.scene7.com/is/image/Target/GUEST_74fc8af2-4885-4860-b6db-55672f1ed3eb?wid=488&hei=488&fmt=pjpeg",width=200)

if __name__ == "__main__":
    main()