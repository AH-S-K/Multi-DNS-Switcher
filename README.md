# Multi-DNS-Switcher 🌐

**Multi-DNS-Switcher** is a collection of Python scripts designed to automatically switch between different sets of preferred and alternative DNS addresses on Windows, requiring administrative privileges to ensure proper configuration.

## ✨ Features
- <span style="font-weight: bold;">Multiple DNS Configurations:</span> Easily switch between different DNS setups with dedicated scripts.
- <span style="font-weight: bold;">Admin Privileges:</span> Automatically requests administrative access to modify network settings.
- <span style="font-weight: bold;">Active Interface Detection:</span> Identifies the active network interface for DNS changes.
- <span style="font-weight: bold;">Reset to Default:</span> Resets DNS to default (DHCP) if the specified DNS addresses are already set.

## 📁 Directory Structure
- **`dns_scripts/`**: Contains Python scripts for different DNS configurations. Each script is used to set a specific DNS configuration.
- **`bat_files/`**: Contains `.bat` files for each DNS configuration that runs the corresponding Python script with admin privileges.

## 🚀 How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/AH-S-K/Multi-DNS-Switcher.git
    ```
2. Go to the `bat_files` folder and choose the appropriate `.bat` file for your desired DNS configuration.
3. Double-click the `.bat` file to execute the script with admin privileges.

> **Note:** Make sure you run the batch files with administrator privileges to ensure DNS changes are applied successfully.

## 📝 Available DNS Configurations
| **Configuration** | **Preferred DNS** | **Alternative DNS** | **Script**                   | **Batch File**               |
|-------------------|-------------------|---------------------|------------------------------|------------------------------|
| Google DNS        | 8.8.8.8           | 8.8.4.4             | `dns_scripts/dns_switcher_google.py`  | `bat_files/set_google_dns.bat` |
| Cloudflare DNS    | 1.1.1.1           | 1.0.0.1             | `dns_scripts/dns_switcher_cloudflare.py` | `bat_files/set_cloudflare_dns.bat` |
| AdGuard DNS       | 94.140.14.14      | 94.140.15.15        | `dns_scripts/dns_switcher_adGuard.py` | `bat_files/set_adguard_dns.bat` |
| OpenDNS           | 208.67.222.222    | 208.67.220.220      | `dns_scripts/dns_switcher_OpenDNS.py`     | `bat_files/set_OpenDNS.bat`  |
| Shecan DNS        | 178.22.122.100    | 185.51.200.2        | `dns_scripts/dns_switcher_shecan.py`  | `bat_files/set_shecan_dns.bat` |
| 403.online        | 10.202.10.202     | 10.202.10.102       | `dns_scripts/dns_switcher_403.online.py`  | `bat_files/set_403.online.bat` |
| Sharif.edu        | 172.26.146.34     | 172.26.146.35       | `dns_scripts/dns_switcher_sharif.edu.py`  | `bat_files/set_sharif.edu.bat` |

## 🔧 Prerequisites
- 🐍 **Python** installed on your system.
- 🔑 **Administrator privileges** for changing network configurations.

## ⚠️ Disclaimer
This script modifies network settings and requires administrative access.  
Please ensure you understand the impact of changing DNS configurations before using this tool.
