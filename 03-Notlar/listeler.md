# 📌 Python Listeler – Özet

### 🔹 1. Listeler Değiştirilebilir (Mutable)
Listeler değiştirilebilir veri tipidir. Eleman ekleyebilir, silebilir veya değiştirebilirsin.
👉 **Aynı liste kalır, sadece içeriği değişir.**

---

### 🔹 2. Eleman Ekleme
* **append():** Listenin sonuna ekler. 
    `meyveler.append("kiwi")`
* **insert():** Belirli bir indekse ekler. 
    `meyveler.insert(1, "orange")` (İndeks ve değer alır)

---

### 🔹 3. Eleman Silme
* **remove():** Değere göre siler. `meyveler.remove("banana")`
* **pop():** İndekse göre siler. `meyveler.pop(2)`

---

### 🔹 4. Eleman Değiştirme
`meyveler[1] = "mango"`
✔ Direkt indeks üzerinden yeni değer atanır.

---

### 🔹 5. String vs List (Önemli ⚠️)
* ❌ **String (Immutable):** `isim[0] = "V"` -> **HATA!**
* ✅ **List (Mutable):** `liste[0] = "V"` -> **ÇALIŞIR.**

---

### 🚀 Kısa Ezber
* **append()** -> sona
* **insert()** -> araya
* **remove()** -> isme göre sil
* **pop()** -> sıraya (index) göre sil
### 🔹 6. Dilimleme (Slicing)
`liste[başlangıç:bitiş]` -> Bitiş indeksi dahil değildir!
* `meyveler[0:2]` -> 0 ve 1. indeksi getirir.
* `meyveler[:3]` -> Baştan başla 3. indekse kadar git.

### 🔹 7. Liste Matematik İşlemleri
* **Toplama (+):** İki listeyi birleştirir. `[1,2] + [3,4]` -> `[1,2,3,4]`
* **Çarpma (*):** Listeyi tekrarlar. `['a'] * 3` -> `['a', 'a', 'a']`

### 🔹 8. Diğer Önemli Metotlar
* **in:** Eleman listede mi? `"elma" in meyveler` -> `True/False`
* **count():** Eleman kaç kez geçiyor? `liste.count("elma")`
* **sort():** Listeyi alfabetik veya küçükten büyüğe sıralar.
* **clear():** Listenin içini tamamen boşaltır.