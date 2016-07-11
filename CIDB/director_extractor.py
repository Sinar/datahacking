from bs4 import BeautifulSoup
import json
import logging
import os
import re

PATH="/home/sweemeng/projects/datahacking/CIDB/data/raw/directors_20150920/"

def director_extractor(page_id):
    path = os.path.join(PATH, str(page_id))
    soup = BeautifulSoup(open(path), "html.parser")
    
    data = {
        "meta":{"id":page_id},
        "directors": []
    }
    
    if re.search("Rekod tidak", soup.text):
        return data
    rows = soup.find("tbody").findAll("tr")
    for row in rows:
        col = row.findAll("td")
        
        director = {
            "name": col[0].text.strip(),
            "idenfity_card_no": col[1].text.strip(),
            "year_of_experience": col[2].text.strip(),
            "shares": col[3].text.strip(),
            "nationality": col[4].text.strip(),
        }
        
        data["directors"].append(director)
    return data

def main():
    f = open("company_directors.jsonl", "w")
    for page_id in os.listdir(PATH): 
        logging.warn("Processing Page: %s" % page_id)
        path = os.path.join(PATH, str(page_id))
        if not os.path.exists(path):
            break
        directors = director_extractor(page_id)
        f.write(json.dumps(directors)+"\n")
    f.close()

if __name__ == "__main__":
    main()
