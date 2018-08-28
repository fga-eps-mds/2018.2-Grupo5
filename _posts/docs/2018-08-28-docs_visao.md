---
title: Documento de visão
author: Emanoel
layout: post
categories: DEV
---


## Sumário

* 1. Introdução
  * 1.1. [Propósito]()
  * 1.2. Escopo]()
  * 1.3. Definições, acrônimos e abreviações]()
  * 1.4. Referências]()
  * 1.5. Visão geral]()
* 2. Posição()
 * 2.1. Oportunidade de Negócios]()
 * 2.2. Instrução do problema]()
 * 2.3. Instrução de posição do produto]()
3. Descrições das Partes Interessadas e Usuários]()
 * 3.1. Demográficos de mercado]()
 * 3.2. Resumo da parte interessada]()
 * 3.3. Resumo do usuário]()
 * 3.4. Ambiente de usuário
 * 3.5. Perfis das partes interessadas
 * 3.5.1. Equipe de Gestão de Projeto
 * 3.5.2. Equipe de Desenvolvimento
 * 3.5.3. Corpo docente
 * 3.5.4. Equipe de avaliação e suporte
 * 3.6. Perfis dos usuários
 * 3.6.1. Corpo docente
 * 3.6.2. Alunos
 * 3.6.3. Responsáveis
* 3.7. Principais necessidades da parte interessada ou do Usuário
* 3.8. Alternativas e Concorrência
 * 3.8.1. Método tradicional de controle de entrada e saída de alunos
 * 3.8.2.
* 4. Visão Geral do Produto
 * 4.1. Perspectiva do Produto
 * 4.2. Resumo das capacidades
* 5. Recursos do Produto
* 6. Restrições
 * 6.1. Restrição de escopo
 * 6.2. Restrição de recursos financeiros
 * 6.3. Restrição de desenvolvimento e implantação
* 7. Faixas de Qualidade
* 8. Outros Requisitos do Produto
 * 8.1. Requisitos de usabilidade
 * 8.2. Requisitos do sistema
 * 8.3. Requisitos de desempenho
 * 8.4. Requisitos de confiabilidade


## 1.Introdução

### 1.1 Propósito

<p align="justify">Este documento tem como objetivo definir e organizar as características sobre o desenvolvimento da solução BI.</p>

### 1.2 Escopo

<p align="justify">Realizar uma analise do mercado de jogos usando business inteligence.</p>
<p align="justify">Buscar uma solução em software para facilitar a visão de negocio.</p>
<p align="justify">O software, a ser implementado, deve fornecer informações sobre jogos.</p>

### 1.3 Definições, acrônimos e abreviações

<p align="justify">Alguns dos acrônimos, definições e abreviações usados neste documento são:</p>

+ BI - Business Inteligence.
+ MDS - disciplina Métodos de Desenvolvimento de Software.
+ EPS - disciplina Engenharia do Produto.

### 1.4 Referências

### 1.5 Visão geral

<p align="justify">Este documento descreve os detalhes sobre as características do GamesColorBI a ser desenvolvido, especificando os problemas que estimularam a criação dessa solução em software. O documento é dividido da seguinte maneira: inicialmente é especificado qual problema motivou o desenvolvimento da solução, em seguida as partes interessadas são descritas, e por fim todos os recursos, restrições e requisitos do produto são apresentados.</p>

## 2. Posição
### 2.1 Oportunidade de Negócios

<p align="justify">O desenvolvimento para o mercado de jogos está cada vez mais competitivo, busca-se indícios a partir da análise de dados para identificar oportunidades de negócio.</p>
<p align="justify">O projeto de BI busca evidenciar estatisticamente usando uma solução informatizada visando experiência do cliente.</p>

### 2.2 Instrução do problema

| **O problema seria** | a dificuldade em encontrar informações sobre jogos |
| :--- | :--- |
| **que afeta** | mercado de jogos |
| **cujo impacto é** | jogos com pouca adesão, lançamento de jogos sem expectativas poupaveis |
| **e uma boa solução seria** | identificar tendências a partir do atual mercado de jogos  |

### 2.3 Instrução de posição do produto

| **Para** | desenvolvedores, analistas, produtores de conteúdo|
| :--- | :--- |
| **que** | necessitam de uma ferramenta para analisar dados |
| **o** | *Games BI* é uma aplicação |
| **que** | sistematiza dados relevantes e os fornece estruturadamente |
| **diferente do** | método tradicional feito manualmente e do aplicativo *Acadêmico Total Pais e Filhos* |
| **nosso produto** | é um alternativa gratuita e funcional para o problema existente. |

