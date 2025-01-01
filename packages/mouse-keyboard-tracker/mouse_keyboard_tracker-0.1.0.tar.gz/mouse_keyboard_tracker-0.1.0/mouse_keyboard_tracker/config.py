class Config:
    """Configurações gerais do sistema."""

    # Configurações de tempo
    TEMPO_MAXIMO_OCIOSO = 600  # Tempo máximo de ociosidade em segundos
    INTERVALO_CHECAGEM_OCIOSIDADE = 1  # Intervalo de checagem de ociosidade em segundos
    INTERVALO_SLEEP = 10  # Intervalo de sleep em segundos
    SEGUNDOS_EM_UM_MINUTO = 60  # Segundos em um minuto
    SEGUNDOS_EM_UMA_HORA = 3600  # Segundos em uma hora

    # Configurações de horário
    HORA_INICIO_MATUTINO = 6  # Hora de início do período matutino
    HORA_INICIO_VESPERTINO = 12  # Hora de início do período vespertino
    HORA_INICIO_NOTURNO = 18  # Hora de início do período noturno

    # Configurações de arquivos
    TAMANHO_MINIMO_ARQUIVO = 0  # Tamanho mínimo do arquivo em bytes
    INTERVALO_VERIFICACAO_ARQUIVO = 1  # Intervalo de verificação do arquivo em segundos

    # Configurações de ociosidade
    TEMPO_OCIOSO_ACUMULADO = 0  # Tempo ocioso acumulado inicial
    TEMPO_OCIOSO_TOTAL = 0  # Tempo ocioso total

    # Configurações de logs
    TECLADO_LOG = 'teclado_eventos.log'  # Nome do arquivo de log de teclado
    MOUSE_LOG = 'mouse_eventos.log'  # Nome do arquivo de log de mouse
    LOG_DIR = 'logs'  # Diretório de logs
    OCIOSIDADE_LOG = 'ociosidade_eventos.log'  # Nome do arquivo de log de ociosidade
    RELATORIOS_DIR = 'relatorios'  # Diretório de relatórios
    LOG_FORMAT = '%(asctime)s - %(message)s'  # Formato do log