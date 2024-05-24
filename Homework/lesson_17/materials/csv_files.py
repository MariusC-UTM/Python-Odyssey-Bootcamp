import csv

# with open("file.csv", 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# data = [
#     {"Name": "Alice", "Age": 20},
#     {"Name": "Vasea", "Age": 14}
# ]

# with open("example.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["Name", "Age"])
#     writer.writeheader()
#     writer.writerows(data)

# import pandas as pd

# data = pd.read_csv("example.csv")
# data.loc[0][1] = 19 #keep in mind the version
# print(data)

# data.to_csv("new_example.csv")
# data.info()

# print(data)

import json

# dt = {"Name": "Alice", "Age": 20}

# with open("example.json", "w") as file:
#     json.dump(dt, file, indent=4)

# with open("exampl.txt", "r") as file:
#     data = json.load(file)
#     print(data)

# string_js = '{"Name": "Alice", "Age": 20}'

# data = json.loads(string_js)
# print(data)

# new_json_string = json.dumps(data, indent=4)
# print(new_json_string)


# from lxml import etree

# radacina = etree.Element("data")
# item = etree.SubElement(radacina, "item", name="Alice")
# item.text = "30"

# tree = etree.ElementTree(radacina)
# tree.write("example.xml", pretty_print=True)

from bs4 import BeautifulSoup

with open("example.xml", 'r') as file:
    content = file.read()

soup = BeautifulSoup(content, "xml")
items = soup.find_all("item")
for item in items:
    print(item["name"], item.text)