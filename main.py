print("=" * 50)
print(" METİN RAPORLAYICIYA HOŞ GELDİN ")
print("=" * 50)
print("Bu program bir .txt dosyasını analiz eder ve")
print("kelime istatistiklerini raporlar.\n")

input("Devam etmek için ENTER'a bas...")
print("=" * 50)

# DOSYA OKUMA
while True:
    file_path = input("Dosya yolunu giriniz: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_read = file.read()
        break
    except Exception:
        print("Hata verdi. Dosya yolu yanlış.")

# TEMİZLEME
file_read = file_read.lower()
noktalama_isaretleri = ["…","!", "\"", "#", "$", "%", "&", "'", "(", ")", "*",
                        "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?",
                        "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

for a in noktalama_isaretleri:
    file_read = file_read.replace(a, '')

splitted_version = file_read.split()

# ANALİZLER
sum_of_words = len(splitted_version)

repeating_words = {}
for kelime in splitted_version:
    repeating_words[kelime] = repeating_words.get(kelime, 0) + 1

top_ten_words = dict(
    sorted(repeating_words.items(), key=lambda x: x[1], reverse=True)[:10]
)

word_length_dist = {}
for kelime in splitted_version:
    l = len(kelime)
    word_length_dist[l] = word_length_dist.get(l, 0) + 1

wanted_word = None

# MENÜ
while True:
    print("\n" + "=" * 50)
    print("1 - Toplam kelime sayısını gör")
    print("2 - En sık geçen 10 kelimeyi gör")
    print("3 - Kelime uzunluğu dağılımını gör")
    print("4 - İstediğin kelimenin kaç kez geçtiğini öğren")
    print("5 - Tüm sonuçları rapor.txt dosyasına yaz")
    print("0 - Çıkış")
    print("=" * 50)

    secim = input("Seçiminiz: ")

    if secim == "1":
        print(f"Toplam kelime sayısı: {sum_of_words}")

    elif secim == "2":
        for k, v in top_ten_words.items():
            print(f"{k} : {v}")

    elif secim == "3":
        for l in sorted(word_length_dist):
            print(f"{l} harfliler : {word_length_dist[l]}")

    elif secim == "4":
        wanted_word = input("Kelimeyi girin: ").lower()
        print(f"{wanted_word} : {repeating_words.get(wanted_word, 0)}")

    elif secim == "5":
        with open("rapor.txt", "w", encoding="utf-8") as rapor:
            rapor.write("METİN ANALİZ RAPORU\n")
            rapor.write("=" * 30 + "\n\n")
            rapor.write(f"Toplam kelime sayısı: {sum_of_words}\n\n")

            rapor.write("En sık geçen 10 kelime:\n")
            for k, v in top_ten_words.items():
                rapor.write(f"- {k} : {v}\n")

            rapor.write("\nKelime uzunluğu dağılımı:\n")
            for l in sorted(word_length_dist):
                rapor.write(f"- {l} harfliler : {word_length_dist[l]}\n")

            rapor.write("\nSorgulanan kelime:\n")
            if wanted_word:
                rapor.write(f"- {wanted_word} : {repeating_words.get(wanted_word, 0)}\n")
            else:
                rapor.write("- Sorgulanan kelime yok\n")

        print("Rapor yazıldı: rapor.txt")

    elif secim == "0":
        print("Çıkılıyor.")
        break

    else:
        print("Geçersiz seçim.")
