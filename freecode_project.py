#Build an Arithmetic Formatter Project

def show_operation(expressions):
    operands = expressions.split("+")
    first_operand = operands[0].strip()
    second_operand = operands[1].strip()
    max_len_operands = max(len(first_operand),len(second_operand))
    first_operand_space_number = 2+max_len_operands - len(first_operand)
    second_operand_space_number = max_len_operands - len(second_operand)
    print(" "*first_operand_space_number + first_operand)
    print("+ " +" "*second_operand_space_number + second_operand)

def expression_parts(expression):
    operands = expression.split("+")
    first_operand = operands[0].strip()
    second_operand = operands[1].strip()
    operation_result = str(int(first_operand) + int(second_operand))
    max_len_operands = max(len(first_operand),len(second_operand))
    first_operand_space_number = 2+max_len_operands - len(first_operand)
    second_operand_space_number = max_len_operands - len(second_operand)
    first_line = " "*first_operand_space_number + first_operand
    second_line = "+ " +" "*second_operand_space_number + second_operand
    third_line = " "*(len(first_line)-len(operation_result)) + operation_result
    return first_line,second_line,third_line

def expression_parts(expression):
    if "+" in expression:
        operator = "+"
    elif "-" in expression:
        operator = "-"
                    
    operands = expression.split(operator)
    first_operand = operands[0].strip()
    second_operand = operands[1].strip()
    if operator == "+":
        operation_result = str(int(first_operand) + int(second_operand))
    elif operator == "-":
        operation_result = str(int(first_operand) - int(second_operand))
    max_len_operands = max(len(first_operand),len(second_operand))
    first_operand_space_number = 2+max_len_operands - len(first_operand)
    second_operand_space_number = max_len_operands - len(second_operand)
    first_line = " "*first_operand_space_number + first_operand
    second_line = operator+" " +" "*second_operand_space_number + second_operand
    third_line = " "*(len(first_line)-len(operation_result)) + operation_result
    return first_line,second_line,third_line

def expression_parts(expression):
    if "+" in expression:
        operator = "+"
    elif "-" in expression:
        operator = "-"
                    
    operands = expression.split(operator)
    first_operand = operands[0].strip()
    second_operand = operands[1].strip()
    if operator == "+":
        operation_result = str(int(first_operand) + int(second_operand))
    elif operator == "-":
        operation_result = str(int(first_operand) - int(second_operand))
    max_len_operands = max(len(first_operand),len(second_operand))
    first_operand_space_number = 2+max_len_operands - len(first_operand)
    second_operand_space_number = max_len_operands - len(second_operand)
    first_line = " "*first_operand_space_number + first_operand
    second_line = operator+" " +" "*second_operand_space_number + second_operand
    third_line = " "*(len(first_line)-len(operation_result)) + operation_result
    return first_line,second_line,third_line



def arithmetic_arranger(problems,show_answers=True):
    if len(problems) > 5:
#        print('Error: Too many problems.')
        return 'Error: Too many problems.'
        
    for expression in problems:
        if "+" not in expression and "-" not in expression:
            #print("Error: Operator must be '+' or '-'.")
            return "Error: Operator must be '+' or '-'."
        
    for expression in problems:
        try:
            if "+" in expression:
                operator = "+"
            elif "-" in expression:
                operator = "-"
            x = expression.split(operator)
            y = int(x[0])
            z = int(x[1])
        except:
           # print("The string does not contain only digits.")
            return 'Error: Numbers must only contain digits.'
        
        
    for expression in problems:
        if "+" in expression:
            operator = "+"
        elif "-" in expression:
            operator = "-"
            
        x = expression.split(operator)
        y = x[0].strip()
        z = x[1].strip()
        if len(y) > 4 or len(z) > 4:
            #print('Error: Numbers cannot be more than four digits.') 
            return 'Error: Numbers cannot be more than four digits.'
        
    all_lines = ""  
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    space_num = 0
    count = 0
    for expression in problems:
        if count > 0:
            space_num = 4    
        first_part,second_part,third_part = expression_parts(expression)
        line1 += " "*space_num+first_part
        line2 += " "*space_num+second_part
        line3 += " "*space_num+"-"*len(first_part)
        line4 += " "*space_num+third_part
        count += 1
    #print(line1)     
    #print(line2)
    #print(line3)
    all_lines = line1 + '\n' +  line2 + '\n' +  line3
    if show_answers:
       # print(line4)
        all_lines += '\n' + line4 

    return all_lines
    
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

