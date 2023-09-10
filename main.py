
# 1 - Faça um Programa que peça dois números e imprima a soma.
def somar(num1: int, num2: int):
    soma = num1 + num2
    print(f"Questão 1: {soma}")
    return soma

somar(1, 2)


# 2 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def mediaDeNotas(nota1: float, nota2: float, nota3: float, nota4: float):
    soma = nota1 + nota2 + nota3 + nota4
    media = format(soma / 4, ".2f")
    print(f"Questão 2: {media}")
    return media

mediaDeNotas(1.5, 2.3, 3.6, 4.9)


# 3 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um
# algoritmo que calcule seu peso ideal.
def calculoDeAltura(h: float):
    homem: float = format((72.7 * h) - 58, ".2f")
    mulher: float = format((62.1 * h) - 44.7, ".2f")
    print(f"Questão 3: homem - {homem}, mulher - {mulher}")
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
    print(f"Questão 4: Salario bruto - {bruto}, INSS - {valorInss}, Sindicato - {valorSindicato}, Salario Líquido - {salarioLiquido}")
    return {bruto, impostoDeRenda, valorInss, valorSindicato, salarioLiquido}

calculoSalario(10, 160)


# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno
def aprovarOuReprovar(nota1: float, nota2: float):
    media = (nota1 + nota2) / 2
    if(media >= 7.0 and media < 10.0):
        print("Questão 5: Aprovado")
    elif(media == 10):
        print("Questão 5: Aprovado com Distinção")
    else:
        print("Questão 5: Reprovado")
    return 0
aprovarOuReprovar(9.9, 9.9)


# 6 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os
# reajustes.
def reajusteSalario(salarioAtual: float):
    if(salarioAtual < 0 or salarioAtual == 0):
        return print("Questão 6: Valor inválido")
    reajustes = {
        20: salarioAtual * 0.20,
        15: salarioAtual * 0.15,
        10: salarioAtual * 0.10,
        5: salarioAtual * 0.05,
    }
    salarioNovo = 0
    percentual = 0
    if(salarioAtual <= 280.00):
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

    return salarioNovo
reajusteSalario(0)


# 7 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
# ver a tabuada. A saída deve ser conforme o exemplo abaixo:
def tabuada(num: int):
    print("Questão 7:", end=' ')
    for i in range(1, 11):
        multiplicao = num * i
        print(f"{num} x {i} = {multiplicao}", end=f"{', ' if i < 10 else ''}")

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

    print("Programa encerrado!")

notas()
