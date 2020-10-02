from django.shortcuts import render
import funcoes


def index(request):
    return render(request, 'index.html')


def deals(request):
    if request.method == 'GET':
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
        return render(request, 'deals.html')


def leads(request):
    if request.method == 'GET':
        obj = funcoes.consumir_api("https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.lead.list")
        conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
        cursor = conexao.cursor()

        for a in obj['result']:
            cursor.execute(f"SELECT ID FROM leads;")
            tlinhas = cursor.rowcount
            if tlinhas > len(obj['result']):
                cursor.execute(funcoes.deletar('leads'))

            cursor.execute(f"SELECT count(*) FROM leads WHERE ID={a['ID']};")
            linhas = cursor.fetchall()
            if linhas[0][0] == 0:
                cursor.execute(funcoes.inserir_leads(a))

            else:
                cursor.execute(funcoes.atualizar_leads(a))

        conexao.commit()
        conexao.close()
        return render(request, 'leads.html')


def get_lead(request, id):
    obj = funcoes.consumir_api(f'https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.lead.get?ID={id}')
    conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
    cursor = conexao.cursor()

    cursor.execute(f"SELECT count(*) FROM leads WHERE ID={obj['result']['ID']};")
    linhas = cursor.fetchall()
    if linhas[0][0] == 0:
        cursor.execute(funcoes.inserir_leads(obj['result']))

    else:
        cursor.execute(funcoes.atualizar_leads(obj['result']))

    conexao.commit()
    conexao.close()
    return render(request, 'get.html')


def get_deal(request, id):
    obj = funcoes.consumir_api(f'https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.deal.get?ID={id}')
    conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
    cursor = conexao.cursor()

    cursor.execute(f"SELECT count(*) FROM deals WHERE ID={obj['result']['ID']};")
    linhas = cursor.fetchall()
    if linhas[0][0] == 0:
        cursor.execute(funcoes.inserir_deals(obj['result']))

    else:
        cursor.execute(funcoes.atualizar_deals(obj['result']))

    conexao.commit()
    conexao.close()
    return render(request, 'get.html')


def delete_lead(request, id):
    conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM leads WHERE ID={id}")

    conexao.commit()
    conexao.close()
    return render(request, 'get.html')


def delete_deal(request, id):
    conexao = funcoes.conectar('bitrix', 'root', 'Luigi3107')
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM deals WHERE ID={id}")

    conexao.commit()
    conexao.close()
    return render(request, 'get.html')
