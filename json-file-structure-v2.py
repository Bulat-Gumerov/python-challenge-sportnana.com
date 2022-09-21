#!/usr/bin/env python3

dirs = [
    "blog/travel/myblog.pdf",
    "blog/travel/yourblog.pdf",
    "whitepaper/travel/mywhitepaper.pdf",
    "whitepaper/travel/yourwhitepaper.pdf",
    "test/1/2/3/4/5/6/7/8"
]

import json
import os

def json_file_structure(dirs):
    root = {}
    for path in dirs:
        parts = path.split('/')
        parent = root
        for part in parts:
            if part not in parent:
                parent[part] = {}
                parent[part]['type'] = 'file' if '.' in part else 'folder'
                parent[part]['name'] = part
                parent[part]['path'] = path
                parent[part]['children'] = []
            parent = parent[part]
    return root

def main():
    print(json.dumps(json_file_structure(dirs), indent=4))

if __name__ == '__main__':
    main()
