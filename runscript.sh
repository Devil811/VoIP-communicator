﻿#!/bin/bash

#Skript na registraci uživatele

#kompletni parametry spusteni:--id sip:xcahat01@sip2sip.info --registrar sip:sip2sip.info --realm sip2sip.info --username xcahat01@sip2sip.info --password xcahat01123456 --contact sip:xcahat01@sip2sip.info
# --outbound sip:proxy.sipthor.net:5060 --thread-cnt 1 --nameserver 8.8.8.8 --nameserver 8.8.4.4 --publish --clock-rate 8000 --add-codec pcma --dis-codec opus/48000/2 --dis-codec AMR-WB/16000/1 --dis-codec AMR/8000/1

#Deklarování promìnných
ID="sip:xcahat01@sip2sip.info"
REGISTRAR="sip:sip2sip.info"
REALM="sip2sip.info"
USERNAME="xcahat01@sip2sip.info"
PASSWORD="xcahat01123456"
CONTACT="sip:xcahat01@sip2sip.info"
OUTBOUND="sip:proxy.sipthor.net:5060"
THREAD="1"
NAMESERVER="8.8.8.8"
NAMESERVER2="8.8.4.4"
CLOCKRATE="8000"
ADDCODEC="pcma"
DISCODEC="opus/48000/2"
DISCODEC2="AMR-WB/16000/1"
DISCODEC3="AMR/8000/1"

python copyfile.py
python call.py --id sip:xcahat01@sip2sip.info --registrar sip:sip2sip.info --realm sip2sip.info --username xcahat01 --password xcahat01123456 --contact sip:xcahat01@sip2sip.info --outbound sip:proxy.sipthor.net:5060 --thread-cnt 1 --nameserver 8.8.8.8 --nameserver 8.8.4.4 --publish --clock-rate 8000 --add-codec pcma --dis-codec opus/48000/2 --dis-codec AMR-WB/16000/1 --dis-codec AMR/8000/1
