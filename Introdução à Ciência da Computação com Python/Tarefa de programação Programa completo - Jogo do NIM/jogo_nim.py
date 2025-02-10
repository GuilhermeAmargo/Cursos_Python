import math

def computador_escolhe_jogada(n, m):
    for i in range(1, m+1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(n, m)

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    computador_joga = n % (m + 1) != 0
    print("Computador começa!" if computador_joga else "Você começa!")
    
    while n > 0:
        if computador_joga:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
        
        n -= jogada
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n > 1:
            print(f"Agora restam {n} peças no tabuleiro.")
        
        computador_joga = not computador_joga
    
    if computador_joga:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def campeonato():
    usuario_pontos = 0
    computador_pontos = 0
    for i in range(1, 4):
        print(f"**** Rodada {i} ****")
        if partida():
            usuario_pontos += 1
        else:
            computador_pontos += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {usuario_pontos} X {computador_pontos} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")
    escolha = int(input())
    if escolha == 1:
        partida()
    else:
        campeonato()

if __name__ == "__main__":
    main()