ShadowXSS

ShadowXSS is a Python-based XSS payload testing tool designed for educational and laboratory environments. The tool helps security researchers and students explore Cross-Site Scripting payload categories, test reflections, and study web application behavior in controlled and authorized environments.

Features

- Organized XSS payload categories
- Fast payload browsing
- Reflection checking
- Payload search system
- Simple terminal interface
- Designed for Termux and Linux environments

Categories

- Basic
- HTML
- Attribute
- JavaScript
- SVG
- WAF
- DOM
- Encoding
- Blacklist
- Advanced payloads

How It Works

1. Start the tool
2. Enter the target URL
3. The tool validates the target
4. Choose a payload category
5. Browse or test payloads inside the selected category

Example target:

https://example.com/search?q=

Installation

pkg update && pkg upgrade -y

pkg install git python -y

git clone https://github.com/Mrobot2937/ShadowXSS.git

cd payload-xss

python3 xss_payload.py

Usage

cd payload-xss

python3 xss_payload.py

Disclaimer

This project is intended only for educational purposes and authorized security testing in controlled environments.

<p align="center">
  <img src="https://i.imghippo.com/files/PoRi3953vf.png" width="100%">
</p>