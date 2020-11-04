from django.shortcuts import render
import funcoes
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')


def deals(request):
    obj = funcoes.consumir_api("https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.deal.list")
    conexao = funcoes.conectar('testeluigi', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
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
    obj = funcoes.consumir_api("https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.lead.list")
    conexao = funcoes.conectar('testeluigi', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
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


@csrf_exempt
def get_lead(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        obj = funcoes.consumir_api(f'https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.lead.get?ID={id}')
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"SELECT count(*) FROM LEAD WHERE ID={obj['result']['ID']};")
        linhas = cursor.fetchall()
        if linhas[0][0] == 0:
            cursor.execute(funcoes.inserir_leads(obj['result']))

        else:
            cursor.execute(funcoes.atualizar_leads(obj['result']))

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')


@csrf_exempt
def get_deal(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        obj = funcoes.consumir_api(f'https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.deal.get?ID={id}')
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"SELECT count(*) FROM DEAL WHERE ID={obj['result']['ID']};")
        linhas = cursor.fetchall()
        if linhas[0][0] == 0:
            cursor.execute(funcoes.inserir_deals(obj['result']))

        else:
            cursor.execute(funcoes.atualizar_deals(obj['result']))

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')


@csrf_exempt
def get_contact(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        obj = funcoes.consumir_api(f'https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.contact.get?ID={id}')
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"SELECT count(*) FROM CONTACT WHERE ID={obj['result']['ID']};")
        linhas = cursor.fetchall()
        if linhas[0][0] == 0:
            cursor.execute(funcoes.inserir_contato(obj['result']))

        else:
            cursor.execute(funcoes.atualizar_contato(obj['result']))

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')


@csrf_exempt
def delete_lead(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"DELETE FROM LEAD WHERE ID={id}")

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')


@csrf_exempt
def delete_deal(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"DELETE FROM DEAL WHERE ID={id}")

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')


@csrf_exempt
def delete_contact(request):
    if request.method == 'POST':
        id = request.POST['data[FIELDS][ID]']
        conexao = funcoes.conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
        cursor = conexao.cursor()

        cursor.execute(f"DELETE FROM CONTACT WHERE ID={id}")

        conexao.commit()
        conexao.close()
        return render(request, 'get.html')