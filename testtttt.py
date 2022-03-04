resul = open("/home/kali/Documents/Test PDF/new/Clarinet.txt")
spl_instr = []
spl_resul = []

text_resul = resul.read()

spl_resul = text_resul.split("\n")

for i in range(len(spl_resul)):
    print(spl_resul[i])