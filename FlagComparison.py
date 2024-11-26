beforefilepath = "D:\\Xenoblade 2 Flag Txts\\Before"
afterfilepath = "D:\\Xenoblade 2 Flag Txts\\After"
filenames = ["\\1bitoutputfile.txt","\\2bitoutputfile.txt","\\4bitoutputfile.txt","\\8bitoutputfile.txt","\\16bitoutputfile.txt","\\32bitoutputfile.txt"]

# before event bit list holders
FullBefore = []
removenewlines = []

for i in range(0, len(filenames)):
    chosenfilename = beforefilepath + filenames[i]
    chosenfile = open(chosenfilename, "r")
    FullBefore.append(chosenfile.readlines())
    chosenfile.close()
    removenewlines = FullBefore[i]
    for j in range(0, len(removenewlines)):
        removenewlines[j] = removenewlines[j].replace("\n", "")
    FullBefore[i] = removenewlines

b1bit = FullBefore[0]
b2bit = FullBefore[1]
b4bit = FullBefore[2]
b8bit = FullBefore[3]
b16bit = FullBefore[4]
b32bit = FullBefore[5]

BeforeFullList = [b1bit, b2bit, b4bit, b8bit, b16bit, b32bit]

# after event bit list holders
FullAfter = []

for i in range(0, len(filenames)):
    chosenfilename = afterfilepath + filenames[i]
    chosenfile = open(chosenfilename, "r")
    FullAfter.append(chosenfile.readlines())
    chosenfile.close()
    removenewlines = FullAfter[i]
    for j in range(0, len(removenewlines)):
        removenewlines[j] = removenewlines[j].replace("\n", "")
    FullAfter[i] = removenewlines

a1bit = FullAfter[0]
a2bit = FullAfter[1]
a4bit = FullAfter[2]
a8bit = FullAfter[3]
a16bit = FullAfter[4]
a32bit = FullAfter[5]

AfterFullList = [a1bit, a2bit, a4bit, a8bit, a16bit, a32bit]

bitnames = ["1","2","4","8","16","32"]

changedict = {"Flag Size": [0], "Flag Location": [0], "Before Value": [0], "After Value": [0]}
#changekeys = ["Flag Size", "Flag Location", "Before Value", "After Value"]

for i in range(0, len(BeforeFullList)):
    for j in range(0, len(BeforeFullList[i])):
        if BeforeFullList[i][j] != AfterFullList[i][j]:
            changedict["Flag Size"].append(bitnames[i] + "-bit")
            changedict["Flag Location"].append(j+1)
            changedict["Before Value"].append(BeforeFullList[i][j])
            changedict["After Value"].append(AfterFullList[i][j])

finalset = []

for i in range(1, len(changedict["Flag Size"])):
    finalset.append([changedict["Flag Size"][i], changedict["Flag Location"][i], changedict["Before Value"][i], changedict["After Value"][i]])

changedflagsfilename = "D:\Xenoblade 2 Flag Txts\Changed Flags\Changed Flags.txt"
changedflagsfile = open(changedflagsfilename, "w")

for i in range(0, len(finalset)):
    changedflagsfile.write(f"{finalset[i]}\n")

