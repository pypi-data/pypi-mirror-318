import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

np.random.seed(123)  # New seed for better class separation
blue_crabs = np.random.normal([5.4, 3.1, 0.35], 0.4, (50, 3))
orange_crabs = np.random.normal([6.2, 3.6, 0.55], 0.4, (50, 3))
data = np.vstack((blue_crabs, orange_crabs))
labels = np.array([0] * 50 + [1] * 50)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model = MLPClassifier(
    hidden_layer_sizes=(8, 8),  
    activation='relu',
    solver='adam',
    learning_rate_init=0.01, 
    max_iter=1000,
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

new_crab = np.array([[5.9, 3.3, 0.5]])
prediction = model.predict(new_crab)
species = ["Blue", "Orange"]
print(f"The predicted species for the new crab is: {species[prediction[0]]}")
