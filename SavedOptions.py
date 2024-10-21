import json


def saveData(DataList):
    print("thing closed")
    with open('SavedOptions.txt', 'w') as file:
        for it in DataList:
            file.write(f"{it.get()} + '\n'")



def loadData(DataList):
    None


# with open('directories.json', 'r') as file:
#     data = json.load(file)
#     InputDirectory = data['InputDirectory']
#     OutputDirectory = data['OutputDirectory']
