def format_price(price):
    return f"Fiyat: {price:.2f} TL"

def format_user(name, number):
    return f"Merhaba {name}, numaran {number}"
import re # Dosyanın en üstüne eklemeyi unutma!

# Mevcut fonksiyonlarının altına bunları ekle:
def clean_text(text):
    """Metni temizler: boşlukları atar ve küçük harf yapar."""
    return text.strip().lower()

def has_pattern(text, pattern):
    """Metin içinde belirli bir desen (regex) var mı diye bakar."""
    return bool(re.search(pattern, text))

def format_percentage(value):
    """Sayiyi yüzde formatına çevirir (Örn: 0.25 -> %25.00)"""
    return f"{value:.2%}"