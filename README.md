# carprediction


Car Price Prediction Project

This project aims to predict car prices using a linear regression model. The key steps and results of the project are as follows:

1. Objective: Develop a model to accurately predict the selling price of cars based on various features.
   
2. Data: The dataset `Cardetails.csv` includes features such as `name`, `year`, `selling_price`, `km_driven`, `fuel`, `seller_type`, `transmission`, `owner`, `mileage`, `engine`, `max_power`, `torque`, and `seats`.

3. Model: A linear regression model was trained and tested. Key factors influencing the predictions included the car's age, mileage, fuel type, and engine size.

4. Results: 
   - The model achieved an R² score of 0.85, indicating a strong correlation between predicted and actual selling prices.
   - Feature importance analysis revealed that `year`, `km_driven`, and `fuel` had the most significant impact on price prediction.

5. Data Preprocessing: Included handling missing values and encoding categorical variables to improve model accuracy.

6. Deployment: The project is deployed as a web app using Streamlit, allowing users to input car details and receive instant price predictions.

How to Run the App

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Run the Streamlit app: `streamlit run app.py`.
4. Open the provided local URL in your web browser to use the app.

Usage

Enter the car details such as year, mileage, fuel type, etc., into the web app. The model will instantly predict the selling price based on the input features.

Acknowledgments

This project utilizes pandas, numpy, scikit-learn, and Streamlit. Special thanks to the dataset providers and the open-source community for their valuable contributions.


