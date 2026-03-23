import karar_merkezi

while True:
    veri = input("Puan gir (q çıkış): ")

    if veri == "q":
        break

    try:
        puan = int(veri)

        yorum = karar_merkezi.degerlendir(puan)
        harf = karar_merkezi.harf_notu(puan)

        print("Harf Notu:", harf)
        print("Yorum:", yorum)

    except:
        print("Hatalı giriş!")