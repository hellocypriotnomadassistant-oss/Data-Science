# 🐍 Python Temel Kuralları ve Veri Tipleri

### 🔢 1. Sayı İşlemleri
* `17 / 3`  -> `5.66` (Normal bölme)
* `17 // 3` -> `5` (**Tam bölme** - küsuratı atar)
* `17 % 3`  -> `2` (**Mod** - kalanı verir)
* `2 ** 3`  -> `8` (**Üs alma**)

### 📝 2. String (Metin) Sihirleri
* **Kaçış:** `'it\'s'` -> Tek tırnak içinde tek tırnak kullanmak için `\` kullanılır.
* **Tekrar:** `3 * "ha"` -> `"hahaha"`
* **Değişmezlik (Immutable):** `word[0] = "J"` **HATA VERİR!** Stringler oluştuktan sonra değiştirilemez.

### ⚠️ 3. Listelerde Kopyalama Tuzağı
* `b = a` -> İkisi de aynı listeyi tutar. Birini değiştirirsen diğeri de değişir!
* `b = a[:]` -> Listenin gerçek bir kopyasını oluşturur. Güvenli yoldur.

### 🔄 4. Döngüler ve Girinti (Indentation)
Python'da süslü parantez `{}` yoktur, **girinti (4 boşluk)** vardır.
```python
while a < 10:
    print(a) # Bu satır içerde olduğu için döngüye aittir.
    >>> 2 + 2
4
>>> _ + 10
14
