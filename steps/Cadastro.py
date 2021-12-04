from behave import *

@given('que acesso o site Blazedemo')
def que_acesso_o_site_Blazedemo(context):
    print('Passo 1 - Abriu o site')

@when('acesso a opção Home e a opção Register')
def acesso_a_opcao_Home_e_a_opcao_Register(context):
    print('Passo 2 - Acessou as opções Home e Register')

@when('preencho os dados de "Name" "Company" "E-mail Address" "Password" e "Confirm Password"')
def preencho_os_dados(context):
    print('Passo 3 - Preencheu os dados para cadastro')

@when('submeto o registro')
def submeto_o_registro(context):
    print('Passo 4 - Gravou o registro')

@then('deve apresentar uma mensagem de que o usuario esta logado')
def deve_apresentar_uma_mensagem_de_que_o_usuario_esta_logado(context):
    print('Passo 5 - Validou se o login foi realizado')