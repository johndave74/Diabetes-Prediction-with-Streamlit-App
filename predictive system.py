import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

# Loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (6,148,72,35,0,33.6,0.627,50)

# Reshaping the input data
input_data_reshaped = np.array(input_data).reshape(1,-1)

# Converting the reshaped data to as_numpy_array
input_data_as_numpy_array = np.asarray(input_data_reshaped)

# standardizing the input_data_as_numpy_array
model_scale = StandardScaler()
scaled_input_data = model_scale.fit_transform(input_data_as_numpy_array)

# Predicting the new data
predicted_value = loaded_model.predict(scaled_input_data)
print(predicted_value)

if predicted_value[0] == 1:
    print('The person is Diabetic')
else:
    print('The person is Non-Diabetic')