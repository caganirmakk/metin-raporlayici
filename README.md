# Metin Raporlayıcı (Python)

Bu proje, bir `.txt` dosyasını analiz ederek metinle ilgili çeşitli istatistikler üreten
başlangıç seviyesi bir Python uygulamasıdır.

## Özellikler
- Toplam kelime sayısını hesaplama
- En sık geçen 10 kelimeyi bulma
- Kelime uzunluklarına göre dağılım çıkarma
- Kullanıcının seçtiği bir kelimenin kaç kez geçtiğini hesaplama
- Tüm sonuçları `rapor.txt` dosyasına yazdırma

## Nasıl Çalışır?
1. Kullanıcıdan bir `.txt` dosya yolu alınır
2. Metin küçük harfe çevrilir ve noktalama işaretleri temizlenir
3. Tüm analizler tek seferde yapılır
4. Menü üzerinden istenen bilgiler ekrana yazdırılır
5. İstenirse tüm sonuçlar `rapor.txt` dosyasına kaydedilir

## Gereksinimler
- Python 3.x
- Harici kütüphane gerekmez

## Kullanım
```bash
python main.py
