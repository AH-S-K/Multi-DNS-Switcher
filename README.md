Multi-DNS-Switcher
Multi-DNS-Switcher is a collection of Python scripts designed to automatically switch between different sets of preferred and alternative DNS addresses on Windows, requiring administrative privileges to ensure proper configuration.

Features
Multiple DNS Configurations: Easily switch between different DNS setups with dedicated scripts.
Admin Privileges: Automatically requests administrative access to modify network settings.
Active Interface Detection: Identifies the active network interface for DNS changes.
Reset to Default: Resets DNS to default (DHCP) if the specified DNS addresses are already set.
Files Included
dns_switcher_<name>.py: Python scripts for different DNS configurations (e.g., dns_switcher_google.py, dns_switcher_custom.py).
Batch Files (.bat): Batch files to execute the corresponding DNS scripts with admin privileges.
Usage
Clone the repository:
git clone https://github.com/yourusername/Multi-DNS-Switcher.git
Choose the appropriate .bat file for your desired DNS configuration.
Double-click the .bat file to execute the script with admin privileges.
Example Configurations
Google DNS:

Preferred: 8.8.8.8, Alternative: 8.8.4.4
Script: dns_switcher_google.py
Batch File: set_google_dns.bat
Custom DNS:

Preferred: 10.202.10.202, Alternative: 10.202.10.102
Script: dns_switcher_custom.py
Batch File: set_custom_dns.bat
Prerequisites
Python installed.
Administrator privileges.
Disclaimer
Modifies network settings and requires admin access. Ensure you understand the changes being made to DNS configurations.

