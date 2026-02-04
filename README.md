# Metin Raporlayıcı (Python)

Bu proje, bir `.txt` dosyasını analiz ederek metinle ilgili çeşitli istatistikler üreten başlangıç–orta seviye bir Python uygulamasıdır.

---

## Özellikler

- Toplam kelime sayısını hesaplar  
- En sık geçen 10 kelimeyi bulur  
- Kelime uzunluklarına göre dağılım çıkarır  
- Kullanıcının seçtiği bir kelimenin kaç kez geçtiğini hesaplar  
- İstenirse tüm sonuçları `rapor.txt` dosyasına yazar  

---

## Nasıl Çalışır?

1. Kullanıcıdan bir `.txt` dosya yolu alınır  
2. Metin küçük harfe çevrilir ve noktalama işaretleri temizlenir  
3. Tüm analizler tek seferde yapılır  
4. Kullanıcıya numaralı bir menü sunulur  
5. Menü üzerinden seçilen bilgiler ekrana yazdırılır  
6. İstenirse tüm sonuçlar `rapor.txt` dosyasına kaydedilir  

---

## Örnek Çıktı

```text
Metinde geçen kelime sayısı = 1245
En çok tekrar eden 10 kelime = ['ve', 'bir', 'bu', 'için', 'olarak']
Kelime uzunluğu dağılımı = {1 harfliler: 12, 2 harfliler: 45, 3 harfliler: 210, 4 harfliler: 330, 5 harfliler: 198}
Seçilen kelimenin tekrar sayısı = 18
```
Gereksinimler
```text 
Python 3.x

Harici kütüphane gerekmez
```
Kullanım
```text
python main.py
Program çalıştığında sizden bir .txt dosya yolu ister ve ardından menü üzerinden seçim yapmanızı bekler.
```