## 3. Descrições da parte interessada e do usuário

### 3.1 Demográficos de mercado

<p align="justify"> Atualmente no DF, as instituições de ensino sofrem com a criminalidade e a evasão escolar, e o método usado por essas escolas é obsoleto e arcaico, não se adaptando às novas forma de comunicação e integração. Apenas no DF, são mais de 667 escolas públicas que podem utilizar o nosso produto, e obter um real impacto na vida dos estudantes e responsáveis, que atualmente clamam por uma escola mais integrada e segura, de modo que nosso sistema ficará em destaque por ser de código aberto, e será disponibilizado para todas as escolas que desejarem usá-lo.</p>

### 3.2 Resumo da parte interessada

| **Nome** | **Descrição** | **Responsabilidade** |
| :--- | :--- | :--- |
| Equipe de desenvolvimento | Estudantes da Universidade de Brasília da disciplina de MDS. | Desenvolver e Implementar o _software_. |
| Equipe de Gestão de Projeto | Estudantes da Universidade de Brasília da disciplina de EPS. | Gerir o desenvolvimento do produto identificando o problema e apontando caminhos e soluções. |
| Equipe de avaliação e suporte | Professores colaboradores das disciplinas EPS e MDS. | Auxiliar as equipes durante o desenvolvimento do projeto. |
| Clientes | Centro de Ensino Médio 01 do Gama. | Disponibilizar informações sobre os alunos . |

### 3.3 Resumo do usuário

| **Nome** | **Descrição** |
| :--- | :--- |
| Aluno | Utilizará o _software_ para validação de entrada e saída. |
| Responsáveis | Serão notificados sobre a frequência dos alunos e comunicados em geral da direção. |
| Diretoria | Poderá comunicar os responsáveis sobre alterações na entrada/saída, advertências, suspensões e boletim dos alunos. |

### 3.4 Ambiente de usuário

<p align="justify"> O <i>software</i> será usado em todos os navegadores, tendo seu uso otimizado para o Google chrome versão 56.0.2924.87 devido a sua performance e por ter a maior base instalada dentre os outros navegadores WEB.</p>

## 3.5 Perfis das partes interessadas

### 3.5.1 Equipe de Engenharia do produto

|    **Representantes** |  <br>  <br>  <br>  <br>  |
| :--- | :--- |
| **Descrição** | Gerentes de Projeto. |
| **Tipo** | Estudantes da Universidade de Brasília da disciplina Engenharia do _Produto_. |
| **Responsabilidades** | Estabelecer prazos e metas, organizar a equipe de desenvolvimento e completar os objetivos propostos. |
| **Critérios de Sucesso** | Manter a equipe focada no projeto, contribuir com a evolução profissional da equipe de desenvolvimento, estabelecer um processo de desenvolvimento de _software_ bem definido e entregar o produto dentro do prazo, custo e nível de qualidade. |
| **Envolvimento** | Alto. |
| **Comentários/Problemas** |  - |

### 3.5.2 Equipe de Desenvolvimento

| **Representantes** |  <br>  <br>  <br>  <br>  <br>  <br>  |
| :--- | :--- |
| **Descrição** | Desenvolvedores. |
| **Tipo** | Estudantes da Universidade de Brasília da disciplina Métodos de Desenvolvimento de _Software_. |
| **Responsabilidades** | Desenvolvimento, implementação e realização de testes da aplicação. |
| **Critérios de sucesso** | Entregar o _software_ com as funções requisitadas funcionando e dentro do prazo. |
| **Envolvimento** | Alto. |
|    **Comentários/Problemas** | Ter a oportunidade de criar um _software_ a partir de uma necessidade e passar por todas as etapas de desenvolvimento que um projeto necessita para ficar coeso e bem estruturado. |

### 3.5.3 Mercado de jogos

| **Representantes** | Matheus de Souza Faria |
| :--- | :--- |
| **Descrição** |Desenvolvedor de jogos que busca uma forma eficiente de ter informações sobre os jogos e o mercado de jogos de forma organizada e atualizada|
| **Tipo** | Desenvolvedor de jogos |
| **Responsabilidades** | Fornecer as informações nescessárias para definir o escopo do projeto |
| **Critérios de sucesso** | Garantir que as informações  nescessárias sejam exibidas de forma precisa e ordenada.|
| **Envolvimento** | Alto |
| **Comentários/Problemas** | - |

