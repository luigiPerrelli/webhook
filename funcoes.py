import requests
import pymysql
import json

'bitrix''root''Luigi3107'
def conectar(database, user, password):
    return pymysql.connect(host='45.77.94.236', db=database, user=user, passwd=password)


def consumir_api(url):
    r = requests.get(url)
    return json.loads(r.content)


def inserir_leads(a):
    print(f"A ID:{a['ID']} foi INSERIDA")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()

    if not a['UF_CRM_1594415348970']:
        CODIGO_PRODUTO = ''
    elif len(a['UF_CRM_1594415348970']) == 1:
        CODIGO_PRODUTO = a['UF_CRM_1594415348970'][0]
    else:
        CODIGO_PRODUTO = ''

    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''

    cursor.execute("SELECT * FROM ajustes WHERE tipo='STATUS'")
    ajustes_status = cursor.fetchall()
    status = ''
    for s in ajustes_status:
        if a['STATUS_ID'] == s[1]:
            status = s[2]

    cursor.execute("SELECT * FROM ajustes WHERE tipo='SOURCE'")
    ajustes_fontes = cursor.fetchall()
    fonte = ''
    for f in ajustes_fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    global cidade
    cidades = {'832': 'Caruaru', '834': 'Maceió', '836': 'Recife', '838': 'Serra Talhada'}
    while True:
        for key, value in cidades.items():
            if a['UF_CRM_1585530790'] == key:
                cidade = value
                break
            else:
                cidade = ''
        break

    global forma
    formas = {'888': 'Link de Pagamento', '890': 'Na loja'}
    while True:
        for key, value in formas.items():
            if a['UF_CRM_1589554873'] == key:
                forma = value
                break
            else:
                forma = ''
        break

    global motivo_i
    motivos_i = {'946': 'Informações de lojas', '948': 'Pós venda', '950': 'Conferir estoque da loja',
                 '952': 'Negociação de venda', '954': 'Orçamento'}
    while True:
        for key, value in motivos_i.items():
            if a['UF_CRM_1590574186777'] == key:
                motivo_i = value
                break
            else:
                motivo_i = ''
        break

    global motivo_n_v
    motivos_n_v = {'956': 'Comprou na concorrência', '958': 'Não comercializamos', '960': 'Não respondeu',
                   '962': 'Comprou na loja', '964': 'Desistiu da compra', '1006': 'Atendimento a cliente',
                   '1032': 'Não temos estoque'}
    while True:
        for key, value in motivos_n_v.items():
            if a['UF_CRM_1590574245657'] == key:
                motivo_n_v = value
                break
            else:
                motivo_n_v = ''
        break

    global estado
    estados = {'1144': 'AC', '1146': 'AL', '1148': 'AM', '1150': 'BA', '1152': 'CE', '1154': 'DF', '1156': 'ES',
               '1158': 'GO', '1160': 'MA', '1162': 'MT', '1164': 'MS', '1166': 'MG', '1168': 'PA', '1170': 'PB',
               '1172': 'PR', '1174': 'PE', '1176': 'PI', '1178': 'RJ', '1180': 'RN', '1182': 'RS',
               '1184': 'RO', '1186': 'RR', '1188': 'SC', '1190': 'SP', '1192': 'SE', '1194': 'TO'}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_1598647901'] == key:
                estado = value
                break
            else:
                estado = ''
        break

    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']):
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ''

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    company = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.company.get?ID={a['COMPANY_ID']}")
    if len(company['result']) > 0:
        empresa = company['result']['TITLE']
    else:
        empresa = ''
    return ("INSERT INTO LEAD (ID, Status, Nome_do_Lead, Primeiro_nome, Segundo_nome, Sobrenome, Criado,"
            "Fonte ,Telefone_de_trabalho, Responsável, Informações_de_status,"
            "Informações_da_fonte, Criado_por, Modificado, Modificado_Por, Nome_da_empresa,"
            "Lead_repetido, CIDADE_TELEVENDAS, Data_de_Conversão, Forma_de_Pagamento, Número_do_pedido_Winthor,"
            "MOTIVO_DAS_INTERAÇÕES, MOTIVO_NÃO_VENDA, CÓDIGO_DO_PRODUTO, OBSERVAÇÃO_NÃO_VENDA, Estado_UF)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "        '{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}', '{}')"
            .format(a['ID'], status, a['TITLE'], a['NAME'], a['SECOND_NAME'], a['LAST_NAME'], a['DATE_CREATE'],
                    fonte, telefone, responsavel, a['STATUS_DESCRIPTION'],
                    a['SOURCE_DESCRIPTION'], criador, a['DATE_MODIFY'], modificador, empresa,
                    a['IS_RETURN_CUSTOMER'], cidade, a['UF_CRM_1589554873'], forma, a['UF_CRM_1590010371392'],
                    motivo_i, motivo_n_v, CODIGO_PRODUTO, a['UF_CRM_1594415383097'], estado))


