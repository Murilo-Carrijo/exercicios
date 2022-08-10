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



dados = [3, 2, 10, 9, 10, 11]
if __name__ == "__main__":
    print("média: ", Estatistica.media(dados))
    print("mediana: ", Estatistica.mediana(dados))
    print("moda: ", Estatistica.moda(dados))