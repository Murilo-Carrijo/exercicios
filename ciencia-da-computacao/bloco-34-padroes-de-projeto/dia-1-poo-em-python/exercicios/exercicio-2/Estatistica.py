import statistics as sts

class Estatistica():
    
    def media(dados):
        return sum(dados) / len(dados)

    def mediana(dados):
        dados.sort()
        i = len(dados) // 2
        if len(dados) % 2 == 0:
            return (dados[i -1] + dados[i] / 2)
        return dados[i]

    def moda(dados):
        return sts.mode(dados)