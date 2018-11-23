# Guia de Instalação

### 1 - Primeiro leia o nosso [guia de contribuição](docs/CONTRIBUTING.md) onde são explicados todos os passos para contribuir. Ah, não esquece de ler nosso [código de conduta](docs/CODE_OF_CONDUCT.md).

<p align="justify">&emsp;&emsp;Para instalar as dependências da máquina virtual, é necessarío rodar o seguinte comando:</p>

```
pip3 install virtualenv virtualenvwrapper
```

<p align="justify">&emsp;&emsp;Após isso é necessário configurar algumas coisas, para isso roda os seguintes comando:</p>

Para Ubuntu:
```
chmod -x config_ubuntu.sh
```
```
./config_ubuntu.sh
```

Para Mac:
```
sudo sh config_mac.sh
```

<p align="justify">&emsp;&emsp;Após a instalação da máquina virtual, é necessário abrir outro terminal ou rodando o seguinte comando:</p>

```
bash
```

<p align="justify">&emsp;&emsp;Para iniciar a máquina virtual, faça o seguinte comando:</p>

```
mkvirtualenv -p python3 -a . -r requirements.txt banca_api
```

<p align="justify">&emsp;&emsp;Após iniciar a máquina virtual, você pode sair dela digitando:</p>

```
deactivate
```

<p align="justify">&emsp;&emsp;E para abrir a máquina virtual:</p>

```
workon banca_api
```

<p align="justify">&emsp;&emsp;Para que seja possível a utilização da API, é preciso executar o makemigrations. Este comando é necessário para criação de novas migrações relacionadas as models:</p>

```
python manage.py makemigrations
```

<p align="justify">&emsp;&emsp;Para que essas migrações possam ser manipuladas, tanto na aplicação de novas quando no exclusão das existentes, é necessário executar o comando:</p>

```
python manage.py migrate
```

<p align="justify">&emsp;&emsp;Para executar a API é fundamental o seguinte comando: </p>

```
python manage.py runserver
```

<p align="justify">&emsp;&emsp;Para acessar o servidor gerado no comando anterior, basta acessar [localhost:8000](http://localhost:8000/)</p>
