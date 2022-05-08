import os
import shutil

if os.path.exists('files'):
    shutil.rmtree('files')
os.mkdir('files')

n = int(input())