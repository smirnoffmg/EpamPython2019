"""

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
import matplotlib.pyplot as plt


# read the file dna.fasta
dna_temp = open("./files/dna.fasta", "r")
dna = dna_temp.read()
dna_temp.close()


def translate_from_dna_to_rna(dna):
    genes = dna.split('>')
    del genes[0]
    rna = open("./files/rna.txt", "w")
    for gene in genes:
        gene = gene.split('\n', maxsplit=1)
        gene[1] = gene[1].replace('T', 'U')
        rna.write(f">{gene[0]}\n{gene[1]}")
    rna.close()
    return rna


def histogram(data, name):
    xdata, ydata = [], []
    for key, value in data.items():
        xdata.append(key)
        ydata.append(value)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(xdata, ydata)
    ax.set_xlabel('Nucleotids')
    ax.set_ylabel('Count of nucleotids')
    ax.set_title(f'Gene name: {name}')
    plt.savefig(f'./hists/{name}.png', bbox_inches='tight')

def count_nucleotides(dna):
    genes = dna.split('>')
    num_of_nucleotides = open("./files/num_of_nucleotides", "w")
    del genes[0]
    for gene in genes:
        gene = gene.split('\n', maxsplit=1)
        gene_name = gene[0].split(' ')[0]
        count_a = gene[1].count('A')
        count_c = gene[1].count('C')
        count_g = gene[1].count('G')
        count_t = gene[1].count('T')
        gene_num = {'A': count_a, 'C': count_c, 'G': count_g, 'T': count_t}
        histogram(gene_num, gene_name)
        num_of_nucleotides.write(f"{gene_name}: ")
        for key, value in gene_num.items():
            num_of_nucleotides.write(f"{key} - {value}, ")
        num_of_nucleotides.write("\n")

    num_of_nucleotides.close()
    return num_of_nucleotides


def translate_rna_to_protein(rna):
    rna_codon_table = open("./files/rna_codon_table.txt", "r")
    alphabet = rna_codon_table.read()
    rna_codon_table.close()
    rna = open("./files/rna.txt", "r")
    rna_temp = rna.read()
    rna.close()
    alphabet = alphabet.strip().replace(' ', '#')
    alphabet = alphabet.replace('######', ' ')
    alphabet = alphabet.replace('###', ' ')
    alphabet = alphabet.split('\n')
    alphabet = [s.strip() for s in alphabet]
    for i in range(len(alphabet)):
        alphabet[i] = alphabet[i].split(' ')
    alphabet = [val for sublist in alphabet for val in sublist]
    alphabet = dict([s.split('#') for s in alphabet])
    rna_temp = rna_temp.split('>')
    del rna_temp[0]
    protein = open("./files/protein.txt", 'w')
    for gene in rna_temp:
        gene = gene.split('\n', maxsplit=1)
        gene[1] = gene[1].replace('\n', '')
        substr = [gene[1][x:x + 3] for x in range(0, len(gene[1]), 3)]
        if len(substr[-1]) < 3:
            substr[-1] = ''
        for i in range(len(substr)):
            for key in alphabet.keys():
                if substr[i] == key:
                    substr[i] = alphabet.get(key)
        protein.write(f">{gene[0]}\n{''.join(substr)}\n")
    protein.close()
    return protein


count_nucleotides(dna)
rna = translate_from_dna_to_rna(dna)
translate_rna_to_protein(rna)
