from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
from Anime import AnimeApp
from Movie import MediaSearchApp


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setFixedSize(700, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)

        layout = QGridLayout()

        # Anime section
        anime_image_label = QLabel(self)
        anime_pixmap = QPixmap("spritedaway.jpg").scaled(300, 500, aspectRatioMode=Qt.KeepAspectRatio)
        anime_image_label.setPixmap(anime_pixmap)
        anime_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(anime_image_label, 0, 0, 1, 1, alignment=Qt.AlignCenter)

        anime_button = QPushButton("Anime", self)
        anime_button.setFixedSize(300, 60)
        anime_button.setStyleSheet("""
            QPushButton {
                font-size: 20px; /* Decreased font size to fit within the button */
                color: #fff;
                background-color: #ff6347;
                border: none;
                padding: 10px; /* Decreased padding */
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #ff4500;
            }
        """)
        anime_button.clicked.connect(self.openAnimeApp)
        layout.addWidget(anime_button, 1, 0, 1, 1, alignment=Qt.AlignCenter)  # row=1, col=0, rowspan=1, colspan=1

        # Movie section
        movie_image_label = QLabel(self)
        movie_pixmap = QPixmap("silence_of_the_lambs_1_.jpg").scaled(300, 500, aspectRatioMode=Qt.KeepAspectRatio)
        movie_image_label.setPixmap(movie_pixmap)
        movie_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(movie_image_label, 0, 1, 1, 1, alignment=Qt.AlignCenter)  #

        movie_button = QPushButton("Movies", self)
        movie_button.setFixedSize(300, 60)
        movie_button.setStyleSheet("""
            QPushButton {
                font-size: 20px; /* Decreased font size to fit within the button */
                color: #fff;
                background-color: #4682b4;
                border: none;
                padding: 10px; /* Decreased padding */
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1e90ff;
            }
        """)
        movie_button.clicked.connect(self.openMovieApp)
        layout.addWidget(movie_button, 1, 1, 1, 1, alignment=Qt.AlignCenter)

        main_layout.addLayout(layout)
        self.setLayout(main_layout)

    def openAnimeApp(self):
        self.anime_app = AnimeApp()
        self.anime_app.show()
        self.hide()

    def openMovieApp(self):
        self.movie_app = MediaSearchApp()
        self.movie_app.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())