#!/usr/bin/env python3

import os

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, 'entry.txt')

    # Original one-liner: surprising, concise, fresh
    line = "I tried to be a photographer... now I'm always in the darkroom."

    with open(entry_path, 'w', encoding='utf-8') as f:
        f.write(line)

if __name__ == '__main__':
    main()