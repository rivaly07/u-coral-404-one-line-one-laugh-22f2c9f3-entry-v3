#!/usr/bin/env python3
import os

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, 'entry.txt')

    # Original one-liner: surprising, concise, fresh
    line = "My therapist says I have a preoccupation with vengeance. We'll see about that."

    with open(entry_path, 'w', encoding='utf-8') as f:
        f.write(line)

if __name__ == '__main__':
    main()