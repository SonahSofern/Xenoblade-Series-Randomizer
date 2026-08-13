import string
from scripts import PackedBits
import base64
import struct
import scripts.SaveLoad
from tkinter import Variable
# credit to github.com/LagoLunatic/wwrando

intBits = 14

def SanitizeUserSeed(SeedName):
    SeedName = str(SeedName)
    SeedName = SeedName.strip()
    SeedName = "".join(char for char in SeedName if char in "-_'%%.%s%s" % (string.ascii_letters, string.digits))
    SeedName = SeedName[:40]
    return SeedName

def GenerateCompressedPermalink(SeedName, OptionsList:list[Variable], Version):
    SeedName = SanitizeUserSeed(SeedName)
    fixedVersion = Version
    for char in ".":
        fixedVersion = fixedVersion.replace(char, "")
    Permalink = b""
    Permalink += fixedVersion.encode("ascii")
    Permalink += b"\0"
    Permalink += SeedName.encode("ascii")
    Permalink += b"\0"

    bitswriter = PackedBits.PackedBitsWriter()
    for i in range(0, len(OptionsList)):
        try:
            optionvalue = OptionsList[i].get()
            if isinstance(optionvalue, bool):
                bitswriter.write(int(optionvalue), 1)
            elif isinstance(optionvalue, int):
                bitswriter.write(optionvalue, intBits)
        except:
            pass

    bitswriter.flush()

    for byte in bitswriter.bytes:
        Permalink += struct.pack(">B", byte)
    base64_encoded_permalink = base64.b64encode(Permalink).decode("ascii")
    return base64_encoded_permalink

def GenerateSettingsFromPermalink(base64_encoded_permalink, OptionsList:list[Variable]):
    base64_encoded_permalink = base64_encoded_permalink.strip()
    if not base64_encoded_permalink:
        raise Exception(f"Permalink is blank.")
    
    permalink = base64.b64decode(base64_encoded_permalink)
    given_version_num, seed, options_bytes = permalink.split(b"\0", 2)
    given_version_num = given_version_num.decode("ascii")
    seed = seed.decode("ascii")
    option_bytes = struct.unpack(">" + "B"*len(options_bytes), options_bytes)
    bitsreader = PackedBits.PackedBitsReader(option_bytes)
    for i in range(0, len(OptionsList)):
        optionvalue = OptionsList[i].get()
        if isinstance(optionvalue, bool):
            boolean_value = bool(bitsreader.read(1))
            if OptionsList[i].get() != boolean_value: # if the option is not changed dont recalculate things by setting it
                OptionsList[i].set(boolean_value)
        elif isinstance(optionvalue, int):
            intvalue = bitsreader.read(intBits)
            if OptionsList[i].get() != intvalue:
                OptionsList[i].set(intvalue)    
    return seed


def AddPermalinkTrace(traceObjects:list[Variable], permaLinkVar:Variable, seedEntryVar:Variable, version):
    def PermalinkFromEntry():
        try:
            seedName = GenerateSettingsFromPermalink(permaLinkVar.get(), traceObjects)
            seedEntryVar.set(seedName)
        except:
            print("Invalid Permalink")
    
    def PermalinkEntryUpdate():
        if scripts.SaveLoad.stopPermalinkUpdate: return
        permaLinkVar.set(GenerateCompressedPermalink(seedEntryVar.get(), traceObjects, version))
        
    for interactable in traceObjects:
        interactable.trace_add("write", lambda i,x,o: PermalinkEntryUpdate())
    
    permaLinkVar.trace_add("write", lambda i,x,o: PermalinkFromEntry())
    # for interactAble in traceObjects[2:]:
    #     interactAble.trace_add("write", lambda i,x,o: PermalinkEntryUpdate())
        