
---

# mouse-keyboard-tracker

Este projeto é uma biblioteca para monitorar atividades de teclado e mouse que registra eventos de uso e períodos de inatividade. Ele é útil para rastrear a produtividade e o uso do computador ao longo do tempo, gerando logs detalhados de todas as ações realizadas pelo usuário.

## Instalação

Você pode instalar a biblioteca usando pip:

```bash
pip install mouse_keyboard_tracker
```

## Uso

Aqui está um exemplo de como usar a biblioteca:

```python
from mouse_keyboard_tracker import iniciar_monitoramento, encerrar_monitoramento
import time

def main():
    configs = {
        'TEMPO_MAXIMO_OCIOSO': 600,
    }
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
```

## Configurações Disponíveis

A biblioteca `mouse_keyboard_tracker` permite a personalização de várias configurações através da classe `Config`. Abaixo estão as configurações disponíveis e seus valores padrão:

### Configurações de Tempo

- **TEMPO_MAXIMO_OCIOSO**: Tempo máximo de ociosidade em segundos (padrão: 600)
- **INTERVALO_CHECAGEM_OCIOSIDADE**: Intervalo de checagem de ociosidade em segundos (padrão: 1)
- **INTERVALO_SLEEP**: Intervalo de sleep em segundos (padrão: 10)
- **SEGUNDOS_EM_UM_MINUTO**: Segundos em um minuto (padrão: 60)
- **SEGUNDOS_EM_UMA_HORA**: Segundos em uma hora (padrão: 3600)

### Configurações de Horário

- **HORA_INICIO_MATUTINO**: Hora de início do período matutino (padrão: 6)
- **HORA_INICIO_VESPERTINO**: Hora de início do período vespertino (padrão: 12)
- **HORA_INICIO_NOTURNO**: Hora de início do período noturno (padrão: 18)

### Configurações de Arquivos

- **TAMANHO_MINIMO_ARQUIVO**: Tamanho mínimo do arquivo em bytes (padrão: 0)
- **INTERVALO_VERIFICACAO_ARQUIVO**: Intervalo de verificação do arquivo em segundos (padrão: 1)

### Configurações de Ociosidade

- **TEMPO_OCIOSO_ACUMULADO**: Tempo ocioso acumulado inicial (padrão: 0)
- **TEMPO_OCIOSO_TOTAL**: Tempo ocioso total (padrão: 0)

### Configurações de Logs

- **TECLADO_LOG**: Nome do arquivo de log de teclado (padrão: 'teclado_eventos.log')
- **MOUSE_LOG**: Nome do arquivo de log de mouse (padrão: 'mouse_eventos.log')
- **LOG_DIR**: Diretório de logs (padrão: 'logs')
- **OCIOSIDADE_LOG**: Nome do arquivo de log de ociosidade (padrão: 'ociosidade_eventos.log')
- **RELATORIOS_DIR**: Diretório de relatórios (padrão: 'relatorios')
- **LOG_FORMAT**: Formato do log (padrão: '%(asctime)s - %(message)s')

## Estrutura do Projeto

### Arquivos e seus papéis

- **config.py**: Contém a classe `Config` que define várias constantes usadas em todo o projeto, como tempos de ociosidade, intervalos de checagem e tamanhos mínimos de arquivos. Este arquivo centraliza a configuração do sistema, facilitando ajustes e manutenção.

- **eventos.py**: Implementa a classe `MonitorEventos` que captura eventos de teclado e mouse usando a biblioteca `pynput`. Ele registra esses eventos em logs e notifica observadores sobre novos eventos. Utiliza o padrão Observer para notificar outras partes do sistema sobre eventos de entrada.

- **log_manager.py**: Contém a classe `LogManager` que gerencia os arquivos de log, verificando períodos de inatividade e movendo os logs para diretórios de relatórios organizados por data e período do dia. Este arquivo garante que os logs sejam armazenados e organizados corretamente.

- **logger.py**: Define a classe `EventoLogger` que configura e gerencia loggers para diferentes tipos de eventos (teclado, mouse, ociosidade). Inclui métodos para registrar eventos e configurar o logger principal. Este arquivo centraliza a lógica de logging, facilitando a manutenção e a expansão.

- **ociosidade.py**: Implementa a classe `MonitorOciosidade` que verifica períodos de inatividade do usuário. Utiliza o padrão Singleton para garantir que apenas uma instância da classe exista. Registra eventos de ociosidade e notifica quando o usuário está inativo por um período prolongado.

