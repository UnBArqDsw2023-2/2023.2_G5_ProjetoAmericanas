<h1 align="center">Americanas (G5) </h1>

<p align="center">
    <img src="/docs/img/americanas-logo.webp" width="400" height="400">
</p>

Este repositório tem como objetivo auxiliar no registro dos artefatos e resultados obtidos no desenvolvimento do projeto do Grupo 5 de Arquitetura e Desenho de Software da Universidade de Brasília (UnB-FGA) no semestre 2023.2.

# Americanas

A Lojas Americanas S.A. é uma empresa brasileira que se dedica essencialmente à operação de lojas de departamento. As atividades da Empresa se dividem em dois segmentos comerciais: Lojas tradicionais e E-commerce. É possível acessar o site clicando aqui ([Americanas](https://www.americanas.com.br/)) ou a partir do link https://www.americanas.com.br/

## Sobre :page_facing_up:

O Grupo é responsável por analisar a Americanas, Perfil Comprador & Plataforma, e fluxos compreendidos nas avaliações dos produtos.

# Instalação e Execução
## Instalação e Execução Local dos Docs

Clonar o repositório :cloud:

```bash
git clone https://github.com/UnBArqDsw2023-2/2023.2_G5_ProjetoAmericanas/
```

Navegar até a pasta root do repositório.

```bash
cd 2023.2_G5_ProjetoAmericanas
```

A geração do site estático é realizada utilizando o [docsify](https://docsify.js.org/).

```shell
"Docsify generates your documentation website on the fly. Unlike GitBook, it does not generate static html files. Instead, it smartly loads and parses your Markdown files and displays them as a website. To start using it, all you need to do is create an index.html and deploy it on GitHub Pages."
```

Instalar o docsify com o seguinte comando:

```shell
npm i docsify-cli -g
```

Para executar o site dos docs localmente, utilize o comando:

```shell
docsify serve ./docs
```

## Instalação e Execução Local do Web App

Requisitos:
* Docker instalado.
* Docker Compose instalado.

Clonar o repositório :cloud:

```bash
git clone https://github.com/UnBArqDsw2023-2/2023.2_G5_ProjetoAmericanas/
```

Navegar até a pasta root do repositório.

```bash
cd 2023.2_G5_ProjetoAmericanas
```

Buildar e rodar o web app.

```bash
docker compose -f docker-compose-local.yml up --build
```

Links:
* Frontend: http://0.0.0.0:3000
* Backend: http://localhost:8000
* Backend admin: http://localhost:8000/admin 
* Postgres: localhost:5432

Conforme definido nas "env files" presentes na pasta [".envs/local"](/.envs/local), o usuário padrão do backend admin é "super" e senha padrão é "senha12345". Esse usuário e senha padrões são diferentes dos utilizados no ambiente de produção.

## Equipe :mortar_board:

[<img src="https://github.com/CDGodoy.png?size=400" width=100><br><sub>Carlos Daniel Godoy</sub>](https://github.com/CDGodoy) |[<img src="https://github.com/fellipepcs.png?size=400" width=100><br><sub>Fellipe Silva</sub>](https://github.com/fellipepcs) | [<img src="https://github.com/joseluis-rt.png?size=400" width=100><br><sub>José Luís Teixeira</sub>](https://github.com/joseluis-rt) |  [<img src="https://github.com/leomichalski.png?size=400" width=100><br><sub>Leonardo Michalski</sub>](https://github.com/leomichalski) | [<img src="https://github.com/PabloChristianno.png?size=400" width=100><br><sub>Pablo Guedes</sub>](https://github.com/PabloChristianno) | 
| :---: | :---: | :---: | :---: | :---: |

[<img src="https://github.com/Peedrooo.png?size=400" width=100><br><sub>Pedro Vitor Jesus</sub>](https://github.com/Peedrooo) |[<img src="https://github.com/PhilipeSousa.png?size=400" width=100><br><sub>Philipe Sousa</sub>](https://github.com/PhilipeSousa) | [<img src="https://github.com/RafaelN0bre.png?size=400" width=100><br><sub>Rafael Nobre</sub>](https://github.com/RafaelN0bre) | [<img src="https://github.com/lacerdaRenan.png?size=400" width=100><br><sub>Renan Lacerda</sub>](https://github.com/lacerdaRenan) | [<img src="https://github.com/Silas-neres.png?size=400" width=100><br><sub>Silas Neres</sub>](https://github.com/Silas-neres) | 
| :---: | :---: | :---: | :---: | :---: |


