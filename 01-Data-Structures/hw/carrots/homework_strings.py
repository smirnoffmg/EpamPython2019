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


def separate_gen(gene_file: str, my_dna_dict = None) -> dict:
    """Separate each gene

     The function separates each gene and converts the into a view
     dictionary and return dict - {gene name : Gene value}
    """
    if my_dna_dict is None:
        my_dna_dict = {}
    with open(gene_file, 'r') as read_gene_file:
        for line in read_gene_file:
            if line.startswith('>'):
                key_dict = line.strip('>\n')
                my_dna_dict[key_dict] = ""
            else:
                my_dna_dict[key_dict] += line.strip()
    return my_dna_dict


def return_dict_count_elements(file: str, dict_count_elements=None) -> dict:
    """ Return count elements of gene

    The function modifies a dictionary containing genes to a view
    dict - {gene name : count nucleotides}
    """
    if dict_count_elements is None:
        dict_count_elements = {}
    for k, v in separate_gen(file).items():
        dict_count_elements[k] = {i: v.count(i) for i in v}
    return dict_count_elements


# print(return_dict_count_elements('files/dna.fasta'))


def parser_for_matplotlib(dict) -> list:
    """ Function returns lists for paint hist using matplotlib

    Function return n nested list in lists
    """
    name_genes = list(dict.keys())
    word_count_dict = dict.values()
    name_and_dict_of_word_count = list(zip(name_genes, word_count_dict))

    list_of_count = [[] for i in enumerate(name_and_dict_of_word_count)]

    list_of_word = [[] for i in enumerate(name_and_dict_of_word_count)]
    for i in range(len(name_and_dict_of_word_count)):
        for word, count in name_and_dict_of_word_count[i][1].items():
            list_of_count[i].append(count)
            list_of_word[i].append(word)

    # list_of_names = [[] for i in enumerate(name_and_dict_of_word_count)]
    # for i, item in enumerate(name_and_dict_of_word_count):
    #     list_of_names[i].append(item[0])

    return list_of_count, list_of_word, name_genes #list_of_names



def build_hists(*args):
    """Build hist using result dict_count_elements

    Takes the result of the function parser_for_matplotlib, and build hist
    """
    number_of_latters, letters_themselves, name_genes = args
    n_groups = len(letters_themselves[0])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    for i, name in enumerate(name_genes):
        if i % 2 == 0:
            color = "r"
        else:
            color = "b"
        plt.bar(index+i/3, number_of_latters[i], bar_width, alpha=opacity, color=color, label=name_genes[i])

    plt.xlabel('Nucleotides')
    plt.ylabel('Count')
    plt.title('Count of nucleotides')
    plt.xticks(index + bar_width, letters_themselves[0])
    plt.legend()

    plt.tight_layout()
    plt.show()
    fig.savefig('hist.jpg')



def translate_from_dna_to_rna(dna):

    """your code here"""

    with open(dna, 'r') as file, open("files/replace.fasta", "w") as new_file:
        for line in file:
            if line.startswith(">"):
                continue
            else:
                line = line.replace("T", "U")
            new_file.write(line)


def count_nucleotides(*dna):

    """your code here"""
    list_of_count, list_of_word, name_genes = dna
    for i, value in enumerate(name_genes):
        a = value
        b = "{A} = {B}".format(A=[w for w in enumerate(list_of_word[i])],
                               B=[k for k in enumerate(list_of_count[i])])
        print(b)


# dict = return_dict_count_elements('files/dna.fasta')
# list = parser_for_matplotlib(dict)
# count_nucleotides(*list)

def translate_rna_to_protein(rna):

    """your code here"""

    # return protein
    pass


