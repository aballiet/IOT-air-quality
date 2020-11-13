#!/bin/bash
sudo openconnect --os win sslvpn.insa-lyon.fr << EOF
INSA
$VPN_USER
$VPN_PASSWORD
EOF
