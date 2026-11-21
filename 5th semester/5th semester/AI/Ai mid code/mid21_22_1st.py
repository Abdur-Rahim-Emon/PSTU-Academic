from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, truth_table
import re

# Step 1: Convert user input into SymPy format
def parse_expression(expr_str):
    # Replace common symbols with SymPy operators
    expr_str = expr_str.replace(" ", "")
    expr_str = expr_str.replace("->", ">>")     # IMPLIES
    expr_str = expr_str.replace("<->", "<<>>")  # IFF (temporary)
    expr_str = expr_str.replace("A", "&")       # AND
    expr_str = expr_str.replace("∧", "&")
    expr_str = expr_str.replace("OR", "|")      # OR
    expr_str = expr_str.replace("∨", "|")
    expr_str = expr_str.replace("~", "~")       # NOT
    
    # Fix IFF properly
    expr_str = expr_str.replace("<<>>", "==")

    return expr_str


# Step 2: Extract variables automatically
def get_variables(expr_str):
    vars_found = sorted(set(re.findall(r'[a-z]', expr_str)))
    symbols_dict = {v: symbols(v) for v in vars_found}
    return symbols_dict


# Step 3: Classification
def classify(expr, variables):
    rows = list(truth_table(expr, variables))
    results = [row[1] for row in rows]
    
    if all(results):
        return "TAUTOLOGY - Always True"
    elif not any(results):
        return "CONTRADICTION - Always False"
    else:
        return "CONTINGENT - Sometimes True, Sometimes False"


# Step 4: Print Truth Table
def print_truth_table(expr, variables):
    col = 5
    var_names = [str(v) for v in variables]

    header = " | ".join(f"{v:^{col}}" for v in var_names) + f" | {'Res':^{col}}"
    sep = "-" * len(header)

    print("\nTruth Table:")
    print(sep)
    print(header)
    print(sep)

    for row in truth_table(expr, variables):
        vals = list(row[0])
        result = row[1]

        line = " | ".join(f"{'T' if v else 'F':^{col}}" for v in vals)
        line += f" | {'T' if result else 'F':^{col}}"
        print(line)

    print(sep)


# ===== MAIN PROGRAM =====
# Input (you can change this)
expr_input = "(p->q) A (q->r) -> (p->r)"

# Parse expression
parsed_str = parse_expression(expr_input)

# Get variables
symbols_dict = get_variables(parsed_str)

# Convert string to actual expression
expr = eval(parsed_str, {}, symbols_dict)

# Sort variables for consistent table
variables = [symbols_dict[v] for v in sorted(symbols_dict)]

# Output
print(f"Input Expression : {expr_input}")
print(f"Parsed Expression: {expr}")

print_truth_table(expr, variables)

print("Classification:", classify(expr, variables))