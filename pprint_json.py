import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r') as fdata:
        return json.load(fdata)


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Укажите имя файла для вывода")
    elif len(sys.argv) == 2:
        pretty_print_json(load_data(sys.argv[1]))
    else:
        print("Слишком много параметров")
    
