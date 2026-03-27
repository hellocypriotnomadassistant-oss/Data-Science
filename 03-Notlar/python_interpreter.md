# ⚙️ Python Yorumlayıcısını (Interpreter) Kullanmak

### 🔹 1. Python Nasıl Başlatılır?
* **Windows:** `python` veya `py`
* **Linux / Mac:** `python3`
* **Çıkış:** `quit()` veya `Ctrl + Z` (Windows) / `Ctrl + D` (Mac/Linux)

---

### 🔹 2. Çalıştırma Modları
1. **Interactive Mode (Etkileşimli):** `>>>` işareti görünür. Kodları tek tek yazıp anında sonuç alırsın.
2. **Script Mode:** `python dosya.py` komutuyla tüm dosyayı bir kerede çalıştırırsın.

---

### 🔹 3. Gelişmiş Çalıştırma Komutları
* **Tek Satır Kod:** `python -c "print(5+5)"`
* **Modül Çalıştırma:** `python -m modul_adi`
* **Dosya Sonrası Interactive Kalmak:** `python -i dosya.py` (Dosya biter ama terminal kapanmaz, değişkenleri inceleyebilirsin).

---

### 🔹 4. Argüman Gönderme (sys.argv) ⚠️
Dışarıdan dosyaya veri göndermek için kullanılır:
`python dosya.py veri1 veri2`

**Kod İçinde Erişimi:**
```python
import sys
print(sys.argv) # Çıktı: ['dosya.py', 'veri1', 'veri2']