# Proxy Scraper

A simple Python script to scrape SOCKS5 proxies from [ProxyDB](https://proxydb.net/) and save them to a text file.

---

## Features

- Scrapes SOCKS5 proxies from `proxydb.net`
- Filters ports starting with `80` (optional removal)
- Saves results to `proxies.txt`
- Easy to use and lightweight

---

## Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies using pip:

```bash
pip install requests beautifulsoup4

```

## Usage

---

-Clone the repository:
```
git clone https://github.com/sharifulislam141/proxy-scrapper.git
cd proxy-scrapper

```
Run the script:
```

python main.py
```

After running, all proxies will be saved in proxies.txt.


## Notes

# Make sure you have a stable internet connection.

# The script only scrapes SOCKS5 proxies.

# Modify the URL if you want to filter by country or protocol.
## License

This project is open-source and available under the MIT License.

Author

Md. Shariful Islam