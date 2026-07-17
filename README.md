# YOLO ile Trafik Akışı ve Araç Takip Sistemi (YOLO Traffic & Vehicle Tracking)

Bu proje, derin öğrenme tabanlı **YOLO (You Only Look Once)** modelini kullanarak video akışları üzerinde gerçek zamanlı araç tespiti, sınıflandırması ve nesne takibi (tracking) gerçekleştirmek amacıyla geliştirilmektedir.

## Proje Özellikleri (Planlanan)

- **Araç Tespiti ve Sınıflandırma:** Trafikteki otomobil, otobüs, kamyon ve motosiklet gibi araçların YOLO modeliyle yüksek doğrulukla tespiti.
- **Nesne Takibi (Object Tracking):** Tespit edilen araçların video kareleri boyunca benzersiz ID'ler ile takip edilmesi.
- **Hız ve Yoğunluk Analizi:** Belirli hatları geçen araçların sayımı ve trafik yoğunluğu haritalandırması.

## Kurulum ve Çalıştırma

Aşağıdaki komut bloğunu terminalinize sırayla yapıştırarak projeyi hızlıca ayağa kaldırabilirsiniz:

```bash
git clone [https://github.com/tuanaunal/yolo-traffic-vehicle-tracking.git](https://github.com/tuanaunal/yolo-traffic-vehicle-tracking.git)
cd yolo-traffic-vehicle-tracking
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

Dosya
├── main.py              # Projenin ana yürütme ve video işleme kodu
├── requirements.txt     # Gerekli kütüphaneler ve bağımlılıklar
├── .gitignore          # Git tarafından takip edilmeyecek dosyalar
└── README.md            # Proje açıklama dokümanı
```
