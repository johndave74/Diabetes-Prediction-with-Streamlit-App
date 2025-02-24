# Diabetes-Prediction-with-Streamlit-App
A Machine Learning-powered Diabetes Prediction System built with Python, Scikit-Learn, and Streamlit for real-time predictions.

![image](https://github.com/user-attachments/assets/73fac92d-685f-4f81-8b05-958a40b1b5b6)

### **📝Diabetes Prediction System**  

# 🩺 Diabetes Prediction System  
A Machine Learning-powered **Diabetes Prediction System** built with **Python, Scikit-Learn, and Streamlit** for real-time predictions.

## 🚀 Project Overview  
This project aims to predict whether a person has diabetes based on medical attributes like glucose levels, BMI, blood pressure, etc. The system is deployed using **Streamlit** for an interactive and user-friendly experience.


# 🩺 Diabetes Prediction System  
A Machine Learning-powered **Diabetes Prediction System** built with **Python, Scikit-Learn, and Streamlit** for real-time predictions.

## 🚀 Project Overview  
This project aims to predict whether a person has diabetes based on medical attributes like glucose levels, BMI, blood pressure, etc. The system is deployed using **Streamlit** for an interactive and user-friendly experience.

## 📌 Features  
✔ **User-friendly Web Interface** powered by Streamlit  
✔ **Machine Learning Model** trained on the PIMA Diabetes dataset  
✔ **Real-time Predictions** based on user input  
✔ **Deployed on Streamlit Cloud** for easy access  

---

## 📊 Technologies Used  
🔹 **Python**  
🔹 **Pandas & NumPy** – Data Processing  
🔹 **Scikit-Learn** – Machine Learning  
🔹 **Streamlit** – Web App Framework  
🔹 **Pickle** – Model Serialization  

---

## ⚙️ Machine Learning Workflow  

### 1️⃣ Data Collection  
The dataset used is the **PIMA Diabetes Dataset**, which contains medical records of **768** individuals, including:  
- Number of Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin Level  
- BMI  
- Diabetes Pedigree Function  
- Age  
- Outcome (Diabetic or Not)  

### 2️⃣ Data Preprocessing  
- **Handling Missing Values**: Replaced zeros in columns like Glucose, Blood Pressure, etc., with the mean.  
- **Feature Scaling**: Used `StandardScaler` to normalize numerical features.  
- **Splitting Data**: Divided into **80% training** and **20% testing** sets using `train_test_split()`.  

### 3️⃣ Model Selection  
We trained multiple models and selected the best based on accuracy:  
✔ **Logistic Regression**  
✔ **Support Vector Machine (SVM)**  

The best model was saved using **Pickle** for deployment.  

### 4️⃣ Model Evaluation  
- **Accuracy Score**: Evaluated using `accuracy_score()`  
- **Confusion Matrix**: Used `confusion_matrix()` for performance insights  

---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction


## 📌 Features  
✔ **User-friendly Web Interface** powered by Streamlit  
✔ **Machine Learning Model** trained on the PIMA Diabetes dataset  
✔ **Real-time Predictions** based on user input  
✔ **Deployed on Streamlit Cloud** for easy access  

---

## 📊 Technologies Used  
🔹 **Python**  
🔹 **Pandas & NumPy** – Data Processing  
🔹 **Scikit-Learn** – Machine Learning  
🔹 **Streamlit** – Web App Framework  
🔹 **Pickle** – Model Serialization  

---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```

### 2️⃣ Install Dependencies  
Create a virtual environment (optional but recommended):  
```bash
pip install virtualenv
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install required packages:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App  
```bash
streamlit run streamlitApp.py
```
This will launch the **Diabetes Prediction System** in your web browser.

---

## 📁 Project Structure  
```
📂 Diabetes-Prediction-App
├── 📄 streamlitApp.py        # Streamlit Web App Code
├── 📄 diabetes_model.pkl     # Trained Machine Learning Model
├── 📄 scaler.pkl             # StandardScaler for input normalization
├── 📄 requirements.txt       # Dependencies for deployment
└── 📄 README.md              # Project Documentation
```

---

## 🚀 Deployment on Streamlit Cloud  
1️⃣ Push your project to **GitHub**  
2️⃣ Go to **[Streamlit Cloud](https://share.streamlit.io/)** and sign in  
3️⃣ Click **"New App"**, select your repo, set the main file as:  
   ```
   streamlitApp.py
   ```
4️⃣ Click **"Deploy"** and wait for the app to go live  

✅ Your app will be available at:  
```
https://your-app-name.streamlit.app
```

---

## 🔥 Demo Screenshot  
![Diabetes Prediction UI](./screenshot.png)  

---

## 🤝 Contributing  
Feel free to fork this repo and submit **pull requests**! Contributions are welcome.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 💡 Author  
👤 **John David**  
🔗 [LinkedIn](https://linkedin.com/in/your-profile) | 🐦 [Twitter](https://twitter.com/your-profile)  

---

⭐ **If you like this project, don't forget to give it a star!** ⭐  
```

---
