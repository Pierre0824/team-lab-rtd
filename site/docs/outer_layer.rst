Outer Layer – Network Access Controls (Quick Wins)
==================================================

Easiest to implement, highest immediate impact, lowest maintenance.

Restrict Management Interface Access
------------------------------------

Keep the Control-Plane Off the Internet.

* Restrict SSH access to trusted IP ranges
* Restrict Configuration Utility (TMUI) by source IP
* Configure management interface firewall (BIG-IP 14.1+)
* Configure Self IP Port Lockdown
* Use dedicated management interface or VLAN
* Isolate management traffic from data-plane traffic

iHealth Verification
--------------------

* H444724: Management interface allowing public access

Implementation Effort: Low  
Maintenance: Minimal  
Impact: High

Session & Access Timeouts
-------------------------

* Configure idle logout for TMUI
* Configure SSH inactivity timeouts
* Configure console and tmsh timeouts
* Configure BIG-IQ idle session timeouts
* Configure pre-login and post-login banners

iHealth Verification
--------------------

* D009908: Idle logout settings
* D006068: Login banner configuration

Implementation Effort: Low  
Maintenance: Minimal  
Impact: High

Basic Administrative Account Hygiene
------------------------------------

* Change default root and admin passwords
* Disable root account where possible
* Configure secure password policy
* Enable password complexity and history
* Set maximum login failure thresholds

iHealth Verification
--------------------

* D015632: Admin and root account status
* H494013: Password policy strength

Implementation Effort: Low  
Maintenance: Low  
Impact: High
