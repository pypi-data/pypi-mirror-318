import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from data_market_index_fetcher.indexes.ibov.utils.LoggerUtil import LoggerUtil  # Importar o LoggerUtil

class WebDriverUtil:
    """
    Classe utilitária para configurar e gerenciar instâncias do Selenium WebDriver.
    """

    # Configurar o logger para esta classe usando LoggerUtil
    logger = LoggerUtil.get_logger("WebDriverUtil")
    logger_selenium = logging.getLogger('selenium')

    @staticmethod
    def configurar_driver_para_chrome(driver_path: str = "./chromedriver_cache") -> SeleniumWebDriver:
        """
        Configura o Selenium WebDriver com Chrome e verifica se o ChromeDriver já está baixado.
        Caso não esteja, faz o download.

        Args:
            driver_path (str): Caminho para o ChromeDriver já baixado. Se None, baixa automaticamente.

        Returns:
            SeleniumWebDriver: Instância configurada do WebDriver.
        """
    
        WebDriverUtil.logger.info("Iniciando configuração do Chrome WebDriver.")

        # Configurar opções do Chrome
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Executa o navegador sem interface gráfica
        options.add_argument("--no-sandbox")  # Desativa o sandbox
        options.add_argument("--disable-dev-shm-usage")  # Resolve problemas de memória limitada
        options.add_argument("--disable-gpu")  # Necessário para ambientes headless
        options.add_argument("--disable-extensions")  # Desativa extensões
        options.add_argument("--disable-notifications")  # Bloqueia notificações push
        options.add_argument("--disable-application-cache")  # Desativa cache de aplicativos
        options.add_argument("--disk-cache-size=0")  # Define cache de disco como zero
        options.add_argument("--disable-blink-features=AutomationControlled")  # Remove sinais de automação
        options.add_argument('--ignore-certificate-errors')  # Ignora erros de certificado SSL
        options.add_argument("--disable-dev-tools")  # Desativa o DevTools Protocol
        
        # Configurar um user-agent realista
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        options.add_argument(f"user-agent={user_agent}")

        try:
            # Configurar o local do cache para o ChromeDriver
            os.environ["WDM_LOCAL"] = driver_path

            # Verifica qual a versão que será baixada para validar se o driver já esta no cache
            driver_manager = ChromeDriverManager()
            version_to_download = driver_manager.driver.get_driver_version_to_download()
           
            # Verificar se o driver já existe no cache
            driver_path=r'C:\Users\flavio.lopes\.wdm'
            driver_version_path = os.path.join(driver_path, "drivers", "chromedriver", "win64", version_to_download)
            WebDriverUtil.logger.info(f'Caminho do Driver para validação {driver_version_path}')
            if os.path.exists(driver_version_path):
                WebDriverUtil.logger.info(f"Driver da versão {version_to_download} já está presente em: {driver_version_path}")
            else:
                WebDriverUtil.logger.info(f"Driver da versão {version_to_download} não encontrado. Realizando o download...")

            
            # Configurar o caminho do ChromeDriver ou baixar automaticamente
            driver_version_path=os.path.join(driver_version_path, 'chromedriver-win32', 'chromedriver.exe')
            if driver_version_path and os.path.exists(driver_version_path):
                WebDriverUtil.logger.info(f"Usando ChromeDriver existente em: {driver_version_path}")
                service = Service(driver_version_path)
            else:
                WebDriverUtil.logger.info("ChromeDriver não encontrado. Baixando novo driver...")
                service = Service(ChromeDriverManager().install())

            # Criar e retornar a instância do WebDriver
            driver = webdriver.Chrome(service=service, options=options)
            WebDriverUtil.logger.info("Chrome WebDriver configurado com sucesso.")
            return driver

        except Exception as e:
            WebDriverUtil.logger.error(f"Erro ao configurar o Chrome WebDriver: {e}")
            raise RuntimeError("Não foi possível configurar o WebDriver.") from e

    @staticmethod
    def obter_driver(caminho_chromedriver: str = "./chromedriver_cache") -> SeleniumWebDriver:
        """
        Obtém uma instância do WebDriver para Chrome.

        Args:
            caminho_chromedriver (str): Caminho opcional para o ChromeDriver já baixado.

        Returns:
            SeleniumWebDriver: Instância do WebDriver configurada.
        """
        try:
            WebDriverUtil.logger.info("Tentando obter o WebDriver para Chrome.")
            driver = WebDriverUtil.configurar_driver_para_chrome(driver_path=caminho_chromedriver)
            WebDriverUtil.logger.info("WebDriver obtido com sucesso.")
            return driver
        except Exception as e:
            WebDriverUtil.logger.error(f"Erro ao obter o WebDriver: {e}")
            raise RuntimeError("Erro ao obter o WebDriver.") from e
