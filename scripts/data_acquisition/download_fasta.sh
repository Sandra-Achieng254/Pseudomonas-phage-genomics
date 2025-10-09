#!/bin/bash

# File with folder links (one per line)
LINKS_FILE="links.tsv"

# Output directory
OUT_DIR="fasta_downloads"
mkdir -p "$OUT_DIR"

# Loop through each link in the file
while read -r link; do
    if [ -n "$link" ]; then
        echo "Downloading from: $link"
        gdown --fuzzy --folder "$link" -O "$OUT_DIR"
    fi
done < "$LINKS_FILE"

echo "✅ All downloads completed. Files saved in $OUT_DIR/"
