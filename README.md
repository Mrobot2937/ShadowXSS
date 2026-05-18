ShadowXSS






ShadowXSS

   

ShadowXSS is a Python-based XSS payload testing tool designed for educational and laboratory environments. The tool helps security researchers and students explore Cross-Site Scripting payload categories, test reflections, and study web application behavior in controlled and authorized environments.


---

Features

Organized XSS payload categories

Fast payload browsing

Reflection checking

Payload search system

Simple terminal interface

Cross-platform support (Termux, Linux, Windows)



---

Categories

Basic

HTML

Attribute

JavaScript

SVG

WAF

DOM

Encoding

Blacklist

Advanced payloads



---

How It Works

1. Start the tool


2. Enter the target URL


3. The tool validates the target


4. Choose a payload category


5. Browse or test payloads inside the selected category




---

Example Target

https://example.com/search?q=


---

Installation

Termux (Android)

pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/Mrobot2937/ShadowXSS.git
cd ShadowXSS
pip install -r requirements.txt 2>/dev/null
python3 xss_payload.py


---

Linux / PC (Ubuntu, Debian, Kali)

sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
git clone https://github.com/Mrobot2937/ShadowXSS.git
cd ShadowXSS
pip3 install -r requirements.txt
python3 xss_payload.py


---

Windows (10/11)

git clone https://github.com/Mrobot2937/ShadowXSS.git
cd ShadowXSS
pip install -r requirements.txt
python xss_payload.py

If it doesn’t work:

py xss_payload.py

or

python3 xss_payload.py


---

Usage

python xss_payload.py


---

Issues & Support

If you find bugs or problems:

Open an issue on GitHub

Provide the error message

Include your system (Termux, Linux or Windows)

Describe steps to reproduce the error



---

Disclaimer

This project is intended only for educational purposes and authorized security testing in controlled environments. Any misuse is the responsibility of the user.



<p align="center">
  <img src="https://i.imghippo.com/files/PoRi3953vf.png" width="100%">
</p>