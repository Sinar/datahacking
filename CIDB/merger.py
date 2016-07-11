import json

class DataMerger(object):
    def __init__(self):
        self.data = {}
    
    # Run this several time with different file
    def add_data(self, filename):
        f = open(filename)
        for line in f:
            # Because we are using json line 
            temp = json.loads(line)
            page_id = temp["meta"]["id"]
            data = self.data.setdefault(page_id, {})
            for key in temp:
                if key in data:
                    data[key].update(temp[key])
                else:
                    data[key] = temp[key]
        f.close()
    
    def output_file(self, filename):
        f = open(filename, "w")
        for key, data in self.data.iteritems():
            f.write(json.dumps(data) + "\n")
        f.close()


if __name__ == "__main__":
    merger = DataMerger()
    merger.add_data("data/project_data_20150914_1221.jsonl")
    merger.add_data("data/results_20150910_1158.json")
    merger.add_data("data/company_name_20150921.jsonl")
    merger.add_data("data/company_directors_20150922.jsonl")
    merger.output_file("data/contractors_20150914_1858.jsonl")
    
