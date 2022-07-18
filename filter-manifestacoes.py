import pandas as pd

def filterCSV():
    # headers = ["IdPedido", "ProtocoloPedido", "Esfera", "OrgaoDestinatario", "Situacao", "DataRegistro", "ResumoSolicitacao", "DetalhamentoSolicitacao", "PrazoAtendimento", "FoiProrrogado", "FoiReencaminhado", "FormaResposta", "OrigemSolicitacao", "IdSolicitante", "AssuntoPedido", "SubAssuntoPedido", "Tag", "DataResposta", "Resposta", "Decisao", "EspecificacaoDecisao"]
    headers = ["DataRegistro", "DataPrazoResposta", "DataResposta", "FaixaEtaria", "RacaCor", "Genero", "MunicipioManifestante", "UFMunicipioManifestante", "MunicipioManifestacao", "UFMunicipioManifestacao", "TipoManifestacao", "CodigoOrgaoSiorg", "NomeOrgao", "Assunto", "DiasParaResolucao", "DiasAtraso", "Formulario", "Situacao", "Esfera", "Servico", "OutroServico", "DemandaAtendida", "Satisfacao"]
    filename = "manifestacoes-ouvidoria"
    
    data = pd.read_csv(filename + ".csv", sep=";", encoding="iso-8859-1", names=headers, low_memory=False)
        # data.query('AssuntoPedido == "Acesso à informação" and OrgaoDestinatario == "FUNAI – Fundação Nacional do Índio"', inplace=True)
    data.query('NomeOrgao == "Fundação Nacional do Índio"', inplace=True)

    data["DataRegistro"] = pd.to_datetime(data["DataRegistro"], dayfirst=True)
    data = data.sort_values(by="DataRegistro")

    data["DataRegistro"] = data["DataRegistro"].dt.strftime("%d/%m/%Y")

    print(data)
    data.to_csv("manifestacoes-ouvidoria-filtered.csv", encoding="utf-16", sep=";", index=False)

filterCSV()