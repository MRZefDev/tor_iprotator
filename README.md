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

⚖️ Legal Disclaimer / Yasal Uyarı
EN: This tool is provided for educational and ethical security testing purposes only. The author (Wroserr) is not responsible for any misuse, illegal activities, or damages caused by this program. Use it at your own risk and in compliance with local laws.

TR: Bu araç sadece eğitim ve etik güvenlik testi amaçları için sunulmuştur. Yapımcı (Wroserr), bu programın kötüye kullanımından, yasa dışı faaliyetlerden veya programın sebep olabileceği zararlardan sorumlu tutulamaz. Kullanım sorumluluğu tamamen kullanıcıya aittir ve yerel yasalarla uyumlu kullanılmalıdır.
