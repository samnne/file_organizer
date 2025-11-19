# A simple file organizer

A quick and fast file organizer using native python library's like,
os, shutil, and sys.

# Quick Start

```
git clone
cd file_sort
python3 file_sort.py <file-to-organize> <key-words>
```

**Key Words**

- "." => To organize by file extention
- ".<key-word>" => To organize by key-word

_Examples_:

- `python3 file_sort.py ~/Downloads/ .`
- `python3 file_sort.py ~/Downloads/ .resume`
