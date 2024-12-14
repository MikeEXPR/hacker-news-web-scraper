import requests
from bs4 import BeautifulSoup

# Target Hacker News
url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Hacker News Headlines:\n")

# Look for <span> or <a> tags with headlines
for item in soup.find_all("span", class_="titleline"):  # Inspecting title container
    headline = item.find("a")  # Get the headline link inside <span>
    if headline:  
        print(headline.text.strip())