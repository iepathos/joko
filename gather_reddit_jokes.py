#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import subprocess


def remove_empty_lines(filename):
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()

file_name = "reddit_jokes.txt"
if not os.path.exists('reddit_jokes.json'):
    url = "https://github.com/taivop/joke-dataset/raw/master/reddit_jokes.json"
    cmd = ['wget', url]
    subprocess.call(cmd)
with open('reddit_jokes.json', 'r') as f:
    data = json.loads(f.read())

sdata = sorted(data, key=lambda x: x['score'], reverse=True)
with open(file_name, 'a') as f:
    # only taking top rated half of reddit jokes
    for entry in sdata[:int(len(sdata) / 2)]:
        f.write(entry['title'] + ' ' + entry['body'] + '\n')

# remove any empty white lines from training txt
remove_empty_lines(file_name)