import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

dataset = fetch_ucirepo(id=45)

print("Dataset Details:")
print(f"Name: {dataset.name}")
print(f"Description: {dataset.description}")
print(f"Number of features: {dataset.data.features.shape[1]}")
print(f"Number of samples: {dataset.data.features.shape[0]}")
print(f"Target Classes: {dataset.data.target_names}")

feature_names = dataset.data.features.columns
print(f"\nFeature Names: {list(feature_names)}\n")

X = dataset.data.features
y = dataset.data.targets.to_numpy().ravel() 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=1)  # Handle undefined precision
recall = recall_score(y_test, y_pred, average='weighted', zero_division=1)  # Handle undefined recall

print(f"\nAccuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nActual vs Predicted:")
print(results_df.head())
