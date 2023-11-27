# main.py

import sys
from PyQt5.QtWidgets import QApplication
from farm_app import FarmSchedulerApp

def main():
    app = QApplication(sys.argv)
    window = FarmSchedulerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()