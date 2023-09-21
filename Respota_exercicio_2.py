# Resposta
class ContaCorrente:
  def __init__ (self, numero_da_Conta, nome_do_correntista, saldo_t):
    self.numero_da_Conta = numero_da_Conta
    self.nome_do_correntista = nome_do_correntista
    self.saldo_t = saldo_t

  def __str__(self): #REALIZEI O PROCEDIMENTO DE FORMA OPCIONAL
    return f"\nNúmero da conta: {self.numero_da_Conta}\nNome do Correntista: {self.nome_do_correntista}\nSaldo atual: {self.saldo_t}"

  def alterarNome(self, n_nome_do_correntista):
    self.nome_do_correntista = n_nome_do_correntista

  def deposito(self, saldo):
    self.saldo_t += saldo

  def saque(self, saque):
    if saque <= self.saldo_t:
      self.saldo_t -= saque
      print("\nSAQUE REALIZADO COM SUCESSO!!!")
    else:
      print("\n\tSAQUE NÃO REALIZADO POR SALDO INSUFICIENTE.")

correntista = ContaCorrente(20116, 'Matias', 0)
print("Dados da CONTA:", correntista.__str__(),"\n") #REALIZEI O PROCEDIMENTO DE FORMA OPCIONAL

correntista.alterarNome(input("Digite o novo nome do correntista: "))
print("\tAgora o novo nome do Correntista é: ",correntista.nome_do_correntista,"\n")

correntista.deposito(float(input("Digite o valor do depósito: ")))
print("\tSeu saldo agora é: ",correntista.saldo_t,"\n")

correntista.saque(float(input("Digite um valor que você deseja sacar: ")))
print("\tSeu saldo é: ",correntista.saldo_t)

print("\nDados atualizados da CONTA:", correntista.__str__()) #REALIZEI O PROCEDIMENTO DE FORMA OPCIONAL
