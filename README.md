# Finance-Accounting-Courses---Udemy

# ✨ Gerçek Zamanlı Büyük Veri Analitiği ile Anomali Tespiti: Spark ve Kafka Entegrasyonu ✨

Bu proje, Udemy'deki finans ve muhasebe kursları veri seti üzerinde Spark ve Kafka teknolojilerini kullanarak anomali tespiti gerçekleştirmeyi amaçlamaktadır. Projede makine öğrenimi ve derin öğrenme teknikleri uygulanmış, TensorFlow tabanlı yapay sinir ağları (ANN) kullanılmıştır. ✨

## 🌐 Proje Amaçları
- **Finans ve muhasebe kurslarının derecelendirmelerinin tahmini.**
- **Spark ve Kafka entegrasyonu ile gerçek zamanlı veri analizi.**
- **Anomali tespiti için makine öğrenimi ve derin öğrenme modellerinin kullanılması.**

---

## ⚖️ Veri Seti 
Kullanılan veri seti, Udemy platformundaki finans ve muhasebe kurslarıyla ilgili çeşitli bilgileri içermektedir:

- **Kurs Sayısı**: 13,000+ 📊
- **Özellikler**: Kurs fiyatları, abone sayıları, derecelendirmeler, yorum sayıları, vb.
- **Kaynak**: [Kaggle Veri Seti](https://www.kaggle.com/datasets/jilkothari/finance-accounting-courses-udemy-13k-course)

---

## ⚙️ Kullanılan Teknolojiler
- **Apache Kafka**: Gerçek zamanlı veri akışı için.
- **Apache Spark**: Veri işleme ve streaming.
- **Python**: Veri işleme ve modelleme.
- **TensorFlow**: Yapay sinir ağı modelleri.

---

## 🚀 Kurulum
Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin:

### Gerekli Bağlımlıkları Yükleme

1. Proje dosyasını klonlayın:
```bash
$ git clone https://github.com/kullaniciadi/proje-adi.git
$ cd proje-adi
```

2. Sanal bir ortam oluşturun ve bağlımlıkları yükleyin:
```bash
$ python -m venv .venv
$ source .venv/bin/activate  # Windows için: .venv\Scripts\activate
$ pip install -r requirements.txt
```

3. Spark ve Kafka kurulumu için aşağıdaki dokümanlara göz atın:
   - [Kafka Kurulum Rehberi](https://kafka.apache.org/quickstart)
   - [Spark Kurulum Rehberi](https://spark.apache.org/docs/latest/)  

---

## 🔧 Proje Adımları

### 1. Veri Ön İşleme
- Eksik değerlerin doldurulması ve normalizasyonu.
- Aykırı değerlerin temizlenmesi.
- OneHotEncoder kullanılarak kategorik değişkenlerin dönüştürülmesi.

### 2. Veri Analizi ve Görselleştirme
- Korelasyon matrisi, scatter plot ve histogramların oluşturulması.

### 3. Model Geliştirme
- **Isolation Forest** kullanılarak anomali tespiti.
- TensorFlow ANN modeli ile tahmin yapılması.

### 4. Kafka ve Spark Entegrasyonu
- Kafka Producer ile veri akışı sağlanması.
- Spark Streaming kullanarak gerçek zamanlı anomali tespiti.

---

## 📊 Model Performansı

- **Eğitim Seti R-Square**: 0.89 ✅
- **Test Seti R-Square**: 0.85 ✅

---

## 🔍 Kod Örnekleri

### Veri Yükleme
```python
import pandas as pd

data = pd.read_csv('udemy_finance.csv')
print(data.head())
```

### Veri Ön İşleme
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data[['price', 'num_subscribers']] = scaler.fit_transform(data[['price', 'num_subscribers']])
```

### ANN Modeli
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_dim=2),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
```

---

## 🎡 Ekran Görüntüleri

**Heatmap Görseli:** Korelasyon matrisi ile veri setindeki özelliklerin ilişkisi.

![Heatmap](link-to-heatmap.png)

**Model Performans Grafiği:** Modelin eğitim ve test verisi üzerindeki performansı.

![Model Performance](link-to-performance.png)

---

## 🙌 Katkıda Bulunun

Katkılarınızı bekliyoruz! Bu projeye katkıda bulunmak için:
1. Bu projeyi forklayın.
2. Yeni bir branch oluşturun.
3. İşinizi taahhüt edin.
4. Pull request gönderin.

---

