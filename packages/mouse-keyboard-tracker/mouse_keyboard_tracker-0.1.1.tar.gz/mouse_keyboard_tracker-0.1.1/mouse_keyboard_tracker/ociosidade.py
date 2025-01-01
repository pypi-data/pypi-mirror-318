import time
from mouse_keyboard_tracker.logger import EventoLogger
from .config import Config

class MonitorOciosidade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MonitorOciosidade, cls).__new__(cls)
        return cls._instance

    def __init__(self, tempo_maximo_ocioso=Config.TEMPO_MAXIMO_OCIOSO):
        if not hasattr(self, 'initialized'):
            self.tempo_maximo_ocioso = tempo_maximo_ocioso
            self.ultimo_evento = time.time()
            self.ociosidade_logger = EventoLogger(Config.OCIOSIDADE_LOG)
            self.ocioso = False
            self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO
            self.tempo_ocioso_total = Config.TEMPO_OCIOSO_TOTAL
            self.initialized = True

    def atualizar_ultimo_evento(self):
        """Atualiza o último evento e registra o tempo de ociosidade se necessário."""
        try:
            if self.ocioso:
                self._registrar_ociosidade()
            self.ultimo_evento = time.time()
            self.ocioso = False
            self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao atualizar último evento: {e}")

    def verificar_ociosidade(self):
        """Verifica periodicamente se o usuário está ocioso."""
        try:
            while True:
                tempo_atual = time.time()
                tempo_ocioso = tempo_atual - self.ultimo_evento
                if tempo_ocioso > self.tempo_maximo_ocioso:
                    self._handle_ociosidade(tempo_ocioso)
                else:
                    self._handle_atividade()
                time.sleep(Config.INTERVALO_CHECAGEM_OCIOSIDADE)
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao verificar ociosidade: {e}")

    def _handle_ociosidade(self, tempo_ocioso):
        """Lida com a ociosidade do usuário."""
        try:
            if not self.ocioso:
                self.ocioso = True
                evento = f"O usuário está ocioso desde {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.ultimo_evento))}."
                self.ociosidade_logger.registrar_evento(evento)
            self.tempo_ocioso_acumulado = tempo_ocioso
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao lidar com ociosidade: {e}")

    def _handle_atividade(self):
        """Lida com a atividade do usuário."""
        try:
            if self.ocioso:
                evento = f"O usuário esteve ocioso por {int(self.tempo_ocioso_acumulado)} segundos."
                self.ociosidade_logger.registrar_evento(evento)
                self.ocioso = False
                self.tempo_ocioso_total += self.tempo_ocioso_acumulado
                self.tempo_ocioso_acumulado = Config.TEMPO_OCIOSO_ACUMULADO
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao lidar com atividade: {e}")

    def _registrar_ociosidade(self):
        """Registra o tempo de ociosidade."""
        try:
            tempo_ocioso = time.time() - self.ultimo_evento
            horas, resto = divmod(tempo_ocioso, Config.SEGUNDOS_EM_UMA_HORA)
            minutos, segundos = divmod(resto, Config.SEGUNDOS_EM_UM_MINUTO)
            evento = f"O usuário esteve ocioso por {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos."
            self.ociosidade_logger.registrar_evento(evento)
            self.tempo_ocioso_total += tempo_ocioso
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao registrar ociosidade: {e}")

    def registrar_tempo_total_ociosidade(self):
        """Registra o tempo total de ociosidade."""
        try:
            horas, resto = divmod(self.tempo_ocioso_total, Config.SEGUNDOS_EM_UMA_HORA)
            minutos, segundos = divmod(resto, Config.SEGUNDOS_EM_UM_MINUTO)
            evento = f"Tempo total de ociosidade: {int(horas)} horas, {int(minutos)} minutos e {int(segundos)} segundos."
            self.ociosidade_logger.registrar_evento(evento)
        except Exception as e:
            self.ociosidade_logger.registrar_evento(f"Erro ao registrar tempo total de ociosidade: {e}")