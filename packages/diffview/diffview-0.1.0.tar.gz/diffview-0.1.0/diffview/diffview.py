# File Diff Viewer
#
# Copyright (c) 2024 Virgil Sisoe
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from __future__ import annotations

import os
import json
import difflib
from enum import Enum
from typing import Any, Tuple, Optional, Generator
from contextlib import contextmanager
from dataclasses import field, asdict, dataclass

from PySide2.QtGui import Qt, QFont, QColor, QWheelEvent, QTextCharFormat
from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import (QFrame, QLabel, QStyle, QAction, QWidget,
                               QSplitter, QScrollBar, QFileDialog, QFontDialog,
                               QHBoxLayout, QListWidget, QMainWindow,
                               QMessageBox, QPushButton, QToolButton,
                               QVBoxLayout, QPlainTextEdit, QListWidgetItem)

SETTINGS_DIR = os.getenv(
    'DIFFVIEWER_SETTINGS', os.path.join(os.path.expanduser('~'), '.config')
)
if not os.path.exists(SETTINGS_DIR):
    os.makedirs(SETTINGS_DIR)
SETTINGS_FILE = os.path.join(SETTINGS_DIR, 'diffviewer.json')

A_COLOR = QColor(0, 200, 0)
B_COLOR = QColor(0, 0, 200)


@dataclass
class _Settings:
    font_family: str = 'Courier New'
    font_size: int = 12
    recent_files: list[str] = field(default_factory=list)


class FileMode(str, Enum):
    WRITE = 'w'
    READ = 'r'


@contextmanager
def open_settings(
    mode: FileMode = FileMode.READ,
    file: str = SETTINGS_FILE
) -> Generator[_Settings, Any, None]:

    try:
        with open(file, 'r') as f:
            s = _Settings(**json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        s = _Settings()

    yield s

    if mode != 'w':
        return

    with open(file, 'w') as f:
        json.dump(asdict(s), f, indent=4)


class Frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFrameStyle(QFrame.StyledPanel)
        self.setStyleSheet('background-color: #3B3B3B;')


class Editor(QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setStyleSheet('background-color: #2B2B2B;')
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

    def wheelEvent(self, e: QWheelEvent) -> None:
        """Override the wheel event to emit no signal"""
        pass


class FileContentViewer(Frame):

    def __init__(self, label: str, parent=None):
        super().__init__(parent)
        self.editor = Editor()

        self.label = QLabel()
        self.set_header(label, '')

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.label)

        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.editor)

        self.setLayout(layout)

    def set_header(self, view: str, filename: str) -> None:
        self.label.setText(
            f'<span style="font-size: 20px; font-weight: bold;">{view}:</span> '
            f'<span style="font-size: 16px;">{filename}</span>'
        )


class Sidebar(Frame):
    latest_dir = ''

    file_a_loaded = Signal(str, str)
    file_b_loaded = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.files_list = QListWidget()
        self.files_list.setStyleSheet('background-color: #2B2B2B;')
        self.files_list.setSortingEnabled(True)

        font = self.files_list.font()
        font.setPixelSize(16)
        self.files_list.setFont(font)

        load_a = QPushButton('Load A')
        load_a.clicked.connect(self.emit_item_a)

        load_b = QPushButton('Load B')
        load_b.clicked.connect(self.emit_item_b)

        browse = QPushButton('Browse files')
        browse.clicked.connect(self._on_browse_files)

        clear = QToolButton()
        clear.setToolTip('Clear sidebar files')
        clear.setIcon(self.style().standardIcon(QStyle.SP_TrashIcon))
        clear.clicked.connect(self._on_clear_files_list)

        buttons_top_layout = QHBoxLayout()
        buttons_top_layout.addWidget(browse)
        buttons_top_layout.addWidget(clear)

        buttons_bottom_layout = QHBoxLayout()
        buttons_bottom_layout.addWidget(load_a)
        buttons_bottom_layout.addWidget(load_b)

        layout = QVBoxLayout()
        layout.addLayout(buttons_top_layout)
        layout.addLayout(buttons_bottom_layout)
        layout.addWidget(self.files_list)
        self.setLayout(layout)

    @Slot()
    def _on_browse_files(self) -> None:
        files, _ = QFileDialog.getOpenFileNames(
            self, 'Open File', '', ''
        )

        if not files:
            return

        self.latest_dir = os.path.dirname(files[0])

        all_items = [
            self.files_list.item(i).data(Qt.UserRole)
            for i in range(self.files_list.count())
        ]

        for file in files:
            if file not in all_items:
                self.add_item(file)

        with open_settings(mode=FileMode.WRITE) as s:
            files.extend(s.recent_files)
            s.recent_files = list(set(files))

    @Slot()
    def _on_clear_files_list(self) -> None:
        self.files_list.clear()
        with open_settings(mode=FileMode.WRITE) as s:
            s.recent_files = []

    def _open_item(self) -> Tuple[str, str]:
        item = self.files_list.currentItem()
        if not item:
            raise ValueError('No file selected')

        file_path = item.data(Qt.UserRole)

        with open(file_path) as f:
            return (os.path.basename(file_path), f.read())

    @Slot()
    def emit_item_a(self) -> None:
        try:
            self.file_a_loaded.emit(*self._open_item())
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    @Slot()
    def emit_item_b(self) -> None:
        try:
            self.file_b_loaded.emit(*self._open_item())
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))

    def add_item(self, file: str) -> None:
        item = QListWidgetItem(os.path.basename(file))
        item.setToolTip(file)
        item.setData(Qt.UserRole, file)
        self.files_list.addItem(item)


class DiffWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.sidebar = Sidebar(self)
        self.sidebar.file_a_loaded.connect(self.load_a_view)
        self.sidebar.file_b_loaded.connect(self.load_b_view)

        self.view_a = FileContentViewer('A')
        self.view_b = FileContentViewer('B')

        splitter = QSplitter()
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.view_a)
        splitter.addWidget(self.view_b)
        splitter.setSizes([1, 1000, 1000])

        self._scroll_bar = QScrollBar()
        self._scroll_bar.valueChanged.connect(self._on_slider_value_changed)

        layout = QHBoxLayout()
        layout.addWidget(splitter)
        layout.addWidget(self._scroll_bar)

        self.setLayout(layout)

    @Slot(int)
    def _on_slider_value_changed(self, value: int) -> None:
        def update_scrollbar_position(obj: Editor, value: int):
            # dont why the value stops at 99... whatever
            if value == 99:
                value += 1
            max_len = obj.verticalScrollBar().maximum()
            obj.verticalScrollBar().setValue(int(value * max_len / 100))

        update_scrollbar_position(self.view_a.editor, value)
        update_scrollbar_position(self.view_b.editor, value)

    def _insert_text(
        self,
        text_edit: QPlainTextEdit,
        text: str,
        color: Optional[QColor] = None
    ) -> None:
        cursor = text_edit.textCursor()
        f = QTextCharFormat()
        if color:
            f.setBackground(color)
        cursor.insertText(text, f)
        cursor.insertBlock()

    def set_font(self, family: str, size: int) -> None:
        self.view_a.editor.setFont(QFont(family, size))
        self.view_b.editor.setFont(QFont(family, size))

    def set_line_wrap(self, checked: bool) -> None:
        mode = QPlainTextEdit.WidgetWidth if checked else QPlainTextEdit.NoWrap
        self.view_a.editor.setLineWrapMode(mode)
        self.view_b.editor.setLineWrapMode(mode)

    @Slot()
    def on_show_diff(self) -> None:

        text1 = self.view_a.editor.toPlainText().splitlines()
        text2 = self.view_b.editor.toPlainText().splitlines()

        # must clear after getting the text (duh!)
        self.view_a.editor.clear()
        self.view_b.editor.clear()

        differ = difflib.SequenceMatcher(None, text1, text2)

        for tag, i1, i2, j1, j2 in differ.get_opcodes():

            a_lines = '\n'.join(text1[i1:i2])
            b_lines = '\n'.join(text2[j1:j2])

            if tag == 'delete':
                self._insert_text(self.view_a.editor, a_lines, A_COLOR)
                self._insert_text(self.view_b.editor, '\n' * (i2 - i1))

            elif tag == 'equal':
                self._insert_text(self.view_a.editor, a_lines)
                self._insert_text(self.view_b.editor, b_lines)

            elif tag == 'insert':
                self._insert_text(self.view_a.editor, '\n' * (j2 - j1))
                self._insert_text(self.view_b.editor, b_lines, B_COLOR)

            elif tag == 'replace':
                self._insert_text(self.view_a.editor, a_lines, A_COLOR)
                self._insert_text(self.view_b.editor, b_lines, B_COLOR)

    def load_a_view(self, title: str, text: str) -> None:
        self.view_a.set_header('A', title)
        self.view_a.editor.setPlainText(text)
        self.on_show_diff()

    def load_b_view(self, title: str, text: str) -> None:
        self.view_b.set_header('B', title)
        self.view_b.editor.setPlainText(text)
        self.on_show_diff()

    def load_files(self, files: list[str]) -> None:
        for file in files:
            if not os.path.isfile(file):
                continue
            self.sidebar.add_item(file)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() & Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                self.view_a.editor.zoomIn(1)
                self.view_b.editor.zoomIn(1)
            else:
                self.view_a.editor.zoomOut(1)
                self.view_b.editor.zoomOut(1)
        else:
            self._scroll_bar.wheelEvent(event)


class DiffViewer(QMainWindow):
    font_changed = Signal(str, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('DiffViewer')

        toolbar = self.addToolBar('Main')
        toolbar.addAction('Font', self._on_pick_font)

        line_wrap = QAction('Line Wrap', self)
        line_wrap.setCheckable(True)

        toolbar.addAction(line_wrap)

        self.widget = DiffWidget()

        self.font_changed.connect(self.widget.set_font)
        line_wrap.triggered.connect(self.widget.set_line_wrap)

        self.setCentralWidget(self.widget)

        with open_settings() as s:
            self.font_changed.emit(s.font_family, s.font_size)
            self.widget.load_files(s.recent_files)

    @Slot()
    def _on_pick_font(self) -> None:
        dialog = QFontDialog()
        dialog.exec_()

        f = dialog.currentFont()

        with open_settings(mode=FileMode.WRITE) as s:
            s.font_family = f.family()
            s.font_size = f.pointSize()

        self.font_changed.emit(f.family(), f.pointSize())

    def load_files(self, files: list[str]) -> None:
        self.widget.load_files(files)

    def load_a_view(self, title: str, text: str) -> None:
        self.widget.load_a_view(title, text)

    def load_b_view(self, title: str, text: str) -> None:
        self.widget.load_b_view(title, text)
