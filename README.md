# 🚀 DevOps Pipeline com AWS, CI/CD e Observabilidade

Este repositório apresenta um projeto prático de **DevOps**, focado em processos reais utilizados em ambientes corporativos, indo além da simples execução de código. O objetivo é demonstrar automação, infraestrutura em cloud e monitoramento profissional.

## 🧠 Visão Geral

O projeto implementa um pipeline completo, capaz de:
* **Executar automações** em Python.
* **Utilizar CI/CD** híbrido com GitHub Actions e Jenkins.
* **Realizar deploy automatizado** em instâncias AWS EC2.
* **Centralizar logs** no Amazon CloudWatch.
* **Prover observabilidade** através de métricas e alarmes baseados em logs.

---

## 🏗 Arquitetura Utilizada

### ☁️ AWS EC2
* Instância Linux (Amazon Linux 2023) provisionada via **Terraform**.
* Responsável pela execução do pipeline e do script Python.
* Acesso seguro via SSH.

### 🔐 IAM Role
* Role associada diretamente à instância (sem chaves fixas no código).
* **Princípio do menor privilégio**, permitindo apenas envio de logs e criação de métricas no CloudWatch.

### 📊 Amazon CloudWatch
* **Log Group:** `devops-pipeline-logs`.
* **Metric Filters:** Filtros para identificar padrões de erro nos logs.
* **Alarmes:** Monitoramento ativo da saúde do pipeline.

### 🔁 CI/CD
* **GitHub Actions:** Responsável pelo Continuous Integration (CI) e validações iniciais.
* **Jenkins:** Orquestrador para automação e execução direta no servidor (CD).

---

## ⚙️ Tecnologias e Ferramentas

| Categoria | Ferramentas |
| :--- | :--- |
| **Linguagem** | Python, Shell Script |
| **Cloud** | AWS (EC2, IAM, CloudWatch) |
| **IaC** | Terraform |
| **CI/CD** | GitHub Actions, Jenkins |
| **OS** | Linux (Amazon Linux) |

---

## 🔄 Fluxo do Pipeline

1.  **Commit & Push:** Alteração no código local enviada ao GitHub.
2.  **CI (GitHub Actions):** Executa linting e validações de segurança.
3.  **CD (Jenkins):** Dispara a automação dentro da instância EC2.
4.  **Execução:** O script Python limpa temporários, organiza diretórios e gera logs.
5.  **Observabilidade:** O CloudWatch Agent coleta os logs em `/var/log/devops-pipeline.log` e atualiza as métricas/alarmes.

---

## 🧪 Automação (Python)

O script simula tarefas críticas de infraestrutura:
* Criação dinâmica de diretórios de trabalho.
* Limpeza de arquivos temporários e manutenção de ambiente.
* Logs estruturados com *timestamp* para rastreabilidade.

> 📄 **Local do log na EC2:** `/var/log/devops-pipeline.log`

---

## 📊 Observabilidade e Monitoramento

* **Logs em Tempo Real:** Visualização centralizada no console AWS.
* **Metric Filters:** Transformação de dados de texto (logs) em dados numéricos.
* **Alarmes:** Configurados para monitorar falhas em janelas de 5 minutos.
* *Nota: Os alarmes são visuais para fins de estudo de observabilidade.*

---

## 🧠 Conceitos Aplicados

* **Infrastructure as Code (IaC)**
* **Pipeline Resiliente**
* **Monitoramento Baseado em Logs**
* **Segurança em Cloud (IAM Roles)**

---

## 📌 Status do Projeto

- [x] Pipeline funcional
- [x] Deploy automatizado
- [x] Logs centralizados no CloudWatch
- [x] Métricas e Alarmes configurados

## 🔮 Próximos Passos (Evolução)

* [ ] Dashboards personalizados no CloudWatch ServiceLens.
* [ ] Notificações via Amazon SNS (E-mail/Slack).
* [ ] Monitoramento de hardware (CPU/Memória).
* [ ] Estratégias de Deploy Blue/Green.

---

## 👨‍💻 Autor

**Bruno Peres**
*DevOps | Cloud | Automação*

* **LinkedIn:** https://www.linkedin.com/in/brunoperes9612/
* **Email:** brunooperesc@gmail.com
