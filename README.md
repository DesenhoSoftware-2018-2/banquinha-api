## Banquinha API

<p align="justify">&emsp;&emsp;Essa API é relacionada com o projeto da Banquinha, presente na mesma organização desse repositório e no seguinte link:
[Banquinha](https://github.com/DesenhoSoftware-2018-2/banquinha-web)</p>

### Instalação

<p align="justify">&emsp;&emsp;Para instalar todas as dependências necessárias do projeto, rode o seguinte comando:</p>

```
pip3 install -r requirements.txt
```

<p align="justify">&emsp;&emsp;Para que seja possível a utilização da API, é preciso executar o makemigrations. Este comando é necessário para criação de novas migrações relacionadas as models:</p>

```
python3 manage.py makemigrations
```

<p align="justify">&emsp;&emsp;Para que essas migrações possam ser manipuladas, tanto na aplicação de novas quando no exclusão das existentes, é necessário executar o comando:</p>

```
python3 manage.py migrate
```

<p align="justify">&emsp;&emsp;Para executar a API é fundamental o seguinte comando: </p>

```
python3 manage.py runserver
```

<p align="justify">&emsp;&emsp;Para acessar o servidor gerado no comando anterior, basta acessar [localhost:8000](http://localhost:8000/)</p>
