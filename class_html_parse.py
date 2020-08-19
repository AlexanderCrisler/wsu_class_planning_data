import bs4
import json

exampleFile = open('ClassList.html', encoding="utf8")
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

class_names = []
for val in exampleSoup.select('h3'):
    val_string = val.string
    val_string = val_string.replace("\n","")
    val_string = val_string.replace("\t","")
    class_names.append(val_string.replace(" ",""))

class_names_file = open('class_names_file.json', 'w', newline='')

separator = "-"
for i in range(0, len(class_names)):
    class_names[i] = class_names[i].split(separator, 1)[0]
    
json.dump(class_names, class_names_file)
print("finished.")