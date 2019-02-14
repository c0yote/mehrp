import signal
import os
import threading

from simpleaudio import WaveObject

HERE = os.path.abspath(os.path.dirname(__file__))
MEHRP_PATH = os.path.join(HERE, 'mehrp.wav')


class LoopRunnableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(LoopRunnableThread, self).__init__()
        self._stop_event = threading.Event()
        
        self.runable = kwargs['target']
        self.args = kwargs['args']

        signal.signal(signal.SIGINT, self.handle_sigint)
    
    def handle_sigint(self, signum, frame):
        self._stop_event.set()

    def run(self):
        while not self._stop_event.is_set():
            self.runable(*self.args)
    
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


def _play_wave(wave):
    play = wave.play()
    play.wait_done()


def mehrp(count):
    mehrp_wave = WaveObject.from_wave_file(MEHRP_PATH)

    for _ in range(0, count):
        _play_wave(mehrp_wave)


def mehrp_until_input(prompt=None):
    mehrp_wave = WaveObject.from_wave_file(MEHRP_PATH)
    
    play_thread = LoopRunnableThread(target=_play_wave, args=(mehrp_wave,))
    play_thread.start()
    
    if prompt:
        value = input(prompt)
    else:
        value = input()
            
    play_thread.stop()
    play_thread.join()

    return value
