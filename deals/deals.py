import funcoes


def deals():
    obj = funcoes.consumir_api("https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.deal.list")
    conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
    cursor = conexao.cursor()

    for a in obj['result']:
        cursor.execute(f"SELECT ID FROM deals;")
        tlinhas = cursor.rowcount
        if tlinhas > len(obj['result']):
            cursor.execute(funcoes.deletar('deals'))

        cursor.execute(f"SELECT count(*) FROM deals WHERE ID={a['ID']};")
        linhas = cursor.fetchall()
        if linhas[0][0] == 0:
            cursor.execute(funcoes.inserir_deals(a))

        else:
            cursor.execute(funcoes.atualizar_deals(a))

    conexao.commit()
    conexao.close()
