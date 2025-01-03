#!/usr/bin/env python
# coding: utf-8

# 第一部分：程序说明###################################################################################
# coding=utf-8
# 药械不良事件工作平台
# 开发人：蔡权周
#!/usr/bin/env python
# coding: utf-8

# 第一部分：程序说明###################################################################################
# coding=utf-8
import sys
import os
import base64
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget, QTextEdit, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QFileDialog, QMessageBox, QFontDialog, QColorDialog, QInputDialog,
                             QToolBar, QAction, QMenu)
from PyQt5.QtGui import (QTextCharFormat, QFont, QColor, QTextCursor, QIcon, QImage, QPixmap, QTextImageFormat,
                         QKeySequence)
from PyQt5.QtCore import Qt, QMimeData, QByteArray, QBuffer, QIODevice
import xml.etree.ElementTree as ET

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = 'notes.xml'  # 当前编辑的文件路径
        self.initUI()
        self.load_notes()

    def initUI(self):
        self.setWindowTitle('笔记软件 v 0.0.2')  # 添加版本号
        self.setGeometry(100, 100, 800, 600)

        # 左侧笔记标题列表
        self.note_list = QListWidget()
        self.note_list.currentItemChanged.connect(self.show_note_content)  # 监听当前项变化

        # 右侧笔记内容编辑框
        self.note_content = QTextEdit()
        self.note_content.textChanged.connect(self.save_note)
        self.note_content.setAcceptRichText(True)  # 允许富文本
        self.note_content.setContextMenuPolicy(Qt.CustomContextMenu)  # 启用自定义右键菜单
        self.note_content.customContextMenuRequested.connect(self.show_context_menu)  # 连接右键菜单事件

        # 设置默认字体为微软雅黑
        font = QFont("微软雅黑", 10)
        self.note_content.setFont(font)

        # 工具栏
        toolbar = QToolBar("格式工具栏")
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        # 加粗按钮
        bold_action = QAction(QIcon(), "加粗", self)
        bold_action.triggered.connect(self.toggle_bold)
        toolbar.addAction(bold_action)

        # 斜体按钮
        italic_action = QAction(QIcon(), "斜体", self)
        italic_action.triggered.connect(self.toggle_italic)
        toolbar.addAction(italic_action)

        # 下划线按钮
        underline_action = QAction(QIcon(), "下划线", self)
        underline_action.triggered.connect(self.toggle_underline)
        toolbar.addAction(underline_action)

        # 字体按钮
        font_action = QAction(QIcon(), "字体", self)
        font_action.triggered.connect(self.change_font)
        toolbar.addAction(font_action)

        # 颜色按钮
        color_action = QAction(QIcon(), "颜色", self)
        color_action.triggered.connect(self.change_color)
        toolbar.addAction(color_action)

        # 按钮
        self.add_button = QPushButton('新增笔记')
        self.add_button.clicked.connect(self.add_note)

        self.delete_button = QPushButton('删除笔记')
        self.delete_button.clicked.connect(self.delete_note)

        self.save_as_button = QPushButton('另存为')
        self.save_as_button.clicked.connect(self.save_as)

        self.open_button = QPushButton('打开')
        self.open_button.clicked.connect(self.open_xml)

        self.rename_button = QPushButton('改名')  # 改名按钮
        self.rename_button.clicked.connect(self.rename_note)

        self.about_button = QPushButton('关于')  # 关于按钮
        self.about_button.clicked.connect(self.show_about)

        # 布局
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.note_list)
        left_layout.addWidget(self.add_button)
        left_layout.addWidget(self.delete_button)
        left_layout.addWidget(self.save_as_button)
        left_layout.addWidget(self.open_button)
        left_layout.addWidget(self.rename_button)  # 添加改名按钮
        left_layout.addWidget(self.about_button)  # 添加关于按钮

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.note_content)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 3)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # 支持 Ctrl+C 和 Ctrl+V
        self.note_content.keyPressEvent = self.custom_key_press_event

    def custom_key_press_event(self, event):
        # 处理 Ctrl+C 和 Ctrl+V
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_C:  # Ctrl+C
                self.note_content.copy()
            elif event.key() == Qt.Key_V:  # Ctrl+V
                self.paste_image_or_text()
        else:
            QTextEdit.keyPressEvent(self.note_content, event)

    def paste_image_or_text(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasImage():  # 粘贴图片
            self.paste_image()
        elif mime_data.hasText():  # 粘贴文本
            self.note_content.paste()

    def show_context_menu(self, pos):
        # 创建右键菜单
        context_menu = QMenu(self)

        # 添加菜单项
        undo_action = context_menu.addAction("撤销")
        undo_action.triggered.connect(self.note_content.undo)

        redo_action = context_menu.addAction("重做")
        redo_action.triggered.connect(self.note_content.redo)

        context_menu.addSeparator()

        copy_action = context_menu.addAction("复制")
        copy_action.triggered.connect(self.note_content.copy)

        paste_action = context_menu.addAction("粘贴")
        paste_action.triggered.connect(self.paste_image_or_text)

        context_menu.addSeparator()

        cut_action = context_menu.addAction("剪切")
        cut_action.triggered.connect(self.note_content.cut)

        delete_action = context_menu.addAction("删除")
        delete_action.triggered.connect(self.note_content.cut)  # 删除功能类似于剪切

        # 显示菜单
        context_menu.exec_(self.note_content.mapToGlobal(pos))

    def load_notes(self):
        try:
            self.tree = ET.parse(self.current_file)
            self.root = self.tree.getroot()
            self.note_list.clear()
            for note in self.root.findall('note'):
                title = note.find('title').text
                self.note_list.addItem(title)
        except FileNotFoundError:
            self.root = ET.Element('notes')
            self.tree = ET.ElementTree(self.root)

    def show_note_content(self):
        # 保存当前笔记内容
        if hasattr(self, 'current_note_title') and self.current_note_title:
            self.save_note()

        # 加载新笔记内容
        selected_item = self.note_list.currentItem()
        if selected_item:
            self.current_note_title = selected_item.text()
            for note in self.root.findall('note'):
                if note.find('title').text == self.current_note_title:
                    content = note.find('content').text
                    self.note_content.setHtml(content)  # 使用 setHtml 加载带格式的内容
                    break

    def save_note(self):
        if hasattr(self, 'current_note_title') and self.current_note_title:
            content = self.note_content.toHtml()  # 使用 toHtml 保存带格式的内容
            for note in self.root.findall('note'):
                if note.find('title').text == self.current_note_title:
                    note.find('content').text = content
                    break
            self.tree.write(self.current_file)

    def add_note(self):
        while True:
            title, ok = QInputDialog.getText(self, '新增笔记', '请输入笔记标题:')
            if not ok:
                return  # 用户取消输入

            # 检查标题是否重复
            if title in [self.note_list.item(i).text() for i in range(self.note_list.count())]:
                QMessageBox.warning(self, "错误", "笔记标题不能重复，请重新输入！")
            else:
                break

        self.note_list.addItem(title)
        new_note = ET.SubElement(self.root, 'note')
        ET.SubElement(new_note, 'title').text = title
        ET.SubElement(new_note, 'content').text = ''
        self.tree.write(self.current_file)

    def delete_note(self):
        selected_item = self.note_list.currentItem()
        if selected_item:
            title = selected_item.text()
            for note in self.root.findall('note'):
                if note.find('title').text == title:
                    self.root.remove(note)
                    break
            self.tree.write(self.current_file)
            self.note_list.takeItem(self.note_list.row(selected_item))

    def rename_note(self):
        selected_item = self.note_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "错误", "请先选择一个笔记！")
            return

        old_title = selected_item.text()
        while True:
            new_title, ok = QInputDialog.getText(self, '改名', '请输入新的笔记标题:', text=old_title)
            if not ok:
                return  # 用户取消输入

            # 检查标题是否重复
            if new_title == old_title:
                break  # 标题未修改，直接退出

            if new_title in [self.note_list.item(i).text() for i in range(self.note_list.count())]:
                QMessageBox.warning(self, "错误", "笔记标题不能重复，请重新输入！")
            else:
                break

        # 更新笔记标题
        selected_item.setText(new_title)
        for note in self.root.findall('note'):
            if note.find('title').text == old_title:
                note.find('title').text = new_title
                break
        self.tree.write(self.current_file)

    def save_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "另存为", "", "XML Files (*.xml);;All Files (*)", options=options)
        if file_name:
            self.tree.write(file_name)
            self.current_file = file_name
            self.setWindowTitle(f'笔记软件 v1.0 - {self.current_file}')  # 更新窗口标题

    def open_xml(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "打开", "", "XML Files (*.xml);;All Files (*)", options=options)
        if file_name:
            self.current_file = file_name
            self.setWindowTitle(f'笔记软件 v1.0 - {self.current_file}')  # 更新窗口标题
            self.load_notes()  # 重新加载笔记

    def show_about(self):
        # 显示关于信息
        QMessageBox.information(self, "关于", "开发者：sysucai\n411703730@qq.com")

    def change_font(self):
        cursor = self.note_content.textCursor()
        if cursor.hasSelection():
            # 设置默认字体为微软雅黑
            default_font = QFont("微软雅黑", 10)
            font, ok = QFontDialog.getFont(default_font, self, "选择字体")
            if ok:
                format = QTextCharFormat()
                format.setFont(font)
                cursor.mergeCharFormat(format)

    def change_color(self):
        cursor = self.note_content.textCursor()
        if cursor.hasSelection():
            color = QColorDialog.getColor()
            if color.isValid():
                format = QTextCharFormat()
                format.setForeground(color)
                cursor.mergeCharFormat(format)

    def toggle_bold(self):
        cursor = self.note_content.textCursor()
        if cursor.hasSelection():
            format = QTextCharFormat()
            if cursor.charFormat().fontWeight() == QFont.Bold:
                format.setFontWeight(QFont.Normal)
            else:
                format.setFontWeight(QFont.Bold)
            cursor.mergeCharFormat(format)

    def toggle_italic(self):
        cursor = self.note_content.textCursor()
        if cursor.hasSelection():
            format = QTextCharFormat()
            format.setFontItalic(not cursor.charFormat().fontItalic())
            cursor.mergeCharFormat(format)

    def toggle_underline(self):
        cursor = self.note_content.textCursor()
        if cursor.hasSelection():
            format = QTextCharFormat()
            format.setFontUnderline(not cursor.charFormat().fontUnderline())
            cursor.mergeCharFormat(format)

    def paste_image(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasImage():
            image = QImage(mime_data.imageData())
            # 将图片转换为 Base64 编码
            byte_array = QByteArray()
            buffer = QBuffer(byte_array)
            buffer.open(QIODevice.WriteOnly)
            image.save(buffer, "PNG")
            base64_data = base64.b64encode(byte_array.data()).decode('utf-8')

            # 插入图片到笔记内容
            cursor = self.note_content.textCursor()
            cursor.insertHtml(f'<img src="data:image/png;base64,{base64_data}" />')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteApp()
    ex.show()
    sys.exit(app.exec_())
