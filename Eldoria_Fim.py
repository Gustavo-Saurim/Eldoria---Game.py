from random import randint, choice, sample
import sys

# =========================
# UTIL / FORMATAÇÃO
# =========================


def linha(char="─", tamanho=50):
    print(char * tamanho)


def titulo(texto):
    linha("═")
    print(f"  {texto}")
    linha("═")


def secao(texto):
    print(f"\n{'─'*20} {texto} {'─'*20}")


def msg_destaque(texto):
    print(f"\n  ★  {texto}  ★\n")


def barra(atual, maximo, tamanho=20, label="HP"):
    proporcao = max(atual, 0) / maximo
    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido

    if proporcao > 0.6:
        bloco = "█"
    elif proporcao > 0.3:
        bloco = "▓"
    else:
        bloco = "░"

    exibido = max(atual, 0)
    barra_str = bloco * preenchido + "─" * vazio
    porcentagem = int(proporcao * 100)
    print(f"  {label:<6} [{barra_str}] {exibido}/{maximo} ({porcentagem}%)")

# =========================
# BANCO DE PODERES DO MAGO
# =========================


BANCO_PODERES_MAGO = [
    {
        "nome": "🔥 Bola de Fogo",
        "descricao": "Esfera flamejante. Dano fixo alto.",
        "tipo": "dano_fixo",
        "valor": 35,
        "custo_mana": 20,
    },
    {
        "nome": "❄️  Toque Glacial",
        "descricao": "Congela o inimigo. Dano moderado.",
        "tipo": "dano_fixo",
        "valor": 25,
        "custo_mana": 12,
    },
    {
        "nome": "⚡ Raio Duplo",
        "descricao": "Dois raios. Cada um causa metade do ATK.",
        "tipo": "duplo",
        "valor": 0,
        "custo_mana": 15,
    },
    {
        "nome": "💜 Drenar Vida",
        "descricao": "Rouba HP do inimigo e recupera metade para você.",
        "tipo": "drenar",
        "valor": 20,
        "custo_mana": 18,
    },
    {
        "nome": "💥 Nova Arcana",
        "descricao": "Explosão colossal. Custo de mana alto.",
        "tipo": "dano_fixo",
        "valor": 60,
        "custo_mana": 40,
    },
    {
        "nome": "🌀 Vórtice Arcano",
        "descricao": "Dano baseado na mana atual (1 dano por 2 mana).",
        "tipo": "mana_dano",
        "valor": 0,
        "custo_mana": 25,
    },
    {
        "nome": "🧊 Barreira de Gelo",
        "descricao": "Recupera HP igual à mana atual dividida por 3.",
        "tipo": "mana_cura",
        "valor": 0,
        "custo_mana": 20,
    },
    {
        "nome": "☄️  Meteoro",
        "descricao": "Invoca um meteoro. Dano alto com chance de crítico duplo.",
        "tipo": "meteoro",
        "valor": 45,
        "custo_mana": 35,
    },
]

# =========================
# BANCO DE DEBUFFS DO ARQUEIRO
# =========================

BANCO_DEBUFFS_ARQUEIRO = [
    {
        "nome": "🔥 Flecha Flamejante",
        "descricao": "Queimadura intensa por 3 turnos.",
        "tipo": "fogo",
        "dano_turno": 8,
        "turnos": 3,
    },
    {
        "nome": "☠️  Flecha Envenenada",
        "descricao": "Veneno profundo. Dano crescente por 4 turnos.",
        "tipo": "veneno",
        "dano_turno": 5,
        "turnos": 4,
    },
    {
        "nome": "🩸 Flecha Sangrenta",
        "descricao": "Causa sangramento moderado por 3 turnos.",
        "tipo": "sangramento",
        "dano_turno": 10,
        "turnos": 3,
    },
    {
        "nome": "⚡ Flecha Elétrica",
        "descricao": "Choque elétrico. Dano alto em 2 turnos.",
        "tipo": "choque",
        "dano_turno": 15,
        "turnos": 2,
    },
    {
        "nome": "🧊 Flecha Glacial",
        "descricao": "Congelamento lento. Dano baixo por 5 turnos.",
        "tipo": "gelo",
        "dano_turno": 4,
        "turnos": 5,
    },
    {
        "nome": "🌑 Flecha das Sombras",
        "descricao": "Maldição sombria. Dano médio por 4 turnos.",
        "tipo": "sombra",
        "dano_turno": 7,
        "turnos": 4,
    },
    {
        "nome": "🍄 Flecha Fúngica",
        "descricao": "Espora tóxica. Dano leve por 6 turnos.",
        "tipo": "toxina",
        "dano_turno": 3,
        "turnos": 6,
    },
    {
        "nome": "💀 Flecha da Morte",
        "descricao": "Maldição fatal. Dano massivo em 1 turno.",
        "tipo": "morte",
        "dano_turno": 30,
        "turnos": 1,
    },
]

