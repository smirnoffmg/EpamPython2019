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
from collections import defaultdict


def read_codon_table(path_to_codon_table):
    with open(path_to_codon_table, "r") as file:
        data = file.read().split()
    table = dict(zip(data[::2], data[1::2]))
    return table


def read_dna_raw(path_to_dna_data):
    dna = {}
    dna_key = ""
    with open(path_to_dna_data, "r") as file:
        for line in file:
            line = line.rstrip()
            if line[0] == ">":
                dna_key = line[1:]
                dna[dna_key] = ""
            else:
                dna[dna_key] += line
        return dna


def write_data():
    for data in write_list:
        with open(f"files/result_{data}.txt", "w") as file:
            for k, v in (globals()[data]).items():
                if isinstance(v, dict):
                    for key_of_list, value_of_list in v.items():
                        file.write(f"{k}: {key_of_list}:{value_of_list}\n")
                if isinstance(v, list):
                    for item_of_list in v:
                        file.write(f"{k}: {item_of_list}\n")
                if isinstance(v, str):
                    file.write(f"{k}: {v}\n")


def translate_from_dna_to_rna(dna):
    rna = {}
    for key, value in dna.items():
        rna[key] = value.replace("T", "U")
    return rna


def count_nucleotides(dna):
    nucliotides_dict = defaultdict(lambda: defaultdict(int))
    for genes, nucliotides in dna.items():
        for gene in nucliotides:
            nucliotides_dict[genes][gene] += 1
    return nucliotides_dict


def translate_rna_to_protein(rna):
    protein = defaultdict(lambda: defaultdict(str))
    protein_by_genes = ""
    protein_data = []
    stop = ""
    start = ""
    for gene, nucleotides in rna.items():
        start = nucleotides.find("AUG")
        for nucleotide in range(
            start, len(nucleotides) - (3 - len(nucleotides) % 3), 3
        ):
            if table[nucleotides[nucleotide : nucleotide + 3]] == "Stop":
                stop = nucleotide
                start = nucleotides.find("AUG", stop + 3)
                if not protein_by_genes:
                    pass
                else:
                    protein_data.append(protein_by_genes)
                protein_by_genes = ""
                continue
            else:
                protein_by_genes += table[nucleotides[nucleotide : nucleotide + 3]]
        protein[gene] = protein_data
    return protein


if __name__ == "__main__":
    path_to_dna_data = "files/dna.fasta"
    path_to_codon_table = "files/rna_codon_table.txt"
    write_list = ("rna", "count_by_gene", "protein")

    table = read_codon_table(path_to_codon_table)
    dna = read_dna_raw(path_to_dna_data)
    rna = translate_from_dna_to_rna(dna)
    count_by_gene = count_nucleotides(dna)
    protein = translate_rna_to_protein(rna)
    write_data()



