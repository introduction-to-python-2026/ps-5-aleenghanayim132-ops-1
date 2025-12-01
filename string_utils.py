def split_by_capitals(formula):
    start = 0
    end = len(formula) + 1
    split_formula = []
    for i in range(start + 1, end):
      if i == end - 1 or formula[i].isupper():
        split_formula.append(formula[start:i])
        start = i
    return split_formula

def split_at_number(formula):
    digit_location = 1
    for ch in formula[1:]:
      if ch.isdigit():
        break
      digit_location += 1
    if digit_location == len(formula):
      return (formula, 1)
    if digit_location < len(formula):
      return (formula[:digit_location], int(formula[digit_location:]))

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    
    # Step 1: Initialize an empty dictionary to store atom counts
    dict_of_atoms = {}
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        if atom_name in dict_of_atoms:
            dict_of_atoms[atom_name] += atom_count
        else:
            dict_of_atoms[atom_name] = atom_count
        # Step 2: Update the dictionary with the atom name and count
    return dict_of_atoms
    # Step 3: Return the completed dictionary

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
