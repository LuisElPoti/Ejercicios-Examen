# Ejercicio #4

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_and_preprocess_data(file_path):
    # Cargar los datos
    df = pd.read_csv(file_path)
    
    # Agrupar los datos por el ID del cliente
    grouped = df.groupby('customer_id')['tran_amount']
    
    # Calcular la frecuencia de compra, habitos de gasto y gasto máximo
    df['purchase_frequency'] = grouped.transform('count')
    df['spending_habit'] = grouped.transform('mean')
    df['max_spending'] = grouped.transform('max')
    
    # Normalizar los datos
    scaler = StandardScaler()
    df[['purchase_frequency', 'spending_habit', 'max_spending']] = scaler.fit_transform(df[['purchase_frequency', 'spending_habit', 'max_spending']])
    
    # Calcular el gasto total y definir las etiquetas de las clases
    df['total_spent'] = df['purchase_frequency'] * df['spending_habit']
    low_limit = df['total_spent'].quantile(0.33)
    high_limit = df['total_spent'].quantile(0.66)
    df['class_label'] = pd.cut(df['total_spent'], bins=[-float('inf'), low_limit, high_limit, float('inf')], labels=['low', 'medium', 'high'])
    
    # Codificar las etiquetas de las clases
    encoder = LabelEncoder()
    df['class_label'] = encoder.fit_transform(df['class_label'])
    
    return df, encoder

def split_data(df):
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X = df[['purchase_frequency', 'spending_habit', 'max_spending']].values
    y = to_categorical(df['class_label'])
    return train_test_split(X, y, test_size=0.2, random_state=42)

def build_model(input_dim, output_dim):
    # Construir el modelo de clasificación
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(output_dim, activation='softmax'))
    
    # Compilar el modelo
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def plot_confusion_matrix(y_test, y_pred):
    # Calcular la matrix de confusión
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test, axis=1)
    confusion_mtx = confusion_matrix(y_true, y_pred_classes)
    
    sns.heatmap(confusion_mtx, annot=True, fmt='d')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()

def main():
    # Cargar los datos
    file_path = 'data/data_customer_classification.csv'
    df, encoder = load_and_preprocess_data(file_path)
    print(df.head())
    
    # Save los datos procesados en un nuevo csv
    df.to_csv('data/data_customer_classification_processed.csv', index=False)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df)
    
    # Entrenar el modelo
    model = build_model(input_dim=X_train.shape[1], output_dim=y_train.shape[1])
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    
    # Evaluar el modelo
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test loss: {loss}, Test accuracy: {accuracy}')
    
    # Predict and plot the confusion matrix
    y_pred = model.predict(X_test)
    plot_confusion_matrix(y_test, y_pred)
    
    # Guardar el modelo
    model.save('customer_classification_model.h5')

if __name__ == '__main__':
    main()
