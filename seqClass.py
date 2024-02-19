#!/usr/bin/env python
# First exercise, after creating fix branch we try to fix seqClass.py to see if it is able to classify correctly any RNA or DNA sequence.
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
#line added to identify motifs
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper() # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    # Add a condition so if the sequence contains both T and U it doesn't compute it as DNA
    if 'T' in args.seq and 'U' in args.seq:
        print('The sequence contains both T and U, and is ambiguous.')
    elif 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        # If the sequence doesn't contains 'T' or 'U', it could be DNA or RNA
        print('The sequence can be DNA or RNA')
else:
    print('The sequence is not DNA or RNA')

#code addition provided by teacher, where motif is searched in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("MOTIF FOUND")
    else:
        print("MOTIF NOT FOUND")
