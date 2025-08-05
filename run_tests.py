import subprocess
import os

os.chdir('frontend')
subprocess.run(['npm', 'test'])
