# Autor:heloisa fernandes silva

def situacao(m):
    """Devolve "Aprovado" se a media for 60 ou mais;
    senao, devolve "Reprovado".
    Ex.: situacao(60) -> "Aprovado"
    """
    # complete aqui: troque o return "?" pelo if
    if m >=60:
        print("aprovado")
    else:
        print("reprovado")
print(situacao(60))