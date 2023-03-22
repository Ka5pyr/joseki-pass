#!/usr/bin/env python3

import args
from rich import print as rprint
from rich.progress import track
import time

# Import file of possible terms to create password
OUTPUT_FILE = "new_passfile.txt"

# Adding new permutated terms to OUTPUT_FILE
def append_file(new_perm_list):
    with open(OUTPUT_FILE, "a") as pass_file:
        for new_term in new_perm_list:
            pass_file.write(f"{new_term}\n")


def generate_char_variants(org_term, org_char, variant_char):
    term_variants = []
    for i in range(2**org_term.count(org_char)):
        binary = bin(i)[2:].zfill(org_term.count(org_char))
        variant = ''
        org_char_count = 0
        for letter in org_term:
            if letter == org_char:
                variant += variant_char if binary[org_char_count] == '1' else org_char
                org_char_count += 1
            else:
                variant += letter
        term_variants.append(variant)

    return term_variants


# GENERATING EVERY POSSIBLE PERMUTATION OF EACH TERM
def generate_case_permutations(input_string):
    # Initialize an empty list to store the results
    permutations = []
    term_variants = []

    term_variants.extend(generate_char_variants(input_string, 'e', '3'))
    term_variants.extend(generate_char_variants(input_string, 'E', '3'))
    term_variants.extend(generate_char_variants(input_string, 's', '5'))
    term_variants.extend(generate_char_variants(input_string, 'S', '5'))
    term_variants.extend(generate_char_variants(input_string, 'o', '0'))
    term_variants.extend(generate_char_variants(input_string, 'O', '0'))

    for term_variant in term_variants:
        # Use a nested loop to generate all possible uppercase and lowercase combinations
        for i in range(len(term_variant)):
            for j in range(2**len(term_variant)):
                # Convert the binary representation of the current permutation to a string of uppercase and lowercase letters
                permutation = "".join([term_variant[k].upper() if (j >> k) & 1 else term_variant[k].lower() for k in range(len(term_variant))])
                permutations.append(permutation)
                permutations.append(f"{permutation}!")
                for k in range(10):
                    permutations.append(f"{permutation}{k}!")
                    #print(f"{permutation}{k}!")
        # Remove duplicates and return the list of permutations
    return (list(set(permutations)))


if __name__ == "__main__":


    # Information from args file
    args = args.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    start = time.time()
    term_file = ""
    # Calling Permutation Function
    with open(input_file, "r") as tf:
        term_file = tf.read().splitlines()

    for term in track(term_file, description='[green]Creating Password List'):
        term = term.replace("\n", "")
        tmp_permutation_list = generate_case_permutations(term)
        append_file(tmp_permutation_list)
    end = time.time()
    rprint(f"Elapsed Time: {end - start}")