### 3.5.4 Equipe de avaliação e suporte

| **Representantes** | Dra. Carla Rocha |
| :--- | :--- |
| **Descrição** | Equipe de avaliação e direcionamento das equipes de gestão e desenvolvimento. |
| **Tipo** | Professor e _Coaches_ das disciplinas. |
| **Responsabilidades** | Guiar os alunos durante o semestre quanto aos assuntos relacionados à disciplina de Métodos de Desenvol0vimento de Software e referidos projetos. |
| **Critérios de sucesso** | A entrega do projeto e sua referente documentação de forma completa e correta para o cliente. |
| **Envolvimento** | Médio. |
| **Comentários/Problemas** | - |

## 3.6 Perfis dos usuários

### 3.6.1 Desenvolvedor de jogos

| **Representantes** | - |
| :--- | :--- |
| **Descrição** | Desenvolvedor de jogos que busca uma forma eficiente de ter informações sobre os jogos e o mercado de jogos de forma organizada e atualizada. |
| **Tipo** | Desenvolvedor de jogos |
| **Responsabilidades** | Fornecer as informações necessárias para definir o escopo do projeto. |
| **Critérios de sucesso** | Garantir que as informações  necessárias sejam exibidas de forma precisa e ordenada.|
| **Envolvimento** | Alto. |
| **Comentário/Problemas** |  - |

### 3.6.2 Jogadores

| **Representantes** | Consumidores do mercado de jogos. |
| :--- | :--- |
| **Descrição** | Usuarios que interagem de alguma forma com o mercado de jogos|
| **Tipo** | Consumidores do mercado de jogos. |
| **Responsabilidades** | - |
| **Critérios de sucesso** | - |
| **Envolvimento** | Baixo |
| **Comentário/Problemas** | - |

### 3.6.3 Produtores de conteúdo

| **Representantes** | Consumidores do mercado de jogos. |
| :--- | :--- |
| **Descrição** | Usuarios que interagem de alguma forma com o mercado de jogos|
| **Tipo** | Consumidores do mercado de jogos. |
| **Responsabilidades** | - |
| **Critérios de sucesso** | - |
| **Envolvimento** | Baixo |
| **Comentário/Problemas** | - |

## 3.7 Principais necessidades da parte interessada ou do Usuário

| **Necessidade** | **Prioridade** | **Interesses** | **Solução atual** | **Solução proposta** |
| --- | --- | --- | --- | --- |
| Indicadores de negocio  | Alta. | | | |

## 3.8 Alternativas e Concorrência

### 3.8.1 Método tradicional de controle de entrada e saída de alunos


## 4. Visão geral do produto

### 4.1 Perspectiva do Produto

<p align="justify"> </p>

### 4.2 Resumo das capacidades

| **Benefício para o Cliente** | **Recursos de suporte** |
| --- | --- |
| | |
| | |
| | |

## 5. Recursos do produto

### 5.1 Recurso X

<p align="justify"></p>

## 6. Restrições

### 6.1 Restrição de escopo

<p align="justify"> </p>

### 6.2 Restrição de recursos financeiros

<p align="justify"></p>

### 6.3 Restrição de desenvolvimento e implantação

<p align="justify"> </p>

## 7. Faixas de qualidade

<p align="justify"> O sistema deve ser utilizado de forma eficiente e estável em qualquer dispositivo com suporte o navegador Google Chrome e acesso à internet.</p>

## 8. Outros requisitos do produto

### 8.1 Requisitos de usabilidade

<p align="justify"> A interface do sistema deve ser intuitiva e agradável para que qualquer usuário tenha acesso a todas as funcionalidades de forma fluida, não comprometendo dessa forma a usabilidade do sistema para diversos tipos de usuários.</p>

### 8.2 Requisitos do sistema

<p align="justify"> O <i>software</i> deve ser acessado de forma rápida e segura pelo usuário através do navegador com um conexão com a internet, de preferência de qualidade, e ter um sistema operacional que tenha suporte para o navegador.</p>

### 8.3 Requisitos de desempenho

<p align="justify"> </p>

### 8.4 Requisitos de confiabilidade

<p align="justify"> </p>
