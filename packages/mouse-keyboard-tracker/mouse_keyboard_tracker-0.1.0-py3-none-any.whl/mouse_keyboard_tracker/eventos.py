from pynput import keyboard, mouse
from threading import Thread
import time
from collections import deque
from mouse_keyboard_tracker.logger import EventoLogger
from .config import Config

class MonitorEventos:
    def __init__(self):
        self.teclado_eventos = deque()
        self.mouse_eventos = deque()
        self.ultimo_evento = time.time()
        self.observers = []
        self.teclado_logger = EventoLogger(Config.TECLADO_LOG)
        self.mouse_logger = EventoLogger(Config.MOUSE_LOG)

    def adicionar_observador(self, observador):
        """Adiciona um observador à lista de observadores."""
        self.observers.append(observador)

    def notificar_observadores(self):
        """Notifica todos os observadores sobre um novo evento."""
        for observador in self.observers:
            observador.atualizar_ultimo_evento()

    def _registrar_evento(self, logger, eventos, evento):
        """Registra um evento e notifica os observadores."""
        try:
            timestamp = time.time()
            eventos.append((timestamp, evento))
            logger.registrar_evento(evento)
            self.ultimo_evento = timestamp
            self.notificar_observadores()
        except Exception as e:
            logger.registrar_evento(f"Erro ao registrar evento: {e}")

    def capturar_teclado(self):
        """Captura eventos de teclado."""
        def on_press(key):
            evento = f"Tecla pressionada: {key}"
            self._registrar_evento(self.teclado_logger, self.teclado_eventos, evento)

        try:
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
        except Exception as e:
            self.teclado_logger.registrar_evento(f"Erro ao capturar eventos de teclado: {e}")

    def capturar_mouse(self):
        """Captura eventos de mouse."""
        def on_click(x, y, button, pressed):
            evento = f"Mouse {'clicado' if pressed else 'solto'} em ({x}, {y}) com {button}"
            self._registrar_evento(self.mouse_logger, self.mouse_eventos, evento)

        def on_move(x, y):
            evento = f"Mouse movido para ({x}, {y})"
            self._registrar_evento(self.mouse_logger, self.mouse_eventos, evento)

        try:
            with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
                listener.join()
        except Exception as e:
            self.mouse_logger.registrar_evento(f"Erro ao capturar eventos de mouse: {e}")

    def iniciar_monitoramento(self):
        """Inicia o monitoramento de eventos de teclado e mouse."""
        try:
            Thread(target=self.capturar_teclado, daemon=True).start()
            Thread(target=self.capturar_mouse, daemon=True).start()
        except Exception as e:
            self.teclado_logger.registrar_evento(f"Erro ao iniciar monitoramento: {e}")
            self.mouse_logger.registrar_evento(f"Erro ao iniciar monitoramento: {e}")