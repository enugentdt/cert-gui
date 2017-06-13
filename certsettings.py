settings = {}
settingsFile = "config/settings.cnf"

def readSettings():
    txt = open(settingsFile)
    data = txt.read()
    data = data.split('\n')
    for item in data:
        line = item.split("=")
        line[0] = line[0].replace(" ", "")
        if line[1][0] is " ":
            line[1] = line[1][1:]
        settings[line[0]] = line[1]
        
def getSettings():
    return settings

            