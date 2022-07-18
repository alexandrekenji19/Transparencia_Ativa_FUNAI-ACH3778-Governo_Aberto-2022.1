import pandas as pd

def filterCSV():
    headers = ["IdPedido", "ProtocoloPedido", "Esfera", "OrgaoDestinatario", "Situacao", "DataRegistro", "ResumoSolicitacao", "DetalhamentoSolicitacao", "PrazoAtendimento", "FoiProrrogado", "FoiReencaminhado", "FormaResposta", "OrigemSolicitacao", "IdSolicitante", "AssuntoPedido", "SubAssuntoPedido", "Tag", "DataResposta", "Resposta", "Decisao", "EspecificacaoDecisao"]
    filenames = ["20220605_Pedidos_csv_2017", "20220605_Pedidos_csv_2018", "20220605_Pedidos_csv_2019", "20220605_Pedidos_csv_2020"]
    dataPerYear = []
    for file in filenames:
        data = pd.read_csv(file + ".csv", sep=";", encoding="utf16", names=headers)
        data.query('AssuntoPedido == "Acesso à informação" and OrgaoDestinatario == "FUNAI – Fundação Nacional do Índio"', inplace=True)
        dataPerYear.append(data)
    print(dataPerYear)
    fullData = pd.concat(objs=dataPerYear)
    print(fullData)
    fullData.to_csv("Pedidos_2017_a_2020.csv", encoding="utf-16", sep=";", index=False)

filterCSV()