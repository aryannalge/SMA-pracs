import requests 
from bs4 import BeautifulSoup

url = "https://www.paruluniversity.ac.in/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(title := soup.title.string if soup.title else "No title found")

h1_tags = soup.find_all("h1")
print("H1 Tags:", len(h1_tags))

for h1 in h1_tags:
    print("H1: ", h1.get_text(strip=True))
    print("--------------------------------------------")
meta_tags = soup.find_all("meta")
print("Meta Tags:", len(meta_tags))