from datetime import datetime

def calcular_idade(data_nascimento_str):
  """
  Calcula a idade em anos a partir da data de nascimento.

  Args:
    data_nascimento_str: Uma string representando a data de nascimento no formato 'AAAA-MM-DD'.

  Returns:
    A idade da pessoa em anos.
  """
  try:
    data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d')
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade
  except ValueError:
    return "Formato de data inválido. Use AAAA-MM-DD."

# Solicita a data de nascimento do usuário
data_nascimento_usuario = input("Digite sua data de nascimento (AAAA-MM-DD): ")

# Calcula a idade
idade_calculada = calcular_idade(data_nascimento_usuario)

# Exibe a idade
print(f"A idade é: {idade_calculada} anos")
