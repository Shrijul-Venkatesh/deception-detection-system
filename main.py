# main.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import torch
import torch.optim as optim
import torch.nn as nn
from audio_engine.model import create_model
import numpy as np

# Load the CSV file
data = pd.read_csv("mfcc_features.csv")

# Separate features and labels
X = data[["mfcc_1", "mfcc_2", "mfcc_3", "mfcc_4", "mfcc_5"]].values
y = data["label"].values

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32).reshape(-1, 1, 5)
X_test = torch.tensor(X_test, dtype=torch.float32).reshape(-1, 1, 5)
y_train = torch.tensor(y_train, dtype=torch.float32).reshape(-1, 1)
y_test = torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1)

# Create the model
model = create_model(input_size=5)

# Define loss function and optimizer
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.0005)

# Train the model
epochs = 20
for epoch in range(epochs):
    model.train()

    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Evaluate the model
model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    test_loss = criterion(test_outputs, y_test)
    accuracy = ((test_outputs > 0.5) == y_test).float().mean().item()
    print(f"Test Loss: {test_loss.item():.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")
