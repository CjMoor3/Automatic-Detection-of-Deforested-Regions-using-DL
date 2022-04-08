import json
import os
from socket import J1939_FILTER_MAX

if __name__ == '__main__':
    fileName = os.path.relpath('./writeGUI/TDSCOCO/COCOTDS.json')# './WriteGUI/TDSCOCO/GM-COCO-2022-3-4.json')
    with open(fileName, 'r') as fileObj:
        newDict = json.load(fileObj)
        
    water = thinIce = shadow = snow = subIce = meltPond = 0
        
    for i in newDict['annotation']:
        if i['category_id'] == 0:
            water +=1
        elif i['category_id'] == 1:
            thinIce += 1
        elif i['category_id'] == 2:
            shadow += 1
        elif i['category_id'] == 3:
            snow += 1
        elif i['category_id'] == 4:
            subIce += 1
        elif i['category_id'] == 5:
            meltPond += 1
        
        
    displayDict = {'Water': water, "Thin Ice": thinIce, "Shadow": shadow, "Snow/Ice": snow, "SubIce": subIce, "Melt Pond": meltPond}
    
    print(displayDict)
    print("Total segments: {}".format(water+thinIce+shadow+snow+subIce+meltPond))
    


