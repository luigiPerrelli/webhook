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
    return ("INSERT INTO LEAD (ID, Status, Nome_do_Lead, Primeiro_nome, Segundo_nome, Sobrenome, Criado,"
            "Fonte ,Telefone_de_trabalho, Responsável, Informações_de_status,"
            "Informações_da_fonte, Criado_por, Modificado, Modificado_Por, Nome_da_empresa,"
            "Lead_repetido, CIDADE_TELEVENDAS, Data_de_Conversão, Forma_de_Pagamento, Número_do_pedido_Winthor,"
            "MOTIVO_DAS_INTERAÇÕES, MOTIVO_NÃO_VENDA, CÓDIGO_DO_PRODUTO, OBSERVAÇÃO_NÃO_VENDA, Estado_UF)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
            "        '{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}','{}', '{}', '{}', '{}')"
            .format(a['ID'], a['STATUS_ID'], a['TITLE'], a['NAME'],a['SECOND_NAME'], a['LAST_NAME'],a['DATE_CREATE'],
                    a['SOURCE_ID'], a['PHONE'][0]['VALUE'],a['ASSIGNED_BY_ID'],a['STATUS_DESCRIPTION'],
                    a['SOURCE_DESCRIPTION'], a['CREATED_BY_ID'], a['DATE_MODIFY'],a['MODIFY_BY_ID'], a['COMPANY_ID'],
                    a['IS_RETURN_CUSTOMER'], a['UF_CRM_1585530790'], a['UF_CRM_1589554873'], a['UF_CRM_1589984561981'], a['UF_CRM_1590010371392'],
                    a['UF_CRM_1590574186777'], a['UF_CRM_1590574245657'], a['UF_CRM_1594415348970'][0], a['UF_CRM_1594415383097'], a['UF_CRM_1598647901']))


def atualizar_leads(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    return ("UPDATE LEAD SET Status='{}', Nome_do_lead='{}', Primeiro_nome='{}', Segundo_nome='{}', Sobrenome='{}', Criado='{}',"
            "Fonte='{}',Telefone_de_trabalho='{}', Responsável='{}', Informações_de_status='{}',"
            "Informações_da_fonte='{}', Criado_por='{}', Modificado='{}', Modificado_Por='{}', Nome_da_empresa='{}',"
            "Lead_repetido='{}', CIDADE_TELEVENDAS='{}', Data_de_Conversão='{}', Forma_de_Pagamento='{}', Número_do_pedido_Winthor='{}',"
            "MOTIVO_DAS_INTERAÇÕES='{}', MOTIVO_NÃO_VENDA='{}', CÓDIGO_DO_PRODUTO='{}', OBSERVAÇÃO_NÃO_VENDA='{}', Estado_UF='{}'"
            "WHERE ID ='{}'"
            .format(a['ID'], a['STATUS_ID'], a['TITLE'], a['NAME'],a['SECOND_NAME'], a['LAST_NAME'],a['DATE_CREATE'],
                    a['SOURCE_ID'], a['PHONE'][0]['VALUE'], a['ASSIGNED_BY_ID'],a['STATUS_DESCRIPTION'],
                    a['SOURCE_DESCRIPTION'], a['CREATED_BY_ID'], a['DATE_MODIFY'],a['MODIFY_BY_ID'], a['COMPANY_ID'],
                    a['IS_RETURN_CUSTOMER'], a['UF_CRM_1585530790'], a['UF_CRM_1589554873'], a['UF_CRM_1589984561981'], a['UF_CRM_1590010371392'],
                    a['UF_CRM_1590574186777'], a['UF_CRM_1590574245657'], a['UF_CRM_1594415348970'][0], a['UF_CRM_1594415383097'], a['UF_CRM_1598647901'],
                    a['ID']))


def inserir_deals(a):
    print(f"A ID:{a['ID']} foi INSERIDA.")
    return("INSERT INTO deals (ID, TITLE, TYPE_ID, STAGE_ID, PROBABILITY, CURRENCY_ID, OPPORTUNITY, "
                   "IS_MANUAL_OPPORTUNITY, TAX_VALUE, LEAD_ID, COMPANY_ID, CONTACT_ID, QUOTE_ID, BEGINDATE, CLOSEDATE, "
                   "ASSIGNED_BY_ID, CREATED_BY_ID, MODIFY_BY_ID, DATE_CREATE, DATE_MODIFY, OPENED, CLOSED, COMMENTS,"
                   "ADDITIONAL_INFO, LOCATION_ID, CATEGORY_ID, STAGE_SEMANTIC_ID, IS_NEW, IS_RECURRING,"
                   "IS_RETURN_CUSTOMER, IS_REPEATED_APPROACH, SOURCE_ID, SOURCE_DESCRIPTION,"
                   "ORIGINATOR_ID, ORIGIN_ID, UTM_SOURCE, UTM_MEDIUM, UTM_CAMPAIGN, UTM_CONTENT, UTM_TERM)"
                   "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
                   "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',"
                   "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                   .format(a['ID'], a['TITLE'], a['TYPE_ID'], a['STAGE_ID'], a['PROBABILITY'], a['CURRENCY_ID'],
                           a['OPPORTUNITY'], a['IS_MANUAL_OPPORTUNITY'], a['TAX_VALUE'], a['LEAD_ID'], a['COMPANY_ID'],
                           a['CONTACT_ID'], a['QUOTE_ID'], a['BEGINDATE'], a['CLOSEDATE'], a['ASSIGNED_BY_ID'],
                           a['CREATED_BY_ID'], a['MODIFY_BY_ID'], a['DATE_CREATE'], a['DATE_MODIFY'], a['OPENED'],
                           a['CLOSED'], a['COMMENTS'], a['ADDITIONAL_INFO'], a['LOCATION_ID'], a['CATEGORY_ID'],
                           a['STAGE_SEMANTIC_ID'], a['IS_NEW'], a['IS_RECURRING'], a['IS_RETURN_CUSTOMER'],
                           a['IS_REPEATED_APPROACH'], a['SOURCE_ID'], a['SOURCE_DESCRIPTION'], a['ORIGINATOR_ID'],
                           a['ORIGIN_ID'], a['UTM_SOURCE'], a['UTM_MEDIUM'], a['UTM_CAMPAIGN'], a['UTM_CONTENT'],
                           a['UTM_TERM']))


