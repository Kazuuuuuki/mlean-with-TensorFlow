from bs4 import BeautifulSoup
html = open("eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

result = []

table = soup.select_one("table")

tr_list = table.find_all("tr")

for tr in tr_list:
    result_row = []
    td_list = tr.find_all(["td", "th"])
    for td in td_list:
        cell = td.get_text()
        result_row.append(cell)
    result.append(result_row)

for now in result:
    print(",".join(row))