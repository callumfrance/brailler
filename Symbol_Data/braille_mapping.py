import unicodedata
import json
import csv

def csvify(in_list):
    exporter = str(in_list[0])
    for item in in_list[1:]:
        add_quotes = False
        if ' ' in str(item):
            add_quotes = True
        exporter += str(',' + (add_quotes * '"') + str(item) + (add_quotes * '"'))
    return exporter

if __name__ == '__main__':
    row_export = ['UNICODE,HEX,UNICODE_NAME,INTEGER,UNICODE_CATEGORY',]

    for i in range(int('2800', 16), int('2840', 16)):
        row = [chr(i), 
                hex(i),
                unicodedata.name(chr(i)), 
                i,
                unicodedata.category(chr(i)),]
        row_export.append(csvify(row))

    row_export_str = "\r\n".join(row_export)

    with open("braille_unicode.csv", 'w') as f:
        for item in row_export_str:
            f.write(item)

    braille_dict_items = list()
    with open("braille_unicode.csv", 'r') as g:
        with open("braille_unicode.json", "w") as h:
            reader = csv.DictReader(g)
            for row in reader:
                braille_dict_items.append(row)
                json.dump(row, h)
                h.write(',\n')
