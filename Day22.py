import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/dataset/360/air+quality'

response = requests.get(url)
response.raise_for_status() # throws an error if request failed

soup = BeautifulSoup(response.text, 'html.parser') # beautiful soup will give a chance to parse

# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)
# print(response.status_code)

# CSS selector
table = soup.select_one('div.drawer-content')

if not table:
    raise ValueError("Could not find the target table on the page.")

# Extract first row's cells
first_row = table.select_one('tr')
cells = first_row.select("td")

for cell in cells:
    print(cell.get_text(strip=True))

