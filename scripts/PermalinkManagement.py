import tkinter
import string
import PackedBits
import base64
import struct


# most of this is from github.com/LagoLunatic/wwrando

def SanitizeUserSeed(SeedName):
    SeedName = str(SeedName)
    SeedName = SeedName.strip()
    SeedName = "".join(char for char in SeedName if char in "-_'%%.%s%s" % (string.ascii_letters, string.digits))
    SeedName = SeedName[:40]
    return SeedName

def GenerateCompressedPermalink(SeedName, OptionsList, Version):
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
    for i in range(2, len(OptionsList)):
        optionvalue = OptionsList[i].get()
        if isinstance(optionvalue, bool):
            bitswriter.write(int(optionvalue), 1)
        elif isinstance(optionvalue, int):
            bitswriter.write(optionvalue, 8)

    bitswriter.flush()

    for byte in bitswriter.bytes:
        Permalink += struct.pack(">B", byte)
    base64_encoded_permalink = base64.b64encode(Permalink).decode("ascii")
    return base64_encoded_permalink

def GenerateSettingsFromPermalink(base64_encoded_permalink, OptionsList):
    base64_encoded_permalink = base64_encoded_permalink.strip()
    if not base64_encoded_permalink:
        raise Exception(f"Permalink is blank.")
    
    permalink = base64.b64decode(base64_encoded_permalink)
    given_version_num, seed, options_bytes = permalink.split(b"\0", 2)
    given_version_num = given_version_num.decode("ascii")
    seed = seed.decode("ascii")
    option_bytes = struct.unpack(">" + "B"*len(options_bytes), options_bytes)
    bitsreader = PackedBits.PackedBitsReader(option_bytes)
    for i in range(2, len(OptionsList)):
        optionvalue = OptionsList[i].get()
        if isinstance(optionvalue, bool):
            boolean_value = bool(bitsreader.read(1))
            OptionsList[i].set(boolean_value)
        elif isinstance(optionvalue, int):
            intvalue = bitsreader.read(8)
            OptionsList[i].set(intvalue)    
    return(seed, OptionsList)


def AddPermalinkTrace(traceObjects, permaLinkVar, seedEntryVar, version, stateUpdate):
    
    def PermalinkFromEntry():
        try:
            seedName, options = GenerateSettingsFromPermalink(permaLinkVar.get(), traceObjects)
            seedEntryVar.set(seedName)
            stateUpdate()
        except:
            print("Invalid Permalink")
    
    def PermalinkEntryUpdate():
        compressedPermalink = GenerateCompressedPermalink(seedEntryVar.get(), traceObjects, version)
        permaLinkVar.set(compressedPermalink)
        
    permaLinkVar.trace_add("write", lambda i,x,o: PermalinkFromEntry())
    for interactAble in traceObjects:
        try:
            interactAble.trace_add("write", lambda i,x,o: PermalinkEntryUpdate())
        except:
            pass
        
# dont include input folder and output folder entry in interactable
# dont calculate until no input for 1 second to stop lag typing
# it prints invalid permalink because when it deleted the link with seedEntry.delete