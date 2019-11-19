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

dna_file = "files/dna.fasta"
rna_file = "files/rna.fasta"
count_nucleotid_file = "files/count_nucleotid.fasta"
protein_table = "files/rna_codon_table.txt"
rna_transform_file = "files/rna_to_prot.txt"



def separate_gene(dna_file: str, my_dna_dict=None) -> dict:
    """Separate each gene

     The function separates each gene and converts the into a view
     dictionary and return dict - {gene name : str(Gene value)}
    """
    if my_dna_dict is None:
        my_dna_dict = {}

    with open(dna_file, 'r') as read_dna_file:
        for line in read_dna_file:
            if line.startswith(">"):
                key_dict = line.strip(">\n")
                my_dna_dict[key_dict] = ""
            else:
                my_dna_dict[key_dict] += line.strip()
    return my_dna_dict  # {name_gene: "nucleotides"}


# print(separate_gene(dna_file))  # uncomment here to check the function


def return_dict_count_nucleotid(dna_file: str, dict_count_nucleotid=None) -> dict:
    """ Return count nucleotid of gene

    The function modifies a dictionary containing genes to a view
    dict - {gene name : {name_nucleotides : count nucleotides}}
    """
    if dict_count_nucleotid is None:
        dict_count_nucleotid = {}
    for k, v in separate_gene(dna_file).items():  # use here func. separate_gene(dna_file)
        dict_count_nucleotid[k] = {i: v.count(i) for i in v}
        # print(dict_count_nucleotid)  # uncomment here to check the dict_count_nucleotid
    return dict_count_nucleotid  # {name_gene : {name_nucleotid : count_nucleotid}}


# print(return_dict_count_nucleotid(dna_file))  # uncomment here to check the function

def write_dna_statistic(count_nucleotid_file: str, dict_count_nucleotid: dict) -> None:
    """The function write in file on readable form

    Write on file:
    Name gene - Name nucleotides on gna - Count nucleotides etc.
    """
    with open(count_nucleotid_file, "w") as print_on_file:

        for name_gene, name_nucl in dict_count_nucleotid.items():
            print("\n{name_gene}".format(name_gene=name_gene),
                  file=print_on_file)

            for name_nucleotid, count_nucleotid in name_nucl.items():
                print(name_nucleotid, "-", count_nucleotid, file=print_on_file)


#  NOTE dna_file = "files/dna.fasta"
dicts_count_nucleotid = return_dict_count_nucleotid(dna_file)  # uncomment here to check the function

# print(dicts_count_nucleotid)  # uncomment here to check the result

# NOTE count_nucleotid = "files/count_nucleotid.fasta"
write_dna_statistic(count_nucleotid_file, dicts_count_nucleotid)  # uncomment here to check the function


def parser_for_matplotlib(dict_count_nucleotid) -> list:
    """ Function returns lists for paint hist using matplotlib

    This function breaks the dict_count_nucleotid -
    {name_gene : {name_nuc : count_nuc}} into 3 lists:
    with the name of the gene, the nucleotides it contains
    and the number of nucleotides of the RNA molecule
    """
    list_name_gene = list(dict_count_nucleotid.keys())
    dict_nucleotid_count = dict_count_nucleotid.values()
    tuple_name_and_dict_of_nucleotid_count = list(zip(list_name_gene, dict_nucleotid_count))

    list_of_count = [[] for i in enumerate(tuple_name_and_dict_of_nucleotid_count)]
    list_of_nucleotid = [[] for i in enumerate(tuple_name_and_dict_of_nucleotid_count)]

    for i in range(len(tuple_name_and_dict_of_nucleotid_count)):
        for nucleotid, count in tuple_name_and_dict_of_nucleotid_count[i][1].items():
            list_of_count[i].append(count)
            list_of_nucleotid[i].append(nucleotid)

    return list_of_count, list_of_nucleotid, list_name_gene


# args = parser_for_matplotlib(dicts_count_nucleotid)  # uncomment here to get the result
# print(args)  # uncomment here to get the result


def build_hists(*args) -> None:
    """Build hist using result dict_count_nucleotid

    Takes the result of the function parser_for_matplotlib,
    and build histogram. It takes the results from the function
    in the form of 3 lists.

    List list_of_count and list_of_nucleotid have nesting
    """

    list_of_count, list_of_nucleotid, list_name_gene = args
    n_groups = len(list_of_nucleotid[0])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    for i, name in enumerate(list_name_gene):
        if i % 2 == 0:
            color = "r"
        else:
            color = "b"
        plt.bar(index + i / 3, list_of_count[i], bar_width,
                alpha=opacity, color=color, label=list_name_gene[i])

    plt.xlabel('Nucleotides')
    plt.ylabel('Count')
    plt.title('Count of nucleotides')
    plt.xticks(index + bar_width, list_of_nucleotid[0])
    plt.legend()
    plt.tight_layout()
    plt.show()
    fig.savefig('hist.jpg')  # save your histogram here


