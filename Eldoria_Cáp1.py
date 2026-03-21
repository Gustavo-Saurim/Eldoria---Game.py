from random import randint, choice
import sys

# =========================
# DADOS DO JOGADOR
# =========================
player = {
    "nome": "",
    "level": 1,
    "hp": 100,
    "hp_max": 100,
    "atk": 10,
    "cura": 15,
    "xp": 0
}

# =========================
# INIMIGOS
# =========================
inimigos = [
    {"nome": "Rato Sombrio", "level": 1, "hp": 30, "atk": 5, "xp": 10},
    {"nome": "Morcego das Cavernas", "level": 2, "hp": 25, "atk": 7, "xp": 15}
]

# =========================
# FUNÇÕES
# =========================


def linha():
    print("-" * 50)


def status():
    print(f"{player['nome']} | LVL {player['level']}")
    print(
        f"HP: {player['hp']}/{player['hp_max']} | ATK: {player['atk']} | XP: {player['xp']}")


def atacar(atacante, defensor):
    dano = atacante["atk"]

    # crítico
    if randint(1, 100) <= 20:
        dano *= 2
        print("\n💥 CRÍTICO!")

    defensor["hp"] -= dano
    print(f"{atacante['nome']} causou {dano} de dano!")


def curar():
    player["hp"] += player["cura"]
    if player["hp"] > player["hp_max"]:
        player["hp"] = player["hp_max"]
    print(f"Você recuperou {player['cura']} de HP!")


def analisar(inimigo):

    print("\n🔍 Analisando inimigo...")

    # chance base + percepção + diferença de nível
    chance = 40 + (player["percepcao"] * 5) + \
        ((player["level"] - inimigo["level"]) * 5)

    # limitar entre 10% e 95%
    if chance < 10:
        chance = 10
    elif chance > 95:
        chance = 95

    if randint(1, 100) <= chance:
        print(f"""
✅ Análise bem-sucedida!

Inimigo: {inimigo['nome']}
Level: {inimigo['level']}
HP: {inimigo['hp']}
Dano: {inimigo['atk']}
""")
    else:
        print("❌ Você não conseguiu obter informações completas...")
        print(f"Inimigo: {inimigo['nome']} | Level: {inimigo['level']}")


def subir_level():
    if player["xp"] >= 30:
        player["xp"] = 0
        player["level"] += 1
        player["hp_max"] += 20
        player["atk"] += 5
        player["hp"] = player["hp_max"]
        print("⭐ LEVEL UP!")
        print("Seus atributos aumentaram!")


def batalha(inimigo):
    linha()
    print(f"⚔️ Um {inimigo['nome']} apareceu!")
    linha()

    while True:
        print("\n--- SEU TURNO ---")
        status()
        print("\n1- Atacar\n2- Curar\n3- Fugir")

        try:
            escolha = int(input("Escolha: "))
        except:
            print("Opção inválida!")
            continue

        if escolha == 1:
            atacar(player, inimigo)

        elif escolha == 2:
            curar()

        elif escolha == 3:
            analisar(inimigo)
            continue

        elif escolha == 4:
            if randint(1, 100) <= 40:
                linha()
                print("\nVocê fugiu com sucesso!")
                return
            else:
                linha()
                print("\nFalha ao fugir!")

        else:
            print("Escolha inválida!")
            continue

        # inimigo morto
        if inimigo["hp"] <= 0:
            print(f"\n🏆 Você derrotou {inimigo['nome']}!")
            player["xp"] += inimigo["xp"]
            print(f"+{inimigo['xp']} XP")
            subir_level()
            return

        # turno inimigo
        print("\n--- TURNO DO INIMIGO ---")
        atacar(inimigo, player)

        if player["hp"] <= 0:
            print("\n💀 GAME OVER!")
            sys.exit()

# =========================
# EVENTO ALEATÓRIO
# =========================


def evento():
    evento = randint(1, 3)

    if evento == 1:
        print("\n🎁 Você encontrou uma poção!")
        player["hp"] += 20

    elif evento == 2:
        print("\n⚠️ Armadilha! Você sofreu dano.")
        player["hp"] -= 10

    else:
        print("\n🌿 Nada aconteceu... silêncio estranho.")

# =========================
# CAPÍTULO 1
# =========================


def capitulo1():
    linha()
    print("📖 CAPÍTULO 1 — O DESPERTAR")
    linha()

    print("""
Você acorda em meio a uma floresta escura...
O vento sussurra entre as árvores.
Algo está errado.

Ao longe, você vê dois caminhos:
""")

    print("1 - Entrar na floresta")
    print("2 - Explorar uma caverna")

    escolha = input("Escolha: ")

    if escolha == "1":
        print("\n🌲 Você entra na floresta...")
        batalha(choice(inimigos))
        evento()

    elif escolha == "2":
        print("\n🕳️ Você entra na caverna...")
        batalha(choice(inimigos))
        evento()

    else:
        print("Você hesita... e o perigo te encontra.")
        batalha(choice(inimigos))

    print("\nVocê sente que algo maior está por vir...")
    print("🔜 Fim do Capítulo 1")

# =========================
# MENU
# =========================


def menu():
    print("=== ELDORIA: FRAGMENTOS DO ABISMO ===")
    print("1 - Novo Jogo")
    print("2 - Sair")

    escolha = input("Escolha: ")

    if escolha == "1":
        player["nome"] = input("Digite seu nome: ")
        capitulo1()
    else:
        print("Até logo!")
        sys.exit()


# =========================
# INÍCIO
# =========================
menu()
