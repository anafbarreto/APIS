# Rick And Morty

Flask: Framework que utiliza a linguagem python para criar apps web.

Criando o ambiente <br/>
terminal: py -3 -m venv .venv

Ativar o ambiente virtual <br/>
terminal: .venv\scripts\activate (pode usar tab pra completar o caminho) <br/>
Se rolar erro de bloqueio de excecução: Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser

Instalar o Flask <br/>
terminal: pip install flask <br/>
Se rolar erro: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Flask -vvv <br/>
** Com o ambiente virtual ativo

Consultar a api criada <br/>
terminal: flask --app app run
