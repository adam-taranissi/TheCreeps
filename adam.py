import os
import json

# Create a list of all files
allFiles = os.listdir("./AdamData")

# Create dictionary of all IPs
Dict = {}


for file in allFiles:
    # print(file)
    openFile = open("./AdamData/"+file,)
    #print(openFile)
    if file == ".DS_Store":
        continue
    jsonList = []
    for info in openFile:
        # print(type(jsonObj))
        objects = info.split("}{")
        for jsonObj in objects:
            ammendObj = jsonObj
            if ammendObj[-1] != "}":
                ammendObj = ammendObj+"}"
            if ammendObj[0] != "{":
                ammendObj = "{" + ammendObj
            #if file == "1513.txt":
                
                #print(ammendObj)
            jsonList.append(json.loads(ammendObj))

    Dict[file.replace(".txt", "")] = jsonList

# print(Dict["1513"])

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item in listOfItems:
        #print(type(item[1]))
        if len(item[1]) > 1:
            for element in item[1]:
                #print(str(element).find(valueToFind))
                if str(element).lower().find(valueToFind) != -1:
        
                    listOfKeys.append(item[0])
                    break
        elif str(item[1]).lower().find(valueToFind) != -1:
            listOfKeys.append(item[0])
    return listOfKeys


# print(len(getKeysByValue(Dict, "topic")))
currentSearchTerm = "alarm"
values = getKeysByValue(Dict, currentSearchTerm)
print(values)
print("Number of instances", len(values))


topTerms = ["email", "username", "user", "password", "laundry", "alarm", "lock", "speaker", "tesla", "car", "garage", "door", "security", "camera", "monitor",
"intruder", "location", "gps", "longitude", "latitude", "alexa", "google", "refrigerator", "fridge", "vacuum", "key", "phone", "laptop", "humidifier", "thermostat", 
"ac", "air conditioner", "bed", "blinds", 'boiler', 'coffee', 'dishwasher', 'window', 'fan', 'gate', 'heater', 'baby', 'microwave', 'switch', 'outlet', 'fridge', 
'sensor', 'smoke', 'fire', 'car',  'speaker', 'sound', 'sonos', 'amazon', 'apple', 'sprinkler', 'tv', 'valve']
topTermsFreq = []
topTermsList = []

for term in topTerms:
    values = getKeysByValue(Dict, term)
    topTermsFreq.append(len(values))
    topTermsList.append(values)
    print(term, len(values), values, "\n")









