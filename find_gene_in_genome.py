__author__ = 'rhenium'

from Bio import SeqIO
from Bio.SeqRecord import  SeqRecord
def find_gene(ref, contig, gene_name, start, stop):
    fasta_dict = SeqIO.to_dict(SeqIO.parse(ref, 'fasta'))
    #print fasta_dict.keys()[0], fasta_dict[fasta_dict.keys()[0]]
    #contig = 'contig00089'
    #print fasta_dict[contig], fasta_dict[contig][::-1], fasta_dict[contig][3:12], fasta_dict[contig].seq.count('\n')
    gene_seq = fasta_dict[contig].seq[start: stop]
    return SeqRecord(seq=gene_seq,
                     id=gene_name,
                     description='')

path_to_ref = '/home/rhenium/work/bacterial_genomes/assemb_newbler/assembly/454AllContigs.fna'
of = '/home/rhenium/work/bacterial_genomes/trans_Ps.fasta'
SeqIO.write(find_gene(path_to_ref, contig='contig00051', start=28625, stop=29144, gene_name='P_syringae_2507 [ trans ]'),
            of, 'fasta')
