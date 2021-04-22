FL=open('python pic\link.txt','r',encoding="utf-8")
s=FL.read()
linkk=[]
for i in range(146):
    si=s.split()
    sii=si[i]
    linkk.append('"'+sii+'"')

print(linkk)
