# 📩 SMS Spam Classifier

This project is a machine learning-based SMS spam classifier that predicts whether a message is spam or not.

## 🚀 Features
- Classifies messages as Spam or Not Spam
- Uses TF-IDF for text vectorization
- Logistic Regression model
- Simple Streamlit web app

## 🧠 Accuracy
Achieved approximately 93% accuracy on test data

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

## 📸 Output
<img width="1230" height="638" alt="image" src="https://github.com/user-attachments/assets/2c69e682-4c84-4973-8742-5d8319dc54ec" />

<img width="1233" height="549" alt="image" src="https://github.com/user-attachments/assets/a375ade6-891f-44f1-9ec8-80792491f0f1" />



📌 Project Approach

The SMS Spam Classifier project uses machine learning to detect whether a message is spam or not. First, the dataset was loaded and the text was cleaned by converting it to lowercase and removing special characters. Then, TF-IDF vectorization was applied to convert text into numerical form. A Logistic Regression model was trained on this data and evaluated, achieving around 93% accuracy. Finally, a Streamlit web application was built to allow users to input messages and get real-time spam predictions.

## ▶️ How to Run
```bash
pip install streamlit scikit-learn pandas
python -m streamlit run main.py
