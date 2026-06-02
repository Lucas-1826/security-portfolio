# Incident Report: Suspicious Login Activity

## Summary
A series of suspicious authentication attempts were detected on 2024-05-12. Multiple failed login attempts targeting the 'root' account originated from the external IP address 185.199.110.153, indicating a likely brute-force attack.

## Timeline of Events
- **14:22:31** — Admin user successfully logged in from 192.168.1.24  
- **14:23:10–14:23:15** — Three failed login attempts for user 'root' from 185.199.110.153  
- **14:24:01** — Admin accessed `/var/www/html/index.php`  
- **14:25:44** — Unauthorized access attempt detected from 185.199.110.153  
- **14:26:02** — Admin user logged out

## Indicators of Compromise (IOCs)
- **Suspicious IP:** 185.199.110.153  
- **Targeted Account:** root  
- **Repeated Failed Logins:** 3 attempts within 5 seconds  
- **Unauthorized Access Attempt:** Logged as ERROR

## Analysis
The repeated failed login attempts from a single external IP suggest automated brute-force activity. The attacker targeted the 'root' account, which is commonly used in brute-force attacks due to its elevated privileges.

The unauthorized access attempt logged at 14:25:44 further supports malicious intent.

No evidence indicates the attacker successfully authenticated.

## Recommendations
- Block IP address 185.199.110.153 at the firewall  
- Disable direct root login  
- Enforce multi-factor authentication (MFA)  
- Review server authentication logs for additional anomalies  
- Implement rate limiting for login attempts

## Conclusion
This event appears to be a brute-force attack attempt against the server. No successful compromise was detected, but preventative measures should be implemented immediately.
