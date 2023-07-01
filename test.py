import math


modulos =['math.tan', 'math.sin', 'math.cos', 'mathsqrt', 'math.log', 'math.log10', 'math.e', 'math.pow', 'math.pi']

todos_valores = 'tan(5-2)+3'

for i in modulos:
    if i=='math.tan':
        todos_valores = todos_valores.replace('tan',i )
    if i=='math.sin':
        todos_valores = todos_valores.replace('sin',i )
    if i=='math.cos':
        todos_valores = todos_valores.replace('cos',i )
    if i=='math.sqrt':
        todos_valores = todos_valores.replace('sqrt',i )

    # -----------------------------------------------

    if i=='math.log':
        todos_valores = todos_valores.replace('log',i )
    if i=='math.log10':
        todos_valores = todos_valores.replace('log10',i )
    if i=='math.e':
        todos_valores = todos_valores.replace('e',i )
    if i=='math.pow':
        todos_valores = todos_valores.replace('pow',i )

    # -----------------------------------------------
    if i=='math.pi':
        todos_valores = todos_valores.replace('pi',i )  


resultado = eval(todos_valores)

print(resultado)