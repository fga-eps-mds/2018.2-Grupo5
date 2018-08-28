---
title: Documento de arquitetura
author: Bruno
layout: post
categories: DEV
---

## Histórico de Revisões

|Data|Versão|Descrição|Autor|
| --- | --- | --- | --- |
|28/08/2018|0.1|Criação da estrutura do documento|Ingrid Soares|
|28/08/2018|0.1|Adição de tópicos|Ingrid Soares|

# Documento de Arquitetura

Sumário
----------------

* 1 .  [Introdução](#1-introdução)
    * 1.1. [Finalidade](#11-finalidade)
    * 1.2. [Escopo](#12-escopo)
    * 1.3 [Definições, acrônimos e abreviações](#13-definições)
    * 1.4. [Referências](#14-referências)
    * 1.5. [Visão Geral](#15-visão)
    
* 2 .  [Representação da Arquitetura](#2-representação)
   * 2.1. [Representação do padrão de Arquitetura MVT](#21-representação)
   * 2.2. [Representação da Arquitetura de Microserviços](#21-representação)


## 1. Introdução

### 1.1 Finalidade

Este documento mostra uma visão geral sobre a arquitetura e ferramentas utilizadas no projeto GamesBI.

### 1.2 Escopo

Neste documento serão retratados os modelos arquiteturais implementados, descrição e utilização de frameworks 
que compõe o projeto GamesBI, plataforma de business intelligence com temática de jogos digitais. Exploramos 
de maneira detalhada o funcionamento e a visão arquitetural do projeto.

### 1.3 Definições, acrônimos e abreviações

MVT - Model, View, Template

### 1.4 Referências

### 1.5 Visão Geral

O presente documento faz o detalhamento e descrição de características da arquitetura escolhidas pela equipe.
Estaremos descrevento o padrão arquitetural MVT, arquitetura de Microserviços e APIs Rest

## 2. Representação da Arquitetura

A arquitetura do projeto possuirá ambientes diferentes: API's REST, por debaixo do framework MVT Django, assim como o ambiente WEB de interação com usuário. Juntando todos os ambientes e coordenando-os, formamos assim uma arquitetura de Microserviços.

### 2.1 Padrão de Arquitetura MVT

### 2.2 Arquitetura de Microserviços