
import re
import subprocess
import ctypes
import sys

# DNS های ترجیحی و جایگزین
preferred_dns = "178.22.122.100"  # Preferred DNS
alternative_dns = "185.51.200.2"  # Alternative DNS

# تابع برای بررسی دسترسی به ادمین
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# تابع برای اجرای دستورات با دسترسی ادمین
def run_as_admin():
    if not is_admin():
        print("This script requires admin privileges.")
        print("Switching to adminstore...")
        # دستور اجرای دوباره اسکریپت با دسترسی ادمین
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

# تابع برای پیدا کردن اینترفیس فعال
def get_active_interface():
    # اجرای دستور netsh و دریافت خروجی
    output = subprocess.check_output(['netsh', 'interface', 'ip', 'show', 'config'])
    decoded_output = output.decode()

    # تقسیم خروجی به بخش‌های جداگانه برای هر اینترفیس
    interface_sections = re.split(r'Configuration for interface "([^"]+)"', decoded_output)

    interfaces = []

    # پیمایش در بخش‌های جداشده و جستجوی آدرس IP
    for i in range(1, len(interface_sections), 2):
        interface_name = interface_sections[i].strip()
        config = interface_sections[i+1]
        ip_match = re.search(r'IP Address:\s*([^\s]+)', config)
        if ip_match:
            ip_address = ip_match.group(1).strip()
            interfaces.append((interface_name, ip_address))

    # انتخاب اولین اینترفیس با IP معتبر به جز loopback
    for interface_name, ip_address in interfaces:
        if ip_address and ip_address != '127.0.0.1':
            return interface_name

    # اگر اینترفیس فعال یافت نشد، خطا می‌دهد
    raise Exception("No active network interface with a valid IP address found.")


# تابع برای بررسی DNS فعلی
def check_current_dns(interface_name):
    output = subprocess.check_output(['netsh', 'interface', 'ip', 'show', 'dns', interface_name])
    return output.decode()


# تابع برای تنظیم DNS ترجیحی و جایگزین
def set_dns(interface_name, preferred, alternative):
    subprocess.call(f'netsh interface ip set dns "{interface_name}" static {preferred}', shell=True)
    subprocess.call(f'netsh interface ip add dns "{interface_name}" {alternative} index=2', shell=True)

# تابع برای بازگرداندن DNS به حالت دیفالت
def reset_dns(interface_name):
    subprocess.call(f'netsh interface ip set dns "{interface_name}" dhcp', shell=True)

# بررسی و اجرای کد
def main():
    # اجرای دستورات با دسترسی ادمین
    run_as_admin()

    # پیدا کردن اینترفیس فعال
    interface_name = get_active_interface()

    # خواندن DNS فعلی برای اینترفیس پیدا شده
    current_dns_output = check_current_dns(interface_name)

    if preferred_dns in current_dns_output and alternative_dns in current_dns_output:
        print(f"Both {preferred_dns} and {alternative_dns} already exist. Resetting DNS to default on interface {interface_name}...")
        reset_dns(interface_name)
    else:
        print(f"Setting {preferred_dns} as Preferred DNS and {alternative_dns} as Alternative DNS on interface {interface_name}...")
        set_dns(interface_name, preferred_dns, alternative_dns)

# اجرای برنامه اصلی
if __name__ == "__main__":
    main()
