# 🤖 Data Classification Using AI

A machine learning project that demonstrates the fundamentals of **Supervised Learning** by building a classification model using a structured dataset. This project focuses on the complete machine learning workflow, including data preprocessing, train-test splitting, model training, prediction, and performance evaluation.

---

## 📌 Project Overview

Data classification is one of the most important tasks in Artificial Intelligence and Machine Learning. In this project, a classification model is trained on a dataset to identify patterns and predict the correct category of unseen data.

The project provides hands-on experience with:

* Data preprocessing
* Feature selection
* Train-test data splitting
* Classification algorithms
* Model evaluation
* Prediction on new data

This project was developed as part of the **DecodeLabs Artificial Intelligence Internship Program (Project 2).**

---

## 🎯 Objectives

* Understand the fundamentals of supervised learning.
* Load and analyze a dataset.
* Prepare data for machine learning.
* Train a classification model.
* Test the model using unseen data.
* Evaluate model performance using accuracy metrics.
* Gain practical experience with Scikit-Learn.

---

## 🧠 Technologies Used

| Technology                 | Purpose                   |
| -------------------------- | ------------------------- |
| Python                     | Programming Language      |
| Pandas                     | Data Manipulation         |
| NumPy                      | Numerical Computation     |
| Scikit-Learn               | Machine Learning          |
| Matplotlib                 | Data Visualization        |
| Seaborn                    | Statistical Visualization |
| Jupyter Notebook / PyCharm | Development Environment   |

---

## 📂 Project Structure

```text
Data-Classification-Using-AI/
│
├── dataset/
│   └── iris.csv
│
├── screenshots/
│   ├── dataset_preview.png
│   ├── model_output.png
│   └── confusion_matrix.png
│
├── src/
│   └── classification.py
│
├── requirements.txt
├── README.md
└── Project_Report.docx
```

---

## 📊 Dataset Information

The project uses a structured dataset for classification purposes.

### Features

* Feature 1
* Feature 2
* Feature 3
* Feature 4

### Target Variable

The target variable contains the class labels that the model learns to predict.

Example:

| Feature 1 | Feature 2 | Feature 3 | Feature 4 | Class      |
| --------- | --------- | --------- | --------- | ---------- |
| 5.1       | 3.5       | 1.4       | 0.2       | Setosa     |
| 7.0       | 3.2       | 4.7       | 1.4       | Versicolor |

---

## ⚙️ Machine Learning Workflow

### Step 1: Import Libraries

Required libraries are imported for data handling, visualization, and machine learning.

### Step 2: Load Dataset

The dataset is loaded using Pandas and inspected for missing values and data types.

### Step 3: Data Preprocessing

Data cleaning and preparation are performed to ensure quality input for the model.

### Step 4: Train-Test Split

The dataset is divided into:

* Training Data (80%)
* Testing Data (20%)

### Step 5: Model Training

A classification algorithm is trained using the training dataset.

Example algorithms:

* K-Nearest Neighbors (KNN)
* Decision Tree
* Logistic Regression

### Step 6: Prediction

The trained model predicts class labels for testing data.

### Step 7: Performance Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

---

## 📈 Results

The trained model successfully classifies unseen data and achieves a high accuracy score.

Performance Metrics:

* Accuracy Score
* Precision
* Recall
* F1 Score

Example Output:

```text
Accuracy: 96.67%

Classification Report:
Precision: 0.97
Recall: 0.96
F1-Score: 0.96
```

---

## 🚀 How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Data-Classification-Using-AI.git
```

### 2. Navigate to Project Folder

```bash
cd Data-Classification-Using-AI
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Program

```bash
python classification.py
```

---


## 🔍 Key Concepts Learned

* Artificial Intelligence
* Machine Learning
* Supervised Learning
* Data Classification
* Feature Engineering
* Model Training
* Model Evaluation
* Performance Metrics

---

## 💡 Future Improvements

* Add multiple classification algorithms.
* Compare model performance.
* Perform hyperparameter tuning.
* Deploy the model using Streamlit.
* Create a web-based prediction interface.

---

## 🏆 Internship Project

This project was completed as part of the **DecodeLabs Artificial Intelligence Internship Program** and demonstrates practical implementation of machine learning classification techniques.

---

## 👨‍💻 Author

**Saumya Thakur**

Artificial Intelligence Intern

Decode Labs Internship Program

Batch 2026

---

## 📜 License

This project is developed for educational and learning purposes.
