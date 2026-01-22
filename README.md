🚀 DevOps Pipeline com AWS, CI/CD e Observabilidade

Este repositório apresenta um projeto prático de DevOps, focado em processos reais utilizados em ambientes corporativos, indo além de apenas executar código.

O objetivo é demonstrar automação, CI/CD, infraestrutura em cloud, observabilidade e boas práticas DevOps, mesmo sem uma aplicação web tradicional.

🧠 Visão Geral

O projeto implementa um pipeline DevOps completo, capaz de:

Executar automações em Python

Utilizar CI/CD com GitHub Actions e Jenkins

Fazer deploy automatizado em uma instância EC2

Centralizar logs no Amazon CloudWatch

Criar métricas a partir de logs

Gerar alarmes baseados em padrões de erro

Prover observabilidade do ambiente

Tudo isso simulando cenários reais de produção usados por times DevOps.

🏗 Arquitetura Utilizada
☁️ AWS EC2

Instância Linux (Amazon Linux)

Provisionada via Terraform

Responsável pela execução do pipeline e do script Python

Acesso via SSH

🔐 IAM Role

Role associada diretamente à instância EC2

Princípio do menor privilégio

Permissões para:

Envio de logs ao CloudWatch

Criação de métricas

Leitura de metadados da instância

📊 Amazon CloudWatch

Centralização de logs da aplicação

Log Group dedicado (devops-pipeline-logs)

Log Streams por execução

Metric Filters baseados em padrões

Alarmes configurados a partir das métricas

🔁 CI/CD

GitHub Actions para CI

Jenkins para automação e execução no servidor

⚙️ Tecnologias e Ferramentas

Python

AWS EC2

AWS IAM

Amazon CloudWatch

Terraform

GitHub Actions

Jenkins

Linux

Shell Script

🔁 Pipeline CI/CD
Fluxo do pipeline:

Alteração no código local

Push para o GitHub

GitHub Actions:

Executa validações

Garante que o pipeline não falhe desnecessariamente

Jenkins:

Executa automações no servidor

Execução do script Python na EC2

Logs são gerados localmente

Logs enviados automaticamente ao CloudWatch

Métricas são geradas a partir dos logs

Alarmes monitoram falhas no pipeline

🧪 Código Python (Automação)

O script Python simula tarefas comuns de automação em pipelines DevOps.

Funcionalidades implementadas:

Criação automática de diretórios

Limpeza de arquivos temporários

Contagem de arquivos .txt

Regras de CI que não quebram o pipeline

Logs estruturados com timestamp

Escrita de logs em arquivo local

📄 Local do arquivo de log:
/var/log/devops-pipeline.log


Esse arquivo é monitorado pelo CloudWatch Agent.

📊 Observabilidade e Monitoramento
Logs

Logs da aplicação centralizados no CloudWatch

Visualização em tempo quase real

Organização por Log Group e Log Stream

Metric Filters

Filtros criados a partir de padrões nos logs

Exemplo: contagem de erros no pipeline

Alarmes

Alarmes baseados em métricas derivadas dos logs

Avaliação em janelas de tempo (ex: 5 minutos)

Monitoramento visual via console AWS

⚠️ Neste projeto, os alarmes não enviam notificações por e-mail, sendo utilizados apenas para observabilidade.

🧠 Conceitos DevOps Aplicados

CI/CD

Infraestrutura como Código (IaC)

Automação

Observabilidade

Monitoramento baseado em logs

Cloud Computing

Boas práticas DevOps

Pipeline resiliente

📌 Status do Projeto

✅ Pipeline funcional
✅ Deploy automatizado
✅ Logs centralizados
✅ Métricas criadas
✅ Alarmes configurados

🔮 Próximos Passos (Evolução Futura)

Dashboards personalizados no CloudWatch

Notificações via SNS

Monitoramento de CPU, memória e disco

Estratégias de deploy (Blue/Green ou Canary)

Integração com outras ferramentas de observabilidade

👨‍💻 Autor

Bruno Peres
DevOps | Cloud | Automação

📌 LinkedIn: (adicione seu link aqui)
