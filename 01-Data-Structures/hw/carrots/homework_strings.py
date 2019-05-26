""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
dna = open("dna.fasta.txt", "r")
rna = open("rna_codon_table.txt", "r")
dna_read = dna.read()
#dna_readlines = dna.readlines()
#print(dna.readlines)
dna_read_list = dna_read.split("\n")
#print(dna_read_list)
rna.close()
dna.close()

def translate_from_dna_to_rna(dna):
    rna = ""
    dna_str = ""
    for l in dna_read_list:
        if l[0] != ">":
            dna_str = dna_str + l
            
    for l in dna_str:
       for z in (str(l)):
           if z == "T":
               z = "U"
           rna  = rna + z
    file = open("rna.txt", "w")
    file.write(str(rna))
    file.close()	
    return rna


def count_nucleotides(dna):
    
    dna_str = ""
    for l in dna_read_list:
        if l[0] != ">":
            dna_str = dna_str + l
		  
    A,G,T,C = 0,0,0,0
    for z in dna_str:
        if z == "A":
            A = A + 1
        elif z == "G":
            G = G + 1
        elif z == "T":
            T = T + 1
        elif z == "C":
            C = C + 1
    num_of_nucleotides = "A - " + str(A) + " G - "  + str(G) + " T - "  + str(T) + " C - " + str(C)
    file = open("dna.txt", "w")
    file.write(str(num_of_nucleotides))
    file.close()
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    protein_str = ""
    protein_list = []
    for l in rna:
        a = (str(l)).split("\n")
        protein_list.append(a)
    #print(protein_list)
    
    m = []
    for z in protein_list:
        for n in z:
            m.append(z[0])
    #print(m)

    x = []
    for t in m:
        x.append(str(t).split(" "))
    #print(x)
    
    rna = ""
    for i in x:
        for z in i:
            if len(z) == 1 or len(z) == 4:
                rna = rna + z + " "            
        
    #print(rna)
    file = open("rna_codon.txt", "w")
    file.write(rna)
    file.close()
    return rna

translate_rna_to_protein(rna)
count_nucleotides(dna)
translate_from_dna_to_rna(dna)

