# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# ==========================================
# Load Dataset
# ==========================================

iris = load_iris()

X = iris.data
y = iris.target

print("\nDataset Loaded Successfully!")
print("Features Shape:", X.shape)
print("Target Shape:", y.shape)

# Convert to DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df["Species"] = y

print("\nFirst Five Records:")
print(df.head())

# ==========================================
# Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================================
# Feature Scaling
# ==========================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==========================================
# Train KNN Model
# ==========================================

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ==========================================
# Predictions
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# Accuracy
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(f"{accuracy * 100:.2f}%")

# ==========================================
# Classification Report
# ==========================================

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)

# ==========================================
# Confusion Matrix
# ==========================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# ==========================================
# Visualization
# ==========================================

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    cmap="Blues",
    fmt="d",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()

# ==========================================
# Sample Prediction
# ==========================================

sample = [[5.1, 3.5, 1.4, 0.2]]

sample_scaled = scaler.transform(sample)

prediction = model.predict(sample_scaled)

print("\nSample Prediction:")
print("Predicted Flower:", iris.target_names[prediction[0]])

print("\nProject Completed Successfully!")