"""Sample application setup."""
from __future__ import annotations

import os
import sys

from PySide2.QtWidgets import QApplication

from .diffview import DiffViewer

_, *args = sys.argv


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    widget = DiffViewer()

    if args and args[0] == '--example':
        widget.load_files(os.listdir())
        widget.load_a_view('Buffer1', 'Line1\nLine2\nLine3')
        widget.load_b_view('Buffer2', 'Line1\nLine3\nLine4')

    widget.setGeometry(800, 1617, 800, 600)
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
