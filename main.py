import os
os.system("pip install pyqt5")#download pyqt5

import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QComboBox  
from PyQt5.QtCore import QTimer, QTime  
from PyQt5.QtGui import QFont  
  
class TimerWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
  
        self.initUI()  
  
    def initUI(self):  
        self.setWindowTitle('计时器')  
        self.setGeometry(100, 100, 400, 300)  
  
        central_widget = QWidget(self)  
        self.setCentralWidget(central_widget)  
  
        layout = QVBoxLayout(central_widget)  
  
        # Language selection  
        self.language_combo = QComboBox(self)  
        self.language_combo.addItems(['English', '中文'])  
        self.language_combo.currentIndexChanged.connect(self.change_language)  
        layout.addWidget(self.language_combo)  
  
        # Timer controls  
        self.start_stop_button = QPushButton(self.get_translated_text('Start/Stop Timer'), self)  
        self.start_stop_button.clicked.connect(self.toggle_timer)  
        layout.addWidget(self.start_stop_button)  
  
        # Fullscreen controls (not fully implemented for simplicity)  
        self.full_screen_button = QPushButton(self.get_translated_text('Go Fullscreen'), self)  
        self.full_screen_button.clicked.connect(self.toggle_fullscreen)  # Placeholder for fullscreen functionality  
        layout.addWidget(self.full_screen_button)  
  
        # Timer display  
        self.time_label = QLabel('00:00:00', self)  
        layout.addWidget(self.time_label)  
  
        # Setup timers  
        self.timer = QTimer(self)  
        self.timer.timeout.connect(self.update_time)  
  
        # Initial timer state  
        self.timer_running = False  
  
        # Set a font that supports both English and Chinese  
        font = QFont()  
        font.setFamily('Microsoft YaHei')  # Or any other font that supports Chinese  
        font.setPointSize(12)  
        self.setFont(font)  # Set the font for the main window, which will propagate to child widgets  
  
    def toggle_timer(self):  
        if self.timer_running:  
            self.timer.stop()  
            self.start_stop_button.setText(self.get_translated_text('Start Timer'))  
        else:  
            self.timer.start(1000)  # Update time every 1000 ms (1 second)  
            self.start_stop_button.setText(self.get_translated_text('Stop Timer'))  
        self.timer_running = not self.timer_running  
  
    def update_time(self):  
        # Placeholder for actual time updating logic  
        # Here we just display a static time for demonstration  
        self.time_label.setText('00:01:00')  # In a real application, you would update this based on elapsed time  
  
    def toggle_fullscreen(self):  
        # Placeholder for fullscreen functionality  
        # In a real application, you would implement this to toggle fullscreen mode  
        pass  
  
    def get_translated_text(self, text):  
        # Simple translation function based on the current language selection  
        # In a real application, you might use a more sophisticated translation system  
        index = self.language_combo.currentIndex()  
        if index == 0:  # English  
            return text  
        elif index == 1:  # Chinese  
            translations = {  
                'Start/Stop Timer': '开始/停止计时器',  
                'Go Fullscreen': '全屏显示',  
                'Stop Timer': '停止计时器',  
                'Start Timer': '开始计时器'  
            }  
            return translations.get(text, text)  # Fallback to original text if no translation is found  
  
# Main function to run the application  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = TimerWindow()  
    ex.show()  
    sys.exit(app.exec_())
