import itertools

def tf(x):
    return 'T' if x else 'F'

def print_table(description, logic, var1, var2, fn):
    w = 18  # column width
    
    print(f"\nProposition : {description}")
    print(f"Logic       : {logic}")
    
    header = f"{var1:<{w}} {var2:<{w}} Result"
    sep = "-" * len(header)
    
    print(sep)
    print(header)
    print(sep)
    
    for v1, v2 in itertools.product([False, True], repeat=2):
        result = fn(v1, v2)
        print(f"{tf(v1):<{w}} {tf(v2):<{w}} {tf(result)}")
    
    print(sep)

# a. Raining IFF Cloudy
print_table(
    "It is raining IFF it is a cloudy day",
    "R <-> C (Biconditional)",
    "R", "C",
    lambda r, c: r == c
)

# b. Score=100 IMPLIES Grade=A
print_table(
    "If Score=100 then Grade=A",
    "S -> A (Implication)",
    "S", "A",
    lambda s, a: (not s) or a
)

# c. 2 Advil OR 3 Tylenol
print_table(
    "Take either 2 Advil or 3 Tylenol",
    "A OR T (Disjunction)",
    "A", "T",
    lambda a, t: a or t
)

# d. Studied hard OR extremely bright
print_table(
    "She studied hard or she is extremely bright",
    "S OR B (Disjunction)",
    "S", "B",
    lambda s, b: s or b
)

# e. Rock AND Island
print_table(
    "I am a rock and I am an island",
    "R AND I (Conjunction)",
    "R", "I",
    lambda r, i: r and i
)