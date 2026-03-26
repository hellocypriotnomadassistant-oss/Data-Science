import pandas as pd
import numpy as np

# 1. NumPy ile rastgele satış verileri üretelim
satislar = np.array([4500, 7800, 3200, 9100, 5600])

# 2. Pandas ile bu verileri bir tabloya (DataFrame) dönüştürelim
veri = {
    'Magaza_ID': ['M01', 'M02', 'M03', 'M04', 'M05'],
    'Gunluk_Satis': satislar,
    'Bolge': ['Kuzey', 'Guney', 'Kuzey', 'Bati', 'Dogu']
}

df = pd.DataFrame(veri)

# 3. Analiz: Satışı 5000'den fazla olan mağazaları filtrele
basarili_magazalar = df[df['Gunluk_Satis'] > 5000]

print("--- Tüm Mağaza Listesi ---")
print(df)
print("\n--- Hedefi Geçen Mağazalar ---")
print(basarili_magazalar)

# 4. Ortalama satışı NumPy ile hesapla
ortalama = np.mean(satislar)
print(f"\nTüm mağazaların satış ortalaması: {ortalama} TL")
