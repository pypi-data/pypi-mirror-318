import argparse
from mouse_keyboard_tracker import iniciar_monitoramento, encerrar_monitoramento
import time

def configurar_parser():
    parser = argparse.ArgumentParser(description='Monitorar atividades de teclado e mouse.')

    # Configurações de tempo
    parser.add_argument('--tempo_maximo_ocioso', type=int, default=600, help='Tempo máximo de ociosidade em segundos')
    parser.add_argument('--intervalo_checagem_ociosidade', type=int, default=1, help='Intervalo de checagem de ociosidade em segundos')
    parser.add_argument('--intervalo_sleep', type=int, default=10, help='Intervalo de sleep em segundos')
    parser.add_argument('--segundos_em_um_minuto', type=int, default=60, help='Segundos em um minuto')
    parser.add_argument('--segundos_em_uma_hora', type=int, default=3600, help='Segundos em uma hora')

    # Configurações de horário
    parser.add_argument('--hora_inicio_matutino', type=int, default=6, help='Hora de início do período matutino')
    parser.add_argument('--hora_inicio_vespertino', type=int, default=12, help='Hora de início do período vespertino')
    parser.add_argument('--hora_inicio_noturno', type=int, default=18, help='Hora de início do período noturno')

    # Configurações de arquivos
    parser.add_argument('--tamanho_minimo_arquivo', type=int, default=0, help='Tamanho mínimo do arquivo em bytes')
    parser.add_argument('--intervalo_verificacao_arquivo', type=int, default=1, help='Intervalo de verificação do arquivo em segundos')

    # Configurações de ociosidade
    parser.add_argument('--tempo_ocioso_acumulado', type=int, default=0, help='Tempo ocioso acumulado inicial')
    parser.add_argument('--tempo_ocioso_total', type=int, default=0, help='Tempo ocioso total')

    # Configurações de logs
    parser.add_argument('--teclado_log', type=str, default='teclado_eventos.log', help='Nome do arquivo de log de teclado')
    parser.add_argument('--mouse_log', type=str, default='mouse_eventos.log', help='Nome do arquivo de log de mouse')
    parser.add_argument('--log_dir', type=str, default='logs', help='Diretório de logs')
    parser.add_argument('--ociosidade_log', type=str, default='ociosidade_eventos.log', help='Nome do arquivo de log de ociosidade')
    parser.add_argument('--relatorios_dir', type=str, default='relatorios', help='Diretório de relatórios')
    parser.add_argument('--log_format', type=str, default='%(asctime)s - %(message)s', help='Formato do log')

    return parser

def construir_configs(args):
    return {
        'TEMPO_MAXIMO_OCIOSO': args.tempo_maximo_ocioso,
        'INTERVALO_CHECAGEM_OCIOSIDADE': args.intervalo_checagem_ociosidade,
        'INTERVALO_SLEEP': args.intervalo_sleep,
        'SEGUNDOS_EM_UM_MINUTO': args.segundos_em_um_minuto,
        'SEGUNDOS_EM_UMA_HORA': args.segundos_em_uma_hora,
        'HORA_INICIO_MATUTINO': args.hora_inicio_matutino,
        'HORA_INICIO_VESPERTINO': args.hora_inicio_vespertino,
        'HORA_INICIO_NOTURNO': args.hora_inicio_noturno,
        'TAMANHO_MINIMO_ARQUIVO': args.tamanho_minimo_arquivo,
        'INTERVALO_VERIFICACAO_ARQUIVO': args.intervalo_verificacao_arquivo,
        'TEMPO_OCIOSO_ACUMULADO': args.tempo_ocioso_acumulado,
        'TEMPO_OCIOSO_TOTAL': args.tempo_ocioso_total,
        'TECLADO_LOG': args.teclado_log,
        'MOUSE_LOG': args.mouse_log,
        'LOG_DIR': args.log_dir,
        'OCIOSIDADE_LOG': args.ociosidade_log,
        'RELATORIOS_DIR': args.relatorios_dir,
        'LOG_FORMAT': args.log_format
    }

def main():
    parser = configurar_parser()
    args = parser.parse_args()
    configs = construir_configs(args)

    horario_inicio, logger, monitor_ociosidade = iniciar_monitoramento(configs=configs)

    if not horario_inicio or not logger or not monitor_ociosidade:
        print("Falha ao iniciar o monitoramento.")
        return

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        encerrar_monitoramento(horario_inicio, logger, monitor_ociosidade)

if __name__ == "__main__":
    main()