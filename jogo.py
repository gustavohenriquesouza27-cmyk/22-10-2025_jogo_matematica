import random
import time
print("Bem-vindo ao jogo de matematica! ")
print("responde o maximo que puder. digite 'sair' para encerrar.\n")

pontos = 0
rodada = 1
while true:
  #gera dois numeros e uma operação aleatoria
n1 = random.randint(1,10)
n2 = random.randint(1,10)
operacao = random.choice(["+", "-", "*"])

# Calcula o resultado certo
if operacao == "+":
  resultado_certo = n1 + n2
elif operacao == "-":
  resultado_certo = n1 - n2
else:
  resultado_certo = n1 * n2

print(f"pergunta {rodada}: quanto e {n1} {operacao} {n2}?")
resposta = input("->")

if resposta.lower() == "sair":
  break

  # verifica se e numero
  if not resposta.isdigit() and not (resposta.startswith("-") and resposta[1:].isdigit()):
    print("por favor, digite um numero ou sair.")
    continue
