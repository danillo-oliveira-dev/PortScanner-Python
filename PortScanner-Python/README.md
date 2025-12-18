# TCP Port Scanner (Python)

Este é um script de automação de segurança desenvolvido para estudos de Red Team e redes de computadores.

O objetivo foi criar uma ferramenta de linha de comando (CLI) leve para realizar a fase de _Reconnaissance_ (reconhecimento), identificando portas abertas em um alvo específico através de conexões TCP.

## Tecnologias e Conceitos da Ferramenta

- **Linguagem:** Python 3
- **Biblioteca:** `socket` (Nativa)
- **Conceitos aplicados:**
  - Handshake TCP e verificação de conectividade.
  - Resolução de DNS (Domain Name System).
  - Tratamento de exceções e erros de rede.

## Como rodar o projeto

### Pré-requisitos

Você precisa ter o [Python](https://www.python.org/) instalado em sua máquina.

### Executando

1. Clone este repositório ou baixe o arquivo.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python scanner.py
```
4. Insira o IP ou domínio (ex: scanme.nmap.org ou um IP local) quando solicitado.

⚠️ Nota de Responsabilidade:
Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes em ambientes autorizados. O uso de scanners de porta em redes de terceiros sem consentimento é ilegal. Eu não me responsabilizo por suas ações.

Projeto desenvolvido por [Danillo] - Estudante de Cibersegurança e Análise e Desenvolvimento de Sistemas

