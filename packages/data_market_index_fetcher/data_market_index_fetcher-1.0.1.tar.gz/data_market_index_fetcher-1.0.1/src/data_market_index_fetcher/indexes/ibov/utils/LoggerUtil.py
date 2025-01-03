import logging
from typing import Optional


class LoggerUtil:
    """
    Classe utilitária para configurar e gerenciar loggers.

    Permite criar loggers configurados com saída para console e/ou arquivos.
    """

    @staticmethod
    def get_logger(name: str,
                   level: int = logging.INFO,
                   log_file: Optional[str] = None) -> logging.Logger:
        """
        Cria e retorna um logger configurado.

        Args:
            name (str): Nome do logger (geralmente o nome do módulo ou classe).
            level (int): Nível de log (ex: logging.INFO, logging.DEBUG, logging.ERROR).
            log_file (Optional[str]): Caminho para salvar o log em um arquivo. Se None, apenas exibe no console.

        Returns:
            logging.Logger: Instância configurada do logger.
        """

        try:
            # Criar o logger
            logger = logging.getLogger(name)
            logger.setLevel(level)

            # Evitar múltiplos handlers duplicados
            if not logger.handlers:
                # Formato do log
                formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s")

                # Manipulador de console
                console_handler = logging.StreamHandler()
                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)

                # Manipulador de arquivo, se necessário
                if log_file:
                    file_handler = logging.FileHandler(log_file)
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)

                # Informar que o logger foi configurado
                logger.info(f"Logger '{name}' configurado com sucesso. Nível: {logging.getLevelName(level)}")
                if log_file:
                    logger.info(f"Logs serão salvos no arquivo: {log_file}")
            else:
                logger.info(f"Logger '{name}' já configurado.")

            return logger
        except Exception as e:
            # Caso algo dê errado durante a configuração
            raise RuntimeError(f"Erro ao configurar o logger '{name}': {e}")
