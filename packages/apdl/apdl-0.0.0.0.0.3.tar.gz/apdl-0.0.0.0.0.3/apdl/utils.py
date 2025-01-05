import time
import itertools
import threading

def display_animation(message, done_event):
    """Menampilkan animasi loading selama proses berjalan."""
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        print(f"\r{message} {c}", end='', flush=True)
        time.sleep(0.1)
    print("\r", end='')
