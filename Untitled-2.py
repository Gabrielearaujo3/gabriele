import random  # Importamos a biblioteca random para gerar a jogada do computador

def jogar():
    # Lista com as opções do jogo
    opcoes = ["Pedra", "Papel", "Tesoura"]

    while True:  # Loop principal do jogo, que só para quando o jogador decidir sair
        print("\nEscolha uma opção:")
        print("0 - Pedra")
        print("1 - Papel")
        print("2 - Tesoura")
        
        try:
            # Usuário insere sua escolha
            jogador = int(input("Digite sua escolha (0, 1 ou 2): "))
            
            # Verifica se a entrada do usuário é válida
            if jogador not in [0, 1, 2]:
                print("Opção inválida! Escolha entre 0, 1 ou 2.")
                continue  # Volta para o início do loop para pedir um novo valor
        except ValueError:  
            # Caso o jogador digite algo que não seja número, o programa exibe erro e reinicia a escolha
            print("Entrada inválida! Digite um número inteiro.")
            continue  

        # O computador escolhe aleatoriamente entre 0, 1 e 2
        computador = random.randint(0, 2)
        
        # Mostra a escolha do jogador e do computador
        print(f"\nVocê escolheu: {opcoes[jogador]}")
        print(f"Computador escolheu: {opcoes[computador]}")
        
        # Verifica o resultado do jogo
        if jogador == computador:
            print("Empate!")  # Se ambos escolherem a mesma opção
        elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
            print("Você venceu!")  # Condições em que o jogador ganha
        else:
            print("Você perdeu!")  # Caso contrário, o computador vence

        # Pergunta ao usuário se ele quer jogar novamente
        novamente = input("\nJogar novamente? (Sim/Não): ").strip().lower()
        if novamente != "sim":  # Se a resposta não for "sim", o jogo encerra
            print("Jogo encerrado. Obrigado por jogar!")
            break  # Sai do loop principal, terminando o jogo

# Chamada da função para iniciar o jogo
jogar()