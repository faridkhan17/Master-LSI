
def write_fasta(outfile, head, seq):
    if outfile.tell() == 0:
        outfile.write(head)
    else:
        outfile.write('\n' + head)
    for j in range(0, len(seq), 70):
        outfile.write('\n' + seq[j:j + 70])


def fasta_list(filename):
    a = []
    for i in filename:
        i = i.rstrip('\n')
        if i[0] == ">":
            i = '*' + i[1:] + '*'
        a.append(i)
    a = ''.join(a)
    h = a.split('*')[1:]
    ll = []
    for f in range(0, len(h), 2):
        ll.append((h[f], h[f + 1]))
    return ll


def complement_seq(sequence):
    seq = ''
    for j in sequence:
        if j == "A":
            seq += "T"
        elif j == "T":
            seq += "A"
        elif j == "C":
            seq += "G"
        else:
            seq += "C"
    return seq


def orf_finder(filename, outfile):
    def codon_checker(position, triplet):
        if triplet == 'ATG' and not openframe[position]:
            start = ''
            if position < 3:
                orf_start = '+' + str(i + 1 + position) + '+'
            else:
                orf_start = '+c' + str(len(sequence) - i - position + 3) + '+'
            seq[position] += '*' + orf_start
            openframe[position] = True
        elif triplet in ['TAA', 'TAG', 'TGA'] and openframe[position]:
            orf_stop = ''
            if position < 3:
                orf_stop = '+' + str(i + 3 + position) + '+'
            else:
                orf_stop = '+' + str(len(sequence) - i + 1 - position) + '+'
            seq[position] += triplet + orf_stop + '*'
            openframe[position] = False

        if openframe[position]:
            seq[position] += triplet

    with open(outfile, 'w') as fw:
        with open(filename, 'r') as f:
            openframe = [False for _ in range(6)]
            seq = ['' for _ in range(6)]
            for head, sequence in fasta_list(f):
                cdna_codon = complement_seq(sequence)[::-1]
                for i in range(0, len(sequence), 3):
                    codon_checker(0, sequence[i:i + 3])
                    codon_checker(1, sequence[i + 1:i + 4])
                    codon_checker(2, sequence[i + 2:i + 5])

                    codon_checker(3, cdna_codon[i:i + 3])
                    codon_checker(4, cdna_codon[i + 1:i + 4])
                    codon_checker(5, cdna_codon[i + 2:i + 5])
                for i in set("".join(seq).split('*')):
                    if len(i) > 6 and i[-1:] == '+':
                        i = i.split('+')
                        write_fasta(fw, "|".join(head.split('|')[:-1]) + '|:' + i[1] + '-' + i[3], i[2])


orf_finder("ecoli-genome-sample.fna", "openrf.txt")
