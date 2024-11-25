import os

# Hosts dosyasını düzenleyerek Google engelini kaldır
def unblock_hosts():
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
    GOOGLE_DOMAINS = [
        "www.google.com",
        "google.com",
        "www.google.co.uk",
        "www.google.co.in",
        "www.google.ca",
        "www.google.com.au",
        "www.google.com.tr",
        "google.co.uk",
        "google.co.in",
        "google.ca",
        "google.com.au",
        "google.com.tr",
    ]

    try:
        with open(HOSTS_PATH, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(domain in line for domain in GOOGLE_DOMAINS):
                    file.write(line)
            file.truncate()
        print("Hosts dosyasındaki Google engellemeleri kaldırıldı.")
    except PermissionError:
        print("Hata: Bu işlemi gerçekleştirmek için yönetici izni gerekiyor.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Güvenlik duvarındaki Google engelini kaldır
def unblock_firewall():
    try:
        os.system('netsh advfirewall firewall delete rule name="Block Google 8.8.8.8"')
        os.system('netsh advfirewall firewall delete rule name="Block Google 8.8.4.4"')
        os.system('netsh advfirewall firewall delete rule name="Block Google 142.250.0.0/15"')
        print("Güvenlik duvarındaki Google engellemeleri kaldırıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    print("Google erişimini engelleyen tüm işlemler kaldırılıyor...")
    unblock_hosts()
    unblock_firewall()
    print("Tüm engellemeler başarıyla kaldırıldı.")
