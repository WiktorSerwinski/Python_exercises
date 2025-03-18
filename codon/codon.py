import typing


class DNAAnalyser:
    REPORT_MAPPING_FILENAME = "codon/codon.tsv"

    @staticmethod
    def get_amin(dna_sequence: str) -> dict[str, int]:

        map_codon = {}
        with open(DNAAnalyser.REPORT_MAPPING_FILENAME, "r") as file:
            for l in file:
                parts = l.strip().split()
                if (len(parts) == 2):
                    map_codon[parts[0]] = parts[1]
        amino_count = {}
        
        if (len(dna_sequence) % 3 != 0):
            print("waring...")
        dna_sequence = dna_sequence.upper()
        for i in range(0, len(dna_sequence)-len(dna_sequence) % 3, 3):
            codon = dna_sequence[i:i+3]
            if codon in map_codon:
                amino = map_codon[codon]
                amino_count[amino] = amino_count.get(amino,0)+1 
        print(amino_count)
        return amino_count
                
                
                

    @staticmethod
    def get_amino_acids_report(dna_sequence: str) -> typing.Dict[str, int]:
        # Load codon mappings from the file into a dictionary
        codon_map = {}
        with open(DNAAnalyser.REPORT_MAPPING_FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    codon, amino_acid = parts
                    codon_map[codon] = amino_acid

        amino_acid_counts = {}

        # Check if the sequence length is not a multiple of 3
        if len(dna_sequence) % 3 != 0:
            print(
                "Warning: DNA sequence length is not a multiple of 3. Ignoring remaining characters.")

        # Process DNA sequence in chunks of 3 characters (codons)
        for i in range(0, len(dna_sequence) - (len(dna_sequence) % 3), 3):
            codon = dna_sequence[i:i+3]
            if codon in codon_map:
                amino_acid = codon_map[codon]
                # Count occurrences of each amino acid
                amino_acid_counts[amino_acid] = amino_acid_counts.get(
                    amino_acid, 0) + 1

        print(amino_acid_counts)

        return amino_acid_counts


DNAAnalyser.get_amin("aat")
