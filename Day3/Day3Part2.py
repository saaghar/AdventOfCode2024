import re
import fileinput

def calculate_conditional_mul_sum(file_paths: list) -> int:
    # Regex pattern to find mul(X, Y), do(), or don't() instructions
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    total_sum = 0
    enabled = True  
    
    for line in fileinput.input(files='dataDay3.txt'):
        
        instructions = re.findall(pattern, line)
        
        for instruction in instructions:
            full_match, x, y = instruction
            
            if full_match == "do()":
                enabled = True
            elif full_match == "don't()":
                enabled = False
            elif full_match.startswith("mul") and enabled:
                
                total_sum += int(x) * int(y)
    
    return total_sum



