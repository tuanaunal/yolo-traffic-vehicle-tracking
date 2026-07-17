"""
araclarin takibi: yolo kullanalim, training yapmayalim zaten yolo default olarak araclarin tespitini yapabiliyor.

veri seti: https://www.kaggle.com/datasets/benjaminguerrieri/car-detection-videos?select=IMG_5270.MOV
"""

import cv2
from ultralytics import YOLO

# veri seti incele

# yolo modeli yukle
model = YOLO("yolov8n.pt") # yolov8s, m, l da kullanabilirsiniz

# video giris kaynagi alalim
video_path = "IMG_5268.MOV"
cap = cv2.VideoCapture(video_path)

# cikis videosunu yazma icin ayar
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) # frame per second, 1 saniyeki kare sayisi
out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (width, heigth))

while cap.isOpened(): # video bitene kadar devam et, video = 100 x kare
    success, frame = cap.read() # bir kare oku
    if not success: # video bittiyse = okuma basarisiz while dongusunden cik
        break

    # yolo ile tracking
    results = model.track(
        frame, # giris goruntusu
        persist=True, # takip id lerinin ayni nesne icin korunmasini saglar
        conf=0.3, # guven skoru 0-1 arasinda degisir, 1 mukemmel, 0 kotu,
        iou=0.5, # iou intersection over union: nesne kutularinin ne kadar ortusmesi gerektigi
        tracker="bytetrack.yaml", # takip algoritmasi konfigurasyonu byte track
        classes=[2] # sadece car lara
    )

    # kutulari ve id leri ekran uzerine cizdir
    annotated_frame = results[0].plot() # yolo sonuclarini kutular ve id lerle cizilmesi

    # goster ve kaydet
    cv2.imshow("YOLO v8 Tracking", annotated_frame) # annotated goruntuyu ekranda goster
    out.write(annotated_frame) # annotated goruntuyu cikti olarak video kaydet

    if cv2.waitKey(1) & 0xFF == ord("q"): # q harfine basinca ciksin
        break

cap.release() # video kaynagini kapat
out.release() # video yazicisini kapat
cv2.destroyAllWindows() # acik tum pencereleri kapat