import re
def extract_ip_addresses(file_content):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(pattern, file_content)
    return ip_addresses
# Input File Content
log_content = '''
192.168.1.1 - Accessed on 2025-01-19
10.0.0.2 - Accessed on 2025-01-20
'''
ip_addresses = extract_ip_addresses(log_content)
print("IP Addresses:", ", ".join(ip_addresses))  