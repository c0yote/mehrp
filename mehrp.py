import pyaudio
import threading
import time
import wave


CHUNK_SIZE = 1024
MEHRP_PATH = 'data/mehrp.wav'


class _MehrpPlayThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(_MehrpPlayThread, self).__init__()
        self._stop_event = threading.Event()
        
        self.runable = kwargs['target']
        self.args = kwargs['args']

    def run(self):
        while not self._stop_event.is_set():
            self.runable(*self.args)
    
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
        

def _play_mehrp_sound(stream, wav_file):
    wav_file.rewind()
    wav_data = wav_file.readframes(CHUNK_SIZE)
    while wav_data:        
        stream.write(wav_data)
        wav_data = wav_file.readframes(CHUNK_SIZE)


def play(count=None, pyaudio_instance=None):
    do_instantiate_pyaudio = not bool(pyaudio_instance)
    pyaudio_iface = pyaudio.PyAudio() if do_instantiate_pyaudio else pyaudio_instance

    with wave.open(MEHRP_PATH, 'rb') as wav_file:
        stream = pyaudio_iface.open(format = pyaudio_iface.get_format_from_width(wav_file.getsampwidth()),
                            channels = wav_file.getnchannels(),
                            rate = wav_file.getframerate(),
                            output = True)
        
        while count is None or count > 0:
            _play_mehrp_sound(stream, wav_file)
            count = count - 1 if count else count
        
        stream.stop_stream()
        stream.close()
    
    if do_instantiate_pyaudio:
        pyaudio_iface.terminate()


def play_until_input(pyaudio_instance=None):
    do_instantiate_pyaudio = not bool(pyaudio_instance)
    pyaudio_iface = pyaudio.PyAudio() if do_instantiate_pyaudio else pyaudio_instance

    with wave.open(MEHRP_PATH, 'rb') as wav_file:
        stream = pyaudio_iface.open(format = pyaudio_iface.get_format_from_width(wav_file.getsampwidth()),
                            channels = wav_file.getnchannels(),
                            rate = wav_file.getframerate(),
                            output = True)
        
        play_thread = _MehrpPlayThread(target=_play_mehrp_sound, args=(stream, wav_file))
        play_thread.start()
        
        value = input()
                
        play_thread.stop()
        play_thread.join()
        
        stream.stop_stream()
        stream.close()
    
    if do_instantiate_pyaudio:
        pyaudio_iface.terminate()

    return value


def main():    
    print('Playing mehrp 3 times...')
    play(3)
    
    print('Playing until user input...')
    value = play_until_input()
    
    print('Echoing input: ' + value)


if __name__ == '__main__':
    main()
