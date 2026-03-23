def degerlendir(puan):
    if puan < 0 or puan > 100:
        return "Geçersiz puan!"

    if puan >= 90:
        return "Harika! Başarılı oldun."
    elif puan >= 50:
        return "Geçtin ama daha iyi olabilir."
    else:
        return "Maalesef kaldın." 
def harf_notu(puan):
    if puan >= 90:
        return "A"
    elif puan >= 80:
        return "B"
    elif puan >= 70:
        return "C"
    elif puan >= 60:
        return "D"
    else:
        return "F"