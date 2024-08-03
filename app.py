import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

# CSS for styling and animation
st.markdown("""
    <style>
    body {
        background-image: url('https://images.pexels.com/photos/235222/pexels-photo-235222.jpeg?auto=compress&cs=tinysrgb&w=600');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin: 0;
        padding: 0;
        height: 100vh;
        width: 100vw;
    }
    .header {
        font-size: 36px;
        color: #ff4b4b;
        text-align: center;
        margin-top: 20px;
        animation: blink 2s infinite; /* Apply the blinking animation */
    }
    .input-container {
        background-color: rgba(245, 245, 245, 0.9); /* Slightly transparent background */
        padding: 10px;
        border-radius: 5px;
        margin: 0 auto;
        width: 80%;
        max-width: 800px;
    }
    .predict-button {
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .output-box {
        margin-top: 20px;
        padding: 20px;
        border: 2px solid #ff4b4b;
        background-color:#ff4b4b ; /* Slightly transparent background */
        border-radius: 5px;
        text-align: center;
    }
    .output-text {
        font-size: 24px;
        color: #FFFFFF;
    }
    /* Animation keyframes */
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="header">Estimate the price of your dream car now!l</h1>', unsafe_allow_html=True)

cars_data = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()
cars_data['name'] = cars_data['name'].apply(get_brand_name)

st.markdown('<div class="input-container">', unsafe_allow_html=True)
name = st.selectbox('Select Car Brand', cars_data['name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No of kms Driven', 11, 200000)
fuel = st.selectbox('Fuel type', cars_data['fuel'].unique())
seller_type = st.selectbox('Seller type', cars_data['seller_type'].unique())
transmission = st.selectbox('Transmission type', cars_data['transmission'].unique())
owner = st.selectbox('Owner type', cars_data['owner'].unique())
mileage = st.slider('Car Mileage', 10, 40)
engine = st.slider('Engine CC', 700, 5000)
max_power = st.slider('Max Power', 0, 200)
seats = st.slider('No of Seats', 5, 10)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Predict"):
    input_data_model = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'],
                                       [1, 2, 3, 4, 5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'], [1, 2, 3, 4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'], [1, 2, 3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'], [1, 2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
                                      'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
                                      'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
                                      'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
                                      'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                                     inplace=True)

    car_price = model.predict(input_data_model)[0]

    
    st.markdown(f'''
    <div class="output-box">
        <p class="output-text">The car you are looking for might cost you around:</p>
        <p class="output-text"><strong>INR {car_price:,.2f}</strong></p>
    </div>
    ''', unsafe_allow_html=True)
