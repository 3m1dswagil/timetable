*********Email Grupo**********************
3m1.dswagil@gmail.com
#M37od0Ag1l!

*********Intruções Python**********************
Para gerar o requirements
pip freeze requirements.txt

Criar ambiente com virtualenv
virtualenv env

ativar ambiente
source env/bin/activate

instalando bibliotecas
pip install -r requirements.txt

executando a aplicacao
python run.py

*********Intruções GIT**********************
Criando novo repositório
git init

Obtendo novo repositório
git clone /caminho/para/o/repositório

Criando uma branch (Sempre que criar uma branch nova, vai criar um clone da master e troca pra nova branch)
git checkout -b <nome_da_branch>

*** git checkout <nome_da_branch> (altera pra branch dada)

Mostra os ultimos commits feitos na branch atual
git log

Levar as alterar feitas na branch para dentro da master
git merge <nome_da_branch>

Mostra se tem algum arquivo que ainda não foi commitado
git status 

Verifica se existe alguma atualização na master
git fetch


Adicionando arquivo no repositório
git add <arquivo>
git add *

Confirmar mudanças no repositório
git commit -m "comentário das alterações"

Enviando alterações para repositório remoto
git push origin master

Atualizando o git
git pull
*********Intruções Git Branch**********************
Adicionar grupos arquivos modificados na branch
git add .

Comitar os arquivos alterados com os comentarios
git commit -m "<comentarios>"

Subir os arquivos comitados para o repositorio
git push



*********Intruções PostGreSQL**********************
usuario: root
senha: timetable

superuser: 3m1
senha: root1234
email: 3m1.dswagil@gmail.com


*********Intruções pgAdmin**********************
email:guimaraesajuliana@gmail.com
senha: root12

cd ~/apps/pgadmin4
source ./venv/bin/activate
python ./venv/lib/python2.7/site-packages/pgadmin4/pgAdmin4.py

