import pandas as pd

file_path = "results/article_links.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    links = file.readlines()

unique_links = list(set(links))

indexed_links = [f"{index + 1}: {link}" for index, link in enumerate(unique_links)]

article_titles = [link.split('/')[-1] for link in indexed_links]

df = pd.DataFrame(article_titles, columns=['Назва статті'])

output_file = "article_titles.csv"
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Результати збережено у файлі: {output_file}")