# build_hists(*args)  # uncomment here to build the histogram


def translate_from_dna_to_rna(dna_file: str, rna_file: str) -> str:
    """The function reads dna from dna_files and
    changes it to rna with writing to a new file

    The function reads file 1, transfers the nucleotide
    sequence from dna to rna and returns the rna object
    """

    with open(dna_file, 'r') as file, open(rna_file, "w") as new_file:
        for line in file:
            if line.startswith(">"):
                pass
            else:
                line = line.replace("T", "U")
            new_file.write(line)
    rna_file_obj = open(rna_file, "r")
    rna = rna_file_obj.read()
    rna_file_obj.close()
    return rna



# print(translate_from_dna_to_rna(dna_file, rna_file))  # uncomment here to get the result

# dict = return_dict_count_nucleotid('file')
# list = parser_for_matplotlib(dict)
# count_nucleotides(*list)

def create_dict_nucleotid_sequence_and_codons(protein_table: str) -> dict:
    """Function creates a dictionary:
        {nucleotide sequence : codon}

        We use result this function for to convert rna
        into protein in the future for each rna gene sequence
        """
    nucleotid_sequence = []
    kodon_sequence = []
    with open(protein_table, "r") as protein_table_obj:
        for line in protein_table_obj:
            line = line.split()
            for i, v in enumerate(line):
                if i % 2 == 0:
                    nucleotid_sequence.append(v)
                else:
                    kodon_sequence.append(v)
        dict_nucleotid_sequence_and_codons = dict(zip(nucleotid_sequence, kodon_sequence))

    return dict_nucleotid_sequence_and_codons


# create_dict_nucleotid_sequence_and_codons(protein_table)  # uncomment here to get the result
# print(create_dict_nucleotid_sequence_and_codons(protein_table))  # uncomment here to get the result




def transalte_rna_to_prot(rna: str, nucleotid_codons: dict) -> str:
    """Function converts RNA data to protein

    The function uses the result dict_nucleotid_sequence_and_codons
    to match the nucleotide sequence in the RNA, matches and
    transformation them into the corresponding codon
    """
    rna_list = rna.split("\n")  # split the string and convert to a list it
    result_transformation_list = []  # final list for appending result of transformation into codon
    for i, v in enumerate(rna_list):
        if rna_list[i].startswith(">"):
            items = "\n" + rna_list[i] + "\n"  # gene name
        else:
            append_items = []  # the list is reset for each iteration elements of rna_list[i]
            for j in range(3, len(rna_list[i]) + 1, 3):
                check_symbol = rna_list[i][j - 3:j]  # check symbol for each 3 elements in rna_list[i]
                if check_symbol in nucleotid_codons:
                    # codon matches key check_symbol in dict nucleotid_codons
                    fit_codon = nucleotid_codons[check_symbol]
                    append_items.append(fit_codon)
            items = "".join(append_items)
        result_transformation_list.append(items)
    string_transformation = "\n".join(result_transformation_list)
    return string_transformation


# rna = translate_from_dna_to_rna(dna_file, rna_file)  # uncomment here to set the rna result
# dict_nucleotid_sequence_and_codons = \  # uncomment here for create dict_nucleotid_sequence_and_codons
#     create_dict_nucleotid_sequence_and_codons(protein_table)

# string_transformation = transalte_rna_to_prot(rna, dict_nucleotid_sequence_and_codons)
# uncomment here to save the  string_transformation result
# with open("files/rna_to_prot.txt", "w") as joinlist:
#                 joinlist.write(list)


if __name__ == "__main__":
    
    dicts_count_nucleotid = return_dict_count_nucleotid(dna_file)
    write_dna_statistic(count_nucleotid_file, dicts_count_nucleotid)

    args = parser_for_matplotlib(dicts_count_nucleotid)
    build_hists(*args)

    translate_from_dna_to_rna(dna_file, rna_file)

    rna = translate_from_dna_to_rna(dna_file, rna_file)
    create_dict_nucleotid_sequence_and_codons(protein_table)
    dict_nucleotid_sequence_and_codons = create_dict_nucleotid_sequence_and_codons(protein_table)
    string_transformation = transalte_rna_to_prot(rna, dict_nucleotid_sequence_and_codons)

    with open(rna_transform_file, "w") as rna_transformation:
                    rna_transformation.write(string_transformation)