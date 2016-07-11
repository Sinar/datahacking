from bs4 import BeautifulSoup
import json
import os
import logging

PATH="data/raw/projects_20150911_1638"
total_company = 0
company_without_project = 0
total_project = 0

def project_page(page_id):
    global total_company
    global company_without_project
    global total_project


    path = "%s/%s" % (PATH, page_id)

    base_path = "%s/%s" % (PATH, page_id)
    page = 1
    while True:
        if not os.path.exists(path):
            break
        raw = open(path)
        soup = BeautifulSoup(raw, "html.parser")
        rows = soup.find("table").find("tbody").findAll("tr")
        json_data = {
            "meta": {
                "id": page_id
            },
            "projects":[]
        }
        if len(rows) == 1:
            company_without_project = company_without_project + 1
            return json_data
        for row in rows:
            datas = row.findAll("td")
            # TODO: Dafuq
            if len(datas) == 1:
                continue
            filter_tab_newline = lambda x: "".join([i for i in x if i not in ("\n", "\t")])
            project = filter_tab_newline(datas[1].text)
            if len(datas) >= 3:
                location = filter_tab_newline(datas[2].text) 
            else:
                location = ""
            if len(datas) >= 4:
                value = filter_tab_newline(datas[3].text)
            else:
                value = ""
            if len(datas) >= 5:
                dates = filter_tab_newline(datas[4].text)
            else:
                dates = ""
            project_data = {
                "project": project,
                "value": value,
                "dates": dates,
                "location": location
            }
            total_project = total_project + 1
            json_data["projects"].append(project_data)
            page = page + 1
            path = "%s.%s" % (base_path, page)
            
    return json_data

if __name__ == "__main__":
    output_file = open("data/project_data_20150914_1221.jsonl", "wb")
    for i in os.listdir(PATH):
        if "." in i:
            continue
        total_company = total_company + 1
        data = project_page(i)
        if not data:
            continue
        output_file.write(json.dumps(data)+"\n")
        logging.warn("Total project: %s" % total_project)
        logging.warn("Total no project: %s" % company_without_project)
        logging.warn("Company processes: %s" % total_company)
    output_file.close()
