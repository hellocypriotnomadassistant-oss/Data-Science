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
