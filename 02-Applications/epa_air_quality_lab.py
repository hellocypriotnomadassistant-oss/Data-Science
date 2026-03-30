import pandas as pd
import os

# --- 1. DOSYA YOLU KONTROLÜ ---
# Kodun çalıştığı klasörü bulalım
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

print(f"Şu an bu klasörde çalışıyorum: {current_dir}\n")

# --- 2. VERİ YÜKLEME (Task 1 & 6) ---
try:
    # İlk dosyayı yükle
    top3 = pd.read_csv('epa_ca_tx_pa.csv')
    print("✅ İlk dosya (top3) başarıyla yüklendi.")

    # İkinci dosyayı yükle
    other_states = pd.read_csv('epa_others.csv')
    print("✅ İkinci dosya (other_states) başarıyla yüklendi.\n")

    # --- 3. ANALİZ BAŞLIYOR (Task 2 & 3) ---
    print("--- Veri Özeti (Info) ---")
    top3.info()

    print("\n--- İstatistiksel Özet (Describe) ---")
    print(top3.describe())

    # --- 4. SIRALAMA VE FİLTRELEME (Task 3b & 4) ---
    # AQI değerine göre büyükten küçüğe sırala
    top3_sorted = top3.sort_values(by='aqi', ascending=False)
    
    # Sadece California verilerini ayır
    ca_df = top3_sorted[top3_sorted['state_name'] == 'California']
    
    # Los Angeles ortalama AQI hesapla
    la_mean = ca_df[ca_df['county_name'] == 'Los Angeles']['aqi'].mean()
    print(f"\n📍 Los Angeles Ortalama AQI: {la_mean:.2f}")

    # --- 5. BİRLEŞTİRME (Task 6b) ---
    # İki tabloyu alt alta ekle
    combined_df = pd.concat([top3, other_states], axis=0).reset_index(drop=True)
    print(f"\n✅ Birleştirme Tamamlandı. Toplam Satır Sayısı: {len(combined_df)}")

    # --- 6. KARMAŞIK FİLTRELEME (Task 7) ---
    # Washington eyaletinde AQI değeri 51 ve üzeri olanlar
    wa_moderate = combined_df[
        (combined_df['state_name'] == 'Washington') & 
        (combined_df['aqi'] >= 51)
    ]
    
    print("\n--- Washington Eyaleti Kritik Seviyeler (AQI >= 51) ---")
    print(wa_moderate if not wa_moderate.empty else "Kayıt bulunamadı.")

except FileNotFoundError as e:
    print(f"❌ HATA: Dosya bulunamadı! Lütfen CSV dosyalarının '.py' dosyasıyla aynı klasörde olduğundan emin ol.")
    print(f"Eksik olan dosya: {e.filename}")
except Exception as e:
    print(f"❌ Beklenmedik bir hata oluştu: {e}")