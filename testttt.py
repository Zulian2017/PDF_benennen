#instrumentelist = ["Piccolo","Flöte","Oboe","Fagott","Bassoon","Klarinette","Altklarinette","Bassklarinette","Altsaxophon","Tenorsaxophon","Baritonsaxophon","Horn","Flügelhorn","Cornet","Trompete","Trumpet","Tenorhorn","Posaune","Bass","Tuba","Schlagzeug","Drums"]
#
#print(instrumentelist)
#
#for i in range(len(instrumentelist)):
#    print(instrumentelist[i])


instr = open("/home/kali/Documents/Test PDF/new/instrumente.txt")
resul = open("/home/kali/Documents/Test PDF/new/Clarinet.txt")

spl_instr = []
spl_resul = []

text_instr = instr.read()
text_resul = resul.read()

spl_instr = text_instr.split()
spl_resul = text_resul.split("\n")

find = 0

for i in range(len(spl_resul)):
    for j in range(len(spl_instr)):
        if spl_resul[i] is spl_instr[j]:
            print(spl_instr[j])
            find = 1
    if "(" in spl_resul[i]: 
        print(spl_resul[i])
    if find == 1:
        break

find = 0
