# cpf_validador
Um simples software que possibilita verificar um CPF.


1. Digite um CPF quando solicitado;

2. Todos os dados salvos no arquivo database/database.json serão transferidos à uma variável;

3. Cria-se uma função em conjunto ao package* validade_docbr que verifica o CPF digitado;

4. Após a analise do CPF é transmitido a tela uma resposta sobre a vericidade do documento;
   
5. E por fim, todos os CPFs válidos são salvos no arquivo database.json, juntamente com os antigos dados salvos na variável (tópico 2);

~

EXEMPLO:

CPF DIGITADO: 466.843.284-91

SOFTWARE: O CPF "466.843.284-91" é válido!

ARQUIVO .json: ["466.843.284-91"]

~

CPF DIGITADO: 123.123.123-12

SOFTWARE: O CPF "123.123.123-12" é inválido!

ARQUIVO .json: [""] (poderá aparecer apenas CPFs válidos antes escritos!)

~

*Package utilizada no código: https://pypi.org/project/validate-docbr/*

Software, Pesquisas e Fontes feitos por Joao Aslan ~ 30/09/2021