def atualizar_deals(a):
    print(f"A ID:{a['ID']} foi ATUALIZADA.")
    return(
        "UPDATE deals SET TITLE='{}', TYPE_ID='{}', STAGE_ID='{}', PROBABILITY='{}', CURRENCY_ID='{}', OPPORTUNITY='{}',"
        "IS_MANUAL_OPPORTUNITY='{}', TAX_VALUE='{}', LEAD_ID='{}', COMPANY_ID='{}', CONTACT_ID='{}', QUOTE_ID='{}', BEGINDATE='{}', CLOSEDATE='{}', "
        "ASSIGNED_BY_ID='{}', CREATED_BY_ID='{}', MODIFY_BY_ID='{}', DATE_CREATE='{}', DATE_MODIFY='{}', OPENED='{}', CLOSED='{}', COMMENTS='{}',"
        "ADDITIONAL_INFO='{}', LOCATION_ID='{}', CATEGORY_ID='{}', STAGE_SEMANTIC_ID='{}', IS_NEW='{}', IS_RECURRING='{}',"
        "IS_RETURN_CUSTOMER='{}', IS_REPEATED_APPROACH='{}', SOURCE_ID='{}', SOURCE_DESCRIPTION='{}',"
        "ORIGINATOR_ID='{}', ORIGIN_ID='{}', UTM_SOURCE='{}', UTM_MEDIUM='{}', UTM_CAMPAIGN='{}', UTM_CONTENT='{}', UTM_TERM='{}'"
        " WHERE ID='{}'"
        .format(a['TITLE'], a['TYPE_ID'], a['STAGE_ID'], a['PROBABILITY'], a['CURRENCY_ID'],
                a['OPPORTUNITY'], a['IS_MANUAL_OPPORTUNITY'], a['TAX_VALUE'], a['LEAD_ID'],
                a['COMPANY_ID'],
                a['CONTACT_ID'], a['QUOTE_ID'], a['BEGINDATE'], a['CLOSEDATE'], a['ASSIGNED_BY_ID'],
                a['CREATED_BY_ID'], a['MODIFY_BY_ID'], a['DATE_CREATE'], a['DATE_MODIFY'], a['OPENED'],
                a['CLOSED'], a['COMMENTS'], a['ADDITIONAL_INFO'], a['LOCATION_ID'], a['CATEGORY_ID'],
                a['STAGE_SEMANTIC_ID'], a['IS_NEW'], a['IS_RECURRING'], a['IS_RETURN_CUSTOMER'],
                a['IS_REPEATED_APPROACH'], a['SOURCE_ID'], a['SOURCE_DESCRIPTION'], a['ORIGINATOR_ID'],
                a['ORIGIN_ID'], a['UTM_SOURCE'], a['UTM_MEDIUM'], a['UTM_CAMPAIGN'], a['UTM_CONTENT'],
                a['UTM_TERM'], a['ID'])
        )


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
