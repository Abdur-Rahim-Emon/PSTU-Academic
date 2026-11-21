import math
import sys
from PyQt6.QtCore import QUrl, Qt, QObject, QEvent
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QLineEdit, QPushButton, QToolBar,
    QStatusBar, QProgressBar, QStackedWidget
)
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile, QWebEnginePage

# Safe math dictionary for mathematical evaluation
SAFE_MATH_DICT = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sqrt": math.sqrt, "exp": math.exp, "log": math.log, "log10": math.log10,
    "pi": math.pi, "e": math.e, "abs": abs, "pow": pow
}

class GlobalHotkeyFilter(QObject):
    """Event filter to catch Ctrl+M globally, bypassing QWebEngineView focus absorption."""
    def __init__(self, window):
        super().__init__()
        self.window = window

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            if (event.modifiers() & Qt.KeyboardModifier.ControlModifier) and event.key() == Qt.Key.Key_M:
                self.window.toggle_view()
                return True
        return super().eventFilter(obj, event)


class CalculatorView(QWidget):
    """Full-screen Standard & Scientific Calculator widget."""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 40, 40, 40)
        self.setLayout(main_layout)

        # Title
        title = QLabel("Calculator")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(title)

        # Display screen
        self.display = QLineEdit()
        self.display.setPlaceholderText("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("""
            QLineEdit {
                font-size: 32px;
                padding: 15px;
                background-color: #f8f9fa;
                border: 2px solid #cccccc;
                border-radius: 8px;
            }
        """)
        self.display.returnPressed.connect(self.calculate_result)
        main_layout.addWidget(self.display)

        # Grid layout for calculator buttons
        grid = QGridLayout()
        grid.setSpacing(10)

        buttons = [
            ('C', 0, 0), ('⌫', 0, 1), ('(', 0, 2), (')', 0, 3), ('/', 0, 4),
            ('sin', 1, 0), ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('*', 1, 4),
            ('cos', 2, 0), ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('-', 2, 4),
            ('tan', 3, 0), ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('+', 3, 4),
            ('sqrt', 4, 0), ('0', 4, 1), ('.', 4, 2), ('**', 4, 3), ('=', 4, 4),
            ('log', 5, 0), ('pi', 5, 1), ('e', 5, 2), ('%', 5, 3), ('abs', 5, 4)
        ]

        for btn_text, r, c in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    font-weight: bold;
                    padding: 20px;
                    border-radius: 6px;
                    background-color: #e9ecef;
                    border: 1px solid #ced4da;
                }
                QPushButton:hover {
                    background-color: #dee2e6;
                }
                QPushButton:pressed {
                    background-color: #ced4da;
                }
            """)
            if btn_text == '=':
                btn.setStyleSheet("""
                    QPushButton {
                        font-size: 18px;
                        font-weight: bold;
                        padding: 20px;
                        border-radius: 6px;
                        background-color: #0d6efd;
                        color: white;
                        border: none;
                    }
                    QPushButton:hover {
                        background-color: #0b5ed7;
                    }
                """)
            btn.clicked.connect(self.on_button_click)
            grid.addWidget(btn, r, c)

        main_layout.addLayout(grid)
        main_layout.addStretch()

    def on_button_click(self):
        text = self.sender().text()

        if text == 'C':
            self.display.clear()
        elif text == '⌫':
            self.display.setText(self.display.text()[:-1])
        elif text == '=':
            self.calculate_result()
        elif text in ('sin', 'cos', 'tan', 'sqrt', 'log', 'abs'):
            self.display.setText(self.display.text() + f"{text}(")
        else:
            self.display.setText(self.display.text() + text)

    def calculate_result(self):
        expr = self.display.text().strip()
        if not expr:
            return

        try:
            context = {"__builtins__": {}}
            context.update(SAFE_MATH_DICT)
            result = eval(expr, context)
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")


class FullyFunctionalBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.home_url = "https://gemini.google.com"

        # Central layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Web view setup
        self.setup_browser_profile()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.home_url))

        # Calculator view
        self.calculator_view = CalculatorView()

        # Stacked Widget setup for full-screen switching
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.browser)          # Index 0: Gemini Page
        self.stacked_widget.addWidget(self.calculator_view)  # Index 1: Calculator Interface
        
        self.main_layout.addWidget(self.stacked_widget)

        # Window settings
        self.setWindowTitle("Gemini Desktop")
        self.resize(1200, 800)

        # UI elements
        self.create_toolbar()
        self.create_status_bar()
        self.setup_listeners()

    def setup_browser_profile(self):
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
        profile.setHttpUserAgent(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )

    def create_toolbar(self):
        navbar = QToolBar("Navigation")
        self.addToolBar(navbar)

        back_btn = QAction("◀", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("▶", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("🔄", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("🏠", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        navbar.addSeparator()

        self.toggle_btn = QAction("🧮 Calculator (Ctrl+M)", self)
        self.toggle_btn.triggered.connect(self.toggle_view)
        navbar.addAction(self.toggle_btn)

        navbar.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

    def create_status_bar(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumHeight(15)
        self.progress_bar.setMaximumWidth(150)

        self.setStatusBar(QStatusBar(self))
        self.statusBar().addPermanentWidget(self.progress_bar)

    def setup_listeners(self):
        self.browser.urlChanged.connect(self.update_url_bar)
        self.browser.titleChanged.connect(self.update_title)
        self.browser.loadProgress.connect(self.progress_bar.setValue)
        self.browser.loadFinished.connect(self.handle_load_finished)

    def toggle_view(self):
        """Switches full-screen between Gemini and the Scientific Calculator."""
        if self.stacked_widget.currentIndex() == 0:
            # Switch to Calculator
            self.stacked_widget.setCurrentIndex(1)
            self.calculator_view.display.setFocus()
            self.statusBar().showMessage("Calculator Active (Press Ctrl+M to return to Gemini)", 3000)
        else:
            # Switch back to Gemini Web View
            self.stacked_widget.setCurrentIndex(0)
            self.browser.setFocus()
            self.statusBar().showMessage("Gemini Desktop Active (Press Ctrl+M for Calculator)", 3000)

    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

    def update_title(self, title):
        if title and self.stacked_widget.currentIndex() == 0:
            self.setWindowTitle(f"{title} - Gemini Desktop")
        elif self.stacked_widget.currentIndex() == 1:
            self.setWindowTitle("Calculator")

    def handle_load_finished(self, success):
        if success:
            self.progress_bar.setValue(0)


if __name__ == "__main__":
    sys.argv.extend([
        "--no-sandbox",
        "--ignore-gpu-blocklist",
        "--enable-gpu-rasterization"
    ])

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = FullyFunctionalBrowser()
    
    # Global shortcut filter for Ctrl+M
    key_filter = GlobalHotkeyFilter(window)
    app.installEventFilter(key_filter)

    window.show()
    sys.exit(app.exec())