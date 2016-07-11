import json

# Yes, it is generated, but you really have to just trust us on that
def add_attribute(data):
    data = json.loads(data)
    page_id = data["meta"]["id"]
    entries = [
        {
            "url":"http://smb.cidb.gov.my/contractor/contractors/public_profile/%s" % page_id,
            "note":"Main page of contractor"
        },
        {
            "url":"http://smb.cidb.gov.my/contractor/contractors/director/%s" % page_id,
            "note":"Director page. This page found by accident hidden from main page of contractor."
        }
    ]
    data["links"] = entries
    return json.dumps(data)

def main():
    f = open("data/contractors_20150922.jsonl")
    out_file = open("data/contractors_20150923.jsonl", "w")
    for entry in f:
        out_file.write(add_attribute(entry)+"\n")
    out_file.close()
    f.close()

if __name__ == "__main__":
    main()
    
