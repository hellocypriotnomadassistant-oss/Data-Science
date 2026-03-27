from string_utils import format_price, format_user

# Fonksiyonları çağırıyoruz
sonuc1 = format_price(15.756)
sonuc2 = format_user("Ahmet", 5)

# Sonuçları ekrana yazdırıyoruz (Bu kısım çok önemli!)
print(sonuc1)
print(sonuc2)
from string_utils import format_price, format_user, clean_text, format_percentage

# Yeni araçları deneyelim
print(clean_text("   Hadi Bakalim   "))
print(format_percentage(0.856))