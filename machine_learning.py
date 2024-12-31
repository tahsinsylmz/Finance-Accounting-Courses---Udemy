from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd

# İşlenmiş veri setini yükleyin
df = pd.read_csv("preprocessed_data.csv")

# IsolationForest Modeli
model_if = IsolationForest()
model_if.fit(df[['discount_price__amount', 'num_subscribers']])
df['anomaly'] = model_if.predict(df[['discount_price__amount', 'num_subscribers']])
df['anomaly_label'] = df['anomaly'].apply(lambda x: 'Normal' if x == 1 else 'Anomaly')
print(df[['discount_price__amount', 'num_subscribers', 'anomaly_label']].head())

# Derin Öğrenme Modeli
X = df[['discount_price__amount', 'num_subscribers']]
y = df[['discount_price__amount', 'num_subscribers']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_dl = Sequential([
    Dense(64, input_dim=2, activation='relu'),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(2, activation='sigmoid')
])
model_dl.compile(optimizer='adam', loss='mse')
model_dl.fit(X_train, y_train, epochs=10)

loss = model_dl.evaluate(X_test, y_test)
print(f"Test kaybı: {loss}")
