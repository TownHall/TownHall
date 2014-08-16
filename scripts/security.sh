#!/bin/bash
# -------------------------------------------------------------------------
# Script responsible for providing some amount of security to the server:
#   - Uncomplicated Firewall (UFW)
#   - Tripwire Intrusion detection system (IDS)
#   - fail2ban
#   - Logging
#   - Proper SSH configuration
# -------------------------------------------------------------------------

# Uncomplicated Firewall (UFW)
# Note : UFW provides a convenient wrapper syntax on top of the more robust `iptables` firewall software.
sudo apt-get -y install ufw
sudo ufw default deny incoming  # deny all incoming connections
sudo ufw default allow outgoing  # allow all outgoing connections
sudo ufw allow 22/tcp  # allow ssh
sudo ufw allow 80/tcp  # allow http
sudo ufw allow 443/tcp  # allow https
sudo ufw enable

# Tripwire: Intrusion detection system (IDS)
# TODO: tripwire email notifications
sudo apt-get -y install tripwire

# fail2ban : Used to ban malicious IP addresses
# TODO: fail2ban email notifications
sudo apt-get -y install fail2ban

# TODO: Logging of various services, configured with email notifications

# TODO: SSH configuration

# Cleanup
sudo ufw status  # display firewall status

