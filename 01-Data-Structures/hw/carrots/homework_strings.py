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

import numpy as np
import matplotlib.pyplot as plt

gene_file = "files/dna.fasta"
count_nucleo = "files/count_nucleo.fasta"

def separate_gene(gene_file: str, my_dna_dict=None) -> dict:
    """Separate each gene

     The function separates each gene and converts the into a view
     dictionary and return dict - {gene name : str(Gene value)}
    """
    if my_dna_dict is None:
        my_dna_dict = {}

    with open(gene_file, 'r') as read_gene_file:
        for line in read_gene_file:
            if line.startswith(">"):
                key_dict = line.strip(">\n")
                my_dna_dict[key_dict] = ""
            else:
                my_dna_dict[key_dict] += line.strip()
    return my_dna_dict  # {name_gene: "nucleotides"}


# print(separate_gene(gene_file))  # uncomment here to check the function

# def f(gene_file: str, dict_dna=None, dict_count_elements=None):
#
#     if dict_dna is None:
#         dict_dna = {}
#     with open(gene_file, "r") as read_gene_file:
#         for line in read_gene_file:
#             if line.startswith(">"):
#                 key_dict = line.strip(">\n")
#                 dict_dna[key_dict] = ""
#             else:
#                 dict_dna[key_dict] += line.strip()
#         # print(dict_dna)  # uncomment here to check the dict_dna
#
#     if dict_count_elements is None:
#         dict_count_elements = {}
#     for k, v in dict_dna.items():  # use here func. separate_gene(gene_file)
#         dict_count_elements[k] = {i: v.count(i) for i in v}
#
#     return dict_count_elements
# print(f(gene_file))

def return_dict_count_nucleotid(gene_file: str, dict_count_nucleotid=None) -> dict:
    """ Return count nucleotid of gene

    The function modifies a dictionary containing genes to a view
    dict - {gene name : {name_nucleotides : count nucleotides}}
    """
    if dict_count_nucleotid is None:
        dict_count_nucleotid = {}
    for k, v in separate_gene(gene_file).items():  # use here func. separate_gene(gene_file)
        dict_count_nucleotid[k] = {i: v.count(i) for i in v}
        # print(dict_count_nucleotid)  # uncomment here to check the dict_count_nucleotid
    return dict_count_nucleotid  # {name_gene : {name_nuc : ciunt_nuc}}


# print(return_dict_count_nucleotid(gene_file))  # uncomment here to check the function

def write_dna_statistic(count_nucleo: str, dict_count_nucleotid: dict) -> None:
    """The function write in file on readable form

    Write on file:
    Name gene - Name nucleotides on gna - Count nucleotides etc.
    """
    with open(count_nucleo, "w") as print_on_file:

        for name_gene, name_nucl in dict_count_nucleotid.items():
            print("\n{name_gene}".format(name_gene=name_gene),
                  file=print_on_file)

            for name_nucleo, count_nucleo in name_nucl.items():
                print(name_nucleo, "-", count_nucleo, file=print_on_file)


#  NOTE gene_file = "files/dna.fasta"
dicts_count_nucleotid = return_dict_count_nucleotid(gene_file)  # uncomment here to check the function
# print(dicts_count_nucleotid)  # uncomment here to check the result
# NOTE count_nucleo = "files/count_nucleo.fasta"
# write_dna_statistic(count_nucleo, dicts_count_nucleotid)  # uncomment here to check the function


def parser_for_matplotlib(dict_count_nucleotid) -> list:
    """ Function returns lists for paint hist using matplotlib

    Function return n nested list in lists
    """
    name_genes = list(dict_count_nucleotid.keys())
    word_count_dict = dict_count_nucleotid.values()
    name_and_dict_of_word_count = list(zip(name_genes, word_count_dict))

    list_of_count = [[] for i in enumerate(name_and_dict_of_word_count)]
    list_of_word = [[] for i in enumerate(name_and_dict_of_word_count)]

    for i in range(len(name_and_dict_of_word_count)):
        for word, count in name_and_dict_of_word_count[i][1].items():
            list_of_count[i].append(count)
            list_of_word[i].append(word)

    return list_of_count, list_of_word, name_genes  # list_names


args = parser_for_matplotlib(dicts_count_nucleotid)  # uncomment here to get the result
# print(args)  # uncomment here to get the result


def build_hists(*args):
    """Build hist using result dict_count_nucleotid

    Takes the result of the function parser_for_matplotlib, and build hist
    """
    number_of_latters, letters_themselves, name_gene = args
    n_groups = len(letters_themselves[0])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    for i, name in enumerate(name_gene):
        if i % 2 == 0:
            color = "r"
        else:
            color = "b"
        plt.bar(index + i / 3, number_of_latters[i], bar_width,
                alpha=opacity, color=color, label=name_gene[i])

    plt.xlabel('Nucleotides')
    plt.ylabel('Count')
    plt.title('Count of nucleotides')
    plt.xticks(index + bar_width, letters_themselves[0])
    plt.legend()
    plt.tight_layout()
    plt.show()
    fig.savefig('hist.jpg')


# build_hists(*args)  # uncomment here to build the histogram


def translate_from_dna_to_rna(dna):
    """your code here"""

    with open(dna, 'r') as file, open("files/replace.fasta", "w") as new_file:
        for line in file:
            if line.startswith(">"):
                pass
            else:
                line = line.replace("T", "U")
            new_file.write(line)
    rna_file = open("files/replace.fasta", "r")
    rna = rna_file.read()
    rna_file.close()
    return rna


# print(translate_from_dna_to_rna(gene_file))  # uncomment here to get the result
# rna = translate_from_dna_to_rna(gene_file)  # uncomment here to set the rna result


def count_nucleotides(*dna):
    """your code here"""
    pass


# dict = return_dict_count_nucleotid('file')
# list = parser_for_matplotlib(dict)
# count_nucleotides(*list)

def translate_rna_to_protein(rna, protein_table):
    """your code here"""
    list_name = []
    list_key = []
    main_dict = {}
    with open(protein_table, "r") as protein_file:
        for line in protein_file:
            line = line.split()
            local_dict = {line[i - 1]: line[i] for i in range(1, len(line), 2)}
            main_dict.update(local_dict)
            for i, v in enumerate(line):
                if i % 2 == 0:
                    list_name.append(v)
                else:
                    list_key.append(v)
            zip_obj = list(zip(list_name, list_key))
        dict_of_codons = dict(zip_obj)
        # print(dict_of_codons)
        # print(main_dict)

    return dict_of_codons
    # return protein


# protein_table = "files/rna_codon_table.txt"
# translate_rna_to_protein(rna, protein_table)

# dict_codons = translate_rna_to_protein(rna, protein_table)


def transalte_rna_to_prot(rna, codons):
    """

    """
    rna = rna.split("\n")
    list = []
    for i, v in enumerate(rna):
        if rna[i].startswith(">"):
            items = "\n" + rna[i] + "\n"
        else:
            append_items = []
            for j in range(3, len(rna[i]) + 1, 3):
                check_simbol = rna[i][j - 3:j]
                if check_simbol in codons:
                    value = codons[check_simbol]
                    append_items.append(value)
            items = "".join(append_items)
        list.append(items)
    list = "\n".join(list)
    return list

# list = transalte_rna_to_prot(rna, dict_codons)
# with open("files/rna_to_prot.txt", "w") as joinlist:
#                 joinlist.write(list)
