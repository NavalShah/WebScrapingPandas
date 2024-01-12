import pandas as pd
import requests
from bs4 import BeautifulSoup

# Create an empty DataFrame
df = pd.DataFrame(columns=['Team Name', 'Year'])

for i in range(1, 3):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    team_names = soup.find_all('td', class_="name")
    years = soup.find_all('td', class_="year")

    for team, year in zip(team_names, years):
        team_name = team.get_text()
        year_text = year.get_text()
        print(team_name +": "+ year_text)

        # Append to the DataFrame
        df = pd.concat([df, pd.DataFrame({'Team Name': [team_name], 'Year': [year_text]})], ignore_index=True)

# Save DataFrame to CSV
df.to_csv('output.csv', index=False, sep=';', encoding='utf-8')
