from random import choice
translated = """
A = r, c     B = o         Ο = g        Φ = u
E = e        Δ = n         Σ = s        ς = a
θ = l        Π = i         X = g        M = m
H = f        Λ = r         I = p        T = t
N = d        Ξ = v         Z = z
good evening
ΟΦEΔ ΣΔBAΦEΣ
 
A partir da linguagem uore uma linguagem formal regular
ς ΙςΛTΠΛ Nς θΠΔXΦςXEM ΦBΛE ΦMς θΠΔXΦςXEM HBΛMςθ ΛEXΦθςΛ
 
desenvolvida na aula passada desenvolva um automato finito
NEΣEΔΞBθΞΠNς Δς ςΦθς IςΣΣςNς NEΣEΔΞBθΞς ΦM ςΦTBMςTB HΠΔΠTB
 
deterministico para um elevador configuravel sem memoria para
NETEΛMΠΔΠΣTΠAB IςΛς ΦM EθEΞςNBA ABΔHΠXΦΛςΞEθ ΣEM MEMBΛΠς IςΛς
 
um predio de dez andares professor
ΦM IΛENΠB NE NEZ ςΔNςΛEΣ IΛBHEΣΣBΛ
"""
 
 
def encrypt(tmp_input):
    tmp = list(tmp_input)
    for i, letter in enumerate(tmp):
        if letter == "a":
            tmp[i] = "ς"
        if letter == "c":
            tmp[i] = "A"
        if letter == "d":
            tmp[i] = "N"
        if letter == "e":
            tmp[i] = "E"
        if letter == "f":
            tmp[i] = "H"
        if letter == "g":
            tmp[i] = "X"
        if letter == "i":
            tmp[i] = "Π"
        if letter == "l":
            tmp[i] = "θ"
        if letter == "m":
            tmp[i] = "M"
        if letter == "n":
            tmp[i] = "Δ"
        if letter == "o":
            tmp[i] = "B"
        if letter == "p":
            tmp[i] = "I"
        if letter == "r":
            tmp[i] = choice(["Λ", "A"])
        if letter == "s":
            tmp[i] = "Σ"
        if letter == "t":
            tmp[i] = "T"
        if letter == "u":
            tmp[i] = "Φ"
        if letter == "v":
            tmp[i] = "Ξ"
        if letter == "z":
            tmp[i] = "Z"
    print("".join(tmp))
while True:
    x = input("Digite a frase a ser codificada" +
              "\n(sem quebra de linha, sem acentuação e sem letras minúsculas)\n")
    encrypt(x)
    print("")
