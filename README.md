# 🛡️ IPChanger from Wroserr (Tor IP Rotator)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇺🇸 English

**IPChanger** is a high-security Python automation tool designed to rotate your public IP address through the Tor network. Unlike basic scripts, it features a professional **Kill Switch** mechanism to ensure zero data leaks by forcing all outgoing traffic through the secure Tor tunnel.

### 🌟 Key Features
- **Automated Rotation:** Automatically requests a new Tor identity every 60 seconds.
- **Advanced Kill Switch:** Configures `iptables` to block any traffic that isn't routed through Tor.
- **Multilingual Support:** Interactive language selection (EN/TR) on startup.
- **Professional ASCII UI:** Clean, color-coded console interface.
- **Safe Exit:** Automatically restores system firewall settings upon termination (Ctrl+C).

### 🛠️ Installation & Usage

1. **Install Tor Service:**
   ```bash
   sudo apt update && sudo apt install tor -y
Configure Tor: Open /etc/tor/torrc and ensure these lines are active (uncommented):

Plaintext

ControlPort 9051
CookieAuthentication 1
Restart Tor: sudo service tor restart

Install Dependencies:

Bash

pip install requests stem
Run as Root:

Bash

sudo python3 ipchanger.py

Harika bir GitHub profili için README.md dosyasını hem profesyonel hem de kullanıcı dostu olacak şekilde, çift dilli (İngilizce - Türkçe) olarak hazırladım. Bu dosya, projenin ciddiyetini ve kalitesini yansıtacaktır.

Aşağıdaki metni kopyalayıp projenin ana dizinindeki README.md dosyasına yapıştırabilirsin:

Markdown

# 🛡️ IPChanger from Wroserr (Tor IP Rotator)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇺🇸 English

**IPChanger** is a high-security Python automation tool designed to rotate your public IP address through the Tor network. Unlike basic scripts, it features a professional **Kill Switch** mechanism to ensure zero data leaks by forcing all outgoing traffic through the secure Tor tunnel.

### 🌟 Key Features
- **Automated Rotation:** Automatically requests a new Tor identity every 60 seconds.
- **Advanced Kill Switch:** Configures `iptables` to block any traffic that isn't routed through Tor.
- **Multilingual Support:** Interactive language selection (EN/TR) on startup.
- **Professional ASCII UI:** Clean, color-coded console interface.
- **Safe Exit:** Automatically restores system firewall settings upon termination (Ctrl+C).

### 🛠️ Installation & Usage

1. **Install Tor Service:**
   ```bash
   sudo apt update && sudo apt install tor -y
Configure Tor: Open /etc/tor/torrc and ensure these lines are active (uncommented):

Plaintext

ControlPort 9051
CookieAuthentication 1
Restart Tor: sudo service tor restart

Install Dependencies:

Bash

pip install requests stem
Run as Root:

Bash

sudo python3 ipchanger.py
<a name="türkçe"></a>

🇹🇷 Türkçe
IPChanger, halka açık IP adresinizi Tor ağı üzerinden periyodik olarak değiştiren, yüksek güvenlikli bir Python otomasyon aracıdır. Sıradan scriptlerin aksine, profesyonel bir Kill Switch mekanizmasına sahiptir; bu sayede tüm trafiği Tor tüneline zorlayarak gerçek IP adresinizin sızmasını engeller.

🌟 Temel Özellikler
Otomatik Değişim: Her 60 saniyede bir otomatik olarak yeni bir Tor kimliği (IP) talep eder.

Gelişmiş Kill Switch: Tor dışındaki tüm internet trafiğini iptables ile engeller.

Çift Dil Desteği: Başlangıçta etkileşimli dil seçimi (EN/TR).

Profesyonel Arayüz: Renk kodlu ve temiz ASCII sanatı içeren konsol ekranı.

Güvenli Kapanış: Program durdurulduğunda (Ctrl+C) güvenlik duvarı ayarlarını otomatik olarak eski haline getirir.

🛠️ Kurulum ve Kullanım
Tor Servisini Kurun:

Bash

sudo apt update && sudo apt install tor -y
Tor Yapılandırması: /etc/tor/torrc dosyasını açın ve şu satırların aktif olduğundan emin olun:

Plaintext

ControlPort 9051
CookieAuthentication 1
Tor'u yeniden başlatın: sudo service tor restart

Bağımlılıkları Yükleyin:

Bash

pip install requests stem
Root Olarak Çalıştırın:

Bash

sudo python3 ipchanger.py

Türkçe Referans
🌟 Temel Özellikler
Dinamik IP Değişimi: Her 60 saniyede bir otomatik olarak yeni bir Tor devresi/kimliği talep eder.

Ağ Kill Switch: iptables kullanarak tüm sistem trafiğini Tor üzerinden geçmeye zorlar. Bağlantı koparsa gerçek IP sızıntısını önler.

Çift Dil Arayüzü: Başlangıçta İngilizce ve Türkçe arasında seçim yapma imkanı.

Profesyonel ASCII Banner: Yüksek görünürlüklü konsol arayüzü.

Güvenli Temizlik: Çıkışta sistem güvenlik duvarını (iptables) otomatik olarak varsayılan ayarlara döndürür.

🛠️ Kurulum ve Yapılandırma
Tor Servisini Kurun:

Bash

sudo apt update && sudo apt install tor -y
Kontrol Portunu Etkinleştirin: /etc/tor/torrc dosyasını düzenleyin ve şu satırları aktif edin:

Plaintext

ControlPort 9051
CookieAuthentication 1
Servisi Yeniden Başlatın: sudo service tor restart

Python Kütüphanelerini Kurun: pip install requests stem

🚀 Kullanım
Bash

sudo python3 ipchanger.py
⚖️ Legal Disclaimer / Yasal Uyarı
EN: This tool is provided for educational and ethical security testing purposes only. The author (Wroserr) is not responsible for any misuse, illegal activities, or damages caused by this program. Use it at your own risk and in compliance with local laws.

TR: Bu araç sadece eğitim ve etik güvenlik testi amaçları için sunulmuştur. Yapımcı (Wroserr), bu programın kötüye kullanımından, yasa dışı faaliyetlerden veya programın sebep olabileceği zararlardan sorumlu tutulamaz. Kullanım sorumluluğu tamamen kullanıcıya aittir ve yerel yasalarla uyumlu kullanılmalıdır.

Author / Yapımcı: Wroserr
