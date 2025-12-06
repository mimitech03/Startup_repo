import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QFileDialog, QTextEdit, QComboBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class BackupGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Automated File Backup System")
        self.setGeometry(200, 200, 550, 450)

        
        self.setStyleSheet("""
            background-color: #F2F5F9; /* light grey/blue */
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        
        label_style = """
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #2C3E50;
            }
        """

        
        button_style = """
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 10px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2E86C1;
            }
            QPushButton:pressed {
                background-color: #1F618D;
            }
        """

        
        dropdown_style = """
            QComboBox {
                padding: 8px;
                border: 2px solid #3498DB;
                border-radius: 8px;
                font-size: 14px;
            }
        """

        
        logbox_style = """
            QTextEdit {
                background-color: white;
                border: 2px solid #D6DBDF;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
        """

        
        self.source_label = QLabel("Source Folder: Not Selected")
        self.source_label.setStyleSheet(label_style)
        layout.addWidget(self.source_label)

        self.source_btn = QPushButton("Select Source Folder")
        self.source_btn.setStyleSheet(button_style)
        self.source_btn.clicked.connect(self.select_source)
        layout.addWidget(self.source_btn)

        
        self.dest_label = QLabel("Destination Folder: Not Selected")
        self.dest_label.setStyleSheet(label_style)
        layout.addWidget(self.dest_label)

        self.dest_btn = QPushButton("Select Destination Folder")
        self.dest_btn.setStyleSheet(button_style)
        self.dest_btn.clicked.connect(self.select_destination)
        layout.addWidget(self.dest_btn)

        
        self.schedule_dropdown = QComboBox()
        self.schedule_dropdown.addItems(["Daily", "Weekly", "Custom"])
        self.schedule_dropdown.setStyleSheet(dropdown_style)
        layout.addWidget(self.schedule_dropdown)

        
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet(logbox_style)
        layout.addWidget(self.log_box)

        self.setLayout(layout)

    def select_source(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if folder:
            self.source_label.setText(f"Source Folder: {folder}")

    def select_destination(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if folder:
            self.dest_label.setText(f"Destination Folder: {folder}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackupGUI()
    window.show()
    sys.exit(app.exec_())