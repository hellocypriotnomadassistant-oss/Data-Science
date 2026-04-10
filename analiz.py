import pandas as pd

# Kılavuzdaki pd.read_csv fonksiyonunu kullanıyoruz
df = pd.read_csv('sirketler.csv')

# Verinin ilk halini ekrana basalım
print("--- Şirketler Veri Seti ---")
print(df)

# Sadece belirli bir sütunu görmek istersek:
print("\n--- Sadece Şirket İsimleri ---")
print(df['Sirket'])