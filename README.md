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
https://github.com/amulyataksande1801-cloud/SMS-spam-classifier/blob/main/Screenshot%202026-04-03%20230633.png?raw=true



📌 Project Approach

The SMS Spam Classifier project uses machine learning to detect whether a message is spam or not. First, the dataset was loaded and the text was cleaned by converting it to lowercase and removing special characters. Then, TF-IDF vectorization was applied to convert text into numerical form. A Logistic Regression model was trained on this data and evaluated, achieving around 93% accuracy. Finally, a Streamlit web application was built to allow users to input messages and get real-time spam predictions.

## ▶️ How to Run
```bash
pip install streamlit scikit-learn pandas
python -m streamlit run main.py
