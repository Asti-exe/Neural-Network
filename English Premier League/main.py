import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv("matches.csv")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data, data["winner"], test_size=0.2)

# Create the ANN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid") 
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(X_train, y_train, epochs=10)

# Evaluate the model on the test set
score = model.evaluate(X_test, y_test, verbose=0)
print("Test accuracy:", score[1])

# Predict the winner of the next season
next_season_data = pd.read_csv("matches.csv")
predictions = model.predict(next_season_data)

# The team with the highest probability of winning is the next season's champion
winner = predictions.argmax()
print("The next season's champion is:", next_season_data["Team"][winner])
