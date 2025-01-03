# Benchmark Indexes - Web Scraper Framework

## Descrição
Este projeto é um framework modular para a captura, processamento e análise de dados históricos de índices de mercado, como IBOVESPA, CDI, entre outros. Ele é projetado para ser flexível, permitindo a adição de novos índices e fontes de dados com facilidade.

---

## Estrutura do Projeto
```plaintext
benchmark_indexes/
├── data/                     # Diretório para armazenamento de dados
│   ├── bronze/               # Dados brutos extraídos
│   ├── silver/               # Dados intermediários
│   ├── gold/                 # Dados tratados
├── indexes/                  # Módulos de captura de índices
│   ├── ibov/                 # Módulo para o índice IBOVESPA
│   ├── cdi/                  # Módulo para o índice CDI
│   ├── index_config.json     # Configurações globais de índices
├── notebooks/                # Notebooks para análise e exploração
│   ├── análise_indices.ipynb # Análises gerais dos índices
├── LICENSE                   # Licença do projeto
├── README.md                 # Documentação do projeto
```

---

## Funcionalidades
- **Scraping Modular**:
  - Captura de dados de múltiplos índices de mercado (IBOV, CDI, etc.).
  - Configuração automatizada do WebDriver com `webdriver_manager`.

- **Transformação e Análise de Dados**:
  - Processamento de dados para análise (ETL).
  - Estrutura flexível para armazenamento em níveis (bronze, silver, gold).

- **Exploração com Jupyter Notebooks**:
  - Notebooks para análise interativa e geração de insights.

---

## Requisitos
- **Python 3.8+**
- **Bibliotecas**:
  - `selenium`
  - `webdriver_manager`
  - `pandas`
  - `numpy`
  - `matplotlib`

Instale as dependências com:
```bash
pip install -r requirements.txt
```

---

## Uso
### **Executando o Scraper para um Índice**
1. Configure o módulo correspondente ao índice desejado (ex.: `ibov/ibov_config.json`).
2. Execute o scraper:
   ```bash
   python indexes/ibov/IbovWebScrapperB3.py
   ```

### **Análise no Jupyter Notebook**
1. Navegue até o diretório `notebooks`.
2. Abra o notebook de análise no Jupyter:
   ```bash
   jupyter notebook análise_indices.ipynb
   ```

### **Logs**
Os logs do sistema são gerenciados pelo `LoggerUtil`. Você pode personalizar os níveis e locais de armazenamento no código:
```python
logger = LoggerUtil.get_logger("IndexLogger")
logger.info("Este é um log de exemplo.")
```

---

## Arquitetura do Framework
O projeto segue o padrão **ETL (Extract, Transform, Load)**:
1. **Extract**:
   - Captura de dados brutos das fontes configuradas (web scraping, APIs, etc.).
2. **Transform**:
   - Processamento e padronização dos dados para análise.
3. **Load**:
   - Armazenamento dos dados tratados em níveis específicos (bronze, silver, gold).

### Configuração do WebDriver
A configuração do WebDriver é gerenciada pelo `WebDriverUtil`, com suporte para:
- Cache de drivers para evitar downloads desnecessários.
- Logs detalhados para rastreamento de erros.

### Adicionando um Novo Índice
1. Crie um diretório para o índice em `indexes/`.
2. Adicione um arquivo de configuração JSON para o índice:
   ```json
   {
       "module": "CdiApiWrapper",
       "description": "Módulo para captura de dados do CDI via API do BACEN.",
       "version": "1.0.0",
       "author": "Seu Nome",
       "indexData": {
           "indexName": "CDI",
           "indexSource": "BACEN",
           "indexSourceReference": "https://bacen.gov.br",
           "indexDocumentation": "https://bacen.gov.br/docs"
       }
   }
   ```
3. Implemente o scraper utilizando as classes utilitárias disponíveis.

---

## Contribuindo
Contribuições são bem-vindas! Por favor:
1. Faça um fork deste repositório.
2. Crie um branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas alterações via pull request.

---

## Licença
Este projeto é licenciado sob a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE).
