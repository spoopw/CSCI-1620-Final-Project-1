from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.setGeometry(100, 100, 300, 100)
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