- **main.py**: Arquivo principal que inicializa e executa o monitoramento. Configura loggers, inicia a captura de eventos e verifica a ociosidade em threads separadas. Este arquivo orquestra a interação entre os diferentes componentes do sistema.

- **requirements.txt**: Lista as dependências do projeto, garantindo que todas as bibliotecas necessárias sejam instaladas. Atualmente, inclui a biblioteca `pynput` para captura de eventos de teclado e mouse.

### Padrões de Projeto Utilizados

- **Singleton**: Utilizado na classe `MonitorOciosidade` para garantir que apenas uma instância da classe exista, evitando conflitos e garantindo consistência nos dados de ociosidade.

- **Observer**: Utilizado na classe `MonitorEventos` para notificar observadores (como `MonitorOciosidade`) sobre novos eventos de entrada, permitindo uma arquitetura desacoplada e extensível.

### Por que esses padrões foram escolhidos?

- **Singleton**: Garante que a verificação de ociosidade seja centralizada e consistente, evitando múltiplas instâncias que poderiam levar a resultados conflitantes.

- **Observer**: Permite que diferentes partes do sistema reajam a eventos de entrada sem estarem fortemente acopladas, facilitando a adição de novos tipos de observadores no futuro.

## Uso via CLI

Você pode usar a biblioteca via linha de comando. Aqui está um exemplo:

```bash
mouse-keyboard-tracker --tempo_maximo_ocioso 300 --intervalo_checagem_ociosidade 2 --log_dir meus_logs
```

### Argumentos Disponíveis

Os seguintes argumentos estão disponíveis. Se você não fornecer um argumento, o valor padrão será usado.

- `--tempo_maximo_ocioso`: Tempo máximo de ociosidade em segundos (padrão: 600)
- `--intervalo_checagem_ociosidade`: Intervalo de checagem de ociosidade em segundos (padrão: 1)
- `--intervalo_sleep`: Intervalo de sleep em segundos (padrão: 10)
- `--segundos_em_um_minuto`: Segundos em um minuto (padrão: 60)
- `--segundos_em_uma_hora`: Segundos em uma hora (padrão: 3600)
- `--hora_inicio_matutino`: Hora de início do período matutino (padrão: 6)
- `--hora_inicio_vespertino`: Hora de início do período vespertino (padrão: 12)
- `--hora_inicio_noturno`: Hora de início do período noturno (padrão: 18)
- `--tamanho_minimo_arquivo`: Tamanho mínimo do arquivo em bytes (padrão: 0)
- `--intervalo_verificacao_arquivo`: Intervalo de verificação do arquivo em segundos (padrão: 1)
- `--tempo_ocioso_acumulado`: Tempo ocioso acumulado inicial (padrão: 0)
- `--tempo_ocioso_total`: Tempo ocioso total (padrão: 0)
- `--teclado_log`: Nome do arquivo de log de teclado (padrão: 'teclado_eventos.log')
- `--mouse_log`: Nome do arquivo de log de mouse (padrão: 'mouse_eventos.log')
- `--log_dir`: Diretório de logs (padrão: 'logs')
- `--ociosidade_log`: Nome do arquivo de log de ociosidade (padrão: 'ociosidade_eventos.log')
- `--relatorios_dir`: Diretório de relatórios (padrão: 'relatorios')
- `--log_format`: Formato do log (padrão: '%(asctime)s - %(message)s')

### Exemplos de Uso

Você pode executar o comando CLI sem fornecer nenhum argumento, e ele usará todos os valores padrão:

```bash
mouse-keyboard-tracker
```

Ou você pode fornecer apenas os argumentos que deseja alterar:

```bash
mouse-keyboard-tracker --tempo_maximo_ocioso 300 --log_dir meus_logs
```

### Threads Utilizadas

O projeto utiliza três threads principais para realizar o monitoramento de atividades. A primeira thread é responsável por capturar eventos de teclado, enquanto a segunda thread captura eventos de mouse, ambas implementadas na classe `MonitorEventos`. A terceira thread, implementada na classe `MonitorOciosidade`, verifica periodicamente a ociosidade do usuário. Essas threads são iniciadas no arquivo `main.py` e permitem que o monitoramento de eventos e a verificação de ociosidade ocorram simultaneamente, garantindo uma captura eficiente e em tempo real das atividades do usuário.

---
