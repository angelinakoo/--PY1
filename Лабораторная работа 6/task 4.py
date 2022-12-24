import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_file, new_line='\n', delimiter=',') -> list[dict]:
    with open(csv_file) as f:
        list_ = []
        name_list = []

        for index, row in enumerate(f):
            row_strip_split = row.strip(new_line).split(delimiter)
            if index == 0:
                for name in row_strip_split:
                    name_list.append(name.strip('"'))
            else:
                dict_ = dict(zip(name_list, row_strip_split))

                list_.append(dict_)
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
