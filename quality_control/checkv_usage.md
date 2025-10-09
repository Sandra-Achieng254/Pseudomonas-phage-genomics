# CHECKV Quality Control

## Overview
Quality assessment pipeline for viral sequences using CHECKV (Check Viral). This workflow evaluates phage genome quality, completeness, and contamination.

## Purpose
- Assess quality of Pseudomonas phage genomes
- Estimate genome completeness 
- Detect cross-contamination
- Filter sequences based on quality thresholds

## Dependencies

### Required Software
- **CHECKV** v1.0.1+: `conda install -c bioconda checkv`
- **Python** 3.8+ with pandas, matplotlib
- **Bash** environment

## Download CHECKV database
checkv download_database ./checkv-db

## Database should contain:
- viral RefSeq genomes
- prokaryotic genomes   
- protein clusters