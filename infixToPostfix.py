exp = input("Enter the expression to be evaluated")

precedence = {1: ["(", ")"], 2: ["*", "/"], 3: ["+", "-"]}  # dictionary representing the precedence of the operators

stack_operator = []  # a stack to keep operands

exp += ")"
stack_operator.append("(")

exp_post = ""

for ch in exp:

    #  for the braces
    if ch in precedence[1]:
        if ch == ")":
            while stack_operator[-1] != "(":
                c = stack_operator.pop()
                exp_post += c
            else:
                stack_operator.pop()
        else:
            stack_operator.append("(")

    # for * and /
    elif ch in precedence[2]:
        while stack_operator[-1] in precedence[2]:
            c = stack_operator.pop()
            exp_post += c
        stack_operator.append(ch)

    # for + and _
    elif ch in precedence[3]:
        while stack_operator[-1] in precedence[2] or stack_operator[-1] in precedence[3]:
            c = stack_operator.pop()
            exp_post += c
        stack_operator.append(ch)

    # for the operands
    else:
        exp_post += ch


print(exp_post)
