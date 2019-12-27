import re, requests, json

html_page = requests.get('https://switchbrew.org/wiki/Calibration').text.replace('\n','')
table = re.search(r"(?<=<tbody>).*(?=</tbody>)",html_page).group(0)
entries = re.findall(r"(?<=<tr><td>).*?(?=</td><\/tr>)",table)
fields = []
for i in entries:
    fields.append(i.split('</td><td>'))

prodinfo = open('prodinfo.bin','rb')

for i in fields:
    prodinfo.seek(int(i[0],16))
    print(i[2],i[3])
    print(prodinfo.read(int(i[1],16)).decode())
    print()
