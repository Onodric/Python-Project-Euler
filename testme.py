import sys
import subprocess

if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
