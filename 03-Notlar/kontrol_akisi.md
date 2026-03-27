# 🚦 Python Kontrol Akışı (Control Flow) Özet

### 🧠 1. Karar Yapıları (if / elif / else)
Python'da koşullar `if` ile başlar, `elif` (else if) ile devam eder ve `else` ile sonlanır.
* **Önemli:** Girinti (4 boşluk) hayati önem taşır.

### 🔁 2. Döngüler (for & while)
* **for:** Bir liste veya string üzerinde döner.
* **range(5):** 0'dan 4'e kadar sayı üretir (5 dahil değil!).
* **break:** Döngüyü tamamen kırar.
* **continue:** Mevcut adımı atlar, sonrakine geçer.



[Image of Python for loop flowchart]


### 🔄 3. Döngülerde `else` Kullanımı
Eğer bir döngü `break` ile **kesilmeden** normal şekilde biterse `else` bloğu çalışır. 
> "Hiç break olmadıysa bunu yap" demektir.

### 🔧 4. Fonksiyonlar (def)
Fonksiyonlar `def` ile tanımlanır.
* **return:** Değer döndürür. Yazılmazsa fonksiyon `None` döndürür.
* **args & kwargs:** * `*args`: Sınırsız isimsiz argüman (Tuple).
    * `**kwargs`: Sınırsız isimli argüman (Sözlük).

### ⚠️ 5. Kritik Hata Tuzağı (Mutable Default Arguments)
Fonksiyon tanımlarken varsayılan değer olarak boş liste `[]` kullanma! Liste bir kez oluşturulur ve her çağrıda şişer.
* **Doğru Yol:** `L=None` kullan ve fonksiyon içinde `if L is None: L = []` de.

### ⚡ 6. Lambda ve Unpacking
* **Lambda:** `add = lambda x, y: x + y` (Tek satırlık fonksiyon).
* **Unpacking:** Listeyi `*` ile, sözlüğü `**` ile parçalayarak fonksiyona gönderme.

---

### 🎨 7. Kodlama Stili (PEP 8)
1. 4 boşluk girinti.
2. Fonksiyonlar için `yilan_hikayesi` (snake_case).
3. Sınıflar için `DeveHorgucu` (CamelCase).
4. Satır uzunluğu max 79 karakter.
