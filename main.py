import requests
from bs4 import BeautifulSoup

url = "https://proxydb.net/?protocol=socks5&country="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')

    tbody = soup.select_one('tbody')
    trs = tbody.select('tr')

    with open("proxies.txt", "w") as f:
        for tr in trs:
            tds = tr.find_all('td')
            if len(tds) < 2:
                continue
            ip = tds[0].get_text(strip=True)
            port = tds[1].get_text(strip=True)
            
            
            if port.startswith('80'):
                port = port[2:]  
            
            print(f"{ip}:{port}")
            f.write(f"{ip}:{port}\n")
    print("Proxies saved correctly to proxies.txt")

except requests.exceptions.RequestException as e:
    print("Error:", e)
