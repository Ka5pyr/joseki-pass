#!/usr/bin/python3

import args
from pathlib import Path
from rich.console import Console
from rich.progress import track
import time

# Adding new permutated terms to OUTPUT_FILE
def append_file(output_file, new_perm_list):
    with open(output_file, "a") as pass_file:
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
def generate_case_permutations(term):
    # Initialize an empty list to store the results
    permutations = []
    term_variants = []

    term_variants.append(term)
    print(term)

    # Replace letters to numbers if user specifies
    if arguments.char_and_num_replace:
        term_variants.extend(generate_char_variants(term, 'e', '3'))
        term_variants.extend(generate_char_variants(term, 'E', '3'))
        term_variants.extend(generate_char_variants(term, 'i', '1'))
        term_variants.extend(generate_char_variants(term, 'I', '1'))
        term_variants.extend(generate_char_variants(term, 'l', '1'))
        term_variants.extend(generate_char_variants(term, 'L', '1'))
        term_variants.extend(generate_char_variants(term, 'o', '0'))
        term_variants.extend(generate_char_variants(term, 'O', '0'))
        term_variants.extend(generate_char_variants(term, 's', '5'))
        term_variants.extend(generate_char_variants(term, 'S', '5'))

    for term_variant in term_variants:
        # Use a nested loop to generate all possible uppercase and  combinations
        for i in range(len(term_variant)):
            for j in range(2**len(term_variant)):
                # Convert the binary representation of the current permutation to a string of uppercase and lowercase letters
                permutation = "".join([term_variant[k].upper() if (j >> k) & 1 else term_variant[k].lower() for k in range(len(term_variant))])
                permutations.append(permutation)
                permutations.append(f"{permutation}!")
                for k in range(10):
                    permutations.append(f"{permutation}{k}!")
        # Remove duplicates and return the list of permutations
    return (list(set(permutations)))


if __name__ == "__main__":

    console = Console()
    # Information from args file
    arguments = args.get_args()

    # Grabbing current time to display Elapsed Time
    start = time.time()
    term_list = ""

    # Calling Permutation Function
    if not arguments.custom_input:
        with open(arguments.input_text, "r") as tf:
            term_list = tf.read().splitlines()
    else:
        term_list = arguments.input_text.split(" ")


    # Loop for calling permutation functions
    for term in track(term_list, description='[green]Creating Password List'):
        term = term.replace("\n", "")
        tmp_permutation_list = generate_case_permutations(term)
        append_file(arguments.output_file, tmp_permutation_list)

    # Grabbing current time to display Elapsed Time
    end = time.time()
    console.print(f"[bold underline magenta]Elapsed Time:[/] [bold green]{end - start:.5f} seconds[/]")
    console.print(f"[bold underline magenta]Output saved in:[/] [bold green]{arguments.output_file}[/]")