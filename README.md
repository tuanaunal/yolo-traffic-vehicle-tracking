# YOLOv8 ile Derin Öğrenme Tabanlı Trafik Akışı ve Nesne Takip Sistemi

Bu proje, bilgisayarlı görü (Computer Vision) ve derin öğrenme metotları kullanılarak video akışları üzerinde eş zamanlı araç tespiti ve kesintisiz nesne takibi (Object Tracking) gerçekleştirmek amacıyla geliştirilmiştir. Projede, nesne tespiti mimarisinin en güçlü modellerinden biri olan **YOLOv8 (You Only Look Once)** ve endüstri standardı takip algoritmalarından **ByteTrack** entegrasyonu kullanılmıştır.

---

## Projenin Amacı ve Teknik Altyapısı

Geleneksel nesne tespiti modelleri, videodaki her kareyi bağımsız birer fotoğraf gibi işler ve kareler değiştiğinde tespit edilen nesnenin geçmişini unutur. Bu projede ise nesnelerin zamansal sürekliliğini korumak amacıyla takip algoritmaları devreye alınmıştır.

### Kullanılan Teknolojiler ve Parametre Detayları

- **YOLOv8 Mimarisi (`yolov8n.pt`):** Projede hız ve doğruluk dengesini optimize etmek adına nano model tercih edilmiştir. Model, trafikteki nesneleri saniyeler içinde sınıflandırabilir.
- **ByteTrack Algoritması (`tracker="bytetrack.yaml"`):** Düşük güven skoruna sahip (örneğin gölgede kalan veya önü kısmen kapanan) araçları bile takip kaybı yaşamadan izleyebilen, hareket tahmini tabanlı gelişmiş bir takip algoritmasıdır.
- **Veri Koruma (`persist=True`):** Araçların video kareleri arasında yer değiştirirken benzersiz kimliklerini (ID) kaybetmesini engeller. Bu sayede her araca kalıcı birer ID atanır.
- **Filtreleme (`classes=[2]`):** COCO veri setindeki yüzlerce nesne arasından sadece "car" (otomobil) sınıfı izole edilerek modelin gereksiz hesaplama yapması önlenmiş ve performansı artırılmıştır.
- **Güven ve Örtüşme Eşikleri (`conf=0.3`, `iou=0.5`):** Yanlış tespitleri (false positive) engellemek adına minimum %30 güven skoru aranmış; üst üste binen araç kutularının doğru ayrıştırılması için %50 örtüşme oranı belirlenmiştir.

---

## Kurulum ve Yayına Alma

Projeyi yerel bilgisayarınızda test etmek, sanal ortamı izole etmek ve bağımlılıkları tek seferde kurmak için aşağıdaki komut bloğunu terminalinize sırayla yapıştırabilirsiniz:

```bash
# 1. Depoyu klonlayın ve proje dizinine geçiş yapın
git clone [https://github.com/tuanaunal/yolo-traffic-vehicle-tracking.git](https://github.com/tuanaunal/yolo-traffic-vehicle-tracking.git)
cd yolo-traffic-vehicle-tracking

# 2. Sanal ortamı (venv) oluşturun ve aktif hale getirin
python -m venv venv
.\venv\Scripts\activate

# 3. Gerekli kütüphaneleri yükleyin ve projeyi başlatın
pip install ultralytics opencv-python
python main.py

├── main.py              # YOLOv8 modelinin yüklendiği, OpenCV kare döngüsünün ve takip algoritmasının çalıştığı ana kod dosyası.
├── requirements.txt     # Projenin bağımlı olduğu harici Python paketlerinin listesi.
├── .gitignore          # Büyük boyutlu video veri setlerinin (.MOV, .mp4) GitHub sınırlarına takılmaması için Git takibinden muaf tutulduğu dosya.
└── README.md            # Projenin tüm mühendislik detaylarını ve kullanım kılavuzunu barındıran teknik dokümantasyon.
```
