<p align="center">
  <h1>🛠️🧪 <b>Flask App With Login</b> 🛠️🧪</h1>
  <h6>by <i>FranciscoCharles</i></h6>
</p>
<p align="justify">

Este projeto basico é o resultado do estudos de algumas funcionalidades do micro framework **Flask** do **Python**. O principal objetivo foi entender alguns conceitos utilizados além de conhecer como um projeto flask deve ser organizado, puxando a questão de organização e arquitetura.

</p>

<div align="center">
    <img src="./app_with_login/static/asserts/screen_1.png">
    <br>
    <h6>
        Figure 1 - principais telas.
    </h6>
</div>
<div align="center">
    <img src="./app_with_login/static/asserts/screen_2.png">
    <br>
    <h6>
        Figure 2 - tela quando logado e telas com alguns erros.
    </h6>
</div>

# <a name=index>Indice📚</a>
- [**Como executar?**](#run)
- [**Arquivo settings**](#settings_file)
- [**Dependências**](#dependencies)
- [**Versão**](#version)
- [**Licença**](#license)

# **<a name=run> ⚙️ Como executar? 🧠💭</a>** <h6>[voltar ao indice](#index)</h6>

Faça o download do projeto, entre na pasta do projeto e instale as dependências com o seguinte comando:
```bash
pip install -r requirements.txt
```
Renomeie o arquivo `example-settings.toml` para `settings.toml` e realize a configuração, veja a seção [**Arquivo settings**](#settings_file) para entender um pouco.

Após realizar as configurações, crie o banco de dado e as tabelas usando o seguinte comando:
```bash
flask create-db
```
⚠️ obs: para esse comando seu usuário deve possuir previlégio de criação de bancos e tabelas.⚠️

Caso deseje é possivel usar o comando abaixo para criar automaticamente 2 usuarios de exemplo para testar o projeto.
```bash
flask populate-db
```
Após esse comando estará disponivel dois usarios com emails sendo `joel@example.com` e `ellie@example.com`, ambos usam a senha `123`.

Tambem está disponivel um comando para deletar o banco de dados, use o seguinte comando para esse proposito:

```bash
flask drop-db
```
para executar utilize o comando abaixo:
```bash
flask run
```
Após esse comando o servidor de desenvolvimento será iniciado e basta acessar o endereço `localhost:3000`(caso o `.env` não tenha sido modificado) em qualquer navegador de sua preferência.

# **<a name=settings_file>🔧📝 Arquivo Settings</a>**  <h6>[voltar ao indice](#index)</h6>
No arquivo `toml` alguns atributos conforme necessario devem ser modificados, esses atributos são os seguintes:
```toml
[default]
TITLE = "App with login"
SECRET_KEY = "1f13965644d67dec60739fc61f51dd97"
SQLALCHEMY_DATABASE_URI = ""
```
Abaixo uma breve descrição de cada um:

+ **TITLE**: titulo da aplicação, por padrão `"App with login"`.
+ **SECRET_KEY**: A secret key que será utilizada pelo flask, por padrão `"1f13965644d67dec60739fc61f51dd97"`.
+ **SQLALCHEMY_DATABASE_URI**: A URI do banco de dados. Consulte o site do SqlAlchemy sobre [Database Urls](https://docs.sqlalchemy.org/en/14/core/engines.html).


# **<a name=dependencies>Dependências</a>**  <h6>[voltar ao indice](#index)</h6>

Verifique o arquivo [requirements.txt](./requeriments.txt)

- [**Flask**](https://pypi.org/project/Flask/) **>= 2.0.2**
- [**Flask-login**](https://pypi.org/project/Flask-Login/) **>= 0.5.0**
- [**Flask-SQLAlchemy**](https://pypi.org/project/Flask-SQLAlchemy/) **>= 2.5.1**
- [**Dynaconf**](https://pypi.org/project/dynaconf/) **>=3.1.7**
- [**SQLAlchemy-Utils**](https://pypi.org/project/SQLAlchemy-Utils/) **>=0.37.8**

# **<a name=version>Versão</a>**  <h6>[voltar ao indice](#index)</h6>
- versão atual do projeto: 0.1.1.

# **<a name=license>Licença</a>**  <h6>[voltar ao indice](#index)</h6>

Para mais informações sobre a licença deste projeto, leia o arquivo <a href="./LICENSE" title="go to license file">LICENSE</a>.

---
<p align="center">
    Copyright © 2021 <b>FranciscoCharles</b>
</p>