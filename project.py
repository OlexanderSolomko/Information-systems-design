import requests
from bs4 import BeautifulSoup
import os

keywords = ['big data', 'computer science', 'python language']

def get_article_links(keyword):
    url = f"https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=uk&search={keyword}&language=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    article_links = []
    for link in soup.find_all('a', href=True):
        if '/wiki/' in link['href']:
            article_links.append(link['href'])
    return article_links

output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

all_links = []
for keyword in keywords:
    links = get_article_links(keyword)
    all_links.extend(links)

file_path = os.path.join(output_folder, "article_links.txt")
with open(file_path, 'w', encoding='utf-8') as file:
    for link in all_links:
        file.write(f"https://www.wikipedia.org{link}\n")

print(f"Результати збережено у файлі: {file_path}")
