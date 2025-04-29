# Brochure Generator

O **Brochure Generator** é uma aplicação Python que utiliza a API da OpenAI para gerar brochuras personalizadas para empresas com base no conteúdo de seus sites. Ele analisa a página inicial e links relevantes, como "Sobre", "Carreiras" e outros, para criar um documento em Markdown que pode ser usado para atrair clientes, investidores e novos talentos.

## Funcionalidades

- **Análise de Sites**: Extrai o título, conteúdo textual e links de uma página da web.
- **Filtragem de Links Relevantes**: Identifica links importantes para a criação de brochuras, como páginas de "Sobre" e "Carreiras".
- **Geração de Brochuras**: Cria um arquivo `brochure.md` com informações detalhadas sobre a empresa.
- **Exibição no Terminal**: Mostra a brochura gerada no terminal com formatação Markdown.

## Pré-requisitos

- Python 3.8 ou superior
- Uma chave de API da OpenAI configurada no arquivo `.env`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/brochure-generator.git
   cd brochure-generator
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure a chave da API da OpenAI:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione a seguinte linha:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Uso

1. Execute o script principal:
   ```bash
   python main.py
   ```

2. Insira a URL da página inicial da empresa e o nome da empresa quando solicitado.

3. O arquivo `brochure.md` será gerado com a brochura da empresa.

4. A brochura também será exibida no terminal com formatação Markdown.

## Exemplo de Saída

Um exemplo de brochura gerada pode ser encontrado no arquivo `brochure.md`. Aqui está um trecho:

```markdown
# Nome da Empresa

## Sobre Nós
Texto extraído da página "Sobre".

## Carreiras
Texto extraído da página "Carreiras".

## Clientes
Texto extraído da página inicial.

## Licença

Este projeto está licenciado sob a MIT License.

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: `seu-email@exemplo.com`.