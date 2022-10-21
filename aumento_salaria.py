# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = float(input()) 

if ( salario<= 600.00 ):
    novoSalario = salario*1.17
    percentual = "17 %"
elif (salario>=600.01 and salario <=900.00  ):
    novoSalario = salario*1.13
    percentual = "13 %"
elif (salario>= 900.01 and salario<= 1500.00  ):
    novoSalario = salario*1.12
    percentual = "12 %"
elif ( salario>= 1500.01 and salario<=2000.00 ):
    novoSalario = salario*1.10
    percentual = "10 %"
else: 
    novoSalario = salario*1.05
    percentual = "5 %"
# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
valorReajuste = novoSalario-salario

print(f'Novo salario: {round(novoSalario,2):.2f}')
print(f'Reajuste ganho: {round(valorReajuste,2):.2f}')
print(f'Em percentual: {percentual}')