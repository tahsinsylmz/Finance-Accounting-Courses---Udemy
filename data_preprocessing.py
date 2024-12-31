import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Veri setini yükleyin
df = pd.read_csv("udemy_finance.csv")  # Veri setinizin dosya adını buraya yazın

# Eksik değerleri kontrol edin ve doldurun
print("Eksik değerlerin sütunlara göre sayısı:")
print(df.isnull().sum())
df.fillna(method='ffill', inplace=True)  # Eksik değerleri bir önceki satırla doldurun

# Sütun adlarını kontrol edin
print("Veri setindeki sütunlar:")
print(df.columns)

# Gerekli sütunları ölçeklendirin
scaler = StandardScaler()
if 'discount_price__amount' in df.columns and 'num_subscribers' in df.columns:
    df[['discount_price__amount', 'num_subscribers']] = scaler.fit_transform(
        df[['discount_price__amount', 'num_subscribers']]
    )
    print("Sütunlar başarıyla normalize edildi.")
else:
    print("Beklenen sütunlar bulunamadı, kontrol edin.")

# Kategorik bir sütunu OneHotEncoder ile encode edin (örnek: 'is_paid')
if 'is_paid' in df.columns:
    encoder = OneHotEncoder()
    encoded_columns = encoder.fit_transform(df[['is_paid']])
    encoded_df = pd.DataFrame(encoded_columns.toarray(), columns=encoder.get_feature_names_out(['is_paid']))
    df = pd.concat([df, encoded_df], axis=1)
    print("Kategorik sütun başarıyla encode edildi.")
else:
    print("Kategorik sütun bulunamadı.")

# Aykırı değerleri tespit edin ve kaldırın (örnek: 'discount_price__amount' sütunu için)
if 'discount_price__amount' in df.columns:
    z_scores = np.abs(
        (df['discount_price__amount'] - df['discount_price__amount'].mean()) / df['discount_price__amount'].std()
    )
    df = df[z_scores < 3]  # Z-Score > 3 olanları kaldırın
    print(f"Aykırı değerler kaldırıldı. Kalan satır sayısı: {len(df)}")

# Yalnızca sayısal sütunları seçin
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Korelasyon matrisini çizdirin
if not numeric_df.empty:
    print("Korelasyon matrisi:")
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.show()
else:
    print("Sayısal sütunlar bulunamadığı için korelasyon matrisi oluşturulamadı.")

# İşlemi doğrulamak için ilk birkaç satırı yazdırın
print("Ön işleme sonrası ilk 5 satır:")
print(df.head())

# Veri işleme sonucunu kaydedin
df.to_csv("preprocessed_data.csv", index=False)
print("Veri işleme tamamlandı ve preprocessed_data.csv dosyasına kaydedildi.")
