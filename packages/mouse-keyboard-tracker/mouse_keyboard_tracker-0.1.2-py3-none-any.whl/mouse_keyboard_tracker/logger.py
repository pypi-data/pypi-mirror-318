import logging
import os
from .config import Config

class EventoLogger:
    def __init__(self, nome_arquivo):
        try:
            self.logger = self._configurar_logger(nome_arquivo, f'{Config.LOG_DIR}/{nome_arquivo}')
        except Exception as e:
            print(f"Erro ao configurar logger: {e}")

    def registrar_evento(self, evento):
        """Registra um evento no logger."""
        try:
            self.logger.info(evento)
        except Exception as e:
            print(f"Erro ao registrar evento: {e}")

    @staticmethod
    def _configurar_logger(nome, caminho_arquivo):
        """Configura um logger com o nome e caminho de arquivo especificados."""
        try:
            logger = logging.getLogger(nome)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler(caminho_arquivo)
            handler.setFormatter(logging.Formatter(Config.LOG_FORMAT))
            logger.addHandler(handler)
            return logger
        except Exception as e:
            print(f"Erro ao configurar logger: {e}")
            return None

    @staticmethod
    def _configurar_diretorio_log():
        """Configura o diretório de logs se não existir."""
        try:
            if not os.path.exists(Config.LOG_DIR):
                os.makedirs(Config.LOG_DIR)
        except Exception as e:
            print(f"Erro ao configurar diretório de logs: {e}")

    @staticmethod
    def configurar_logger_principal():
        """Configura o logger principal."""
        try:
            EventoLogger._configurar_diretorio_log()
            return EventoLogger._configurar_logger('monitoramento', f'{Config.LOG_DIR}/monitoramento.log')
        except Exception as e:
            print(f"Erro ao configurar logger principal: {e}")
            return None

    @staticmethod
    def fechar_loggers():
        """Fecha todos os loggers configurados."""
        try:
            loggers = ['monitoramento', 'teclado_eventos.log', 'mouse_eventos.log', 'ociosidade_eventos.log']
            for logger_name in loggers:
                logger = logging.getLogger(logger_name)
                for handler in logger.handlers:
                    handler.close()
                logger.handlers = []
        except Exception as e:
            print(f"Erro ao fechar loggers: {e}")