# 🔒 Python Tuple (Demetler) Özet

### 🔹 1. Tuple Nedir?
Tuple, farklı veri türlerini tutabilen **değiştirilemez (immutable)** bir veri yapısıdır. Listelere benzer ancak oluşturulduktan sonra içeriği değiştirilemez.

### 🔑 En Kritik Özellikler
* **Değiştirilemezlik:** Eleman eklenemez, silinemez veya güncellenemez.
* **Sabit İndeks:** Veri yapısı daha güvenilir ve bellek açısından daha verimlidir.
* **Tanımlama:** Parantez `()` veya `tuple()` fonksiyonu ile oluşturulur.



### 🔄 2. Tuple Oluşturma ve Dönüştürme
```python
# Doğrudan tanımlama
isimler = ("Ali", "V", "Yılmaz")

# Listeyi Tuple'a çevirme
liste = ["Elma", "Armut"]
demet = tuple(liste)
fiyat_bilgisi = (6, 55)
dolar, sent = fiyat_bilgisi 
# Artık 'dolar' 6, 'sent' 55 değerine sahip bağımsız değişkenlerdir.
def koordinat_getir():
    return 40.7128, 74.0060  # Aslında bir tuple döner
    