import re


decompressed = ""
currIndex = 0
with open("inputs/9") as f:
    lines = f.read()
    markers = re.findall(r"\((.*?)\)", lines)
    for marker in markers:
        markerIndex = lines.find(marker, currIndex)
        if marker == markers[-1]:
            decompressed += lines[currIndex:markerIndex]
            print("Adding " + lines[currIndex:markerIndex])
        else:
            decompressed += lines[currIndex:markerIndex-1]
            print("Adding " + lines[currIndex:markerIndex-1])
        if markerIndex < currIndex:
            print("Skipping " + marker)
            continue
        size = int(marker.split("x")[0])
        repeats = int(marker.split("x")[1])
        start = markerIndex + len(marker)+1
        end = markerIndex + len(marker) + 1 + size
        print(lines[start:end] + " repeats " + str(repeats) + " times")
        for j in range(repeats):
            decompressed += lines[start:end]
            print("Adding " + lines[start:end])
        currIndex = end
#    decompressed += lines[currIndex+1:]
    print(decompressed)
    print(len(decompressed)-1)
