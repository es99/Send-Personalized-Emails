def text_msg(d):
  msg = f"Olá {d['nome']},\n\n\
Para acesso ao nosso sistema TS utilize os dados abaixo:\n\
Login: {d['login']}\nSenha: {d['senhaTS']}\n\n\
Senha do sistema {d['sistema']}\nSenha: {d['senhaSistema']}\n\n\
Para maiores informações e dúvidas, entre em contato com o nosso Suporte ao cliente.\n\
Atenciosamente,"

  return msg

def text_html(d):
  msg = f"<!DOCTYPE html>\n\
<html>\
<head><meta charset='UTF-8'></head>\
<body>\
<h2>Informações para Acesso TS e Sistemas</h2>\
<p>Olá {d['nome']},<br />Para acesso ao nosso sistema TS utilize os dados abaixo:<br />\
Login: {d['login']}<br />Senha: {d['senhaTS']}<br />\
Senha do sistema {d['sistema']}: {d['senhaSistema']}<br /></p>\
<p>Para maiores informações e dúvidas, entre em contato com o nosso Suporte ao cliente.<br />\
<a href='http://www.infopublic.com.br'>Site Infopublic</a><br /></p>\
<ul><li>83 99692-3456 / 98841-4481</li><li>WhatsApp: 83 98841-4481</li></ul>\
<p>Horários de atendimento: <br />\
De segunda a sexta: Das 08h-12h e das 13h-17h<br />\
</p>\
</body>\
</html>"
  return msg


def escolhaSistema():
  print(
        "Escolha o sistema correspondente abaixo.\n"
        "1.PJFolha\n"
        "2.PJCheque\n"
        "3.PJPCTB(Contabilidade)\n"
        "4.PJFrota\n"
        "5.PJTributos\n"
        "6.AcessoTS\n"
        )

  escolha = input("Entre como número correspondente ao sistema: ")
  index = list('123456')
  nomes = ['PJFolha', 'PJCheque', 'PJPCTB(Contabilidade)', 'PJFrota', 'PJTributos', 'AcessoTS']
  dicionario = dict(zip(index, nomes))
  nome_sistema_escolhido = dicionario[escolha]
  return nome_sistema_escolhido

def entrada_dados():
  dados = []
  nome = input("Nome do cliente: ")
  dados.append(nome)
  login = input("Entre com o CPF do cliente (apenas números): ")
  dados.append(login)
  sistema = escolhaSistema()
  dados.append(sistema)
  senhaTS = input("Senha do TS: ")
  dados.append(senhaTS)
  senhaSistema = input("Senha do Sistema: ")
  dados.append(senhaSistema)
  cabecalhos = ['nome', 'login', 'sistema', 'senhaTS', 'senhaSistema']
  dicionario = dict(zip(cabecalhos, dados))

  text_message = text_msg(dicionario)
  message_html = text_html(dicionario)

  return text_message, message_html


#if __name__ == '__main__':


