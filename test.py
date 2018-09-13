titles=['  1  ',' 2 ',' 3 ']
addresses=[' 5 ',' 6','7 ']
info_lists = []
for title, address in zip(titles,addresses):
    info = {
       # 'url':url,
        'title':title.strip(),
        'address':address.strip(),
    }
    info_lists.append(info)

print(info_lists)

for info_list in info_lists:
    print(info_list)
    print(info_list['title'])
