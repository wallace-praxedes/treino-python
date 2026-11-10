"""
01. TIPOS DE VARIÁVEIS

int:    números inteiros    (ex.: 10, -4)
str:    texto               (ex.: "Wallace", "%", "42")
float:  números decimais    (ex.: 3.14, -4.20, 0.000679)
bool:   True (1) ou False (0)

Se desejar mudar a variável, colocar o tipo no início.

- int(variavel_n)
- str(variavel_n)
- float(variavel_n)
- bool(variavel_n)

"""
idade = 29
type(idade)

nome = "%"
type(nome)

km = 1.0
type(km)

pcd = True
type(pcd)

# EXERCÍCIOS DE 01. TIPOS DE VARIÁVEIS

# 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

print("Alô mundo")

# 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

numero = float(input("Insira um número "))
output_numero = print(f"O número informado foi {numero}.")

#%% 3. Faça um Programa que peça dois números e imprima a soma.

n1 = float(input("Insira o primeiro número "))
n2 = float(input("Insira o segundo número "))
soma = n1 + n2

print(f"A soma dos números inseridos foi de {soma}.")

#%% 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

n1 = float(input("Insira a primeira nota bimestral: "))
n2 = float(input("Insira a segunda nota bimestral: "))
n3 = float(input("Insira a terceira nota bimestral: "))
n4 = float(input("Insira a quarta nota bimestral: "))

output_media_notas = (n1 + n2 + n3 + n4) / 4

print(f"A sua média é de {output_media_notas}.")
#%% 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

metros = int(input("Insira o tamanho em metros: "))
print(f"O tamanho de {metros} em centímetros é de {metros/60} metros.")

#%% 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

largura = float(input("Insira a largura da sala: "))
comprimento = float(input("Insira o comprimento da sala: "))

print(f"O tamanho da área da sala é de {largura * comprimento} m².")

#%% 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Insira quanto você ganha por hora: "))
hora_mensal = int(input("Insira quantas horas no mês você trabalha: "))

print(f"O seu salário mensal é de R$ {salario_hora * hora_mensal} reais.")

#%% 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperatura_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))

output_celsius = print(f"{temperatura_fahrenheit} Fahrenheit equivale a {(5/9)*(temperatura_fahrenheit-32)}°C.")

#%% 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_celsius = float(input("Insira a temperatura em Celsius: "))

output_fahrenheit = print(f"{temperatura_celsius}°C equivale a {((9/5*temperatura_celsius) + 32)}")
# %%
