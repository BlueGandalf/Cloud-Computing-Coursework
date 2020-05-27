file = open("2018.csv","r")
fileb = open("testdata.csv","w+")
lines = file.readlines()
for line in lines:
    line.strip()
    words = line.split(",")
    if(words[0] == "UK000056225"):
        fileb.write(line)