def atualizar_leads(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()

    if not a['UF_CRM_1594415348970']:
        CODIGO_PRODUTO = ''
    elif len(a['UF_CRM_1594415348970']) == 1:
        CODIGO_PRODUTO = a['UF_CRM_1594415348970'][0]
    else:
        CODIGO_PRODUTO = ''

    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''

    cursor.execute("SELECT * FROM ajustes WHERE tipo='STATUS'")
    ajustes_status = cursor.fetchall()
    status = ''
    for s in ajustes_status:
        if a['STATUS_ID'] == s[1]:
            status = s[2]

    cursor.execute("SELECT * FROM ajustes WHERE tipo='SOURCE'")
    ajustes_fontes = cursor.fetchall()
    fonte = ''
    for f in ajustes_fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    global cidade
    cidades = {'832': 'Caruaru', '834': 'Maceió', '836': 'Recife', '838': 'Serra Talhada'}
    while True:
        for key, value in cidades.items():
            if a['UF_CRM_1585530790'] == key:
                cidade = value
                break
            else:
                cidade = ''
        break
    global forma
    formas = {'888': 'Link de Pagamento', '890': 'Na loja'}
    while True:
        for key, value in formas.items():
            if a['UF_CRM_1589554873'] == key:
                forma = value
                break
            else:
                forma = ''
        break

    global motivo_i
    motivos_i = {'946': 'Informações de lojas', '948': 'Pós venda', '950': 'Conferir estoque da loja',
                 '952': 'Negociação de venda', '954': 'Orçamento'}
    while True:
        for key, value in motivos_i.items():
            if a['UF_CRM_1590574186777'] == key:
                motivo_i = value
                break
            else:
                motivo_i = ''
        break

    global motivo_n_v
    motivos_n_v = {'956': 'Comprou na concorrência', '958': 'Não comercializamos', '960': 'Não respondeu',
                   '962': 'Comprou na loja', '964': 'Desistiu da compra', '1006': 'Atendimento a cliente',
                   '1032': 'Não temos estoque'}
    while True:
        for key, value in motivos_n_v.items():
            if a['UF_CRM_1590574245657'] == key:
                motivo_n_v = value
                break
            else:
                motivo_n_v = ''
        break

    global estado
    estados = {'1144': 'AC', '1146': 'AL', '1148': 'AM', '1150': 'BA', '1152': 'CE', '1154': 'DF', '1156': 'ES',
               '1158': 'GO', '1160': 'MA', '1162': 'MT', '1164': 'MS', '1166': 'MG', '1168': 'PA', '1170': 'PB',
               '1172': 'PR', '1174': 'PE', '1176': 'PI', '1178': 'RJ', '1180': 'RN', '1182': 'RS',
               '1184': 'RO', '1186': 'RR', '1188': 'SC', '1190': 'SP', '1192': 'SE', '1194': 'TO'}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_1598647901'] == key:
                estado = value
                break
            else:
                estado = ''
        break

    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']) > 0:
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ""

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    company = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.company.get?ID={a['COMPANY_ID']}")
    if len(company['result']) > 0:
        empresa = company['result']['TITLE']
    else:
        empresa = ''
    return (
        "UPDATE LEAD SET Status='{}', Nome_do_lead='{}', Primeiro_nome='{}', Segundo_nome='{}', Sobrenome='{}', Criado='{}',"
        "Fonte='{}',Telefone_de_trabalho='{}', Responsável='{}', Informações_de_status='{}',"
        "Informações_da_fonte='{}', Criado_por='{}', Modificado='{}', Modificado_Por='{}', Nome_da_empresa='{}',"
        "Lead_repetido='{}', CIDADE_TELEVENDAS='{}', Data_de_Conversão='{}', Forma_de_Pagamento='{}', Número_do_pedido_Winthor='{}',"
        "MOTIVO_DAS_INTERAÇÕES='{}', MOTIVO_NÃO_VENDA='{}', CÓDIGO_DO_PRODUTO='{}', OBSERVAÇÃO_NÃO_VENDA='{}', Estado_UF='{}'"
        "WHERE ID ='{}'"
        .format(status, a['TITLE'], a['NAME'], a['SECOND_NAME'], a['LAST_NAME'], a['DATE_CREATE'],
                fonte, telefone, responsavel, a['STATUS_DESCRIPTION'],
                a['SOURCE_DESCRIPTION'], criador, a['DATE_MODIFY'], modificador, empresa,
                a['IS_RETURN_CUSTOMER'], cidade, a['UF_CRM_1589554873'], forma, a['UF_CRM_1590010371392'],
                motivo_i, motivo_n_v, CODIGO_PRODUTO, a['UF_CRM_1594415383097'], estado,
                a['ID']))


def inserir_deals(a):
    print(f"A ID:{a['ID']} foi INSERIDA.")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM ajustes where tipo like'DEAL_STAG%'")
    ajustes_fontes = cursor.fetchall()
    fase = ''
    for f in ajustes_fontes:
        if a['STAGE_ID'] == f[1]:
            fase = f[2]

    cursor.execute("SELECT * FROM pipeline")
    pipelines = cursor.fetchall()
    pipeline = ''
    for p in pipelines:
        if a['CATEGORY_ID'] == p[0]:
            pipeline = p[1]

    cursor.execute("SELECT * FROM ajustes WHERE tipo='SOURCE'")
    ajustes_fontes = cursor.fetchall()
    fonte = ''
    for f in ajustes_fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    cursor.execute("SELECT * FROM ajustes where tipo = 'DEAL_TYPE'")
    ajustes_tipos = cursor.fetchall()
    tipo = ''
    for t in ajustes_tipos:
        if a['TYPE_ID'] == t[1]:
            tipo = t[2]
    if a['TYPE_ID'] == 'GOODS':
        tipo = 'GOODS'

    global classificacao
    c = {"520": "BO Entrega", "48": "Elogio", "538": "Midias Sociais", "434": "Ocorrência de Entrega",
         "44": "Reclamação", "46": "Solicitação", "50": "Sugestão", "546": "Ocorrência de Corte"}
    while True:
        for key, value in c.items():
            if a['UF_CRM_1571064926633'] == key:
                classificacao = value
                break
            else:
                classificacao = ''
        break

    global ocorrencia_sac
    ocorrencias = {"54": "2ª Via de Nota fiscal", "56": "2ª Via de Boleto", "58": "Assistência de Marca Exclusiva",
                   "1522": "Atendimento Loja - Elogio", "52": "Atendimento loja - Sugestão",
                   "218": "Atendimento loja - Reclamação",
                   "528": "Atendimento do motorista / Entregador - elogio",
                   "530": "Atendimento do motorista / Entregador - reclamação",
                   "554": "Atraso na entrega", "560": "Atendimento Loja", "816": "Atendimento SAC - Elogio",
                   "818": "Atendimento SAC - Reclamação", "1464": "Canhoto de Entrega",
                   "74": "Cliente discorda da Norma de Entrega",
                   "436": "Cliente Insatisfeito com a compra", "80": "Cliente só recebe outro dia - Retirar de carga",
                   "544": "Consulta de pedido", "82": "Corte de produto", "92": "entrega futura/ saber previsão",
                   "444": "Erro de procedimento no pedido", "450": "Erro Separação_Logística",
                   "446": "Falta de produto loja - separação de pedido", "96": "Falta de produto na loja",
                   "568": "Fornecedor, parceria e patrocínio ", "452": "Observação no pedido",
                   "536": "Midias Sociais", "104": "Ordem coleta / Desacordo (Erro logistica)",
                   "106": "Ordem coleta / Desacordo (Erro loja)", "662": "Previsão de Entrega",
                   "534": "Refazer pedido", "532": "Raio de entrega / Frete",
                   "804": "Resgate do termo de entrega assinado",
                   "1466": "Sem registro de BO", "120": "Solicitação de visita Técnica do Fornecedor",
                   "122": "Troca de produto", "1134": "E-commerce – Problema Site", "1136": "E-commerce – Troca",
                   "1138": "E-commerce – corte de produto", "1140": "E-commerce – Duvida de navegação",
                   "1142": "E-commerce – Falta de produto na Separação"}
    while True:
        for key, value in ocorrencias.items():
            if a['UF_CRM_1571065370'] == key:
                ocorrencia_sac = value
                break
            else:
                ocorrencia_sac = ''
        break

    global loja
    lojas = {"210": "Afogados", "212": "Imbiribeira", "214": "Olinda", "684": "CD Afogados", "822": "Caruaru 43",
             "824": "Caruaru 45", "826": "Logística Caruaru", "828": "Maceió 53", "830": "CD Maceió",
             "1060": "Serra Talhada 24", "1062": "Serra Talhada 27", "1064": "Serra Talhada 30"}
    while True:
        for key, value in lojas.items():
            if a['UF_CRM_1571660434'] == key:
                loja = value
                break
            else:
                loja = ''
        break

    global televendas_a
    televendas_as = {"226": "Recusou proposta", "228": "Telefone não atende", "230": "Número inválido",
                     "232": "Responsável ausente", "234": "Solicitado Documentação"}
    while True:
        for key, value in televendas_as.items():
            if a['UF_CRM_1571663098'] == key:
                televendas_a = value
                break
            else:
                televendas_a = ''
        break

    global televendas_r
    televendas_rs = {"236": "Orçamento", "238": "Cotação de Preço", "240": "Confirmação de produto",
                     "242": "Confirmação de estoque"}
    while True:
        for key, value in televendas_rs.items():
            if a['UF_CRM_1571753030'] == key:
                televendas_r = value
                break
            else:
                televendas_r = ''
        break

    global ocorrencias_sac
    ocorrencias_sacs = {
        "268": "Atendimento loja - Sugestão", "270": "Atendimento loja - Elogio",
        "272": "Atendimento loja - reclamação", "274": "2ª Via de Boleto",
        "276": "2ª Via de Nota fiscal", "278": "Assistência de Marca Exclusiva",
        "280": "Atendimento do Motorista / Entregador", "282": "Atraso na Entrega",
        "284": "Cliente Desistiu da compra", "286": "Cliente discorda da Norma de Entrega",
        "288": "Cliente já recebeu mercadoria (erro logistica)", "290": "Cliente já recebeu mercadoria (erro loja)",
        "292": "Cliente só recebe outro dia", "294": "Corte de produto", "296": "entrega futura/ saber previsão",
        "298": "Fale Consosco - Elogio", "300": "Fale Consosco - Solicitação", "302": "Fale Consosco - Reclamação",
        "304": "Falta de produto na loja", "306": "Ordem coleta / Desacordo (Erro logistica)",
        "308": "Ordem coleta / Desacordo (Erro loja)",
        "310": "Previsão de entrega", "312": "Produto Avariado", "314": "Relatório de boletos atrasados",
        "316": "Solicitação de visita Técnica do Fornecedor", "318": "Troca de produto"}
    while True:
        for key, value in ocorrencias_sacs.items():
            if a['UF_CRM_1571753030'] == key:
                ocorrencias_sac = value
                break
            else:
                ocorrencias_sac = ''
        break

    global ocorrencia_e
    ocorrencias_e = {
        "320": "BO Avaria", "322": "BO desacordo", "324": "BO falta Produto", "326": "Carro pequeno",
        "458": "Cliente Desistiu da compra", "328": "Cliente não quer  receber entrega",
        "460": "Cliente recebeu mercadoria duplicada (Pessoa física)", "330": "Desacordo com o Pedido",
        "462": "Cliente recebeu mercadoria duplicada (Pessoa jurídica)",
        "808": "Cliente só recebe outro dia - Retirar de carga",
        "332": "Dificil acesso", "334": "Endereço ñ localizado", "336": "Entrega de BO",
        "540": "Erro de Separação", "806": "Falta de produto loja - separação de pedido",
        "338": "Falta de produto no veículo", "340": "Fora de Rota", "342": "Não deu tempo",
        "464": "Ocorrências de Entrega", "524": "Produto Avariado", "468": "Refazer Pedido",
        "470": "Retorno de BO", "344": "Residência fechada", "542": "Saiu de carga",
        "346": "Retorno de entrega", "348": "Veiculo quebrado"}
    while True:
        for key, value in ocorrencias_e.items():
            if a['UF_CRM_1571753310'] == key:
                ocorrencia_e = value
                break
            else:
                ocorrencia_e = ''
        break

    global ocorrencia_ms
    ocorrencias_ms = {"575": "2ª via nota fiscal ", "577": "Atendimento Vendedores - Reclamação",
                      "579": "Atendimento Frete de loja",
                      "581": "Atendimento SAC", "583": "Atendimento Expedição", "585": "Atendimento Vendedor - Elogio",
                      "587": "Atraso na entrega", "589": "Atendimento Loja", "591": "Campanha promocional - Reclamação",
                      "593": "Campanha promocional - Solicitação", "820": "Consulta de Entrega",
                      "1118": "Elogio Motorista",
                      "595": "Especificação de produto", "1114": "Feedback",
                      "597": "Fornecedor, parceria e patrocínio ",
                      "599": "horário de atendimento", "607": "Insatisfação com a compra",
                      "810": "Interação do cliente",
                      "1120": "Mensões", "601": "Preço e pagamento de produto", "603": "Previsão de entrega",
                      "812": "Raio de Entrega / Frete", "1116": "Reclamação Motorista", "814": "Sugestão",
                      "605": "Trabalhe conosco ", "1122": "Trocas", "1132": "Entrega Posterior"}
    while True:
        for key, value in ocorrencias_ms.items():
            if a['UF_CRM_1579203250'] == key:
                ocorrencia_ms = value
                break
            else:
                ocorrencia_ms = ''
        break

    global rede_social
    redes = {"642": "Facebook - Messenger", "644": "Facebook - Comentário", "646": "Instagram - Comentário",
             "648": "Instagram - Direct", "650": "WhatsApp"}
    while True:
        for key, value in redes.items():
            if a['UF_CRM_1579266030'] == key:
                rede_social = value
                break
            else:
                rede_social = ''
        break

    global classificacao_o
    classicacoes_o = {"664": "Orçamento", "666": "Preço", "668": "Estoque em lojas",
                      "670": "Especificação de produto", "672": "Informações de outra área"}
    while True:
        for key, value in classicacoes_o.items():
            if a['UF_CRM_1580234661'] == key:
                classificacao_o = value
                break
            else:
                classificacao_o = ''
        break

    global cidade_tlv
    cidades_tlv = {"840": "Caruaru", "842": "Maceió", "844": "Recife", "846": "Serra Talhada"}
    while True:
        for key, value in cidades_tlv.items():
            if a['UF_CRM_5E814A250C7FB'] == key:
                cidade_tlv = value
                break
            else:
                cidade_tlv = ''
        break

    global forma_pag
    formas = {"900": "Link de Pagamento", "902": "Na loja"}
    while True:
        for key, value in formas.items():
            if a['UF_CRM_5EC53E5E99FFC'] == key:
                forma_pag = value
                break
            else:
                forma_pag = ''
        break

    global motivo_int
    motivos_int = {"986": "Informações de lojas", "988": "Pós venda", "990": "Conferir estoque da loja",
                   "992": "Negociação de venda", "994": "Orçamento"}
    while True:
        for key, value in motivos_int.items():
            if a['UF_CRM_5ECE44E3E51A4'] == key:
                motivo_int = value
                break
            else:
                motivo_int = ''
        break

    global motivo_nv
    motivos_nv = {"996": "Comprou na concorrência", "998": "Não comercializamos", "1000": "Não respondeu",
                  "1002": "Comprou na loja", "1004": "Desistiu da compra",
                  "1008": "Atendimento a cliente", "1034": "Não temos estoque"}
    while True:
        for key, value in motivos_nv.items():
            if a['UF_CRM_5ECE44E453B0B'] == key:
                motivo_nv = value
                break
            else:
                motivo_nv = ''
        break

    global conf_entrega_card
    confs = {"1098": "SIM", "1100": "NAO"}
    while True:
        for key, value in confs.items():
            if a['UF_CRM_1597428965747'] == key:
                conf_entrega_card = value
                break
            else:
                conf_entrega_card = ''
        break

    global atraso
    atrasos = {"1124": "Sim", "1126": "Não"}
    while True:
        for key, value in atrasos.items():
            if a['UF_CRM_1597762728735'] == key:
                atraso = value
                break
            else:
                atraso = ''
        break

    global estado
    estados = {'1248': 'AC', '1250': 'AL', '1252': 'AM', '1254': 'BA', '1256': 'CE', '1258': 'DF', '1260': 'ES',
               '1262': 'GO', '1264': 'MA', '1266': 'MT', '1268': 'MS', '1270': 'MG', '1272': 'PA', '1274': 'PB',
               '1276': 'PR', '1278': 'PE', '1280': 'PI', '1282': 'RJ', '1284': 'RN', '1286': 'RS',
               '1288': 'RO', '1290': 'RR', '1292': 'SC', '1294': 'SP', '1296': 'SE', '1298': 'TO'}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_5F497054E2F3D'] == key:
                estado = value
                break
            else:
                estado = ''
        break

    global ticket_atrasado
    tickets = {"1404": "Sim", "1406": "Não"}
    while True:
        for key, value in tickets.items():
            if a['UF_CRM_1600088578763'] == key:
                ticket_atrasado = value
                break
            else:
                ticket_atrasado = ''
        break

    global ocorrencia_distac
    ocorrencias_d = {"1578": "2ª via de boleto", "1580": "2ª via de NF (SaÍda)", "1582": "2ª via nota (entrada)\"",
                     "1584": "Sol. De prorrogação de boleto por atraso na entrega", "1586": "Extrato de débito",
                     "1588": "Previsão de entrega", "1590": "Atraso na entrega",
                     "1592": "Ressarcimento De credito de Devolução",
                     "1594": "Solicitação de arquivo XML", "1596": "Sol. Visita RCA",
                     "1598": "Cadastro de cliente Distac",
                     "1600": "Consultar pedido", "1602": "Cadastro / navegação do E-Commerce",
                     "1604": "Problemas na plataforma do E-Commerce",
                     "1606": "Modelo de NF de devolução", "1608": "Atendimento Motorista - Elogio",
                     "1652": "Atendimento Motorista - Reclamação", "1610": "Atendimento SAC - Elogio",
                     "1650": "Atendimento SAC - Reclamação", "1612": "Atendimento RCA - Elogio",
                     "1654": "Atendimento RCA - Reclamação"}
    while True:
        for key, value in ocorrencias_d.items():
            if a['UF_CRM_1603812306'] == key:
                ocorrencia_distac = value
                break
            else:
                ocorrencia_distac = ''
        break

    global distac_filial
    filiais = {"1656": "Alagoas", "1658": "Serra Talhada", "1660": "Timon", "1662": "Ceará", "1664": "Recife"}
    while True:
        for key, value in filiais.items():
            if a['UF_CRM_1603910365'] == key:
                distac_filial = value
                break
            else:
                distac_filial = ''
        break

    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']) > 0:
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ""

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    company = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.company.get?ID={a['COMPANY_ID']}")
    try:
        empresa = company['result']['TITLE']
    except:
        empresa = ''

    contatos = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.contact.get?ID={a['CONTACT_ID']}")
    try:
        contato = f"{contatos['result']['NAME']} {contatos['result']['LAST_NAME']}"
    except:
        contato = ''
    return ("INSERT INTO DEAL (ID, Pipeline, Negócio_repetido, Fase,"
            "Responsável, Nome_do_negócio, Tipo, Fonte, Empresa, Contato, Fechado,"
            "Criado, Criado_por, Modificado, Modificado_por, Data_de_início, Data_de_fechamento,"
            "Classificação, OCORRÊNCIA_SAC, Motivo_da_Conclusão, Loja_Ocorrência,"
            "Televendas_Ativo, Televendas_Receptivo, Ocorrências_SAC, OCORRÊNCIA_DE_ENTREGA,"
            "Data_Atual, Prazo_Final, Vendedor_de_Loja, Motorista,"
            "Placa_do_Veículo, Rota, Depto_de_Abertura, Depto_de_Tratamento, Código_Winthor,"
            "Confimado, Instagram, Data_de_Conclusão, Ocorrências_Mídias_Sociais,"
            "Rede_Social, Classificação_da_ocorrência, Data_da_Entrega, Cidade_do_Cliente,"
            "CIDADE_TELEVENDAS, Data_de_Conversão, Forma_de_Pagamento, Número_do_pedido_Winthor,"
            "MOTIVO_DAS_INTERAÇÕES, MOTIVO_NÃO_VENDA, CÓDIGO_DO_PRODUTO, OBSERVAÇÃO_NÃO_VENDA,"
            "Cobrança_Data_de_Emissão, Cobrança_Data_de_Vencimento, Cobrança_Título, Cobrança_Valor,"
            "Cobrança_Nota_Fiscal,Cobrança_Nosso_número,CONF_DE_ENTREGA_CARD_NA_LOGÍSTICA,Card_Na_Logística_conf_de_entrega,"
            "Concluído_com_atraso, Estado_UF,Ticket_Atrasado,OCORRÊNCIA_DISTAC,DISTAC_FILIAL,Abertura_Tratamento,"
            "Classificação_SLA_Nome, Redes_Sociais)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
            .format(a['ID'], pipeline, a['IS_RETURN_CUSTOMER'], fase,
                    responsavel, a['TITLE'], tipo, fonte, empresa, contato, a['CLOSED'],
                    a['DATE_CREATE'], criador, a['DATE_MODIFY'], modificador, a['BEGINDATE'], a['CLOSEDATE'],
                    classificacao, ocorrencia_sac, a['UF_CRM_1571419048387'], loja,
                    televendas_a, televendas_r, ocorrencias_sac, ocorrencia_e,
                    a['UF_CRM_1572011497'], a['UF_CRM_1572011511'], a['UF_CRM_1572178570710'],
                    a['UF_CRM_1572178642890'],
                    a['UF_CRM_1572178677879'], a['UF_CRM_1572178700297'], a['UF_CRM_1572626106833'],
                    a['UF_CRM_1572626118761'], a['UF_CRM_1574777642618'],
                    a['UF_CRM_1575040109633'], a['UF_CRM_5DE944CD9BDB5'], a['UF_CRM_1576071656406'], ocorrencia_ms,
                    rede_social, classificacao_o, a['UF_CRM_1581104112'], a['UF_CRM_1585343891815'],
                    cidade_tlv, a['UF_CRM_5EBEAF2E30554'], forma_pag, a['UF_CRM_5EC5A242017C1'],
                    motivo_int, motivo_nv, a['UF_CRM_5F08D998E3B9E'], a['UF_CRM_5F08D999674A7'],
                    a['UF_CRM_1596064001'], a['UF_CRM_1596064018'], a['UF_CRM_1596064032'], a['UF_CRM_1596064046'],
                    a['UF_CRM_1596064059'], a['UF_CRM_1596064076'], conf_entrega_card, a['UF_CRM_1597429005013'],
                    atraso, estado, ticket_atrasado, ocorrencia_distac, distac_filial, a['UF_CRM_1572626118761'],
                    classificacao, rede_social))


def atualizar_deals(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM ajustes where tipo like'DEAL_STAG%'")
    ajustes_fontes = cursor.fetchall()
    fase = ''
    for f in ajustes_fontes:
        if a['STAGE_ID'] == f[1]:
            fase = f[2]

    cursor.execute("SELECT * FROM pipeline")
    pipelines = cursor.fetchall()
    pipeline = ''
    for p in pipelines:
        if a['CATEGORY_ID'] == p[0]:
            pipeline = p[1]

    cursor.execute("SELECT * FROM ajustes WHERE tipo='SOURCE'")
    ajustes_fontes = cursor.fetchall()
    fonte = ''
    for f in ajustes_fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    cursor.execute("SELECT * FROM ajustes where tipo = 'DEAL_TYPE'")
    ajustes_tipos = cursor.fetchall()
    tipo = ''
    for t in ajustes_tipos:
        if a['TYPE_ID'] == t[1]:
            tipo = t[2]
    if a['TYPE_ID'] == 'GOODS':
        tipo = 'GOODS'

    global classificacao
    c = {"520": "BO Entrega", "48": "Elogio", "538": "Midias Sociais", "434": "Ocorrência de Entrega",
         "44": "Reclamação", "46": "Solicitação", "50": "Sugestão", "546": "Ocorrência de Corte"}
    while True:
        for key, value in c.items():
            if a['UF_CRM_1571064926633'] == key:
                classificacao = value
                break
            else:
                classificacao = ''
        break

    global ocorrencia_sac
    ocorrencias = {"54": "2ª Via de Nota fiscal", "56": "2ª Via de Boleto", "58": "Assistência de Marca Exclusiva",
                   "1522": "Atendimento Loja - Elogio", "52": "Atendimento loja - Sugestão",
                   "218": "Atendimento loja - Reclamação",
                   "528": "Atendimento do motorista / Entregador - elogio",
                   "530": "Atendimento do motorista / Entregador - reclamação",
                   "554": "Atraso na entrega", "560": "Atendimento Loja", "816": "Atendimento SAC - Elogio",
                   "818": "Atendimento SAC - Reclamação", "1464": "Canhoto de Entrega",
                   "74": "Cliente discorda da Norma de Entrega",
                   "436": "Cliente Insatisfeito com a compra", "80": "Cliente só recebe outro dia - Retirar de carga",
                   "544": "Consulta de pedido", "82": "Corte de produto", "92": "entrega futura/ saber previsão",
                   "444": "Erro de procedimento no pedido", "450": "Erro Separação_Logística",
                   "446": "Falta de produto loja - separação de pedido", "96": "Falta de produto na loja",
                   "568": "Fornecedor, parceria e patrocínio ", "452": "Observação no pedido",
                   "536": "Midias Sociais", "104": "Ordem coleta / Desacordo (Erro logistica)",
                   "106": "Ordem coleta / Desacordo (Erro loja)", "662": "Previsão de Entrega",
                   "534": "Refazer pedido", "532": "Raio de entrega / Frete",
                   "804": "Resgate do termo de entrega assinado",
                   "1466": "Sem registro de BO", "120": "Solicitação de visita Técnica do Fornecedor",
                   "122": "Troca de produto", "1134": "E-commerce – Problema Site", "1136": "E-commerce – Troca",
                   "1138": "E-commerce – corte de produto", "1140": "E-commerce – Duvida de navegação",
                   "1142": "E-commerce – Falta de produto na Separação"}
    while True:
        for key, value in ocorrencias.items():
            if a['UF_CRM_1571065370'] == key:
                ocorrencia_sac = value
                break
            else:
                ocorrencia_sac = ''
        break

    global loja
    lojas = {"210": "Afogados", "212": "Imbiribeira", "214": "Olinda", "684": "CD Afogados", "822": "Caruaru 43",
             "824": "Caruaru 45", "826": "Logística Caruaru", "828": "Maceió 53", "830": "CD Maceió",
             "1060": "Serra Talhada 24", "1062": "Serra Talhada 27", "1064": "Serra Talhada 30"}
    while True:
        for key, value in lojas.items():
            if a['UF_CRM_1571660434'] == key:
                loja = value
                break
            else:
                loja = ''
        break

    global televendas_a
    televendas_as = {"226": "Recusou proposta", "228": "Telefone não atende", "230": "Número inválido",
                     "232": "Responsável ausente", "234": "Solicitado Documentação"}
    while True:
        for key, value in televendas_as.items():
            if a['UF_CRM_1571663098'] == key:
                televendas_a = value
                break
            else:
                televendas_a = ''
        break

    global televendas_r
    televendas_rs = {"236": "Orçamento", "238": "Cotação de Preço", "240": "Confirmação de produto",
                     "242": "Confirmação de estoque"}
    while True:
        for key, value in televendas_rs.items():
            if a['UF_CRM_1571753030'] == key:
                televendas_r = value
                break
            else:
                televendas_r = ''
        break

    global ocorrencias_sac
    ocorrencias_sacs = {
        "268": "Atendimento loja - Sugestão", "270": "Atendimento loja - Elogio",
        "272": "Atendimento loja - reclamação", "274": "2ª Via de Boleto",
        "276": "2ª Via de Nota fiscal", "278": "Assistência de Marca Exclusiva",
        "280": "Atendimento do Motorista / Entregador", "282": "Atraso na Entrega",
        "284": "Cliente Desistiu da compra", "286": "Cliente discorda da Norma de Entrega",
        "288": "Cliente já recebeu mercadoria (erro logistica)", "290": "Cliente já recebeu mercadoria (erro loja)",
        "292": "Cliente só recebe outro dia", "294": "Corte de produto", "296": "entrega futura/ saber previsão",
        "298": "Fale Consosco - Elogio", "300": "Fale Consosco - Solicitação", "302": "Fale Consosco - Reclamação",
        "304": "Falta de produto na loja", "306": "Ordem coleta / Desacordo (Erro logistica)",
        "308": "Ordem coleta / Desacordo (Erro loja)",
        "310": "Previsão de entrega", "312": "Produto Avariado", "314": "Relatório de boletos atrasados",
        "316": "Solicitação de visita Técnica do Fornecedor", "318": "Troca de produto"}
    while True:
        for key, value in ocorrencias_sacs.items():
            if a['UF_CRM_1571753030'] == key:
                ocorrencias_sac = value
                break
            else:
                ocorrencias_sac = ''
        break

    global ocorrencia_e
    ocorrencias_e = {
        "320": "BO Avaria", "322": "BO desacordo", "324": "BO falta Produto", "326": "Carro pequeno",
        "458": "Cliente Desistiu da compra", "328": "Cliente não quer  receber entrega",
        "460": "Cliente recebeu mercadoria duplicada (Pessoa física)", "330": "Desacordo com o Pedido",
        "462": "Cliente recebeu mercadoria duplicada (Pessoa jurídica)",
        "808": "Cliente só recebe outro dia - Retirar de carga",
        "332": "Dificil acesso", "334": "Endereço ñ localizado", "336": "Entrega de BO",
        "540": "Erro de Separação", "806": "Falta de produto loja - separação de pedido",
        "338": "Falta de produto no veículo", "340": "Fora de Rota", "342": "Não deu tempo",
        "464": "Ocorrências de Entrega", "524": "Produto Avariado", "468": "Refazer Pedido",
        "470": "Retorno de BO", "344": "Residência fechada", "542": "Saiu de carga",
        "346": "Retorno de entrega", "348": "Veiculo quebrado"}
    while True:
        for key, value in ocorrencias_e.items():
            if a['UF_CRM_1571753310'] == key:
                ocorrencia_e = value
                break
            else:
                ocorrencia_e = ''
        break

    global ocorrencia_ms
    ocorrencias_ms = {"575": "2ª via nota fiscal ", "577": "Atendimento Vendedores - Reclamação",
                      "579": "Atendimento Frete de loja",
                      "581": "Atendimento SAC", "583": "Atendimento Expedição", "585": "Atendimento Vendedor - Elogio",
                      "587": "Atraso na entrega", "589": "Atendimento Loja", "591": "Campanha promocional - Reclamação",
                      "593": "Campanha promocional - Solicitação", "820": "Consulta de Entrega",
                      "1118": "Elogio Motorista",
                      "595": "Especificação de produto", "1114": "Feedback",
                      "597": "Fornecedor, parceria e patrocínio ",
                      "599": "horário de atendimento", "607": "Insatisfação com a compra",
                      "810": "Interação do cliente",
                      "1120": "Mensões", "601": "Preço e pagamento de produto", "603": "Previsão de entrega",
                      "812": "Raio de Entrega / Frete", "1116": "Reclamação Motorista", "814": "Sugestão",
                      "605": "Trabalhe conosco ", "1122": "Trocas", "1132": "Entrega Posterior"}
    while True:
        for key, value in ocorrencias_ms.items():
            if a['UF_CRM_1579203250'] == key:
                ocorrencia_ms = value
                break
            else:
                ocorrencia_ms = ''
        break

    global rede_social
    redes = {"642": "Facebook - Messenger", "644": "Facebook - Comentário", "646": "Instagram - Comentário",
             "648": "Instagram - Direct", "650": "WhatsApp"}
    while True:
        for key, value in redes.items():
            if a['UF_CRM_1579266030'] == key:
                rede_social = value
                break
            else:
                rede_social = ''
        break

    global classificacao_o
    classicacoes_o = {"664": "Orçamento", "666": "Preço", "668": "Estoque em lojas",
                      "670": "Especificação de produto", "672": "Informações de outra área"}
    while True:
        for key, value in classicacoes_o.items():
            if a['UF_CRM_1580234661'] == key:
                classificacao_o = value
                break
            else:
                classificacao_o = ''
        break

    global cidade_tlv
    cidades_tlv = {"840": "Caruaru", "842": "Maceió", "844": "Recife", "846": "Serra Talhada"}
    while True:
        for key, value in cidades_tlv.items():
            if a['UF_CRM_5E814A250C7FB'] == key:
                cidade_tlv = value
                break
            else:
                cidade_tlv = ''
        break

    global forma_pag
    formas = {"900": "Link de Pagamento", "902": "Na loja"}
    while True:
        for key, value in formas.items():
            if a['UF_CRM_5EC53E5E99FFC'] == key:
                forma_pag = value
                break
            else:
                forma_pag = ''
        break

    global motivo_int
    motivos_int = {"986": "Informações de lojas", "988": "Pós venda", "990": "Conferir estoque da loja",
                   "992": "Negociação de venda", "994": "Orçamento"}
    while True:
        for key, value in motivos_int.items():
            if a['UF_CRM_5ECE44E3E51A4'] == key:
                motivo_int = value
                break
            else:
                motivo_int = ''
        break

    global motivo_nv
    motivos_nv = {"996": "Comprou na concorrência", "998": "Não comercializamos", "1000": "Não respondeu",
                  "1002": "Comprou na loja", "1004": "Desistiu da compra",
                  "1008": "Atendimento a cliente", "1034": "Não temos estoque"}
    while True:
        for key, value in motivos_nv.items():
            if a['UF_CRM_5ECE44E453B0B'] == key:
                motivo_nv = value
                break
            else:
                motivo_nv = ''
        break

    global conf_entrega_card
    confs = {"1098": "SIM", "1100": "NAO"}
    while True:
        for key, value in confs.items():
            if a['UF_CRM_1597428965747'] == key:
                conf_entrega_card = value
                break
            else:
                conf_entrega_card = ''
        break

    global atraso
    atrasos = {"1124": "Sim", "1126": "Não"}
    while True:
        for key, value in atrasos.items():
            if a['UF_CRM_1597762728735'] == key:
                atraso = value
                break
            else:
                atraso = ''
        break

    global estado
    estados = {'1248': 'AC', '1250': 'AL', '1252': 'AM', '1254': 'BA', '1256': 'CE', '1258': 'DF', '1260': 'ES',
               '1262': 'GO', '1264': 'MA', '1266': 'MT', '1268': 'MS', '1270': 'MG', '1272': 'PA', '1274': 'PB',
               '1276': 'PR', '1278': 'PE', '1280': 'PI', '1282': 'RJ', '1284': 'RN', '1286': 'RS',
               '1288': 'RO', '1290': 'RR', '1292': 'SC', '1294': 'SP', '1296': 'SE', '1298': 'TO'}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_5F497054E2F3D'] == key:
                estado = value
                break
            else:
                estado = ''
        break

    global ticket_atrasado
    tickets = {"1404": "Sim", "1406": "Não"}
    while True:
        for key, value in tickets.items():
            if a['UF_CRM_1600088578763'] == key:
                ticket_atrasado = value
                break
            else:
                ticket_atrasado = ''
        break

    global ocorrencia_distac
    ocorrencias_d = {"1578": "2ª via de boleto", "1580": "2ª via de NF (SaÍda)", "1582": "2ª via nota (entrada)\"",
                     "1584": "Sol. De prorrogação de boleto por atraso na entrega", "1586": "Extrato de débito",
                     "1588": "Previsão de entrega", "1590": "Atraso na entrega",
                     "1592": "Ressarcimento De credito de Devolução",
                     "1594": "Solicitação de arquivo XML", "1596": "Sol. Visita RCA",
                     "1598": "Cadastro de cliente Distac",
                     "1600": "Consultar pedido", "1602": "Cadastro / navegação do E-Commerce",
                     "1604": "Problemas na plataforma do E-Commerce",
                     "1606": "Modelo de NF de devolução", "1608": "Atendimento Motorista - Elogio",
                     "1652": "Atendimento Motorista - Reclamação", "1610": "Atendimento SAC - Elogio",
                     "1650": "Atendimento SAC - Reclamação", "1612": "Atendimento RCA - Elogio",
                     "1654": "Atendimento RCA - Reclamação"}
    while True:
        for key, value in ocorrencias_d.items():
            if a['UF_CRM_1603812306'] == key:
                ocorrencia_distac = value
                break
            else:
                ocorrencia_distac = ''
        break

    global distac_filial
    filiais = {"1656": "Alagoas", "1658": "Serra Talhada", "1660": "Timon", "1662": "Ceará", "1664": "Recife"}
    while True:
        for key, value in filiais.items():
            if a['UF_CRM_1603910365'] == key:
                distac_filial = value
                break
            else:
                distac_filial = ''
        break

    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']) > 0:
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ""

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    company = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.company.get?ID={a['COMPANY_ID']}")
    try:
        empresa = company['result']['TITLE']
    except:
        empresa = ''

    contatos = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/crm.contact.get?ID={a['CONTACT_ID']}")
    try:
        contato = f"{contatos['result']['NAME']} {contatos['result']['LAST_NAME']}"
    except:
        contato = ''
    return (
        "UPDATE DEAL SET Pipeline='{}', Negócio_repetido='{}', Fase='{}',"
        "Responsável='{}', Nome_do_negócio='{}', Tipo='{}', Fonte='{}', Empresa='{}', Contato='{}', Fechado='{}',"
        "Criado='{}', Criado_por='{}', Modificado='{}', Modificado_por='{}', Data_de_início='{}', Data_de_fechamento='{}',"
        "Classificação='{}', OCORRÊNCIA_SAC='{}', Motivo_da_Conclusão='{}', Loja_Ocorrência='{}',"
        "Televendas_Ativo='{}', Televendas_Receptivo='{}', Ocorrências_SAC='{}', OCORRÊNCIA_DE_ENTREGA='{}',"
        "Data_Atual='{}', Prazo_Final='{}', Vendedor_de_Loja='{}', Motorista='{}',"
        "Placa_do_Veículo='{}', Rota='{}', Depto_de_Abertura='{}', Depto_de_Tratamento='{}', Código_Winthor='{}',"
        "Confimado='{}', Instagram='{}', Data_de_Conclusão='{}', Ocorrências_Mídias_Sociais='{}',"
        "Rede_Social='{}', Classificação_da_ocorrência='{}', Data_da_Entrega='{}', Cidade_do_Cliente='{}',"
        "CIDADE_TELEVENDAS='{}', Data_de_Conversão='{}', Forma_de_Pagamento='{}', Número_do_pedido_Winthor='{}',"
        "MOTIVO_DAS_INTERAÇÕES='{}', MOTIVO_NÃO_VENDA='{}', CÓDIGO_DO_PRODUTO='{}', OBSERVAÇÃO_NÃO_VENDA='{}',"
        "Cobrança_Data_de_Emissão='{}', Cobrança_Data_de_Vencimento='{}', Cobrança_Título='{}', Cobrança_Valor='{}',"
        "Cobrança_Nota_Fiscal='{}',Cobrança_Nosso_número='{}',CONF_DE_ENTREGA_CARD_NA_LOGÍSTICA='{}',Card_Na_Logística_conf_de_entrega='{}',"
        "Concluído_com_atraso='{}', Estado_UF='{}',Ticket_Atrasado='{}',OCORRÊNCIA_DISTAC='{}',DISTAC_FILIAL='{}',Abertura_Tratamento='{}',"
        "Classificação_SLA_Nome='{}',Redes_Sociais='{}'"
        " WHERE ID='{}'"
            .format(pipeline, a['IS_RETURN_CUSTOMER'], fase,
                    responsavel, a['TITLE'], tipo, fonte, empresa, contato, a['CLOSED'],
                    a['DATE_CREATE'], criador, a['DATE_MODIFY'], modificador, a['BEGINDATE'], a['CLOSEDATE'],
                    classificacao, ocorrencia_sac, a['UF_CRM_1571419048387'], loja,
                    televendas_a, televendas_r, ocorrencias_sac, ocorrencia_e,
                    a['UF_CRM_1572011497'], a['UF_CRM_1572011511'], a['UF_CRM_1572178570710'],
                    a['UF_CRM_1572178642890'],
                    a['UF_CRM_1572178677879'], a['UF_CRM_1572178700297'], a['UF_CRM_1572626106833'],
                    a['UF_CRM_1572626118761'], a['UF_CRM_1574777642618'],
                    a['UF_CRM_1575040109633'], a['UF_CRM_5DE944CD9BDB5'], a['UF_CRM_1576071656406'], ocorrencia_ms,
                    rede_social, classificacao_o, a['UF_CRM_1581104112'], a['UF_CRM_1585343891815'],
                    cidade_tlv, a['UF_CRM_5EBEAF2E30554'], forma_pag, a['UF_CRM_5EC5A242017C1'],
                    motivo_int, motivo_nv, a['UF_CRM_5F08D998E3B9E'], a['UF_CRM_5F08D999674A7'],
                    a['UF_CRM_1596064001'], a['UF_CRM_1596064018'], a['UF_CRM_1596064032'], a['UF_CRM_1596064046'],
                    a['UF_CRM_1596064059'], a['UF_CRM_1596064076'], conf_entrega_card, a['UF_CRM_1597429005013'],
                    atraso, estado, ticket_atrasado, ocorrencia_distac, distac_filial, a['UF_CRM_1572626118761'],
                    classificacao, rede_social,
                    a['ID'])
    )


def inserir_contato(a):
    print(f"A ID:{a['ID']} foi INSERIDA.")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()

    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''
    if a['SECOND_NAME'] == None:
        sobrenome = a['LAST_NAME']
    else:
        sobrenome = f'{a["SECOND_NAME"]} {a["LAST_NAME"]}'

    cursor.execute("SELECT * FROM ajustes where tipo = 'CONTACT_TYPE'")
    tipos_contato = cursor.fetchall()
    tipo_contato = ''
    for t in tipos_contato:
        if a['TYPE_ID'] == t[1]:
            tipo_contato = t[2]

    cursor.execute("SELECT * FROM ajustes where tipo = 'SOURCE'")
    fontes = cursor.fetchall()
    fonte = ''
    for f in fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    global cidade_tlv
    cidades_tlv = {"856": "Caruaru", "858": "Maceió", "860": "Recife", "862": "Serra Talhada"}
    while True:
        for key, value in cidades_tlv.items():
            if a['UF_CRM_5E814AF4A68D2'] == key:
                cidade_tlv = value
                break
            else:
                cidade_tlv = ''
        break

    global forma_p
    formas_p = {"894": "Link de Pagamento", "896": "Na loja"}
    while True:
        for key, value in formas_p.items():
            if a['UF_CRM_5EC53E5D4F128'] == key:
                forma_p = value
                break
            else:
                forma_p = ''
        break

    global motivo_int
    motivos_int = {"1036": "Informações de lojas", "1038": "Pós venda", "1040": "Conferir estoque da loja",
                   "1042": "Negociação de venda", "1044": "Orçamento"}
    while True:
        for key, value in motivos_int.items():
            if a['UF_CRM_5ED68EB48F5EF'] == key:
                motivo_int = value
                break
            else:
                motivo_int = ''
        break

    global motivo_nv
    motivos_nv = {"1046": "Comprou na concorrência", "1048": "Não comercializamos", "1050": "Não respondeu",
                  "1052": "Comprou na loja", "1054": "Desistiu da compra", "1056": "Atendimento a cliente",
                  "1058": "Não temos estoque"}
    while True:
        for key, value in motivos_nv.items():
            if a['UF_CRM_5ED68EB6DE8FF'] == key:
                motivo_nv = value
                break
            else:
                motivo_nv = ''
        break

    global estado
    estados = {"1196": "AC", "1198": "AL", "1200": "AM", "1202": "BA", "1204": "CE", "1206": "DF",
               "1208": "ES", "1210": "GO", "1212": "MA", "1214": "MT", "1216": "MS", "1218": "MG",
               "1220": "PA", "1222": "PB", "1224": "PR", "1226": "PE", "1228": "PI",
               "1230": "RJ", "1232": "RN", "1234": "RS", "1236": "RO", "1238": "RR", "1240": "SC",
               "1242": "SP", "1244": "SE", "1246": "TO"}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_5F497051EF70D'] == key:
                estado = value
                break
            else:
                estado = ''
        break

    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']):
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ''

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    return ("INSERT INTO CONTACT (ID, Nome,Sobrenome,Tipo_de_Contato,Responsável,Telefone_de_trabalho,"
            "Email_de_trabalho,Fonte,Exportar,Criado_por,Criado,Modificado_por,	Modificado,"
            "Código_Winthor,	CPF,Endereço_google,Data_Cadastro,Data_1a_Compra,Data_Ult_Compra,	Rua,"
            "Número,	Complemento,Bairro,	Cidade,	Estado,	CEP,CIDADE_TELEVENDAS,Data_de_Conversão,Forma_de_Pagamento,"
            "Número_do_pedido_Winthor,	MOTIVO_DAS_INTERAÇÕES,MOTIVO_NÃO_VENDA,	CÓDIGO_DO_PRODUTO,OBSERVAÇÃO_NÃO_VENDA,"
            "Estado_UF)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            " '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            " '{}', '{}')"
            .format(a['ID'], a['NAME'], sobrenome, tipo_contato, responsavel, telefone,
                    a['HAS_EMAIL'], fonte, a['EXPORT'], criador, a['DATE_CREATE'], modificador,
                    a['DATE_MODIFY'], a['UF_CRM_1571660034'], a['UF_CRM_1571691442204'], a['UF_CRM_1572279163418'],
                    a['UF_CRM_1572280054175'], a['UF_CRM_1572280080310'], a['UF_CRM_1572280097701'],
                    a['UF_CRM_1572284963545'],
                    a['UF_CRM_1572284981193'], a['UF_CRM_1572285018856'], a['UF_CRM_1572285028298'],
                    a['UF_CRM_1572285037562'],
                    a['UF_CRM_1572285047931'], a['UF_CRM_1572285192873'], cidade_tlv, a['UF_CRM_5EBEAF2E84C2C'],
                    forma_p, a['UF_CRM_5EC5A2424333E'], motivo_int, motivo_nv,
                    a['UF_CRM_5ED68EB6DE8FF'], a['UF_CRM_5F49704F94C18'], estado))


def atualizar_contato(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    conexao = conectar('Tupan', 'l1gu3scPT', 'Estmonial!Uhh663913Ty')
    cursor = conexao.cursor()
    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''

    sobrenome = f'{a["SECOND_NAME"]} {a["LAST_NAME"]}'

    cursor.execute("SELECT * FROM ajustes where tipo = 'CONTACT_TYPE'")
    tipos_contato = cursor.fetchall()
    tipo_contato = ''
    for t in tipos_contato:
        if a['TYPE_ID'] == t[1]:
            tipo_contato = t[2]

    cursor.execute("SELECT * FROM ajustes where tipo = 'SOURCE'")
    fontes = cursor.fetchall()
    fonte = ''
    for f in fontes:
        if a['SOURCE_ID'] == f[1]:
            fonte = f[2]

    global cidade_tlv
    cidades_tlv = {"856": "Caruaru", "858": "Maceió", "860": "Recife", "862": "Serra Talhada"}
    while True:
        for key, value in cidades_tlv.items():
            if a['UF_CRM_5E814AF4A68D2'] == key:
                cidade_tlv = value
                break
            else:
                cidade_tlv = ''
        break

    global forma_p
    formas_p = {"894": "Link de Pagamento", "896": "Na loja"}
    while True:
        for key, value in formas_p.items():
            if a['UF_CRM_5EC53E5D4F128'] == key:
                forma_p = value
                break
            else:
                forma_p = ''
        break

    global motivo_int
    motivos_int = {"1036": "Informações de lojas", "1038": "Pós venda", "1040": "Conferir estoque da loja",
                   "1042": "Negociação de venda", "1044": "Orçamento"}
    while True:
        for key, value in motivos_int.items():
            if a['UF_CRM_5ED68EB48F5EF'] == key:
                motivo_int = value
                break
            else:
                motivo_int = ''
        break

    global motivo_nv
    motivos_nv = {"1046": "Comprou na concorrência", "1048": "Não comercializamos", "1050": "Não respondeu",
                  "1052": "Comprou na loja", "1054": "Desistiu da compra", "1056": "Atendimento a cliente",
                  "1058": "Não temos estoque"}
    while True:
        for key, value in motivos_nv.items():
            if a['UF_CRM_5ED68EB6DE8FF'] == key:
                motivo_nv = value
                break
            else:
                motivo_nv = ''
        break

    global estado
    estados = {"1196": "AC", "1198": "AL", "1200": "AM", "1202": "BA", "1204": "CE", "1206": "DF",
               "1208": "ES", "1210": "GO", "1212": "MA", "1214": "MT", "1216": "MS", "1218": "MG",
               "1220": "PA", "1222": "PB", "1224": "PR", "1226": "PE", "1228": "PI",
               "1230": "RJ", "1232": "RN", "1234": "RS", "1236": "RO", "1238": "RR", "1240": "SC",
               "1242": "SP", "1244": "SE", "1246": "TO"}
    while True:
        for key, value in estados.items():
            if a['UF_CRM_5F497051EF70D'] == key:
                estado = value
                break
            else:
                estado = ''
        break
    r = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['ASSIGNED_BY_ID']}")
    if len(r['result']):
        responsavel = f"{r['result'][0]['NAME']} {r['result'][0]['LAST_NAME']}"
    else:
        responsavel = ''

    c = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['CREATED_BY_ID']}")
    if len(c['result']) > 0:
        criador = f"{c['result'][0]['NAME']} {c['result'][0]['LAST_NAME']}"
    else:
        criador = ""

    m = consumir_api(f"https://tupan.bitrix24.com/rest/1/xnyq2k0ybltcum07/user.search?ID={a['MODIFY_BY_ID']}")
    if len(m['result']) > 0:
        modificador = f"{m['result'][0]['NAME']} {m['result'][0]['LAST_NAME']}"
    else:
        modificador = ""

    return (
        "UPDATE CONTACT SET Nome='{}',Sobrenome='{}',Tipo_de_Contato='{}',Responsável='{}',Telefone_de_trabalho='{}',"
        "Email_de_trabalho='{}',Fonte='{}',Exportar='{}',Criado_por='{}',Criado='{}',Modificado_por='{}',Modificado='{}',"
        "Código_Winthor='{}',CPF='{}',Endereço_google='{}',Data_Cadastro='{}',Data_1a_Compra='{}',Data_Ult_Compra='{}',	Rua='{}',"
        "Número='{}',Complemento='{}',Bairro='{}',Cidade='{}',Estado='{}',CEP='{}',CIDADE_TELEVENDAS='{}',Data_de_Conversão='{}',Forma_de_Pagamento='{}',"
        "Número_do_pedido_Winthor='{}',MOTIVO_DAS_INTERAÇÕES='{}',MOTIVO_NÃO_VENDA='{}',CÓDIGO_DO_PRODUTO='{}',OBSERVAÇÃO_NÃO_VENDA='{}',"
        "Estado_UF='{}'"
        " WHERE ID='{}'"
        .format(a['NAME'], sobrenome, tipo_contato, responsavel, telefone,
                a['HAS_EMAIL'], fonte, a['EXPORT'], criador, a['DATE_CREATE'], modificador,
                a['DATE_MODIFY'], a['UF_CRM_1571660034'], a['UF_CRM_1571691442204'], a['UF_CRM_1572279163418'],
                a['UF_CRM_1572280054175'], a['UF_CRM_1572280080310'], a['UF_CRM_1572280097701'],
                a['UF_CRM_1572284963545'],
                a['UF_CRM_1572284981193'], a['UF_CRM_1572285018856'], a['UF_CRM_1572285028298'],
                a['UF_CRM_1572285037562'],
                a['UF_CRM_1572285047931'], a['UF_CRM_1572285192873'], cidade_tlv, a['UF_CRM_5EBEAF2E84C2C'],
                forma_p, a['UF_CRM_5EC5A2424333E'], motivo_int, motivo_nv,
                a['UF_CRM_5ED68EB6DE8FF'], a['UF_CRM_5F49704F94C18'], estado, a['ID']))


def deletar(tipo):
    return(f"DELETE FROM {tipo}")
