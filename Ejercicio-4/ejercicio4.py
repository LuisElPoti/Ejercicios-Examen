import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Paso 1: Cargar y preprocesar los datos
data = pd.read_csv('data_customer_classification.csv')

# Ingeniería de características
# A. Conteo de transacciones por cliente (Shopping Frequency)
shopping_frequency = data['customer_id'].value_counts().reset_index()
shopping_frequency.columns = ['customer_id', 'shopping_frequency']

# B. Suma total de transacciones por cliente (Spending Habits)
spending_habits = data.groupby('customer_id')['tran_amount'].sum().reset_index()
spending_habits.columns = ['customer_id', 'spending_habits']

# C. Máximo monto de transacción por cliente (Maximum Amount Spent)
max_amount_spent = data.groupby('customer_id')['tran_amount'].max().reset_index()
max_amount_spent.columns = ['customer_id', 'max_amount_spent']

# Combina todas las características en un solo DataFrame
customer_data = shopping_frequency.merge(spending_habits, on='customer_id').merge(max_amount_spent, on='customer_id')

# Paso 2: Preparar características y etiquetas
X = customer_data[['shopping_frequency', 'spending_habits', 'max_amount_spent']]
y = customer_data['customer_id']  # No utilizamos esto para entrenar el modelo, ya que no es un problema de clasificación

# Paso 3: División de datos
X_train, X_test, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Construcción del modelo
model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))  # Capa oculta con 10 neuronas y función de activación ReLU
model.add(Dense(3, activation='softmax'))  # Capa de salida con 3 neuronas y función de activación softmax

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Paso 5: Entrenamiento del modelo
model.fit(X_train, X_train, epochs=100, batch_size=10)

# Paso 6: Evaluación del modelo
loss, accuracy = model.evaluate(X_test, X_test)
print(f'Accuracy: {accuracy}')
