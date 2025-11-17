#!/usr/bin/env python3
import sys

# Read tail gene IDs
with open(sys.argv[2], 'r') as f:
    tail_genes = set(line.strip() for line in f)

# Filter clusters that contain at least one tail gene
with open(sys.argv[1], 'r') as clusters:
    for line in clusters:
        centroid, members = line.strip().split('\t')
        member_list = members.split(',')
        
        # Check if any member is a tail gene
        if any(gene in tail_genes for gene in member_list):
            print(line.strip())

print(f"Found clusters containing tail-associated proteins")
