import json

from Service import request

jsonfile = json.loads(request.r.text)
artists = jsonfile["result"]["artists"]
names = jsonfile["result"]["names"]
name_id = str(jsonfile["result"]["artistIds"][0])
name = jsonfile["result"]["artists"][name_id]["name"]
compo = jsonfile["result"]["tracks"]


def artist_name_list(artistname):
    name_from_json = ''
    id_from_json = []
    for key in artists:
        name_from_json = jsonfile["result"]["artists"][key]["name"]
        name_from_json.lower()
        if artistname.lower() in name_from_json.lower() or artistname.lower() == name_from_json.lower():
            #id_from_json.append(key)
            id_from_json.append(jsonfile["result"]["artists"][key]["name"])
    return id_from_json

def artists_id_list(artistname):
    name_from_json = ''
    id_from_json = []
    list_name_from_json = []
    for key in names:
        name_from_json = jsonfile["result"]["names"][key]["value"]
        name_from_json = name_from_json.lower()
        if artistname.lower() in name_from_json or artistname.lower() == name_from_json:
            id_from_json.append(key)
            list_name_from_json.append(jsonfile["result"]["names"][key]["value"])
    return id_from_json




def compositions(id):
    comositions_list = ''
    comp_list = []

    for key in compo:
        comositions_list = jsonfile["result"]["tracks"][key]["artistNames"]
        comositions_list = comositions_list[0]
        comositions_list = str(comositions_list)
        for i in range(len(id)):
                if id[i] in comositions_list:
                    comp_list.append(jsonfile["result"]["tracks"][key]["name"])
    return comp_list


print (compositions(artists_id_list(request.search_query)))
print (artists_id_list(request.search_query))
print (artist_name_list(request.search_query))
#print (name)
