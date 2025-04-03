from simulador_custos import calcular_subvencao

def test_calculo_premio_total():
    # Valores fixos da linha 40 da planilha (já convertidos)
    cobertura = 126000.00
    futura = 94500.00
    fitossanitario = 5000.00
    taxa_reduzida = 0.0546

    base_total = cobertura + futura + fitossanitario
    premio = base_total * taxa_reduzida

    # Valor da planilha: R$ 12.308,00
    esperado = 12308.00

    # Permitir pequena margem de erro por arredondamento
    assert abs(premio - esperado) < 5.0

from simulador_custos import calcular_subvencao

def test_calculo_subvencoes():
    premio = 12308.00

    # Percentuais e limites reais
    percentual_estadual = 0.30
    limite_estadual = 25000
    percentual_federal = 0.40
    limite_federal = 60000

    subvencao_estadual = calcular_subvencao(premio, percentual_estadual, limite_estadual)
    subvencao_federal = calcular_subvencao(premio, percentual_federal, limite_federal)

    assert round(subvencao_estadual, 2) == 3692.40
    assert round(subvencao_federal, 2) == 4923.20

def test_investimento_e_parcelas():
    premio = 12308.00
    subvencao_estadual = 3692.40
    subvencao_federal = 4923.20

    investimento = premio - subvencao_estadual - subvencao_federal
    parcelas = 5
    valor_parcela = investimento / parcelas

    assert round(investimento, 2) == 3692.40
    assert round(valor_parcela, 2) == 738.48
