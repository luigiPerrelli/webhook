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
    return ("INSERT INTO LEAD (ID, Status, Nome_do_Lead, Primeiro_nome, Segundo_nome, Sobrenome, Criado,"
            "Fonte ,Telefone_de_trabalho, Responsável, Informações_de_status,"
            "Informações_da_fonte, Criado_por, Modificado, Modificado_Por, Nome_da_empresa,"
            "Lead_repetido, CIDADE_TELEVENDAS, Data_de_Conversão, Forma_de_Pagamento, Número_do_pedido_Winthor,"
            "MOTIVO_DAS_INTERAÇÕES, MOTIVO_NÃO_VENDA, CÓDIGO_DO_PRODUTO, OBSERVAÇÃO_NÃO_VENDA, Estado_UF)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "        '{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}', '{}')"
            .format(a['ID'], a['STATUS_ID'], a['TITLE'], a['NAME'],a['SECOND_NAME'], a['LAST_NAME'],a['DATE_CREATE'],
                    a['SOURCE_ID'], telefone,a['ASSIGNED_BY_ID'],a['STATUS_DESCRIPTION'],
                    a['SOURCE_DESCRIPTION'], a['CREATED_BY_ID'], a['DATE_MODIFY'],a['MODIFY_BY_ID'], a['COMPANY_ID'],
                    a['IS_RETURN_CUSTOMER'], a['UF_CRM_1585530790'], a['UF_CRM_1589554873'], a['UF_CRM_1589984561981'], a['UF_CRM_1590010371392'],
                    a['UF_CRM_1590574186777'], a['UF_CRM_1590574245657'], CODIGO_PRODUTO, a['UF_CRM_1594415383097'], a['UF_CRM_1598647901']))


