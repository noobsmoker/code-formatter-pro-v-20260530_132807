#!/usr/bin/env python3
import argparse
import sys
import re
VERSION = "1.0.0"

def format_code(content, language='python'):
    if language == 'python':
        content = re.sub(r'\s+$', '', content, flags=re.MULTILINE)
        content = re.sub(r'
{3,}', '

', content)
    return content.strip()

def main():
    parser = argparse.ArgumentParser(description='Code Formatter Pro - Universal formatter')
    parser.add_argument('file', help='File to format')
    parser.add_argument('-l', '--language', default='python')
    parser.add_argument('-w', '--write', action='store_true')
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        content = f.read()
    formatted = format_code(content, args.language)
    if args.write:
        with open(args.file, 'w') as f:
            f.write(formatted)
        print(f"Formatted {args.file}")
    else:
        print(formatted)
if __name__ == '__main__':
    main()
