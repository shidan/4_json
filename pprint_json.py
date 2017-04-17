import json
import sys


def load_data(filepath):
    fdata = open(filepath, 'r')
    return fdata.read().strip()


def pretty_print_json(data):
    json_data = json.loads(data)
    print(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Укажите имя файла для вывода")
    elif len(sys.argv) == 2:
        pretty_print_json(load_data(sys.argv[1]))
    else:
        print("Слишком много параметров")
    