# =========================
# SORTEAR HABILIDADES
# =========================


def sortear_poderes_mago():
    return sample(BANCO_PODERES_MAGO, 3)


def sortear_debuffs_arqueiro():
    return sample(BANCO_DEBUFFS_ARQUEIRO, 3)

# =========================
# CLASSES
# =========================


def escolher_classe():
    titulo("ESCOLHA SUA CLASSE")
    print("  1 - ⚔️  Guerreiro  │ HP alto, resistente")
    print("  2 - 🔮  Mago       │ Mana e poderes mágicos variados")
    print("  3 - 🏹  Arqueiro   │ Flechas com debuffs elementais")
    print("  4 - 🗡️  Ladino     │ Sorte alta, críticos frequentes")
    linha()

    escolha = input("  Sua escolha: ").strip()

    classes = {
        "1": {"classe": "Guerreiro", "hp": 130, "atk": 12, "cura": 25, "percepcao": 4, "sorte": 3},
        "2": {"classe": "Mago",      "hp": 80,  "atk": 18, "cura": 40, "percepcao": 5, "sorte": 3},
        "3": {"classe": "Arqueiro",  "hp": 100, "atk": 12, "cura": 28, "percepcao": 8, "sorte": 4},
        "4": {"classe": "Ladino",    "hp": 90,  "atk": 10, "cura": 25, "percepcao": 6, "sorte": 10},
    }

    return classes.get(escolha, classes["1"])

# =========================
# PLAYER
# =========================


def criar_player():
    classe = escolher_classe()
    linha()
    nome = input("  Nome do herói: ").strip() or "Herói"

    player = {
        "nome": nome,
        "classe": classe["classe"],
        "level": 1,
        "xp": 0,
        "hp": classe["hp"],
        "hp_max": classe["hp"],
        "atk": classe["atk"],
        "cura": classe["cura"],
        "percepcao": classe["percepcao"],
        "sorte": classe["sorte"],
        "ouro": 50,
        "inventario": [],
        "mana": 0,
        "mana_max": 0,
        "poderes_mago": [],
        "debuffs_arqueiro": [],
    }

    if player["classe"] == "Mago":
        player["mana"] = 80
        player["mana_max"] = 80
        player["poderes_mago"] = sortear_poderes_mago()
        secao("✨ SEUS PODERES SORTEADOS")
        for i, p in enumerate(player["poderes_mago"]):
            print(f"  {i+1} - {p['nome']}  (Mana: {p['custo_mana']})")
            print(f"      {p['descricao']}")
        linha()
        print("  Escolha seus poderes durante a batalha na opção 2.")
        input("  Pressione ENTER para continuar...")

    elif player["classe"] == "Arqueiro":
        player["debuffs_arqueiro"] = sortear_debuffs_arqueiro()
        secao("🏹 SEUS DEBUFFS SORTEADOS")
        for i, d in enumerate(player["debuffs_arqueiro"]):
            print(f"  {i+1} - {d['nome']}")
            print(f"      {d['descricao']}")
            print(
                f"      {d['dano_turno']} dano/turno por {d['turnos']} turno(s)")
        linha()
        print("  Use flechas com debuff na opção 2 durante as batalhas!")
        input("  Pressione ENTER para continuar...")

    return player

# =========================
# STATUS
# =========================


def status(player):
    secao(f"{player['nome']} — {player['classe']} (LVL {player['level']})")
    barra(player["hp"], player["hp_max"], label="HP")
    if player["classe"] == "Mago":
        print()
        barra(player["mana"], player["mana_max"], label="MANA")
    print(
        f"  ATK {player['atk']}  │  XP {player['xp']}  │  Ouro {player['ouro']}💰")
    print(f"  Percepção {player['percepcao']}  │  Sorte {player['sorte']}")


def status_inimigo(inimigo):
    print(f"\n  👹 {inimigo['nome']}")
    barra(inimigo["hp"], inimigo["hp_max"], label="HP")
    print(f"  ATK {inimigo['atk']}")
    if inimigo.get("debuffs_ativos"):
        for d in inimigo["debuffs_ativos"]:
            print(
                f"  ⚠️  {d['nome']} — {d['turnos_restantes']} turno(s) restante(s)")

# =========================
# MANA
# =========================


def regenerar_mana(player, quantidade=10):
    player["mana"] = min(player["mana"] + quantidade, player["mana_max"])

# =========================
# PODERES DO MAGO (em batalha)
# =========================


