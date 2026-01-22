# 🚀 DevOps Pipeline com AWS, CI/CD e Observabilidade

Este repositório representa um **projeto prático de DevOps**, focado em **processos reais utilizados em empresas**, indo além de apenas rodar código.

O objetivo é demonstrar **automação, CI/CD, infraestrutura em cloud, observabilidade e boas práticas DevOps**, mesmo sem uma aplicação web tradicional.

---

## 🧠 Visão Geral

O projeto implementa um **pipeline automatizado** que:

- Executa tarefas automatizadas em Python
- Realiza CI/CD via GitHub Actions e Jenkins
- Faz deploy em uma instância EC2 na AWS
- Centraliza logs no CloudWatch
- Cria métricas e alarmes baseados em logs
- Permite observabilidade e monitoramento do ambiente

Tudo isso simulando **cenários reais de produção**.

---

## 🏗 Arquitetura Utilizada

- **AWS EC2**  
  - Instância Linux
  - Criada via **Terraform**
  - Acesso via SSH

- **IAM Role**
  - Permissões mínimas necessárias
  - Envio de logs e métricas ao CloudWatch

- **CloudWatch**
  - Logs centralizados
  - Metric Filters
  - Alarmes baseados em erros

- **CI/CD**
  - GitHub Actions
  - Jenkins

---

## ⚙️ Tecnologias e Ferramentas

- **Python**
- **AWS EC2**
- **AWS IAM**
- **AWS CloudWatch**
- **Terraform**
- **GitHub Actions**
- **Jenkins**
- **Linux**
- **Shell Script**

---

## 🔁 Pipeline CI/CD

### Fluxo do pipeline:

1. Alteração no código
2. Push para o GitHub
3. GitHub Actions:
   - Executa validações
   - Garante que o pipeline não falhe
4. Jenkins:
   - Executa tarefas automatizadas
5. Deploy na EC2
6. Logs gerados localmente
7. Logs enviados automaticamente ao CloudWatch
8. Alarmes disparam caso erros sejam detectados

---

## 🧪 Código Python (Automação)

O script Python realiza:

- Criação de diretórios necessários
- Limpeza de arquivos temporários
- Contagem de arquivos `.txt`
- Geração de logs estruturados com timestamp
- Escrita de logs locais em:
