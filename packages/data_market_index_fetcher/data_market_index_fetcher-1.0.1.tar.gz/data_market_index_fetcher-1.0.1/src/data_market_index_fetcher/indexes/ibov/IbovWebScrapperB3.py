# Bibliotecas Nativas
import pandas as pd
import numpy as np
import os
import datetime
from typing import Optional

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Bibliotecas do Projeto
from data_market_index_fetcher.indexes.ibov.utils.DateUtil import DateUtil
from data_market_index_fetcher.indexes.ibov.utils.WebDriverUtil import WebDriverUtil
from data_market_index_fetcher.indexes.ibov.utils.LoggerUtil import LoggerUtil
from data_market_index_fetcher.indexes.ibov.utils.SeleniumUtil import SelenimUtil

class IBovWebScrapperB3:

  # Configurar o logger para esta classe usando LoggerUtil
  logger = LoggerUtil.get_logger("IBovWebScrapper")

  # Configurações
  data_path = './data'
  data_file = data_path + '/ibovespa_diario.csv'
  url_webscraping='https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-estatisticas-historicas.htm'
  iframe_webscrapting='bvmf_iframe'

  def __init__(self):
      """
      Inicializa o WebScrapper do Ibovespa.
      """
      self.data=pd.DataFrame()
      self.driver=None
      self.last_date=None

      self.logger.info("Inicializando o WebScrapper do Ibovespa...")
      self.driver=WebDriverUtil.obter_driver()

      # Carrega os dados existentes
      self.logger.info("Carregando dados Existentes do Ibovespa...")      
      self.load_existing_data()

      self.logger.info("Dados Carregados...")
      self.logger.info(self.data.head())
            
      if not self.data.empty:
        # Carrega a ultima data do arquivo
        self.last_date=self.data['date'].iloc[-1]

  def __del__(self):
      if self.driver != None:
          self.driver.quit()
          self.logger.info('Driver encerrado on destruct')
  
  # Candidate to ETL.extract method
  def extrair_dados_ibovespa(self, semestre):
    """
    Extrai os dados da tabela do Ibovespa para o semestre especificado.

    Args:
        semestre (str): '1' para 1º semestre ou '2' para 2º semestre.
        driver (webdriver): Instância do Selenium WebDriver.

    Returns:
        pd.DataFrame: Dados extraídos no formato original.
    """
    try:

        # Mudar para o iframe onde os dados estão
        if not SelenimUtil.is_in_iframe(self.driver,"bvmf_iframe"):
            SelenimUtil.select_iframe(self.driver, "bvmf_iframe")

        # Seleciona o semestre no dropdown
        self.logger.info(f"Selecionando semestre {semestre}...")
        select = Select(self.driver.find_element(By.ID, "semester"))
        select.select_by_value(semestre)
        #time.sleep(3)

        # Aguarda a tabela carregar
        tabela_xpath = "/html/body/app-root/app-daily-evolution/div/div/div[1]/form/div[2]/div/table"
        tabela = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tabela_xpath))
        )

        # Extrai os dados da tabela
        linhas = tabela.find_elements(By.TAG_NAME, "tr")
        dados = []
        for linha in linhas:
            colunas = linha.find_elements(By.TAG_NAME, "td")
            if colunas:
                dados.append([coluna.text for coluna in colunas])

        # Voltar ao contexto principal (iframe original)
        self.driver.switch_to.default_content()
        
        # Retorna os dados como DataFrame
        if semestre=='1':
            colunas = ["Dia", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
        if semestre=='2':
            colunas = ["Dia", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

        return pd.DataFrame(dados, columns=colunas)

    except Exception as e:
        self.logger.error(f"Erro ao extrair os dados do semestre {semestre}: {e}", exc_info=True)
        return pd.DataFrame()

  # Candidate to ETL.transform method
  def transformar_dados(self, ano, dados):
      """
      Converte a tabela de dias e meses em formato de linhas únicas, com colunas Data e Valor.

      Args:
          dados (pd.DataFrame): DataFrame com colunas representando os meses e os dias como índice.

      Returns:
          pd.DataFrame: DataFrame transformado com colunas Data e Valor.
      """
      try:
          registros = []
          meses_map = {
              "Jan": "01", "Fev": "02", "Mar": "03", "Abr": "04",
              "Mai": "05", "Jun": "06", "Jul": "07", "Ago": "08",
              "Set": "09", "Out": "10", "Nov": "11", "Dez": "12"
          }

          for _, row in dados.iterrows():
              dia = row["Dia"]
              for mes, valor in row.items():
                  # cabeçalhos e rodapés ['Dia', 'MÁXIMO', 'MÍNIMO']
                  ignorar=['Dia', 'MÁXIMO', 'MÍNIMO']
                  if mes not in ignorar and dia.isdigit(): # Ignora colunas vazias, de cabeçalho, rodapé e meses não numéricos
                      mes_num = meses_map.get(mes, None)
                      if mes_num:
                          data = f"{ano}-{mes_num.zfill(2)}-{str(dia).zfill(2)}"
                          valor=str(valor)
                          if valor.strip() !='':
                              valor=valor.replace('.','')
                              valor=valor.replace(',','.')
                              #valor=float(valor)
                          if DateUtil.is_valid_date(data):    
                              registros.append({"date": data, "value": valor})

          df_registros=pd.DataFrame(registros)
                  
          # Ordenar o DataFrame pela coluna 'Data'
          df_registros = df_registros.sort_values(by="date")

          self.logger.debug('Estrutura do Dataframe')
          self.logger.debug(df_registros.info())

          # Preencher os valores ausentes: primeiro com forward fill, depois com backward fill
          # Isso é necessário caso o primeiro valor esteja em branco
          df_registros["value"] = df_registros["value"].replace('', np.nan)
          df_registros["value"] = df_registros["value"].ffill()
          df_registros["value"] = df_registros["value"].bfill()

          # Converte a coluna para numero decimal
          df_registros["value"] = pd.to_numeric(df_registros["value"], errors="coerce").round(2)

                
          return df_registros
      
      except Exception as e:
          self.logger.error(f"Erro ao transformar os dados: {e}", exc_info=True)
          # raise(e)
          return pd.DataFrame()

  def obter_conteudo_pagina_ibov(self):
      try:
          # Acessa o site
          #url = "https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-estatisticas-historicas.htm"
          
          self.logger.info("Acessando o site da B3...")
          self.driver.get(self.url_webscraping)
      except Exception as e:
          self.logger.error(f"Erro ao obter o conteudo da pagina: {e}", exc_info=True)

  def selecionar_ano(self, ano):
      """
      Seleciona um ano no dropdown selectYear.

      Args:
          driver (webdriver): Instância do Selenium WebDriver.
          ano (str): Ano a ser selecionado no dropdown.

      Returns:
          bool: True se o ano foi selecionado com sucesso, False caso contrário.
      """
      try:

          if not SelenimUtil.is_in_iframe(self.driver, self.iframe_webscrapting):
              # Mudar para o iframe onde os dados estão
              SelenimUtil.select_iframe(self.driver, self.iframe_webscrapting)
              
          # Localizar o elemento <select> pelo ID
          select_element = self.driver.find_element(By.ID, "selectYear")
          
          # Criar o objeto Select
          select = Select(select_element)
          
          # Selecionar o ano pelo valor
          select.select_by_value(ano)
          self.logger.info(f"Ano {ano} selecionado com sucesso.")
          return True
      except NoSuchElementException:
          self.logger.info(f"Ano {ano} não encontrado no dropdown selectYear.")
          return False
      except Exception as e:
          self.logger.error(f"Erro ao selecionar o ano {ano}: {e}", exc_info=True)
          return False

  def get_all_years(self):

      if not SelenimUtil.is_in_iframe(self.driver, self.iframe_webscrapting):
          SelenimUtil.select_iframe(self.driver, self.iframe_webscrapting)

      # Localizar o elemento <select> pelo ID
      select_element = self.driver.find_element(By.ID, "selectYear")

      # Criar um objeto Select para interagir com o <select>
      select = Select(select_element)

      # Obter todos os valores disponíveis nas opções
      anos_disponiveis = [option.get_attribute("value") for option in select.options]

      # Converter para inteiros e ordenar
      anos_ordenados = sorted(anos_disponiveis, key=int)

      return anos_ordenados

  # Candidate to ETL.load method
  def obter_ibov_b3(self, ano=None, pagina_ibov_selecionada=False):
      #is_external_driver=(driver!=None)

      # Configura o driver
      if self.driver==None:
          self.driver = WebDriverUtil.obter_driver()
      
      try:
          # Obtem o conteudo do site
          if not pagina_ibov_selecionada:
              self.obter_conteudo_pagina_ibov()
          
          # Selecionar Ano, se especificado
          if ano != None:
              self.logger.info(f"Selecionando o ano {ano}...")
              self.selecionar_ano(ano)
          else:
              ano=datetime.now().year 

          # Extrai os dados dos dois semestres
          dados_1_semestre = self.extrair_dados_ibovespa("1")
          self.logger.debug('Dados do Primeiro Semestre')
          self.logger.debug(dados_1_semestre.head())
          dados_transformados_semestre_1=self.transformar_dados(ano, dados_1_semestre)
          #dados_transformados_semestre_1.to_csv('dados_transformados_semestre_1.csv', index=False)

          dados_2_semestre = self.extrair_dados_ibovespa("2")
          self.logger.debug('Dados do Segundo Semestre')
          self.logger.debug(dados_2_semestre.head())
          dados_transformados_semestre_2=self.transformar_dados(ano, dados_2_semestre)
          #dados_transformados_semestre_2.to_csv('dados_transformados_semestre_2.csv', index=False)
        
          # Combina os dados dos dois semestres
          dados_completos = pd.concat([dados_transformados_semestre_1, dados_transformados_semestre_2], ignore_index=True)
          
          # ETL Load
          if os.path.exists(self.data_file):
              dados_existente=pd.read_csv(self.data_file, 
                                          parse_dates=['date'],
                                          dtype={'value': 'float64'})
              dados_existente['date'] = pd.to_datetime(dados_existente['date'])  # Convert strings to timestamps

              dados_completos=pd.concat([dados_completos, dados_existente], ignore_index=True)
              # Ordenar o DataFrame pela coluna 'Data
              
              #dados_completos = dados_completos.sort_values("date", ascending=True)
              #dados_completos = dados_completos.sort_values()
              #pd.to_datetime(dados_completos['date'], format="%Y-%m-%d").sort_values()
              #dados_completos = dados_completos.drop_duplicates(subset="date")
    
              dados_completos['date'] = pd.to_datetime(dados_completos['date'], format='%Y-%m-%d', errors='coerce')
              dados_completos = dados_completos.dropna(subset=['date'])  # Remove linhas com valores nulos em 'date'
              dados_completos = dados_completos.sort_values("date")
              
          # Obter a data atual e formatá-la no formato yyyy-MM-dd
          data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
          self.logger.info(f"Data atual formatada: {data_atual}")

          # Filtrar as datas até a data atual
          dados_completos["date"] = pd.to_datetime(dados_completos["date"])  # Converter para datetime
          dados_completos = dados_completos[dados_completos["date"] <= pd.to_datetime(data_atual)]

          # Exibe os dados
          self.logger.info("Dados transformados com sucesso.")
          self.logger.debug("Dados obtidos")
          self.logger.debug(dados_completos.head())

          # Salva os dados em CSV
          dados_completos.to_csv(self.data_file, index=False)
          self.logger.info(f"Dados salvos em {self.data_file}.")

          # Reload and Cache Data in instance
          self.data=dados_completos
          self.last_date=self.data['date'].iloc[-1]

      except Exception as e:
          self.logger.error(f"Erro durante a execução: {e}", exc_info=True)
  
  def load_existing_data(self, reload: Optional[bool] = False):
      if reload:        
        # TODO: Remove File to Recreate It and backup it as fallback
        if os.path.exists(self.data_file):
            os.remove(self.data_file)

        self.obter_conteudo_pagina_ibov()
        anos_disponiveis=self.get_all_years()
        self.logger.debug(anos_disponiveis)
                
        for ano in anos_disponiveis:
            self.obter_ibov_b3(ano=ano, pagina_ibov_selecionada=True)

        self.last_date=self.data['date'].iloc[-1]

        return self.data
      elif os.path.exists(self.data_file):
          self.data=pd.read_csv(self.data_file, 
                                parse_dates=['date'],
                                dtype={'value': 'float64'})
      
  def fetch_data(self, start_date: str, end_date: str) -> pd.DataFrame:
      try:
        # Valida e converte as datas
        if not isinstance(start_date, str) or not isinstance(end_date, str):
            raise TypeError("start_date and end_date must be strings")
        
        if DateUtil.is_valid_date(start_date):
          start_date=pd.to_datetime(start_date, format="%Y-%m-%d")
        else:
            raise ValueError('Data Inicial invalida')
            
        if DateUtil.is_valid_date(end_date):
            end_date=pd.to_datetime(end_date, format="%Y-%m-%d")
        else:
            raise ValueError('Data Final invalida')


        # Carrega / Atualiza os dados caso a data final seja maior que 
        # a ultima data carregada
        data_atual = datetime.datetime.now()

        # Ajustar a data final se ela for uma data futura
        if end_date > data_atual:
            self.logger.info(f"A data final {end_date} é futura. Ajustando para hoje ({data_atual}).")
            end_date = data_atual

        # Verifica se self.data está vazio
        if self.data.empty:
          self.logger.warning(f"{self.data} está vazio. Carregando dados iniciais...")
          # Lógica para carregar os dados iniciais
          self.load_existing_data(reload=True)
        
        missing_dates = pd.date_range(start=start_date, end=end_date).difference(self.data['date'])

        if missing_dates.empty:
            self.logger.info("Todas as datas solicitadas estão disponíveis no arquivo.")
        else:
            self.logger.info(f"Datas ausentes: {missing_dates}. Iniciando scraping...")
            for year in missing_dates.year.unique():
                self.obter_ibov_b3(ano=str(year), pagina_ibov_selecionada=False)
        
        # Filtrar os dados pelo intervalo de datas
        df_filtrado = self.data[(self.data['date'] >= pd.to_datetime(start_date)) & (self.data['date'] <= pd.to_datetime(end_date))]
        return df_filtrado
      
      except Exception as e:
          self.logger.exception('Erro ao obter os dados do ibov', e)    