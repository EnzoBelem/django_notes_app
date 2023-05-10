# Django_notes_app
Projeto de um web site simples implementado com framework Django. A ideia do projeto é implementar funcionalidades de login, 
criação, personalização e compartilhamento de notinhas com texto e foto no site.

## Tecnologias usadas
* Python
* Django
* Html/Css
* Bootstrap
* Javascript

## Como executar o projeto
Atualmente o projeto não está hospedado e será preciso configurar um ambiente django localmente.
### Clonando o projeto localmente
```
git clone https://github.com/EnzoBelem/django_notes_app.git
```
### Versão do python
O projeto usa a versão 3.11.2 do **Python**. [download](https://www.python.org/downloads/release/python-3112/)
### Configurando o ambiente virtual 
Usando o terminal da sua preferência, crie o ambiente virtual dentro da pasta do projeto:
```
python -m venv venv
```
Inicie o ambiente virtual e instale os pacotes através do arquivo requirements.txt:
```
pip install -r requirements.txt
``` 
### Executanto o servidor local do Django
Após as etapas anteriores basta executar o servidor local do Django com o seguinte comando:
```
py manage.py runserver
``` 
