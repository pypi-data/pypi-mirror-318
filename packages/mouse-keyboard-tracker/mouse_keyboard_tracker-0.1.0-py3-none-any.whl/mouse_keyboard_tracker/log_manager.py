import os
import shutil
import time
from datetime import datetime
from mouse_keyboard_tracker.config import Config

class LogManager:

    @staticmethod
    def verificar_ociosidade(horario_inicio):
        """Verifica se houve períodos de ociosidade e registra no log."""
        try:
            ociosidade_log_path = os.path.join(Config.LOG_DIR, Config.OCIOSIDADE_LOG)
            if not os.path.exists(ociosidade_log_path) or os.path.getsize(ociosidade_log_path) == Config.TAMANHO_MINIMO_ARQUIVO:
                with open(ociosidade_log_path, 'a') as log_file:
                    horario_fim = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_file.write(f'Não foram registrados períodos de inatividade entre {horario_inicio} e {horario_fim}.\n')
        except Exception as e:
            print(f"Erro ao verificar ociosidade: {e}")

    @staticmethod
    def esperar_arquivo_preenchido(arquivo_path):
        """Espera até que o arquivo especificado seja preenchido."""
        try:
            while not os.path.exists(arquivo_path) or os.path.getsize(arquivo_path) == Config.TAMANHO_MINIMO_ARQUIVO:
                time.sleep(Config.INTERVALO_VERIFICACAO_ARQUIVO)
        except Exception as e:
            print(f"Erro ao esperar arquivo preenchido: {e}")

    @staticmethod
    def determinar_periodo():
        """Determina o período do dia (matutino, vespertino, noturno)."""
        try:
            hora_atual = datetime.now().hour
            if Config.HORA_INICIO_MATUTINO <= hora_atual < Config.HORA_INICIO_VESPERTINO:
                return 'matutino'
            elif Config.HORA_INICIO_VESPERTINO <= hora_atual < Config.HORA_INICIO_NOTURNO:
                return 'vespertino'
            else:
                return 'noturno'
        except Exception as e:
            print(f"Erro ao determinar período: {e}")
            return 'desconhecido'

    @staticmethod
    def mover_logs_para_relatorios(horario_inicio):
        """Move os logs para o diretório de relatórios."""
        try:
            LogManager.verificar_ociosidade(horario_inicio)

            ociosidade_log_path = os.path.join(Config.LOG_DIR, Config.OCIOSIDADE_LOG)
            LogManager.esperar_arquivo_preenchido(ociosidade_log_path)

            timestamp = datetime.now().strftime('%Y-%m-%d')
            periodo = LogManager.determinar_periodo()
            horario_inicio = horario_inicio.replace(':', '_')
            destino = os.path.join(Config.RELATORIOS_DIR, timestamp, periodo, horario_inicio)
            os.makedirs(destino, exist_ok=True)

            for arquivo in os.listdir(Config.LOG_DIR):
                if arquivo.endswith('.log'):
                    shutil.move(os.path.join(Config.LOG_DIR, arquivo), os.path.join(destino, arquivo))
        except Exception as e:
            print(f"Erro ao mover logs para relatórios: {e}")