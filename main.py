import sympy
from sympy.logic.boolalg import simplify_logic
from sympy.abc import A, B, C, D, E  # Pre-defining standard variables

def print_truth_table(expr, variables):
    """Generates and prints the truth table for a given boolean expression."""
    print(f"\n--- Truth Table for {expr} ---")
    
    # Print Header
    header = [str(v) for v in variables] + ['Output']
    print(" | ".join(header))
    print("-" * (len(header) * 4))
    
    # Get truth table from sympy
    table = sympy.logic.boolalg.truth_table(expr, variables)
    
    for row in table:
        inputs = row[0]
        output = row[1]
        # Format true/false as 1/0
        input_str = " | ".join(['1' if val else '0' for val in inputs])
        output_str = '1' if output else '0'
        print(f"{input_str} |   {output_str}")

def main():
    print("=========================================")
    print("   Boolean Algebra Circuit Simulator     ")
    print("=========================================")
    print("Supported operators:")
    print("  AND  -> &")
    print("  OR   -> |")
    print("  NOT  -> ~")
    print("  XOR  -> ^")
    print("Example format: (A & B) | (~A & C)")
    print("=========================================\n")
    
    # 1. Input Boolean expression
    user_input = input("Enter your Boolean expression: ")
    
    try:
        # Parse the string into a logical expression
        original_expr = sympy.sympify(user_input)
        
        # Extract variables used in the expression and sort them alphabetically
        variables = sorted(list(original_expr.free_symbols), key=lambda x: str(x))
        
        print("\n[+] Original Expression Parsed Successfully:")
        print(f"    F = {original_expr}")
        
        # 2. Generate Truth Table
        print_truth_table(original_expr, variables)
        
        # 3. Simplify circuit using Boolean laws
        minimized_expr = simplify_logic(original_expr)
        
        print("\n[+] Minimization Complete:")
        print(f"    Original Circuit Expression:  {original_expr}")
        print(f"    Minimized Circuit Expression: {minimized_expr}")
        
        # 4. Compare Complexity (Gate Count estimation)
        # We estimate the size based on the number of mathematical operations
        original_size = original_expr.count_ops()
        minimized_size = minimized_expr.count_ops()
        
        print("\n--- Complexity Comparison ---")
        print(f"Original Gate/Operation Count:  {original_size}")
        print(f"Minimized Gate/Operation Count: {minimized_size}")
        
        if minimized_size < original_size:
            print("-> The circuit was successfully simplified!")
        elif minimized_size == original_size:
            print("-> The circuit is already at its most optimal form.")
            
    except Exception as e:
        print("\n[!] Error parsing expression. Please ensure you are using the correct variables (A, B, C...) and operators (&, |, ~, ^).")
        print(f"Details: {e}")

if __name__ == "__main__":
    main()
