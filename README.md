# RLRankScraper
Uses a python script to scrape player MMRs from rlstats.net and output them into a salary csv file.

### Pre-requirements
1. Have python installed on your PC.
2. Have a basic understanding of how to clone a repository and run a python script.
3. Fill out the players.csv file with all the desired players, their platform, and their peak MMRs. Their platform MUST be one of the following options: [Epic, Steam, PS4, Xbox).
4. Clone the repository and run the command ```pip install -r requirements.txt```

### Run Steps
1. To run the script, simply run the command ```python rl_rank_scraper.py``` or ```python3 rl_rank_scraper.py```
---
This will read the players from the players.csv file, utilize the rlstats.net API to retrieve the MMRs, perform the calculations to get the salaries, and output the results to rocket_league.csv.
It will also determine if the player's current MMR in 2s or 3s is higher than the listed peak MMR from the players.csv file and update both files appropriately.
