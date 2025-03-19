
### **EyeOnU - Gerçek Zamanlı Nesne Algılama ve Bildirim Sistemi**

**Geliştirici:** Kemal Burak YILDIRIM  
**GitHub:** [Ultrareflex8672](https://github.com/Ultrareflex8672)  
**E-Posta:** ultrareflex@ultrareflex.com  
**Proje Adresi:** [EyeOnU GitHub](https://github.com/Ultrareflex8672/EyeOnU)

----------

### **📌 EyeOnU Nedir?**

EyeOnU, **PyQt5** ile geliştirilmiş, kamera görüntüsünü analiz ederek belirli nesneleri **gerçek zamanlı** olarak algılayıp verilen bir **URL’ye bildirim gönderen** bir sistemdir. Kullanıcı dostu bir arayüze sahip olan EyeOnU, **olay kayıtlarını** hem arayüzde liste halinde gösterir hem de bir **log dosyasında** saklar.

----------

### **🚀 Özellikler**

✅ **Gerçek Zamanlı Nesne Algılama:** Kamera görüntüsünden belirlenen nesneleri anında tespit eder.  
✅ **Bildirim Gönderme:** Algılanan nesneler, belirlenen **URL’ye** anlık olarak gönderilir. Örnek format:


```URL?nesne=&id=&zaman=&tel=&email=&sparam=```

✅ **FPS Ayarlanabilirliği:** Algılama hızını **kare/saniye (FPS)** olarak ayarlama imkanı sunar.  
✅ **Olay Kayıt Sistemi:** Algılanan tüm nesneleri arayüzde **liste halinde görüntüler**.  
✅ **Log Kaydı:** Tüm olaylar bir **log dosyasına** kaydedilir.  
✅ **Basit ve Kullanışlı Arayüz:** **PyQt5** ile tasarlanmış, anlaşılır ve sade bir kullanıcı deneyimi sunar.  
✅ **Kalıcı Ayarlar:** Bildirim ve FPS gibi ayarlar hafızada tutulur ve kapanıp açıldığında korunur.

----------

### **🎯 Algılanabilen Nesneler**

EyeOnU, geniş bir nesne yelpazesini tanıyabilir:

**🚗 Taşıtlar:**

-   Bisiklet, Araba, Motosiklet, Uçak, Otobüs, Tren, Kamyon, Tekne

**🚦 Trafik Nesneleri:**

-   Trafik Lambası, Yangın Musluğu, Dur Tabelası, Parkmetre

**🐾 Hayvanlar:**

-   Kuş, Kedi, Köpek, At, Koyun, İnek, Fil, Ayı, Zebra, Zürafa

**🎒 Kişisel Eşyalar:**

-   Sırt Çantası, Şemsiye, El Çantası, Kravat, Valiz

**🏀 Spor ve Eğlence:**

-   Frizbi, Kayak, Kar Kayağı, Spor Topu, Uçurtma, Beyzbol Sopası, Beyzbol Eldiveni, Kaykay, Sörf Tahtası, Tenis Raketi

**🍽️ Mutfak Eşyaları:**

-   Şişe, Şarap Kadehi, Bardak, Çatal, Bıçak, Kaşık, Kase

**🍔 Gıdalar:**

-   Muz, Elma, Sandviç, Portakal, Brokoli, Havuç, Sosisli Sandviç, Pizza, Donut, Pasta

**🛋️ Ev ve Ofis Eşyaları:**

-   Sandalye, Kanepe, Saksı Bitkisi, Yatak, Yemek Masası, Tuvalet, Televizyon, Dizüstü Bilgisayar, Fare, Uzaktan Kumanda, Klavye, Cep Telefonu, Mikrodalga Fırın, Fırın, Tost Makinesi, Lavabo, Buzdolabı

**📚 Diğer Nesneler:**

-   Kitap, Saat, Vazo, Makas, Oyuncak Ayı, Saç Kurutma Makinesi, Diş Fırçası

----------

### **💻 Kurulum & Kullanım**

1.  **Gerekli bağımlılıkları yükleyin:**
    
    ```pip install -r requirements.txt``` 
    
2.  **Uygulamayı başlatın:**
    
    ```python eyeonu.py```
    
3.  **Kamera bağlantısını yapın ve nesne algılamayı başlatın.**
4.  **Algılanan nesneler belirlenen URL’ye anlık olarak bildirilir.**

----------

### **📜 Lisans ve Katkı**

Bu proje açık kaynaklıdır ve GitHub üzerinden katkıda bulunabilirsiniz!

🔗 **[GitHub Proje Sayfası](https://github.com/Ultrareflex8672/EyeOnU)**

🚀 **EyeOnU ile güvenliği ve nesne algılamayı bir üst seviyeye taşıyın!**