def menu_poderes_mago(player):
    secao("⚗️  PODERES MÁGICOS")
    print(f"  Mana atual: {player['mana']}/{player['mana_max']}\n")

    disponiveis = []
    for i, poder in enumerate(player["poderes_mago"]):
        sem_mana = player["mana"] < poder["custo_mana"]
        status_str = "❌ Sem mana" if sem_mana else f"Mana: {poder['custo_mana']}"
        print(f"  {i+1} - {poder['nome']}  ({status_str})")
        print(f"      {poder['descricao']}")
        if not sem_mana:
            disponiveis.append(i)

    print(f"  0 - ↩️  Voltar")
    linha()

    try:
        escolha = int(input("  Escolha: ").strip()) - 1
    except ValueError:
        return None

    if escolha == -1:
        return None
    if escolha not in disponiveis:
        print("\n  ❌ Poder indisponível ou mana insuficiente.")
        return None

    return player["poderes_mago"][escolha]


def usar_poder_mago(player, inimigo, poder):
    player["mana"] -= poder["custo_mana"]
    nome = poder["nome"]

    if poder["tipo"] == "dano_fixo":
        dano = poder["valor"]
        inimigo["hp"] -= dano
        print(f"\n  {nome}: {inimigo['nome']} recebeu {dano} de dano mágico!")

    elif poder["tipo"] == "duplo":
        d1 = max(player["atk"] // 2, 1)
        d2 = max(player["atk"] // 2, 1)
        inimigo["hp"] -= d1 + d2
        print(f"\n  {nome}: Primeiro raio {d1}, segundo raio {d2} de dano!")

    elif poder["tipo"] == "drenar":
        dano = poder["valor"]
        recuperado = dano // 2
        inimigo["hp"] -= dano
        player["hp"] = min(player["hp"] + recuperado, player["hp_max"])
        print(f"\n  {nome}: Causou {dano} de dano e recuperou {recuperado} HP!")

    elif poder["tipo"] == "mana_dano":
        dano = player["mana"] // 2
        inimigo["hp"] -= dano
        print(f"\n  {nome}: Converteu mana em {dano} de dano arcano!")

    elif poder["tipo"] == "mana_cura":
        cura = player["mana"] // 3
        player["hp"] = min(player["hp"] + cura, player["hp_max"])
        print(f"\n  {nome}: Converteu mana em {cura} de cura!")

    elif poder["tipo"] == "meteoro":
        dano = poder["valor"]
        if randint(1, 100) <= 30:
            dano *= 2
            print(f"\n  ☄️  METEORO CRÍTICO! {dano} de dano devastador!")
        else:
            print(f"\n  {nome}: Causou {dano} de dano!")
        inimigo["hp"] -= dano

    print(f"  Mana restante: {player['mana']}/{player['mana_max']}")

# =========================
# DEBUFFS DO ARQUEIRO
# =========================


def menu_debuffs_arqueiro(player, inimigo):
    secao("🏹 FLECHAS COM DEBUFF")

    ja_ativos = {d["tipo"] for d in inimigo.get("debuffs_ativos", [])}

    for i, debuff in enumerate(player["debuffs_arqueiro"]):
        ativo = "  ✅ Ativo" if debuff["tipo"] in ja_ativos else ""
        print(f"  {i+1} - {debuff['nome']}{ativo}")
        print(f"      {debuff['descricao']}")
        print(
            f"      {debuff['dano_turno']} dano/turno por {debuff['turnos']} turno(s)")

    print(f"  0 - ↩️  Voltar")
    linha()

    try:
        escolha = int(input("  Escolha: ").strip()) - 1
    except ValueError:
        return False

    if escolha == -1:
        return False
    if escolha < 0 or escolha >= len(player["debuffs_arqueiro"]):
        print("\n  ❌ Escolha inválida.")
        return False

    debuff = player["debuffs_arqueiro"][escolha]

    if "debuffs_ativos" not in inimigo:
        inimigo["debuffs_ativos"] = []

    # Remove versão anterior do mesmo tipo para renovar
    inimigo["debuffs_ativos"] = [
        d for d in inimigo["debuffs_ativos"] if d["tipo"] != debuff["tipo"]]
    inimigo["debuffs_ativos"].append({
        "nome": debuff["nome"],
        "tipo": debuff["tipo"],
        "dano_turno": debuff["dano_turno"],
        "turnos_restantes": debuff["turnos"],
    })

    dano_base = player["atk"]
    inimigo["hp"] -= dano_base
    print(f"\n  🏹 Disparou {debuff['nome']}! Dano base: {dano_base}")
    print(
        f"  Debuff aplicado: {debuff['dano_turno']} dano/turno por {debuff['turnos']} turno(s).")
    return True


def processar_debuffs(inimigo):
    if not inimigo.get("debuffs_ativos"):
        return

    expirados = []
    for d in inimigo["debuffs_ativos"]:
        dano = d["dano_turno"]
        # Veneno é mais forte nos turnos iniciais
        if d["tipo"] == "veneno":
            dano += (d["turnos_restantes"] - 1)

        inimigo["hp"] -= dano
        print(
            f"  {d['nome']}: {inimigo['nome']} sofreu {dano} de dano! ({d['turnos_restantes']-1} turno(s) restante(s))")
        d["turnos_restantes"] -= 1

        if d["turnos_restantes"] <= 0:
            expirados.append(d)

    for d in expirados:
        inimigo["debuffs_ativos"].remove(d)
        print(f"  ✦ Efeito {d['nome']} expirou.")

# =========================
# HABILIDADES DO GUERREIRO
# =========================


def golpe_brutal(player, inimigo):
    """Ataque poderoso: 1.5x ATK, mas deixa o jogador exposto."""
    dano = int(player["atk"] * 1.5)
    inimigo["hp"] -= dano
    print(f"\n  🗡️  Golpe Brutal! {inimigo['nome']} recebeu {dano} de dano!")
    print(f"  ⚠️  Você ficou exposto — inimigo ataca com +5 neste turno.")
    player["_exposto"] = True


def grito_de_guerra(player):
    """Buff: aumenta ATK em 8 por 3 turnos."""
    if player.get("_grito_turnos", 0) > 0:
        print(
            f"\n  ❌ Grito de Guerra já está ativo! ({player['_grito_turnos']} turno(s) restante(s))")
        return False
    player["atk"] += 8
    player["_grito_turnos"] = 3
    print(
        f"\n  📣 Grito de Guerra! ATK +8 por 3 turnos! (ATK: {player['atk']})")
    return True


def processar_buffs_guerreiro(player):
    """Decrementa buffs do Guerreiro ao fim do turno."""
    if player.get("_grito_turnos", 0) > 0:
        player["_grito_turnos"] -= 1
        if player["_grito_turnos"] == 0:
            player["atk"] -= 8
            print(
                f"  ✦ Grito de Guerra expirou. ATK voltou a {player['atk']}.")

# =========================
# HABILIDADES DO LADINO
# =========================


def ataque_furtivo(player, inimigo):
    """Ataque com alta chance de crítico baseada na sorte."""
    chance_critico = 35 + player["sorte"] * 5
    dano = player["atk"]
    if randint(1, 100) <= chance_critico:
        dano = int(dano * 2.5)
        print(
            f"\n  🗡️  ATAQUE FURTIVO CRÍTICO! {inimigo['nome']} recebeu {dano} de dano!")
    else:
        dano = int(dano * 1.2)
        print(
            f"\n  🗡️  Ataque Furtivo! {inimigo['nome']} recebeu {dano} de dano.")
    inimigo["hp"] -= dano


def roubar(player, inimigo):
    """Tenta roubar ouro do inimigo com base na sorte."""
    chance = 30 + player["sorte"] * 4
    if randint(1, 100) <= chance:
        ouro_roubado = randint(5, 20)
        player["ouro"] += ouro_roubado
        print(
            f"\n  💰 Você roubou {ouro_roubado} de ouro de {inimigo['nome']}!")
        print(f"  Ouro atual: {player['ouro']}💰")
    else:
        print(f"\n  ❌ Tentativa de roubo falhou!")

# =========================
# COMBATE BASE
# =========================


def atacar(atacante, defensor):
    dano = atacante["atk"]
    critico = randint(1, 100) <= 20

    if critico:
        dano *= 2
        print(f"\n  💥 CRÍTICO! {atacante['nome']} causou {dano} de dano!")
    else:
        print(f"\n  ⚔️  {atacante['nome']} causou {dano} de dano.")

    defensor["hp"] -= dano


def curar(player):
    antes = player["hp"]
    player["hp"] = min(player["hp"] + player["cura"], player["hp_max"])
    recuperado = player["hp"] - antes
    print(f"\n  🧪 Você se curou e recuperou {recuperado} HP!")


def analisar(player, inimigo):
    chance = 40 + (player["percepcao"] * 5)
    if randint(1, 100) <= chance:
        print(f"\n  🔍 Análise bem-sucedida!")
        status_inimigo(inimigo)
    else:
        print("\n  ❌ Falha na análise!")


def ver_vida_inimigo(inimigo):
    print(f"\n  👁️  Observando {inimigo['nome']}...")
    barra(inimigo["hp"], inimigo["hp_max"], label=inimigo["nome"][:6])


def usar_item(player):
    if not player["inventario"]:
        print("\n  🎒 Inventário vazio!")
        return

    secao("INVENTÁRIO")
    for i, item in enumerate(player["inventario"]):
        print(f"  {i+1} - {item}")
    linha()

    try:
        escolha = int(input("  Escolha o item (0 para cancelar): ")) - 1
        if escolha < 0:
            return
        item = player["inventario"][escolha]
    except (ValueError, IndexError):
        print("\n  ❌ Escolha inválida.")
        return

    if item == "Poção":
        player["hp"] = min(player["hp"] + 50, player["hp_max"])
        player["inventario"].remove(item)
        print("\n  🧪 Você usou uma Poção e recuperou 50 HP!")
    elif item == "Poção Maior":
        player["hp"] = min(player["hp"] + 80, player["hp_max"])
        player["inventario"].remove(item)
        print("\n  🧪 Você usou uma Poção Maior e recuperou 80 HP!")

# =========================
# LEVEL UP
# =========================


def xp_para_proximo_nivel(level):
    return 0  # level up garantido a cada vitória


def subir_level(player):
    necessario = 0

    if True:  # sobe sempre ao chamar
        player["xp"] = 0
        player["level"] += 1
        player["hp_max"] += 20
        player["atk"] += 5
        player["percepcao"] += 1
        player["sorte"] += 1
        player["hp"] = player["hp_max"]

        if player["classe"] == "Mago":
            player["mana_max"] += 15
            player["mana"] = player["mana_max"]

        msg_destaque(f"⭐ LEVEL UP! Você chegou ao nível {player['level']}!")
        print(f"  HP máximo: {player['hp_max']}  │  ATK: {player['atk']}")
        if player["classe"] == "Mago":
            print(f"  Mana máxima: {player['mana_max']}")
        print(f"  Próximo nível em: {necessario} XP")

        # Mago sorteia novo poder ao subir de nível
        if player["classe"] == "Mago":
            novos = [
                p for p in BANCO_PODERES_MAGO if p not in player["poderes_mago"]]
            if novos:
                novo = choice(novos)
                print(f"\n  ✨ Novo poder disponível: {novo['nome']}")
                print(
                    f"      {novo['descricao']}  (Mana: {novo['custo_mana']})")
                trocar = input(
                    "  Deseja adicionar ao seu conjunto? (s/n): ").strip().lower()
                if trocar == "s":
                    secao("SUBSTITUIR PODER")
                    for i, p in enumerate(player["poderes_mago"]):
                        print(f"  {i+1} - {p['nome']}")
                    try:
                        idx = int(input("  Substituir qual? ").strip()) - 1
                        if 0 <= idx < len(player["poderes_mago"]):
                            antigo = player["poderes_mago"][idx]["nome"]
                            player["poderes_mago"][idx] = novo
                            print(
                                f"  ✅ {antigo} substituído por {novo['nome']}!")
                    except ValueError:
                        pass

        # Arqueiro sorteia novo debuff ao subir de nível
        if player["classe"] == "Arqueiro":
            novos = [
                d for d in BANCO_DEBUFFS_ARQUEIRO if d not in player["debuffs_arqueiro"]]
            if novos:
                novo = choice(novos)
                print(f"\n  🏹 Nova flecha disponível: {novo['nome']}")
                print(
                    f"      {novo['descricao']}  ({novo['dano_turno']} dano/turno por {novo['turnos']} turno(s))")
                trocar = input(
                    "  Deseja adicionar ao seu conjunto? (s/n): ").strip().lower()
                if trocar == "s":
                    secao("SUBSTITUIR DEBUFF")
                    for i, d in enumerate(player["debuffs_arqueiro"]):
                        print(f"  {i+1} - {d['nome']}")
                    try:
                        idx = int(input("  Substituir qual? ").strip()) - 1
                        if 0 <= idx < len(player["debuffs_arqueiro"]):
                            antigo = player["debuffs_arqueiro"][idx]["nome"]
                            player["debuffs_arqueiro"][idx] = novo
                            print(
                                f"  ✅ {antigo} substituído por {novo['nome']}!")
                    except ValueError:
                        pass

# =========================
# LOOT
# =========================


def drop_item(player):
    chance = randint(1, 100) + player["sorte"]

    if chance < 50:
        item = "Poção"
    elif chance < 80:
        item = "Espada"
    else:
        item = "Item Lendário"

    print(f"\n  🎁 Você obteve: {item}!")
    player["inventario"].append(item)

# =========================
# LOJA
# =========================


# Armamentos por classe — bônus de ATK ao equipar
ARMAMENTOS = {
    "Guerreiro": [
        {"nome": "🗡️  Espada de Ferro",    "preco": 30,
            "atk_bonus": 8,  "desc": "Lâmina resistente."},
        {"nome": "⚔️  Espada de Aço",      "preco": 60,
            "atk_bonus": 18, "desc": "Forjada por mestres."},
        {"nome": "🔱 Lança Sombria",        "preco": 100,
            "atk_bonus": 30, "desc": "Arma amaldiçoada e poderosa."},
    ],
    "Mago": [
        {"nome": "🪄 Cajado de Carvalho",   "preco": 30,
            "atk_bonus": 8,  "desc": "Canaliza magia básica."},
        {"nome": "🔮 Orbe Arcano",          "preco": 60,
            "atk_bonus": 18, "desc": "Amplifica feitiços."},
        {"nome": "✨ Bastão do Vórtice",    "preco": 100,
            "atk_bonus": 30, "desc": "Poder mágico supremo."},
    ],
    "Arqueiro": [
        {"nome": "🏹 Arco Curto",           "preco": 30,
            "atk_bonus": 8,  "desc": "Ágil e preciso."},
        {"nome": "🎯 Arco Longo",           "preco": 60,
            "atk_bonus": 18, "desc": "Alcance superior."},
        {"nome": "💫 Arco das Estrelas",    "preco": 100,
            "atk_bonus": 30, "desc": "Imbuído de energia celestial."},
    ],
    "Ladino": [
        {"nome": "🗡️  Adaga Enferrujada",  "preco": 30,
            "atk_bonus": 8,  "desc": "Rápida e silenciosa."},
        {"nome": "⚡ Adaga Élfica",         "preco": 60,
            "atk_bonus": 18, "desc": "Levíssima, corte certeiro."},
        {"nome": "☠️  Lâmina da Morte",     "preco": 100,
            "atk_bonus": 30, "desc": "Um toque e é o fim."},
    ],
}


def vendedor(player):
    armas = ARMAMENTOS.get(player["classe"], [])

    while True:
        secao("🧑‍💼 VENDEDOR AMBULANTE")
        print(
            f"  Seu ouro: {player['ouro']}💰  │  ATK atual: {player['atk']}\n")

        print("  1 - 🧪 Poção Maior       (20 ouro)  — Recupera 50 HP")

        opcao_mana = None
        if player["classe"] == "Mago":
            print(
                f"  2 - 💧 Elixir de Mana    (15 ouro)  — Recupera 40 Mana  (atual: {player['mana']}/{player['mana_max']})")
            opcao_mana = "2"
            base = 3
        else:
            base = 2

        for i, arma in enumerate(armas):
            equipado = "  ✅ Equipado" if player.get(
                "_arma_equipada") == arma["nome"] else ""
            print(
                f"  {base+i} - {arma['nome']}  ({arma['preco']} ouro)  +{arma['atk_bonus']} ATK  │ {arma['desc']}{equipado}")

        sair = base + len(armas)
        print(f"  {sair} - Sair da loja")
        linha()

        op = input("  Escolha: ").strip()

        if op == "1":
            if player["ouro"] >= 20:
                player["ouro"] -= 20
                player["inventario"].append("Poção Maior")
                print("\n  ✅ Poção Maior comprada!")
            else:
                print("\n  ❌ Ouro insuficiente!")

        elif op == opcao_mana:
            if player["ouro"] >= 15:
                player["ouro"] -= 15
                player["mana"] = min(player["mana"] + 40, player["mana_max"])
                print(
                    f"\n  ✅ Mana recuperada! Mana: {player['mana']}/{player['mana_max']}")
            else:
                print("\n  ❌ Ouro insuficiente!")

        elif op.isdigit() and base <= int(op) < sair:
            arma = armas[int(op) - base]
            if player.get("_arma_equipada") == arma["nome"]:
                print(f"\n  ⚠️  {arma['nome']} já está equipada!")
            elif player["ouro"] >= arma["preco"]:
                # Remove bônus da arma anterior se houver
                if player.get("_arma_atk_bonus", 0) > 0:
                    player["atk"] -= player["_arma_atk_bonus"]
                player["ouro"] -= arma["preco"]
                player["atk"] += arma["atk_bonus"]
                player["_arma_equipada"] = arma["nome"]
                player["_arma_atk_bonus"] = arma["atk_bonus"]
                print(f"\n  ✅ {arma['nome']} equipada! ATK: {player['atk']}")
            else:
                print("\n  ❌ Ouro insuficiente!")

        elif op == str(sair):
            print("\n  Até a próxima, aventureiro!")
            break

# =========================
# BATALHA
# =========================


def submenu_ataque(player, inimigo):
    """Submenu de ataque com habilidades da classe. Retorna True se consumiu turno."""
    secao("⚔️  ATACAR")
    print("  1 - 🗡️  Ataque Normal")

    if player["classe"] == "Guerreiro":
        print("  2 - 💥 Golpe Brutal              │ 1.5x dano, fica exposto")

    elif player["classe"] == "Mago":
        print(
            f"  2 - ✨ Poder Mágico              │ Mana: {player['mana']}/{player['mana_max']}")

    elif player["classe"] == "Arqueiro":
        print("  2 - 🏹 Flecha com Debuff         │ Ataque + efeito elemental")

    elif player["classe"] == "Ladino":
        print("  2 - 🗡️  Ataque Furtivo           │ Alta chance de crítico")

    print("  0 - ↩️  Voltar")
    linha()

    op = input("  Escolha: ").strip()

    if op == "0":
        return False

    if op == "1":
        atacar(player, inimigo)
        return True

    if player["classe"] == "Guerreiro":
        if op == "2":
            golpe_brutal(player, inimigo)
            return True

    elif player["classe"] == "Mago":
        if op == "2":
            poder = menu_poderes_mago(player)
            if poder is None:
                return False
            usar_poder_mago(player, inimigo, poder)
            return True

    elif player["classe"] == "Arqueiro":
        if op == "2":
            return menu_debuffs_arqueiro(player, inimigo)

    elif player["classe"] == "Ladino":
        if op == "2":
            ataque_furtivo(player, inimigo)
            return True

    return False


def menu_batalha(player):
    print("\n  O que deseja fazer?")
    print("  1 - ⚔️  Atacar / Habilidades")
    print("  2 - 🧪 Curar")
    print("  3 - 🔍 Analisar inimigo")
    print("  4 - 👁️  Ver vida do inimigo")
    print("  5 - 🎒 Inventário")
    print("  6 - 🏃 Fugir")
    linha()
    return input("  Escolha: ").strip()


def batalha(player, inimigo):
    if "hp_max" not in inimigo:
        inimigo["hp_max"] = inimigo["hp"]
    if "debuffs_ativos" not in inimigo:
        inimigo["debuffs_ativos"] = []

    titulo(f"⚔️  BATALHA — {inimigo['nome']}")
    status_inimigo(inimigo)

    while True:
        status(player)
        op = menu_batalha(player)
        consumiu_turno = True

        if op == "1":
            consumiu_turno = submenu_ataque(player, inimigo)

        elif op == "2":
            curar(player)

        elif op == "3":
            analisar(player, inimigo)
            consumiu_turno = False

        elif op == "4":
            ver_vida_inimigo(inimigo)
            consumiu_turno = False

        elif op == "5":
            usar_item(player)
            consumiu_turno = False

        elif op == "6":
            if randint(1, 100) <= 40:
                print("\n  🏃 Você conseguiu fugir!")
                return
            else:
                print("\n  ❌ Não conseguiu fugir!")

        if not consumiu_turno:
            continue

        # --- Checa morte do inimigo ---
        if inimigo["hp"] <= 0:
            msg_destaque(f"🏆 {inimigo['nome']} foi derrotado!")
            player["xp"] += inimigo["xp"]
            player["ouro"] += 20
            print(f"  Ouro ganho: +20💰")
            drop_item(player)
            subir_level(player)
            vendedor(player)
            return

        # --- Processa debuffs antes do turno inimigo ---
        if inimigo.get("debuffs_ativos"):
            secao("⚠️  EFEITOS DE TURNO")
            processar_debuffs(inimigo)

        # Checa morte por debuff
        if inimigo["hp"] <= 0:
            msg_destaque(f"🏆 {inimigo['nome']} foi destruído pelos efeitos!")
            player["xp"] += inimigo["xp"]
            player["ouro"] += 20
            print(f"  Ouro ganho: +20💰")
            drop_item(player)
            subir_level(player)
            vendedor(player)
            return

        # --- Turno do inimigo ---
        # Guerreiro exposto pelo Golpe Brutal sofre +5 de dano
        if player.get("_exposto"):
            inimigo["atk"] += 5
            atacar(inimigo, player)
            inimigo["atk"] -= 5
            player["_exposto"] = False
        else:
            atacar(inimigo, player)

        # Decrementa buffs do Guerreiro
        if player["classe"] == "Guerreiro":
            processar_buffs_guerreiro(player)

        if player["hp"] <= 0:
            titulo("💀 GAME OVER")
            print(f"  {player['nome']} foi derrotado por {inimigo['nome']}.\n")
            sys.exit()

# =========================
# CAPÍTULOS
# =========================


def capitulo1(player):
    titulo("📖 CAPÍTULO 1 — A Floresta Sombria")

    print("""
  A floresta ao sul de Eldoria já foi um lugar pacífico.

  Hoje, o silêncio é perturbador.

  As árvores parecem vivas...
  observando cada passo seu.

  Você sente algo errado.

  Algo... te observando.
""")
    linha()

    print("""
  🧙 Feiticeiro Errante — Kael, o Observador

  "Você também sente isso, não sente?

  A floresta... ela não está natural.

  Criaturas pequenas já foram corrompidas.

  Se até os ratos mudaram...

  temo o que está por vir."
""")
    linha()
    input("  Pressione ENTER para continuar...")

    inimigo = {"nome": "Rato Sombrio", "hp": 30,
               "hp_max": 30, "atk": 5, "xp": 10}
    batalha(player, inimigo)

    print("""
  🛡️ Cavaleiro Caído — Sir Aldren

  "Você... conseguiu derrotar a criatura?

  Então ainda há esperança...

  Eu falhei em proteger estas terras.

  Siga para as ruínas de Aethel...

  Mas cuidado...

  algo antigo despertou lá."
""")
    linha()


def capitulo2(player):
    titulo("📖 CAPÍTULO 2 — As Ruínas de Aethel")

    print("""
  As ruínas de Aethel se erguem diante de você.

  Antigas, silenciosas... e ameaçadoras.

  Você sente o poder dos fragmentos mais forte aqui.

  Mas também sente...

  algo te observando das sombras.

  Você não está sozinho.
""")
    linha()

    print("""
  🍺 Dono da Taverna — Borin, o Sobrevivente

  "Eu vi aventureiros mais fortes que você entrarem nessas ruínas...

  Nenhum voltou.

  Mas você tem algo diferente...

  Se for entrar, leve isso a sério.

  Aqui... monstros não são os únicos perigos."
""")
    linha()

    inimigos = [
        {"nome": "Esqueleto",       "hp": 80, "hp_max": 80, "atk": 15, "xp": 25},
        {"nome": "Mago Corrompido", "hp": 70, "hp_max": 70, "atk": 18, "xp": 30},
    ]

    batalha(player, choice(inimigos).copy())

    print("""
  🔮 Maga do Véu — Lysara

  "Os fragmentos estão corrompendo tudo.

  O Guardião... não é mais o mesmo.

  Se você enfrentá-lo...

  não hesite.

  Ou você morre...
  ou Eldoria morre."
""")
    linha()

    batalha(player, choice(inimigos).copy())

    print("""
  👹 Guardião de Aethel

  "VOCÊ NÃO DEVERIA TER VINDO.

  O CORAÇÃO... É MEU AGORA.

  NINGUÉM IRÁ RESTAURÁ-LO."
""")
    linha()
    input("  Pressione ENTER para lutar...")

    boss = {"nome": "Guardião de Aethel", "hp": 120,
            "hp_max": 120, "atk": 18, "xp": 60}
    msg_destaque("O Guardião de Aethel bloqueia seu caminho!")
    batalha(player, boss)

    msg_destaque("🎉 Parabéns! Aethel foi libertada!")

# =========================
# MENU PRINCIPAL
# =========================


def menu():
    titulo("🌌 A QUEDA DE ELDORIA")

    print("""
  Há séculos, o reino de Eldoria prosperava sob a proteção do artefato sagrado:
  o Coração de Aethel.

  Mas algo deu errado...

  O artefato se fragmentou.

  Desde então, criaturas sombrias surgem das sombras,
  e antigos guardiões foram corrompidos.

  Você é um dos poucos capazes de sentir os fragmentos.

  E talvez...
  o único capaz de restaurar o equilíbrio.

  Sua jornada começa agora.
""")
    linha()
    input("  Pressione ENTER para continuar...")

    titulo("⚔️  ELDORIA — O RPG")
    print("  1 - 🗡️  Novo Jogo")
    print("  2 - 🚪 Sair")
    linha()

    op = input("  Escolha: ").strip()

    if op == "1":
        player = criar_player()
        capitulo1(player)
        capitulo2(player)
        titulo("FIM DE JOGO")
        print(f"  Obrigado por jogar, {player['nome']}!\n")
        linha("═")
        print("  🎮 CRÉDITOS")
        linha("═")
        print("""
  Jogo criado por:

  Gustavo Saurim de Aguiar Minighitti

  Obrigado por aventurar-se por Eldoria.
  Que o Coração de Aethel guie seus passos.
""")
        linha("═")
    else:
        print("\n  Até mais, aventureiro!\n")
        sys.exit()

# =========================
# START
# =========================


menu()