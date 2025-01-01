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
    horario_inicio, logger, monitor_ociosidade = iniciar_monitoramento()

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

### Threads Utilizadas

O projeto utiliza três threads principais para realizar o monitoramento de atividades. A primeira thread é responsável por capturar eventos de teclado, enquanto a segunda thread captura eventos de mouse, ambas implementadas na classe `MonitorEventos`. A terceira thread, implementada na classe `MonitorOciosidade`, verifica periodicamente a ociosidade do usuário. Essas threads são iniciadas no arquivo `main.py` e permitem que o monitoramento de eventos e a verificação de ociosidade ocorram simultaneamente, garantindo uma captura eficiente e em tempo real das atividades do usuário.