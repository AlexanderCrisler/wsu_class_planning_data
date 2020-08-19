import bs4
import re

plan_file = open('ClassPlan.html', encoding="utf8")
plan_soup = bs4.BeautifulSoup(plan_file, 'html.parser')

list_items = plan_soup.findAll("li")

identifier = "Planned Course Design"
plan_dict = {}
plans = []
for item in list_items:
    if item.text.find(identifier) >= 0:
        plans.append(item)
        if item.text[len(identifier):] in plan_dict:
            plan_dict[item.text[len(identifier):]] += 1
        else:
            plan_dict[item.text[len(identifier):]] = 0

for x, y in plan_dict.items():
    print(x, ":", y)
