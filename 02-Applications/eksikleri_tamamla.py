import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Veriyi Oku
df = pd.read_csv("yeni_veriler.csv")

# 2. SET ile Benzersiz Ürünleri Gör (Eksiğin olan Set kullanımı)
benzersizler = set(df['urun'])
print(f"Benzersiz Ürünler Kümesi: {benzersizler}")

# 3. LIST COMPREHENSION ile İsimleri Düzenle (Eksiğin olan List Comp.)
df['urun'] = [u.upper() for u in df['urun']]

# 4. NUMPY ile Hesaplama
df['toplam'] = df['miktar'] * df['fiyat']

# 5. PANDAS ile Gruplama
ozet = df.groupby('urun')['toplam'].sum()
print("\n--- Satış Özeti ---")
print(ozet)

# 6. MATPLOTLIB ile Görselleştirme (Final Dokunuşu)
ozet.plot(kind='bar', color='orange')
plt.title("Ürün Bazlı Kazanç Raporu")
plt.show()

    