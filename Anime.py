from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QComboBox, QHBoxLayout, QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import requests
import random

class AnimeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OtakuSuggest")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.title_label = QLabel("OtakuSuggester", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; color: #333; margin-top: 20px;")
        self.layout.addWidget(self.title_label)


        mainframe_image = QLabel(self)
        pixmap_mainframe = QPixmap("mainframe.png")
        mainframe_image.setPixmap(pixmap_mainframe)
        mainframe_image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(mainframe_image)

        self.anime_image_label = QLabel(self)
        self.anime_image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.anime_image_label)

        self.info_textedit = QTextEdit(self)
        self.info_textedit.setReadOnly(True)
        self.info_textedit.setStyleSheet("font-size: 14px; color: #333;")
        self.layout.addWidget(self.info_textedit)

        self.genre_layout = QHBoxLayout()
        self.layout.addLayout(self.genre_layout)

        genre_label = QLabel("Select Genre:", self)
        genre_label.setStyleSheet("font-size: 16px; color: #555; margin-right: 10px;")
        self.genre_layout.addWidget(genre_label)

        self.genre_combobox = QComboBox(self)
        self.genre_combobox.addItem("Action")
        self.genre_combobox.addItem("Adventure")
        self.genre_combobox.addItem("Comedy")
        self.genre_combobox.addItem("Drama")
        self.genre_combobox.addItem("Fantasy")
        self.genre_combobox.addItem("Horror")
        self.genre_combobox.addItem("Mystery")
        self.genre_combobox.addItem("Romance")
        self.genre_combobox.addItem("Sci-Fi")
        self.genre_combobox.setStyleSheet("font-size: 16px; color: #333; padding: 5px;")
        self.genre_layout.addWidget(self.genre_combobox)

        self.genre_button = QPushButton("Show Anime", self)
        self.genre_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                color: #fff;
                background-color: #007bff;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.genre_button.clicked.connect(self.showGenreAnime)
        self.genre_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.genre_button, alignment=Qt.AlignRight)

        random_anime_button = QPushButton("Get Random Anime", self)
        random_anime_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                color: #fff;
                background-color: #28a745;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        random_anime_button.clicked.connect(self.getRandomAnime)
        random_anime_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(random_anime_button, alignment=Qt.AlignRight)

        self.setLayout(self.layout)

    def getRandomAnime(self):
        try:
            randomID = random.randint(1, 2500)
            url = f"https://api.jikan.moe/v4/anime/{randomID}"

            response = requests.get(url)
            response.raise_for_status()

            anime_data = response.json()['data']

            title = anime_data['title']
            genres = ', '.join(genre['name'] for genre in anime_data['genres'])
            theme_names = ', '.join(theme['name'] for theme in anime_data['themes'])
            episodes = anime_data['episodes']
            status = anime_data['status']
            mal_score = anime_data['score']
            rating = anime_data['rating']
            popularity = anime_data['popularity']
            year = anime_data['year']
            synopsis = anime_data['synopsis']
            image_url = anime_data['images']['jpg']['large_image_url']


            image_data = requests.get(image_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaledToHeight(500)
            pixmap = pixmap.scaledToWidth(300)

            info = f"Title: {title}\nGenres: {genres}\nThemes: {theme_names}\nEpisodes: {episodes}\nStatus: {status}\nMyAnimeList Score: {mal_score}\nRating: {rating}\nPopularity Rank: {popularity}\nYear Released: {year}\nSynopsis:\n{synopsis}"


            dialog = QDialog(self)
            dialog.setWindowTitle("Random Anime Details")
            dialog.setGeometry(100, 100, 800, 950)
            dialog_layout = QVBoxLayout()


            info_label = QLabel("Anime Information", dialog)
            info_label.setAlignment(Qt.AlignCenter)
            info_label.setStyleSheet("font-size: 24px; color: #333; margin-top: 20px;")
            dialog_layout.addWidget(info_label)


            image_label = QLabel(dialog)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)
            dialog_layout.addWidget(image_label)


            info_textedit = QTextEdit(dialog)
            info_textedit.setReadOnly(True)
            info_textedit.setStyleSheet("font-size: 14px; color: #333;")
            info_textedit.setPlainText(info)
            dialog_layout.addWidget(info_textedit)

            dialog.setLayout(dialog_layout)
            dialog.exec_()

        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Error", f"Failed to fetch data: {str(e)}")

    def showGenreAnime(self):
        genre = self.genre_combobox.currentText().lower()
        genre_ids = {
            "action": 1,
            "adventure": 2,
            "comedy": 4,
            "drama": 8,
            "fantasy": 10,
            "horror": 14,
            "mystery": 7,
            "romance": 22,
            "sci-fi": 24
        }
        genre_id = genre_ids.get(genre)
        if genre_id is None:
            QMessageBox.warning(self, "Error", "Genre ID not found.")
            return

        anime_data = self.get_anime_by_genre(genre_id)
        if anime_data and 'data' in anime_data:
            self.displayAnimeList(anime_data['data'])
        else:
            QMessageBox.warning(self, "Error", "Failed to fetch anime data.")

    def get_anime_by_genre(self, genre_id):
        url = f"https://api.jikan.moe/v4/anime?genres={genre_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            QMessageBox.warning(self, "Error", f"Failed to fetch data: {e}")
            return None

    def displayAnimeList(self, anime_list):
        self.clearLayout(self.layout)
        self.layout.addWidget(self.title_label)
        self.layout.addLayout(self.genre_layout)
        self.layout.addWidget(self.genre_button, alignment=Qt.AlignRight)

        num_columns = 4
        row_layout = None
        for index, anime in enumerate(anime_list):
            if index % num_columns == 0:
                if row_layout:
                    self.layout.addSpacing(20)
                row_layout = QHBoxLayout()
                self.layout.addLayout(row_layout)

            title = anime['title']
            image_url = anime['images']['jpg']['large_image_url']

            image_data = requests.get(image_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            pixmap = pixmap.scaledToWidth(150)

            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)

            title_label = QLabel(title, self)
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setStyleSheet("font-size: 12px; color: #333;")

            item_layout = QVBoxLayout()
            item_layout.addWidget(image_label, alignment=Qt.AlignCenter)
            item_layout.addWidget(title_label, alignment=Qt.AlignCenter)

            row_layout.addLayout(item_layout)


        self.adjustSize()

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QPushButton:hover {
            background-color: #0056b3;
        }
        QPushButton#genreButton {
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton#randomAnimeButton {
            font-size: 16px;
            color: #fff;
            background-color: #28a745;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton#randomAnimeButton:hover {
            background-color: #218838;
        }
    """)
    window = AnimeApp()
    window.show()
    sys.exit(app.exec_())
