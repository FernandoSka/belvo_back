#!/bin/bash

apt-get update
apt install -y --no-install-recommends gcc curl gnupg2 gcc libc6-dev g++ unixodbc-dev

pip install --upgrade pip
echo "Installing Postgres Support"
pip install 'psycopg2_binary>=2.8,<2.9'

apt-get install -y openssl build-essential libssl-dev libxrender-dev git-core libx11-dev libxext-dev libfontconfig1-dev libfreetype6-dev fontconfig

pip install -r /requirements.txt
apt purge -y --auto-remove gcc curl gnupg2 gcc libc6-dev g++ unixodbc-dev
apt-get clean
rm -rf /var/lib/apt/lists/* 
rm -rf /root/.cache

if [ "${debug}" == "true" ]; then 
    pip install debugpy -t /tmp
fi