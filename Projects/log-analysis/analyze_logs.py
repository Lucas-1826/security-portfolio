import re
from collections import Counter

log_file = "logs/sample.log"

failed_attempts = []
suspicious_ips = []

with open(log_file, "r") as f:
    for line in f:
        # Detect failed login attempts
        if "Failed login attempt" in line:
            ip = re.search(r"from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
            if ip:
                failed_attempts.append(ip.group(1))

        # Detect unauthorized access attempts
        if "Unauthorized access attempt" in line:
            ip = re.search(r"from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
            if ip:
                suspicious_ips.append(ip.group(1))

print("=== Log Analysis Summary ===")
print(f"Total failed login attempts: {len(failed_attempts)}")

if failed_attempts:
    print("\nFailed login attempts by IP:")
    for ip, count in Counter(failed_attempts).items():
        print(f"  {ip}: {count} attempts")

if suspicious_ips:
    print("\nUnauthorized access attempts detected from:")
    for ip in suspicious_ips:
        print(f"  {ip}")

print("\nAnalysis complete.")
