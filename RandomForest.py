import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import serial
import pyttsx3
import time

# 1. Load and preprocess the data
data = pd.read_csv('Book1.csv')

feature_names = ['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5']  # Adjust based on your actual CSV file

# Split features and labels
X = data.iloc[:, :-1]  # All columns except the last one
y = data.iloc[:, -1]   # The last column as the target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data (not mandatory for Random Forest but retained for consistency)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. Train a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 3. Set up serial communication with Arduino
arduino_port = 'COM7'  # Replace with the correct port for your Arduino
baud_rate = 9600  # Set the baud rate as per your Arduino's configuration
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# 4. Set up text-to-speech engine
engine = pyttsx3.init()

# 5. Function to predict and speak the result
def predict_and_speak(data):
    try:
        # Convert the data to the format the model expects
        data_list = [float(i) for i in data.split(',')]  # Assuming data comes as a comma-separated string
        live_data_df = pd.DataFrame([data_list], columns=feature_names)  # Convert to DataFrame with correct feature names

        # Scale the data using the same scaler as during training
        data_scaled = scaler.transform(live_data_df)

        # Make prediction
        prediction = rf_model.predict(data_scaled)

        # Speak the prediction
        engine.say(f'{prediction[0]}')
        engine.runAndWait()
        
        # Print prediction to the console as well
        print(f"Prediction: {prediction[0]}")

    except Exception as e:
        print(f"Error: {e}")

# 6. Read live data from Arduino and make predictions
try:
    while True:
        # Read a line from Arduino
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            print(f"Received data: {line}")
            predict_and_speak(line)
        
        time.sleep(0)  # Delay to prevent overwhelming the serial port
        
except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    ser.close()
