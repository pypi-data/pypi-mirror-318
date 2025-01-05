from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from data_market_index_fetcher.indexes.ibov.utils.LoggerUtil import LoggerUtil # Importar a classe utilitária de log

class SelenimUtil:
    """
    Classe utilitária para manipulação de iframes e interações básicas com o Selenium WebDriver.
    """

    # Configurar o logger usando o LoggerUtil
    logger = LoggerUtil.get_logger("Selenim")

    @staticmethod
    def is_in_iframe(driver: WebDriver, iframe_id: str) -> bool:
        """
        Verifica se o driver está atualmente em um iframe específico.

        Args:
            driver (WebDriver): Instância do Selenium WebDriver.
            iframe_id (str): ID do iframe a ser verificado.

        Returns:
            bool: True se o driver estiver no iframe especificado, False caso contrário.
        """
        try:
            current_iframe_id = driver.execute_script(
                "return window.frameElement ? window.frameElement.id : null;"
            )
            SelenimUtil.logger.info(f"Driver está no iframe com ID '{current_iframe_id}'.")
            return current_iframe_id == iframe_id
        except Exception as e:
            SelenimUtil.logger.error(f"Erro ao verificar o iframe: {e}")
            return False

    @staticmethod
    def select_iframe(driver: WebDriver, iframe_id: str) -> bool:
        """
        Seleciona um iframe específico pelo ID. Antes de selecionar, volta ao contexto principal.

        Args:
            driver (WebDriver): Instância do Selenium WebDriver.
            iframe_id (str): ID do iframe a ser selecionado.

        Returns:
            bool: True se o iframe foi selecionado com sucesso, False caso contrário.
        """
        try:
            # Voltar ao contexto principal
            driver.switch_to.default_content()
            SelenimUtil.logger.info("Retornado ao contexto principal.")

            # Verificar se já está no iframe desejado
            if not SelenimUtil.is_in_iframe(driver, iframe_id):
                SelenimUtil.logger.info(f"Tentando acessar o iframe com ID '{iframe_id}'...")
                iframe = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, iframe_id))
                )
                driver.switch_to.frame(iframe)
                SelenimUtil.logger.info(f"Iframe com ID '{iframe_id}' selecionado com sucesso.")
                return True
            else:
                SelenimUtil.logger.info(f"O driver já está no iframe com ID '{iframe_id}'.")
                return True
        except TimeoutException:
            SelenimUtil.logger.error(f"O iframe com ID '{iframe_id}' não foi encontrado dentro do tempo limite.")
        except NoSuchElementException:
            SelenimUtil.logger.error(f"O elemento do iframe com ID '{iframe_id}' não existe.")
        except Exception as e:
            SelenimUtil.logger.error(f"Erro ao selecionar o iframe com ID '{iframe_id}': {e}")
        return False
