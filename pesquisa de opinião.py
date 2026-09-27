# Configuração do total de entrevistados para o teste (altere para 50 na versão final)
TOTAL_ENTREVISTADOS = 10

# Contadores de respostas
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

print("=== PESQUISA DE SATISFAÇÃO DE ATENDIMENTO - TUDOWEB ===\n")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"--- Entrevistado {i} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Validação e coleta da opinião
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opcao = int(input("Digite a sua opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para verificar a opinião
    if opcao == 1:
        print(f"Resposta registrada: EXCELENTE\n")
        qtd_excelente += 1
    elif opcao == 2:
        print(f"Resposta registrada: BOM\n")
        qtd_bom += 1
    elif opcao == 3:
        print(f"Resposta registrada: RUIM\n")
        qtd_ruim += 1
    else:
        print("Opção inválida! Resposta não contabilizada.\n")

# Exibição do relatório final
print("=" * 45)
print("          RESULTADO FINAL DA PESQUISA          ")
print("=" * 45)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM':      {qtd_ruim}")
print(f"   Quantidade de respostas 'BOM':       {qtd_bom}")
print("=" * 45)