#! /usr/local/bin/python
"""
    SJS.
    Prepare data for input to HyPhy, using mafft to align sequences (align amino acid and back translate to nucleotide) and FastTree to construct the phylogeny.
    Usage: python prepare_data.py <infile> [optional arguments]. To see optional arguments and full instructions, enter python align.py -h/--help .
    
    Dependencies:
        mafft and FastTree need to be installed and in your path! 
"""

import os
import sys
import argparse
import subprocess
from random import randint
from Bio import Seq
from Bio import SeqIO
from Bio.Alphabet import generic_dna


class HyPhyPrep():
    def __init__(self, infile):

        self.infile = infile
        
        prefix = "".join( self.infile.split(".")[:-1] )
        
        self.alnfile = prefix + "_aligned.fasta"
        self.treefile = prefix + "_tree.tre"
        self.hyphyfile = prefix + "_hyphy_input.dat"

        self.sequence_dictionaries = {'protein':{}, 'nucleotide':{}}
        self.parsed_alignment = []
        x = randint(1,1e5)
        self.mafft_infile = str(x) + ".fasta"
        self.mafft_outfile = str(x+1) + ".fasta"

        self.parse_translate_infile()
        self.perform_alignment()
        self.pal_to_nal()
        self.construct_tree()
        os.system("cat " + self.alnfile + " " + self.treefile + " > " + self.hyphyfile)
        os.remove(self.mafft_infile)
        os.remove(self.mafft_outfile)
        print("\nComplete! Your input file for HyPhy analysis is in " + self.hyphyfile + ". The individual alignment and phylogeny are available in " + self.alnfile + " and " + self.treefile + ", respectively.")

    def parse_translate_infile(self):
        """
            Parse the input sequence file and translate to amino acid sequence.
            Save a dictionary of the nucleotide and amino acid sequences.
        """
        ## Load
        nuc_dict = {}
        try:
            records = list(SeqIO.parse(self.infile, 'fasta'))
        except:
            raise AssertionError("Sequences must be provided in FASTA format.")
        for rec in records:
            nuc_dict[str(rec.id)] = str(rec.seq)
            
        ## Translate
        prot_dict = {}
        for entry in nuc_dict:
            nuc_dict[entry] = nuc_dict[entry].replace('-','') # Remove any possible gaps in nucleotide sequence
            nucseq = nuc_dict[entry]
            assert(len(nucseq)%3 == 0), "\n\nERROR: Nucleotide sequence length is not a multiple of three.."

            prot_seq = ''
            for i in range(0,len(nucseq),3):
                codon = nucseq[i:i+3]
                try:
                    amino = str( Seq.Seq(codon, generic_dna).translate() )
                except:
                    raise AssertionError("\n\nERROR: Input codon cannot be translated.")
                if amino == '*':
                    # If stop codon is the last codon, just remove it
                    if i == len(nucseq)-3:
                        nuc_dict[entry] = nuc_dict[entry][:-3]
                    else:
                        raise AssertionError("\n\nERROR: Internal stop codons detected.")
                else:
                    prot_seq += amino
            prot_dict[entry] = prot_seq
        self.sequence_dictionaries["protein"] = prot_dict
        self.sequence_dictionaries["nucleotide"] = nuc_dict



    def perform_alignment(self):
        """
            Construct amino acid MSA using mafft
        """

        with open(self.mafft_infile, 'w') as inf:
            for rec in self.sequence_dictionaries["protein"]:
                inf.write('>' + str(rec) + '\n' + str(self.sequence_dictionaries["protein"][rec]) + '\n')
        run_align = subprocess.call('mafft --auto --quiet ' + self.mafft_infile + ' > ' + self.mafft_outfile, shell=True)
        assert(run_align == 0), "Could not perform mafft alignment."
        self.parsed_protein_alignment = list(SeqIO.parse(self.mafft_outfile, 'fasta'))


    def back_translate(self, protseq, nucseq):
        """
            Back-translate an aligned amino acid sequence into its aligned nucleotide sequence.
        """
        nucaln = ''
        start = 0; end = 3;
        for amino in protseq:
            if amino == '-':
                codon = '---'
            else:
                codon = nucseq[start:end]
                start += 3
                end += 3
            nucaln += codon
        assert(len(protseq)*3 == len(nucaln)), "\n\nERROR: Back-translation failed."
        return nucaln


    def pal_to_nal(self):
        """
            Convert protein alignment to nucleotide alignment.
        """
        nucf  = open(self.alnfile, 'w')

        for rec in self.parsed_protein_alignment:
            id = str(rec.id)
            aln_nuc = self.back_translate( str(rec.seq), self.sequence_dictionaries["nucleotide"][id] )
            nucf.write('>' + id + '\n' + aln_nuc + '\n')
            
        nucf.close()


    def construct_tree(self):
        """
            Construct a minimum evolution tree from nucleotide alignment, without support values, in FastTree.
        """
        tree_cmd = "FastTree -nt -gtr -nosupport -quiet " + self.alnfile + " > " + self.treefile
        run_tree = subprocess.call(tree_cmd, shell=True)
        assert(run_tree == 0), "Could not construct phylogeny."


def parse_args():
    parser = argparse.ArgumentParser(description = "Takes a file of FASTA-formatted nucleotide sequences and provides an input file for HyPhy analysis, obtained via codon-aware alignment with mafft and phylogenetic reconstruction with FastTree.")
    parser.add_argument("infile", metavar = "infile",  type = str, help = "A file containing nucleotide sequences to align. Must be in FASTA format.")
    return parser.parse_args()


def main():
    args = parse_args()
    while args.infile is None:
        args.infile = raw_input("\nCould not find specified input file. Try again: ")
        if not os.path.exists(args.infile):
            args.infile = None

    # Check paths
    devnull = open(os.devnull, 'w')
    foundmafft = subprocess.call(["which", "mafft"], stdout = devnull)
    assert (foundmafft == 0), "\n\nERROR: MAFFT needs to be installed and on the system path."
    foundft = subprocess.call(["which", "FastTree"], stdout = devnull)
    assert (foundft == 0), "\n\nERROR: FastTree needs to be installed and on the system path."
    devnull.close()
    
    HyPhyPrep(args.infile)
        
main()
