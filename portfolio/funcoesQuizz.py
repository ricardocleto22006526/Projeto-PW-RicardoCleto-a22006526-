import matplotlib.pyplot as graficos


def informacao_sobre_utilizadores(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizzPontuacao(quizz)

    return dados


def desenha_grafico_resultados(objetos):
    dados = informacao_sobre_utilizadores(objetos)

    dadosOrdenados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dadosOrdenados.keys())
    pontuacao = list(dadosOrdenados.values())

    graficos.figure(figsize=(13, 5))

    graficos.barh(pessoa, pontuacao, color='green')

    graficos.title("Pontuação dos participantes!")
    graficos.ylabel("Nome dos participantes")
    graficos.xlabel("Pontuação")

    graficos.savefig('portfolio/static/portfolio/images/grafico_final.png')


def QuizzPontuacao(input):
    pontuacaoDaPessoa = 0

    if input.pergunta1 == 1991:
        pontuacaoDaPessoa += 4

    if input.pergunta2 == 1994:
        pontuacaoDaPessoa += 4

    if input.pergunta3 == 1989:
        pontuacaoDaPessoa += 4

    if input.pergunta4.lower() == "framework":
        pontuacaoDaPessoa += 4

    if input.pergunta5 == 2005:
        pontuacaoDaPessoa += 4

    return pontuacaoDaPessoa
