import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

#acima possui as importações necessárias para realizar a conexao, exigida pelo brevo

#abaixo configura api utilizando a chave criada
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '' # nesta linha inserir a chave que criei no .env, para funcionar o email

# Criar instância da API
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Monta a msg e para onde vai
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=[{"email": "bryanoli121@gmail.com", "name": "Eduardo"}],
    sender={"email": "fala.inossotcc@gmail.com", "name": "Fala.i"},
    subject="olá aqui é do falai rsrsrsrsrsrs, vamo dar I pro iuri",
    html_content="<html><body><h1>Olá!</h1><p>Este é um e-mail de teste.</p></body></html>"
)

try:
    # Enviar o email de fato, fazendo a conexão
    response = api_instance.send_transac_email(send_smtp_email)
    pprint(response)
except ApiException as e:
    print("Erro ao enviar e-mail: %s\n" % e)
