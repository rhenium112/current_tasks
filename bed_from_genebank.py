#!/usr/bin/env python
# encoding: utf-8
"""
bed_from_genbank.py

grab the gene records from a genbank file (edit for other record types).

- requires:  biopython

"""
 
from Bio import SeqIO
import sys
 
import pdb
 
def main():
    outf = open('/home/rhenium/work/bacterial_genomes/annotation/RAST/Pseudomonas_syringae_B728a.bed', 'w')
    header = """track name=vitVinGenes description="V. vinifera cpdna genes" itemRgb=On\n"""
    outf.write(header)
    for record in SeqIO.parse(open("/home/rhenium/work/bacterial_genomes/sequence.gb", "rU"), "genbank") :
        #print record
        #print record.name
        #sys.exit()
        for feature in record.features:
            #print feature
            #sys.exit()
            if feature.type == 'CDS' or feature.type == 'tRNA' or feature.type == 'rRNA':
                #print feature
                #sys.exit()
                start = feature.location.start.position
                stop = feature.location.end.position
                try:
                    name = feature.qualifiers['product'][0]
                except:
                    # some features only have a locus tag
                    #name = feature.qualifiers['locus_tag'][0]
                    pass
                if feature.strand < 0:
                    strand = "-"
                else:
                    strand = "+"
                bed_line = "{4}\t{0}\t{1}\t{3}\t{2}\n".format(start, stop, name, strand, record.name)
                outf.write(bed_line)
    outf.close()
 
 
if __name__ == '__main__':
    main()
