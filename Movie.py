import sys
from datetime import datetime

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QListWidget, QListWidgetItem, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class MediaSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Search")
        self.setGeometry(100, 100, 800, 600)  # Ana pencere boyutu ayarla
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        # Resim eklemek için QLabel
        pixmap = QPixmap("C:/Users/Bora/Desktop/Kodlar/AnimeRecommend/poster.jpg")
        image_label = QLabel(self)
        image_label.setPixmap(pixmap.scaledToWidth(300))  # Resmi genişlik olarak ölçeklendir
        image_label.setAlignment(Qt.AlignCenter)  # Resmi ortala
        main_layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Üst bilgi etiketi
        title_label = QLabel("Movie Recommendations", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setStyleSheet("color: #800080;")  # Başlık rengi
        main_layout.addWidget(title_label)

        # Kategori seçimi için ComboBox
        self.category_combobox = QComboBox(self)
        self.category_combobox.addItems(
            ["Top Rated Movies", "Top Rated Series", "Airing Today Series", "Popular Series", "Upcoming Movies"])
        self.category_combobox.setStyleSheet(
            "QComboBox { font-size: 16px; color: #333; background-color: #f0f0f0; border: 1px solid #ccc; padding: 5px; }")
        main_layout.addWidget(self.category_combobox)

        # Arama düğmesi
        search_button = QPushButton("Search", self)
        search_button.clicked.connect(self.search_button_clicked)
        search_button.setStyleSheet(
            "QPushButton { background-color: #800080; color: white; border: none; padding: 10px 20px; font-size: 16px; }"
            "QPushButton:hover { background-color: #45a049; }")  # Düğme hover rengi
        main_layout.addWidget(search_button)

        # Sonuçlar için liste görünümü
        self.results_list = QListWidget(self)
        self.results_list.setStyleSheet("QListWidget { font-size: 14px; border: 1px solid #ccc; }"
                                        "QListWidget::item { background-color: #f0f0f0; padding: 10px; }"
                                        "QListWidget::item:selected { background-color: #4CAF50; color: white; }")  # Seçili öğe rengi
        main_layout.addWidget(self.results_list)

        self.setLayout(main_layout)

    def fetch_data(self, url, params):
        response = requests.get(url, params=params)
        return response.json()['results']

    def print_media_results(self, media_type, results):
        dialog = QDialog(self)
        dialog.setWindowTitle("Search Results")
        dialog.setGeometry(self.geometry())  # Ana pencere boyutunda açılan pencere
        dialog_layout = QVBoxLayout(dialog)

        if media_type == 'movie':
            title_key = 'title'
            release_date_key = 'release_date'
            genre_url = "https://api.themoviedb.org/3/genre/movie/list"
        elif media_type == 'tv':
            title_key = 'name'
            release_date_key = 'first_air_date'
            genre_url = "https://api.themoviedb.org/3/genre/tv/list"

        api_key = "dc2cb6eba9dc7aa882ffe77d243ec2e3"

        for media_info in results:
            title = media_info[title_key]
            release_date = media_info[release_date_key]
            genre_ids = media_info['genre_ids']

            genres = []
            for genre_id in genre_ids:
                genre_response = requests.get(genre_url, params={"api_key": api_key})
                genre_data = genre_response.json()['genres']
                for genre in genre_data:
                    if genre['id'] == genre_id:
                        genres.append(genre['name'])

            genre_str = ", ".join(genres)

            details = f"Title: {title}\nRelease Date: {release_date}\nGenres: {genre_str}"
            item = QListWidgetItem(details)
            dialog_layout.addWidget(QLabel(details))

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def search_top_rated_movies(self):
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {"api_key": "dc2cb6eba9dc7aa882ffe77d243ec2e3"}
        movies = self.fetch_data(url, params)
        self.print_media_results('movie', movies)

    def search_top_rated_series(self):
        url = "https://api.themoviedb.org/3/tv/top_rated"
        params = {"api_key": "dc2cb6eba9dc7aa882ffe77d243ec2e3"}
        series = self.fetch_data(url, params)
        self.print_media_results('tv', series)

    def search_airing_today_series(self):

        url = "https://api.themoviedb.org/3/tv/airing_today"
        params = {"api_key": "dc2cb6eba9dc7aa882ffe77d243ec2e3"}
        series = self.fetch_data(url, params)
        self.print_media_results('tv', series)

    def search_popular_series(self):
        url = "https://api.themoviedb.org/3/tv/popular"
        params = {"api_key": "dc2cb6eba9dc7aa882ffe77d243ec2e3"}
        series = self.fetch_data(url, params)
        self.print_media_results('tv', series)

    def search_upcoming_movies(self):

        url = "https://api.themoviedb.org/3/movie/upcoming"
        params = {"api_key": "dc2cb6eba9dc7aa882ffe77d243ec2e3"}
        movies = self.fetch_data(url, params)
        self.print_media_results('movie', movies)

    def search_button_clicked(self):
        selected_category = self.category_combobox.currentText().lower()
        if selected_category == "top rated movies":
            self.search_top_rated_movies()
        elif selected_category == "top rated series":
            self.search_top_rated_series()
        elif selected_category == "airing today series":
            self.search_airing_today_series()
        elif selected_category == "popular series":
            self.search_popular_series()
        elif selected_category == "upcoming movies":
            self.search_upcoming_movies()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaSearchApp()
    window.show()
    sys.exit(app.exec_())
