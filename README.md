# Separador de E-mails por Provedor

Este script Python foi desenvolvido para separar e-mails com base no provedor ao qual pertencem. Ele permite a leitura de uma lista de e-mails (.txt) e os separa em arquivos de texto distintos para cada provedor. Além disso, oferece a capacidade de tratar a interrupção do usuário (Ctrl+C) durante a execução.

## Funcionalidades

- **Separação de E-mails por Provedor:**
   - O script analisa uma lista de e-mails e os separa em arquivos de texto para provedores específicos.

- **Tratamento de Interrupção do Usuário:**
   - Ao pressionar Ctrl+C durante a execução, o script pergunta se o usuário deseja realmente encerrar o programa.

## Como Usar

### Requisitos

- Python 3.x instalado.

### Execução

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/separador-emails-provedor.git
    ```

2. Navegue até o diretório do script:

    ```bash
    cd separador-emails-provedor
    ```

3. Execute o script:

    ```bash
    python separador_emails_provedor.py
    ```

4. Siga as instruções interativas para fornecer o caminho da lista de e-mails (.txt).
5. Os e-mails serão separados por provedor, e os resultados serão armazenados em arquivos de texto específicos.

### Exemplo

```bash
$ python separador_emails_provedor.py
Digite o caminho da lista de e-mails (.txt): -> caminho/para/sua/lista.txt

+1   ->   exemplo@gmail.com
+1   ->   usuario@yahoo.com
+1   ->   contato@hotmail.com
...

Processo Finalizado! Pressione ENTER Para Continuar!
```
### Tratamento de Interrupção

Ao pressionar Ctrl+C, o script perguntará se deseja realmente encerrar o programa.

Este script é útil para organizar e-mails por provedor, facilitando a análise e gerenciamento de dados. Certifique-se de respeitar a privacidade e conformidade ao usar este script em dados sensíveis.
