# Benchmark Indexes - IBOVESPA Web Scraper

## Descrição
Este projeto automatiza a coleta, processamento e análise de dados históricos do índice IBOVESPA, utilizando Selenium para scraping diretamente do site da B3. Ele é projetado para ser modular e extensível, permitindo que novos índices sejam adicionados com facilidade.

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
│   │   ├── IbovWebScrapperB3.py  # Script principal de scraping do IBOVESPA
│   │   ├── TestIbovWebScrapper.py  # Testes para o módulo IBOVESPA
│   │   ├── ibov_config.json  # Configurações específicas do IBOVESPA
│   │   ├── ibov_metadata.json  # Metadados do IBOVESPA
├── notebooks/                # Notebooks para análise e exploração
│   ├── chart_ibov_b3.ipynb   # Gráfico de evolução do IBOVESPA
│   ├── Resumo_dos_Eventos_de_Alta_Volatilidade_no_IBOVESPA.csv
├── utils/                    # Classes utilitárias
│   ├── LoggerUtil.py         # Gerenciamento de logs
│   ├── WebDriverUtil.py      # Configuração do WebDriver
│   ├── SeleniumUtil.py       # Interação com o Selenium
│   ├── DateUtil.py           # Manipulação de datas
├── LICENSE                   # Licença do projeto
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do projeto
```

---

## Funcionalidades
- **Scraping Automatizado**:
  - Coleta de dados históricos diretamente do site da B3.
  - Configuração automatizada do WebDriver com `webdriver_manager`.

- **Transformação e Análise de Dados**:
  - Conversão de tabelas para formatos analisáveis (ETL).
  - Dados tratados e salvos em diferentes níveis (bronze, silver, gold).

- **Exploração com Jupyter Notebooks**:
  - Análises interativas e geração de gráficos para insights rápidos.

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
### **Executando o Scraper do IBOVESPA**
```bash
python indexes/ibov/IbovWebScrapperB3.py
```

### **Análise no Jupyter Notebook**
1. Navegue até o diretório `notebooks`.
2. Abra o notebook de análise no Jupyter:
   ```bash
   jupyter notebook chart_ibov_b3.ipynb
   ```

### **Logs**
Os logs do sistema são gerenciados pelo `LoggerUtil`. Você pode personalizar os níveis e locais de armazenamento no código:
```python
logger = LoggerUtil.get_logger("IBovLogger")
logger.info("Este é um log de exemplo.")
```

---

## Arquitetura do Web Scraper
O projeto segue o padrão **ETL (Extract, Transform, Load)**:
1. **Extract**:
   - O módulo `IbovWebScrapperB3` utiliza Selenium para capturar os dados brutos do site da B3.
2. **Transform**:
   - Os dados capturados são processados, filtrados e organizados em um formato uniforme para análise.
3. **Load**:
   - Os dados processados são salvos no formato CSV em diferentes níveis (bronze, silver, gold).

### Configuração do WebDriver
A configuração do WebDriver é gerenciada pelo `WebDriverUtil`, com suporte para:
- Cache de drivers para evitar downloads desnecessários.
- Logs detalhados para rastreamento de erros.

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
