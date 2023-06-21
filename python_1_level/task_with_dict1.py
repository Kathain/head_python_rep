tut_list = []
slovar = {'ObjectID':None,'AddressTitle':None,'Longitude':None,'Latitude':None}
first_list = xhr['data']['ObjectsList']

for elem_dict in first_list:
    if len(elem_dict['Files']) > 0:
        files_dict = elem_dict['Files'][0]
        if 'FileType' in files_dict:
            slovar['ObjectID'] = elem_dict['ObjectID']
            slovar['AddressTitle'] = elem_dict['AddressTitle']
            slovar['Longitude'] = elem_dict['Longitude']
            slovar['Latitude'] = elem_dict['Latitude']
            tut_list.append(slovar)
#print(tut_list)



