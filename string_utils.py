


def split_before_each_uppercases(formula):
    start = 0
    end = len(formula) + 1
    split_formula = []
    for i in range(start + 1, end):
      if i == end - 1 or formula[i].isupper():
        split_formula.append(formula[start:i])
        start = i
    return split_formula

def split_at_first_digit(formula):
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
    formula_dict = {}
    split_formula = split_before_each_uppercases(molecular_formula) 
    for i in split_formula:
        split_i = split_at_first_digit(i)
        if split_i[0] in formula_dict:
          formula_dict[split_i[0]] += split_i[1]
        else:
          formula_dict[split_i[0]] = split_i[1]
    return formula_dict

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
