@cadastro_usuario
Feature: Cadastro de usuario
  Scenario: Realizar cadastro de usuário
    Given que acesso o site Blazedemo
	When acesso a opção Home e a opção Register
	And preencho os dados de "Name" "Company" "E-mail Address" "Password" e "Confirm Password"
	And submeto o registro
	Then deve apresentar uma mensagem de que o usuario esta logado