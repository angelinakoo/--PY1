import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_file, new_line='\n', delimiter=',') -> list[dict]:
    with open(csv_file, 'r') as f:
        list_ = []
        headers = f.readline().strip(new_line).split(delimiter)
        for line in f:
            dict_ = dict(zip(headers, line.strip(new_line).split(delimiter)))
            list_.append(dict_)
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
