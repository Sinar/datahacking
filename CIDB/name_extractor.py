from bs4 import BeautifulSoup
import json
import os
import logging

PATH="/home/sweemeng/projects/datahacking/CIDB/data/raw/profiles_20150915"

def extract_name(page_id):
    path = os.path.join(PATH, str(page_id))
    soup = BeautifulSoup(open(path), "html.parser")

    name = soup.find("h1").text
    name = name.strip()
    data = {
        "meta":{"id":page_id},
        "name": name
    }
    return data


def main():
    f = open("company_name.jsonl", "w")
    for page_id in os.listdir(PATH):
        path = os.path.join(PATH, str(page_id))
        logging.warn("Processing path %s" % path)
        if not os.path.exists(path):
            break
        name_data = extract_name(page_id)
        f.write(json.dumps(name_data)+"\n")
    f.close()


if __name__ == "__main__":
    main()

