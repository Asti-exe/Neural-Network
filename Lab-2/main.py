import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
def build_feedforward_model(input_nodes, hidden_nodes, output_nodes):
    model = Sequential()
    
    model.add(Dense(hidden_nodes, input_dim=input_nodes, activation='relu'))
    
    model.add(Dense(hidden_nodes, activation='relu'))
    
    model.add(Dense(output_nodes, activation='softmax'))

    return model
input_nodes = 10
hidden_nodes = 32
output_nodes = 3

model = build_feedforward_model(input_nodes, hidden_nodes, output_nodes)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
