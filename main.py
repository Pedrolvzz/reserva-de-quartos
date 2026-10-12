import time

print("=== RESERVA DE QUARTOS ===")

quartos = list(range(1,11))  #quartos disponiveis
TODOS = list(range(1,11))

print("Bem vindo à reserva de quartos! O que deseja fazer?")

while True:
    print("\n 1- Disponibilidade \n 2- Reservar Quarto \n 3- Cancelar Reserva \n 4- Sair")
    r = input("Como podemos ajudar? ").lower().strip()

    if r in ("1", "disponibilidade"):
        print("Nossos quartos disponíveis:")
        print(quartos)

    elif r in ("2", "reservar quarto"):
        try:
            reserva = int(input("Qual quarto deseja reservar? "))
        except ValueError:
            print("Digite um quarto válido!")
            continue
        
        if reserva not in quartos:
            print("Quarto indisponível! cheque a disponibilidade de quartos primeiro!")

        else:
            quartos.remove(reserva)
            print("Quarto reservado com sucesso! Aproveite.")


    elif r in ("3", "cancelar reserva"):
        try:
            cancelar = int(input("Qual quarto deseja cancelar a reserva?"))
        except ValueError:
            print("Digite um quarto válido!")
            continue

        if cancelar not in TODOS:
            print("Esse quarto não existe!")
        elif cancelar in quartos:
            print("Esse quarto não está reservado!")
        else:
            quartos.append(cancelar)
            quartos.sort()
            print("Reserva cancelada com sucesso!")

    elif r in ("4", "sair"):
        print("Saindo do sistema...")
        time.sleep(1)
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Opção inválida! Tente novamente.")


