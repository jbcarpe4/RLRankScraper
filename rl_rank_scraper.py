import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import csv

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.129 Safari/537.36',
    'cookie': 'seasonalstats=0; PHPSESSID=2agtnct4st9htutjkofags36s4; lastnote=30'
}

players = []
with open('players.csv', 'r') as fd:
    reader = csv.reader(fd)
    next(reader, None) # skip header line
    for row in reader:
        players.append(row)

final = []
new_players = []

with open('players.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['username', 'platform', 'peak mmr'])
    
    for player in players:
        url = f'https://rlstats.net/profile/{player[1]}/{player[0]}'

        resp = requests.get(url,headers=headers)

        soup = BeautifulSoup(resp.text,'html.parser')

        mmr_rows = soup.find(string="1v1 Solo Duel").find_parent("table").find_all("tr")[3].find_all("td")

        for row in mmr_rows:
            if row.mmr is None:
                continue;
            row.mmr.decompose()
            row.mmr.decompose()
            
        doubles_mmr = int(mmr_rows[1].text.strip())
        standard_mmr = int(mmr_rows[2].text.strip())
        peak_mmr = max(doubles_mmr, standard_mmr, int(player[2]))
        salary = round(((max(doubles_mmr, standard_mmr) * 0.4) + (min(doubles_mmr, standard_mmr) * 0.2) + (peak_mmr * 0.4)) / 25) / 4

        item = {
            'username': player[0],
            'solo': mmr_rows[0].text.strip(),
            'doubles': doubles_mmr,
            'standard': standard_mmr,
            'peak mmr': peak_mmr,
            'salary': salary
        }
        
        final.append(item)
        
        writer.writerow([player[0], player[1], peak_mmr])

df = pd.DataFrame(final)
df.to_csv('rocket_league.csv', index=False)

print('Saved to rocket_league.csv')