def atualizar_leads(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
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
    return ("UPDATE LEAD SET Status='{}', Nome_do_lead='{}', Primeiro_nome='{}', Segundo_nome='{}', Sobrenome='{}', Criado='{}',"
            "Fonte='{}',Telefone_de_trabalho='{}', Responsável='{}', Informações_de_status='{}',"
            "Informações_da_fonte='{}', Criado_por='{}', Modificado='{}', Modificado_Por='{}', Nome_da_empresa='{}',"
            "Lead_repetido='{}', CIDADE_TELEVENDAS='{}', Data_de_Conversão='{}', Forma_de_Pagamento='{}', Número_do_pedido_Winthor='{}',"
            "MOTIVO_DAS_INTERAÇÕES='{}', MOTIVO_NÃO_VENDA='{}', CÓDIGO_DO_PRODUTO='{}', OBSERVAÇÃO_NÃO_VENDA='{}', Estado_UF='{}'"
            "WHERE ID ='{}'"
            .format(a['ID'], a['STATUS_ID'], a['TITLE'], a['NAME'],a['SECOND_NAME'], a['LAST_NAME'],a['DATE_CREATE'],
                    a['SOURCE_ID'], telefone, a['ASSIGNED_BY_ID'],a['STATUS_DESCRIPTION'],
                    a['SOURCE_DESCRIPTION'], a['CREATED_BY_ID'], a['DATE_MODIFY'],a['MODIFY_BY_ID'], a['COMPANY_ID'],
                    a['IS_RETURN_CUSTOMER'], a['UF_CRM_1585530790'], a['UF_CRM_1589554873'], a['UF_CRM_1589984561981'], a['UF_CRM_1590010371392'],
                    a['UF_CRM_1590574186777'], a['UF_CRM_1590574245657'], CODIGO_PRODUTO, a['UF_CRM_1594415383097'], a['UF_CRM_1598647901'],
                    a['ID']))



def inserir_deals(a):
    print(f"A ID:{a['ID']} foi INSERIDA.")
    return("INSERT INTO DEAL (ID, Pipeline, Negócio_repetido, Fase,"
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
           "Cobrança_Nota_Fiscal,	Cobrança_Nosso_número,CONF_DE_ENTREGA_CARD_NA_LOGÍSTICA,Card_Na_Logística_conf_de_entrega,"
           "Concluído_com_atraso, Estado_UF,Ticket_Atrasado,OCORRÊNCIA_DISTAC,DISTAC_FILIAL,Abertura_Tratamento,"
           "Classificação_SLA_Nome, Redes_Sociais)"
           "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
           .format(a['ID'],a['CATEGORY_ID'],a['IS_RETURN_CUSTOMER'],a['STAGE_ID'],
                   a['ASSIGNED_BY_ID'], a['TITLE'], a['TYPE_ID'], a['SOURCE_ID'], a['COMPANY_ID'], a['CONTACT_ID'], a['CLOSED'],
                   a['DATE_CREATE'], a['CREATED_BY_ID'], a['DATE_MODIFY'], a['MODIFY_BY_ID'], a['BEGINDATE'], a['CLOSEDATE'],
                   a['UF_CRM_1571064926633'], a['UF_CRM_1571065370'], a['UF_CRM_1571419048387'], a['UF_CRM_1571660434'],
                   a['UF_CRM_1571663098'], a['UF_CRM_1571663163'], a['UF_CRM_1571663163'], a['UF_CRM_1571753310'],
                   a['UF_CRM_1572011497'], a['UF_CRM_1572011511'], a['UF_CRM_1572178570710'], a['UF_CRM_1572178642890'],
                   a['UF_CRM_1572178677879'], a['UF_CRM_1572178700297'], a['UF_CRM_1572626106833'], a['UF_CRM_1572626118761'], a['UF_CRM_1574777642618'],
                   a['UF_CRM_1575040109633'], a['UF_CRM_5DE944CD9BDB5'], a['UF_CRM_1576071656406'], a['UF_CRM_1579203250'],
                   a['UF_CRM_1579266030'], a['UF_CRM_1580234661'], a['UF_CRM_1581104112'], a['UF_CRM_1585343891815'],
                   a['UF_CRM_5E814A250C7FB'], a['UF_CRM_5EBEAF2E30554'], a['UF_CRM_5EC53E5E99FFC'], a['UF_CRM_5EC5A242017C1'],
                   a['UF_CRM_5ECE44E3E51A4'], a['UF_CRM_5ECE44E453B0B'], a['UF_CRM_5F08D998E3B9E'], a['UF_CRM_5F08D999674A7'],
                   a['UF_CRM_1596064001'], a['UF_CRM_1596064018'], a['UF_CRM_1596064032'], a['UF_CRM_1596064046'],
                   a['UF_CRM_1596064059'], a['UF_CRM_1596064076'], a['UF_CRM_1597428965747'], a['UF_CRM_1597429005013'],
                   a['UF_CRM_1597762728735'], a['UF_CRM_5F497054E2F3D'], a['UF_CRM_1600088578763'], a['UF_CRM_1603812306'], a['UF_CRM_1603910365'], a['UF_CRM_1572626118761'],
                   a['UF_CRM_1571064926633'],a['UF_CRM_1579266030']))


def atualizar_deals(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    return(
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
        .format(a['CATEGORY_ID'],a['IS_RETURN_CUSTOMER'],a['STAGE_ID'],
                   a['ASSIGNED_BY_ID'], a['TITLE'], a['TYPE_ID'], a['SOURCE_ID'], a['COMPANY_ID'], a['CONTACT_ID'], a['CLOSED'],
                   a['DATE_CREATE'], a['CREATED_BY_ID'], a['DATE_MODIFY'], a['MODIFY_BY_ID'], a['BEGINDATE'], a['CLOSEDATE'],
                   a['UF_CRM_1571064926633'], a['UF_CRM_1571065370'], a['UF_CRM_1571419048387'], a['UF_CRM_1571660434'],
                   a['UF_CRM_1571663098'], a['UF_CRM_1571663163'], a['UF_CRM_1571663163'], a['UF_CRM_1571753310'],
                   a['UF_CRM_1572011497'], a['UF_CRM_1572011511'], a['UF_CRM_1572178570710'], a['UF_CRM_1572178642890'],
                   a['UF_CRM_1572178677879'], a['UF_CRM_1572178700297'], a['UF_CRM_1572626106833'], a['UF_CRM_1572626118761'], a['UF_CRM_1574777642618'],
                   a['UF_CRM_1575040109633'], a['UF_CRM_5DE944CD9BDB5'], a['UF_CRM_1576071656406'], a['UF_CRM_1579203250'],
                   a['UF_CRM_1579266030'], a['UF_CRM_1580234661'], a['UF_CRM_1581104112'], a['UF_CRM_1585343891815'],
                   a['UF_CRM_5E814A250C7FB'], a['UF_CRM_5EBEAF2E30554'], a['UF_CRM_5EC53E5E99FFC'], a['UF_CRM_5EC5A242017C1'],
                   a['UF_CRM_5ECE44E3E51A4'], a['UF_CRM_5ECE44E453B0B'], a['UF_CRM_5F08D998E3B9E'], a['UF_CRM_5F08D999674A7'],
                   a['UF_CRM_1596064001'], a['UF_CRM_1596064018'], a['UF_CRM_1596064032'], a['UF_CRM_1596064046'],
                   a['UF_CRM_1596064059'], a['UF_CRM_1596064076'], a['UF_CRM_1597428965747'], a['UF_CRM_1597429005013'],
                   a['UF_CRM_1597762728735'], a['UF_CRM_5F497054E2F3D'], a['UF_CRM_1600088578763'], a['UF_CRM_1603812306'], a['UF_CRM_1603910365'], a['UF_CRM_1572626118761'],
                   a['UF_CRM_1571064926633'],a['UF_CRM_1579266030'],
                   a['ID'])
        )


def inserir_contato(a):
    print(f"A ID:{a['ID']} foi INSERIDA.")
    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''
    if a['SECOND_NAME'] == None:
        sobrenome = a['LAST_NAME']
    else:
        sobrenome = f'{a["SECOND_NAME"]} {a["LAST_NAME"]}'
    return ("INSERT INTO CONTACT (ID, Nome,Sobrenome,Tipo_de_Contato,Responsável,Telefone_de_trabalho,"
            "Email_de_trabalho,Fonte,Exportar,Criado_por,Criado,Modificado_por,	Modificado,"
            "Código_Winthor,	CPF,Endereço_google,Data_Cadastro,Data_1a_Compra,Data_Ult_Compra,	Rua,"
            "Número,	Complemento,Bairro,	Cidade,	Estado,	CEP,CIDADE_TELEVENDAS,Data_de_Conversão,Forma_de_Pagamento,"
            "Número_do_pedido_Winthor,	MOTIVO_DAS_INTERAÇÕES,MOTIVO_NÃO_VENDA,	CÓDIGO_DO_PRODUTO,OBSERVAÇÃO_NÃO_VENDA,"
            "Estado_UF)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            " '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            " '{}', '{}')"
            .format(a['ID'], a['NAME'], sobrenome, a['TYPE_ID'], a['ASSIGNED_BY_ID'], telefone,
                    a['HAS_EMAIL'], a['SOURCE_ID'], a['EXPORT'], a['CREATED_BY_ID'], a['DATE_CREATE'],
                    a['MODIFY_BY_ID'],
                    a['DATE_MODIFY'], a['UF_CRM_1571660034'], a['UF_CRM_1571691442204'], a['UF_CRM_1572279163418'],
                    a['UF_CRM_1572280054175'], a['UF_CRM_1572280080310'], a['UF_CRM_1572280097701'],
                    a['UF_CRM_1572284963545'],
                    a['UF_CRM_1572284981193'], a['UF_CRM_1572285018856'], a['UF_CRM_1572285028298'],
                    a['UF_CRM_1572285037562'],
                    a['UF_CRM_1572285047931'], a['UF_CRM_1572285192873'], a['UF_CRM_5E814AF4A68D2'],
                    a['UF_CRM_5EBEAF2E84C2C'],
                    a['UF_CRM_5EC53E5D4F128'], a['UF_CRM_5EC5A2424333E'], a['UF_CRM_5ED68EB48F5EF'],
                    a['UF_CRM_5ED68EB6DE8FF'],
                    a['UF_CRM_5ED68EB6DE8FF'], a['UF_CRM_5F49704F94C18'], a['UF_CRM_5F497051EF70D']))


def atualizar_contato(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    if a['HAS_PHONE'] == 'Y':
        telefone = a['PHONE'][0]['VALUE']
    else:
        telefone = ''
    sobrenome = f'{a["SECOND_NAME"]} {a["LAST_NAME"]}'
    return("UPDATE CONTACT SET Nome='{}',Sobrenome='{}',Tipo_de_Contato='{}',Responsável='{}',Telefone_de_trabalho='{}',"
           "Email_de_trabalho='{}',Fonte='{}',Exportar='{}',Criado_por='{}',Criado='{}',Modificado_por='{}',Modificado='{}',"
           "Código_Winthor='{}',CPF='{}',Endereço_google='{}',Data_Cadastro='{}',Data_1a_Compra='{}',Data_Ult_Compra='{}',	Rua='{}',"
           "Número='{}',Complemento='{}',Bairro='{}',Cidade='{}',Estado='{}',CEP='{}',CIDADE_TELEVENDAS='{}',Data_de_Conversão='{}',Forma_de_Pagamento='{}',"
           "Número_do_pedido_Winthor='{}',MOTIVO_DAS_INTERAÇÕES='{}',MOTIVO_NÃO_VENDA='{}',CÓDIGO_DO_PRODUTO='{}',OBSERVAÇÃO_NÃO_VENDA='{}',"
           "Estado_UF='{}'"
           " WHERE ID='{}'"
           .format(a['NAME'], sobrenome, a['TYPE_ID'], a['ASSIGNED_BY_ID'], telefone,
                   a['HAS_EMAIL'], a['SOURCE_ID'], a['EXPORT'], a['CREATED_BY_ID'], a['DATE_CREATE'], a['MODIFY_BY_ID'],
                   a['DATE_MODIFY'],a['UF_CRM_1571660034'], a['UF_CRM_1571691442204'], a['UF_CRM_1572279163418'],
                   a['UF_CRM_1572280054175'], a['UF_CRM_1572280080310'], a['UF_CRM_1572280097701'], a['UF_CRM_1572284963545'],
                   a['UF_CRM_1572284981193'], a['UF_CRM_1572285018856'], a['UF_CRM_1572285028298'], a['UF_CRM_1572285037562'],
                   a['UF_CRM_1572285047931'], a['UF_CRM_1572285192873'], a['UF_CRM_5E814AF4A68D2'], a['UF_CRM_5EBEAF2E84C2C'],
                   a['UF_CRM_5EC53E5D4F128'],a['UF_CRM_5EC5A2424333E'], a['UF_CRM_5ED68EB48F5EF'], a['UF_CRM_5ED68EB6DE8FF'],
                   a['UF_CRM_5ED68EB6DE8FF'], a['UF_CRM_5F49704F94C18'],a['UF_CRM_5F497051EF70D'], a['ID']))


def deletar(tipo):
    return(f"DELETE FROM {tipo}")


def add(tipo, TITLE, TYPE_ID, CONTACT_ID, OPENED, CURRENCY_ID, OPPORTUNITY, ASSIGNED_BY_ID,STAGE_ID):
    consumir_api(
    f"https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.{tipo}.add?fields[TITLE]={TITLE}&fields[TYPE_ID]={TYPE_ID}&fields[CONTACT_ID]={CONTACT_ID}&fields[OPENED]={OPENED}&fields[CURRENCY_ID]={CURRENCY_ID}&fields[OPPORTUNITY]={OPPORTUNITY}&fields[ASSIGNED_BY_ID]={ASSIGNED_BY_ID}&fields[STAGE_ID]:={STAGE_ID}")
    print(f'O {tipo} {TITLE} foi adicionado')


def get(tipo):
    ID = str(input('Qual a sua ID? '))
    obj = consumir_api(f'https://staffmobi.bitrix24.com/rest/1/a69xicp1xnmi8ope/crm.{tipo}.get?ID={ID}')
    print(f"Olá, {obj['result']['TITLE']}!")
