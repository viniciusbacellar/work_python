# 1 - Faça um Programa que peça dois números e imprima a soma.
def somar(num1: int, num2: int):
    soma = num1 + num2
    print(f"Questão 1: {soma}")
    print()
    return soma


somar(1, 2)


# 2 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def mediaDeNotas(nota1: float, nota2: float, nota3: float, nota4: float):
    soma = nota1 + nota2 + nota3 + nota4
    media = format(soma / 4, ".2f")
    print(f"Questão 2: {media}")
    print()
    return media


mediaDeNotas(1.5, 2.3, 3.6, 4.9)


# 3 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um
# algoritmo que calcule seu peso ideal.
def calculoDeAltura(h: float):
    homem: float = format((72.7 * h) - 58, ".2f")
    mulher: float = format((62.1 * h) - 44.7, ".2f")
    print(f"Questão 3: homem - {homem}, mulher - {mulher}")
    print()
    return {homem, mulher}


calculoDeAltura(1.80)


# 4 - Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
# mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
# para o INSS e 5% para o sindicato
def calculoSalario(valorPorHora: float, qtdDeHoras: int):
    bruto = valorPorHora * qtdDeHoras
    impostoDeRenda = bruto * 0.11
    valorInss = bruto * 0.08
    valorSindicato = bruto * 0.05
    salarioLiquido = bruto - impostoDeRenda - valorInss - valorSindicato
    print(
        f"Questão 4: Salario bruto - {bruto}, INSS - {valorInss}, Sindicato - {valorSindicato}, Salario Líquido - {salarioLiquido}")
    print()
    return {bruto, impostoDeRenda, valorInss, valorSindicato, salarioLiquido}


calculoSalario(10, 160)


# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno
def aprovarOuReprovar(nota1: float, nota2: float):
    media = (nota1 + nota2) / 2
    if (media >= 7.0 and media < 10.0):
        print("Questão 5: Aprovado")
    elif (media == 10):
        print("Questão 5: Aprovado com Distinção")
    else:
        print("Questão 5: Reprovado")

    print()
    return 0


aprovarOuReprovar(9.9, 9.9)


# 6 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os
# reajustes.
def reajusteSalario(salarioAtual: float):
    if (salarioAtual < 0 or salarioAtual == 0):
        print("Questão 6: Valor inválido")
        return print()
    reajustes = {
        20: salarioAtual * 0.20,
        15: salarioAtual * 0.15,
        10: salarioAtual * 0.10,
        5: salarioAtual * 0.05,
    }
    salarioNovo = 0
    percentual = 0
    if (salarioAtual <= 280.00):
        percentual = 20
        salarioNovo = salarioAtual + reajustes[percentual]
    elif (salarioAtual > 280.00 and salarioAtual < 700.00):
        percentual = 15
        salarioNovo = salarioAtual + reajustes[percentual]
    elif (salarioAtual >= 700.00 and salarioAtual < 1500.00):
        percentual = 10
        salarioNovo = salarioAtual + reajustes[percentual]
    else:
        percentual = 5
        salarioNovo = salarioAtual + reajustes[percentual]
    print(f"Questão 6: Salario anterior - {salarioAtual}, Percentual aumentado - {percentual}%, "
          f"Valor aumentado - {reajustes[percentual]}, Salario atualizado - {salarioNovo}")
    print()

    return salarioNovo


reajusteSalario(500)


# 7 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
# ver a tabuada. A saída deve ser conforme o exemplo abaixo:
def tabuada(num: int):
    print("Questão 7:", end=' ')
    for i in range(1, 11):
        multiplicao = num * i
        print(f"{num} x {i} = {multiplicao}", end=f"{', ' if i < 10 else ''}")

    print()
    print()


tabuada(5)


# 8 - Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando for informado
# um valor igual a -1 (que não deve ser armazenado).
def notas():
    total_notas = []
    soma = 0
    qtdValoresAcimaDaMedia = 0
    qtdValoresAbaixoDeSete = 0
    print("Questão 8:", end=' ')
    while True:
        nota = int(input("Digite um numero: "))
        if nota != -1:
            total_notas.append(nota)
        else:
            break

    print(f"Quantidade de valores: {len(total_notas)}")
    print("Itens em ordem: ", end=' ')
    for item in total_notas:
        print(f"{item}", end=' ')
    print()

    print("Itens em ordem inversa: ", end=' ')
    for item in list(reversed(total_notas)):
        print(f"{item}", end=' ')
        soma += item
    print()

    media = soma / len(total_notas)
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media}")

    for item in total_notas:
        if item > media:
            qtdValoresAcimaDaMedia += 1
        if item < 7:
            qtdValoresAbaixoDeSete += 1

    print(f"Quantidade de valores acima da média: {qtdValoresAcimaDaMedia}")
    print(f"Quantidade de valores abaixo de sete: {qtdValoresAcimaDaMedia}")

    print("Questão 8 finalizada!")
    print()


notas()


# 9 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana
# mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
# vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais
# 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando
# um array de contadores) que determine quantos vendedores receberam
# salários nos seguintes intervalos de valores:
def salarios(vendas_brutas: list):
    intervalos_salario = [200, 300, 400, 500, 600, 700, 800, 900, 1000]

    contadores = [0] * len(intervalos_salario)

    for venda in vendas_brutas:
        salario = 200 + 0.09 * venda
        for i, limite in enumerate(intervalos_salario):
            if salario < limite:
                contadores[i] += 1
                break
        else:
            contadores[-1] += 1

    print("Questão 9:")
    for i, limite in enumerate(intervalos_salario):
        if i < len(intervalos_salario) - 1:
            print(f"${limite} - ${intervalos_salario[i + 1] - 1}: {contadores[i]} vendedores")
        else:
            print(f"${limite} ou mais: {contadores[i]} vendedores")
    print()


vendas_brutas = [3000, 4700, 250, 800, 1200, 6000, 950, 1100, 2200, 1800]
salarios(vendas_brutas)


# 10 - Faça um programa que use a função valorPagamento() para determinar o valor
# a ser pago por uma prestação de uma conta. O programa deverá solicitar ao
# usuário o valor da prestação e o número de dias em atraso e passar estes
# valores para a função valorPagamento, que calculará o valor a ser pago e
# devolverá este valor ao programa que a chamou. O programa deverá então
# exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a
# pedir outro valor de prestação e assim continuar até que seja informado um
# valor igual a zero para a prestação. Neste momento o programa deverá ser
# encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
# de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte
# forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando
# houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def prestacoes():
    print("Questão 10: ")
    total_dia = []
    total = 0
    valorPrestacao = float(input("Digite o valor da prestação: "))
    diasAtrasados = int(input("Digite a quantidade de dias em atraso: "))
    while True:
        if valorPrestacao == 0:
            break
        else:
            resultado = valorPagamento(valorPrestacao, diasAtrasados)
            print(f"Valor da ser pago: {resultado}")
            total += resultado
            total_dia.append(resultado)
        valorPrestacao = float(input("Digite o valor da prestação: "))

    print(f"Quantidade de prestações - {len(total_dia)}, Valor total das prestações - {total}")

def valorPagamento(valorPrestacao: float, diasAtrasados: int):
    if diasAtrasados <= 0:
        return valorPrestacao
    else:
        jurosTotal = (valorPrestacao * 0.03) + 0.001 * diasAtrasados * valorPrestacao
        return valorPrestacao + jurosTotal

prestacoes()