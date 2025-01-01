from .config import Config
from .eventos import MonitorEventos
from .log_manager import LogManager
from .logger import EventoLogger
from .ociosidade import MonitorOciosidade
from threading import Thread
from datetime import datetime
import time

def iniciar_monitoramento():
    """Configura e inicializa o monitoramento de eventos e ociosidade."""
    try:
        horario_inicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger = EventoLogger.configurar_logger_principal()
        logger.info("Monitoramento iniciado.")

        monitor_eventos = MonitorEventos()
        monitor_ociosidade = MonitorOciosidade(tempo_maximo_ocioso=Config.TEMPO_MAXIMO_OCIOSO)

        monitor_eventos.adicionar_observador(monitor_ociosidade)
        monitor_eventos.iniciar_monitoramento()

        Thread(target=monitor_ociosidade.verificar_ociosidade, daemon=True).start()

        return horario_inicio, logger, monitor_ociosidade
    except Exception as e:
        print(f"Erro ao configurar monitoramento: {e}")
        return None, None, None

def encerrar_monitoramento(horario_inicio, logger, monitor_ociosidade):
    """Encerra o monitoramento de eventos e ociosidade."""
    try:
        logger.info("Monitoramento encerrado.")
        monitor_ociosidade.registrar_tempo_total_ociosidade()
        EventoLogger.fechar_loggers()
        LogManager.mover_logs_para_relatorios(horario_inicio)
        print("Monitoramento encerrado.")
    except Exception as e:
        print(f"Erro ao encerrar monitoramento: {e}")