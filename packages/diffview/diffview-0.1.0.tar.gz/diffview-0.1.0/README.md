# File Diff Viewer

A simple file diff viewer built with PySide2 to do one job: compare the contents of two text files side by side.

![image](/screenshot.png)

## What It Does

- Load two files and view them side by side with sync scrolling.
- Highlights differences to make changes easy to spot.

## Install

You can install it using `pip install diffview` (requires Python 3.10) or by copying `diffview/diffview.py` into your source code, which is compatible with Python versions 3.7 and above.

## How to Use

```python
import os
from diffview import DiffViewer

# Create the diff viewer widget
diff_viewer = DiffViewer()

# Load some files into the sidebar for the user to select
diff_viewer.load_files(os.listdir())

# Show the widget
diff_viewer.show()
```

Or you can load buffers directly

```python
diff_viewer.load_a_view(title='File A', content='abc')
diff_viewer.load_b_view(title='File B', content='abcd')
```

> **Note:** You can also load files through the UI with the built-in file selection buttons.

## Notes

- This works with text files only.
- The diffing logic is basic—line-level differences only. If you need something fancier, you should definitely look elsewhere.

## Roadmap

- [x] Multi view scroll
- [x] File selector with last folder selected memory
- [x] Persisten settings: font options, colors, recent files
- [x] Shortcuts: font size (wheelScroll + ctrl)
- [x] Line wrap option
- [x] Tests
- [ ] Line number?
- [ ] Auto-Reload files?
- [ ] Status for file changes?
