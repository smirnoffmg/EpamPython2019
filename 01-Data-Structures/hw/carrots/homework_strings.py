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

dna = None

def separate_gen(gene_file: str, my_dna_dict = None) -> dict:
    """
     The function separates each gene and converts the into a view
     dictionary and return dict - {gene name : Gene value}
    """
    if my_dna_dict is None:
        my_dna_dict = {}
    with open(gene_file, 'r') as new:
        for line in new:
            if line.startswith('>'):
                key_dict = line.strip('>\n')
                my_dna_dict[key_dict] = ""
            else:
                my_dna_dict[key_dict] += line.strip()
    return my_dna_dict


def return_dict_count_elements(file: str, dict_count_elements=None) -> dict:
    """
    The function modifies a dictionary containing genes to a view
    dict - {gene name : count nucleotides}
    """
    if dict_count_elements is None:
        dict_count_elements = {}
    for k, v in separate_gen(file).items():
        dict_count_elements[k] = {i: v.count(i) for i in v}
    return dict_count_elements


# print(return_dict_count_elements('files/dna.fasta'))


def translate_from_dna_to_rna(dna):

    """your code here"""

    # return rna
    pass

def count_nucleotides(dna):

    """your code here"""

    # return num_of_nucleotides
    pass



# with open ('files/dna.fasta', 'r') as file:
#     file = file.readlines()
#     for i, line in enumerate(file):
#         print(i)
#         print(line)

        # line = line.lstrip('\n')
        # line = line.rstrip('\n')
    # file = file.split('>', maxsplit=1)
# print(file)


def translate_rna_to_protein(rna):
    
    """your code here"""
    
    # return protein
    pass