# Multi-DNS-Switcher 🌐

**Multi-DNS-Switcher** is a collection of Python scripts designed to automatically switch between different sets of preferred and alternative DNS addresses on Windows, requiring administrative privileges to ensure proper configuration.

## ✨ Features
- <span style="font-weight: bold;">Multiple DNS Configurations:</span> Easily switch between different DNS setups with dedicated scripts.
- <span style="font-weight: bold;">Admin Privileges:</span> Automatically requests administrative access to modify network settings.
- <span style="font-weight: bold;">Active Interface Detection:</span> Identifies the active network interface for DNS changes.
- <span style="font-weight: bold;">Reset to Default:</span> Resets DNS to default (DHCP) if the specified DNS addresses are already set.

## 📁 Files Included
- **`dns_switcher_<name>.py`**: Python scripts for different DNS configurations (e.g., `dns_switcher_google.py`, `dns_switcher_custom.py`).
- **Batch Files (`.bat`)**: Batch files to execute the corresponding DNS scripts with admin privileges.

## 🚀 How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Multi-DNS-Switcher.git
    ```
2. Choose the appropriate `.bat` file for your desired DNS configuration.
3. Double-click the `.bat` file to execute the script with admin privileges.

> **Note:** Make sure you run the batch files with administrator privileges to ensure DNS changes are applied successfully.

## 📝 Example Configurations
| **Configuration** | **Preferred DNS** | **Alternative DNS** | **Script**               | **Batch File**         |
|-------------------|-------------------|---------------------|--------------------------|------------------------|
| Google DNS        | 8.8.8.8           | 8.8.4.4             | `dns_switcher_google.py` | `set_google_dns.bat`   |
| Custom DNS        | 10.202.10.202     | 10.202.10.102       | `dns_switcher_custom.py` | `set_custom_dns.bat`   |

## 🔧 Prerequisites
- 🐍 **Python** installed on your system.
- 🔑 **Administrator privileges** for changing network configurations.

## ⚠️ Disclaimer
This script modifies network settings and requires administrative access.  
Please ensure you understand the impact of changing DNS configurations before using this tool.
