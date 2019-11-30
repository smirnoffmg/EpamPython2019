import json

# with open("winedata_2.json", "r") as winedata_2, open("serialize_winedata_2.json", "w") \
#         as serialize_winedata_2:
    # deserialize_winedata_1 = json.load(winedata_1)
    # deserialize_winedata_2 = json.load(winedata_2)
    # serialize_winedata_2 = json.dump(deserialize_winedata_2, serialize_winedata_2)

# print(deserialize_winedata_1)
# print(deserialize_winedata_2)
# print("type", type(deserialize_winedata_2))
# print(serialize_winedata_2)
# print("type", type(serialize_winedata_2))

# with open("winedata_2.json", "r") as winedata_2_read:
#     for line in winedata_2_read:
#         new_line = line.split()
#         print("new_line", new_line)

import matplotlib.pyplot as plt
import numpy as np
import re


def split_file(lines):
    gene_nucleotides = ''
    for i in lines:
        gene_nucleotides += i
    gene_nucleotides = gene_nucleotides.strip('>')
    splitted_lines = str(gene_nucleotides).split('>')

    return splitted_lines


def translate_from_dna_to_rna(dna):
    rna = []
    splitted_lines = split_file(dna)
    output_file = open('./files/translation_from_dna_to_rna.txt', 'w')

    for i in range(len(splitted_lines)):
        curr_line = splitted_lines[i]
        ind_name = curr_line.find('\n')
        gene_name = str(curr_line)[:ind_name]
        curr_dna = str(curr_line)[ind_name:]
        curr_rna = curr_dna.replace('T', 'U')
        rna.append(curr_rna)

        output_file.write(f'>{gene_name}')
        output_file.write(f'{curr_rna} \n')

    output_file.close()

    return rna


def count_nucleotides_for_gene(curr_line, output_file):
    nucleotides = ['A', 'C', 'G', 'T']
    gene_dict = dict.fromkeys(nucleotides, 0)

    ind_name = curr_line.find('\n')
    gene_name = str(curr_line)[:ind_name]
    gene_nucleotides = str(curr_line)[ind_name:]
    output_file.write(f'>{gene_name} \n')

    for i in nucleotides:
        gene_dict[i] = gene_nucleotides.count(i)
        output_file.write(f'{i} - {gene_dict[i]} ')
    output_file.write('\n')

    return gene_dict


def count_nucleotides(dna):
    num_of_nucleotides = []
    output_file = open('./files/num_of_nucleotides.txt', 'w')

    splitted_lines = split_file(dna)

    for i in range(len(splitted_lines)):
        gene_dict = count_nucleotides_for_gene(splitted_lines[i], output_file)
        num_of_nucleotides.append(gene_dict)

    output_file.close()

    return num_of_nucleotides


def translate_rna_to_protein(rna):
    rna_codon_table = open('./files/rna_codon_table.txt', 'r')
    lines = rna_codon_table.readlines()
    rna_codon_table.close()
    output_file = open('./files/translation_rna_to_protein.txt', 'w')
    codons = []
    new_values = []

    for line in lines:
        line = line.replace('\n', '')
        for codon in re.finditer(r'[U,A,C,G]{3}', line):  # finding codons
            codons.append(codon[0])
            line = line.replace(codon[0], '')

        for value in re.finditer(r'[^ ]+', line):  # finding new codons' values
            if value[0] != '':
                new_values.append(value[0])

    rules_to_translate = dict(zip(tuple(codons), tuple(new_values)))

    protein = []
    for i in range(len(rna)):
        curr_protein = ''
        j = 0
        curr_str = rna[i].replace('\n', '')
        while j < len(curr_str) - 3:
            curr_codon = curr_str[j:j + 3]
            j += 3
            curr_protein += rules_to_translate[curr_codon]
            curr_protein += ' '
        output_file.write(f'{curr_protein} \n')
        protein.append(curr_protein)

    output_file.close()

    return protein


def make_chart(num_of_nucleotides):
    x = []
    y = []
    fig, ax = plt.subplots()
    size = len(num_of_nucleotides)

    for i in range(size):
        if i == 0:
            x.append(num_of_nucleotides[i].keys())
        else:
            x.append(np.arange(0, len(num_of_nucleotides[i])) + 0.2 * i)
        y.append(num_of_nucleotides[i].values())
        ax.bar(x[i], y[i], width=0.2)

    ax.set_facecolor('whitesmoke')
    fig.set_figwidth(10)
    fig.set_figheight(5)

    plt.show()


dna = open('./files/dna.fasta', 'r')
lines = dna.readlines()
dna.close()
num_of_nucleotides = count_nucleotides(lines)
rna = translate_from_dna_to_rna(lines)
translate_rna_to_protein(rna)
make_chart(num_of_nucleotides)