# python PyQt5 weather_Gui.py
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import Qt
import requests


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vabox = QVBoxLayout()
        vabox.addWidget(self.city_label)
        vabox.addWidget(self.city_input)
        vabox.addWidget(self.get_weather_button)
        vabox.addWidget(self.temperature_label)
        vabox.addWidget(self.emoji_label)
        vabox.addWidget(self.description_label)

        self.setLayout(vabox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_button.setObjectName("get_weather_button")

        self.setStyleSheet(
            """
            QLabel, QPushButton{
                font-family: calibri;               
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 30px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 70px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }

        """
        )

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key = "Your own api key"
        city = self.city_input.text()
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error(
                        "Bad Request:\nPlease check the city name and try again."
                    )
                case 401:
                    self.display_error("Unauthorized:\nPlease check your API key.")
                case 403:
                    self.display_error(
                        "Forbidden:\nYou do not have permission to access this resource."
                    )
                case 404:
                    self.display_error(
                        "City Not Found:\nPlease check the city name and try again."
                    )
                case 500:
                    self.display_error(
                        "Internal Server Error:\nThe server encountered an error. Please try again later."
                    )
                case 502:
                    self.display_error(
                        "Bad Gateway:\nThe server received an invalid response. Please try again later."
                    )
                case 503:
                    self.display_error(
                        "Service Unavailable:\nThe server is currently unavailable. Please try again later."
                    )
                case 504:
                    self.display_error(
                        "Gateway Timeout:\nThe server took too long to respond. Please try again later."
                    )
                case _:
                    self.display_error(f"HTTP Error Occured: {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error(
                "Network Error:\nPlease check your internet connection and try again."
            )
        except requests.exceptions.Timeout:
            self.display_error(
                "Request Timed Out:\nThe request took too long to complete. Please try again later."
            )
        except requests.exceptions.TooManyRedirects:
            self.display_error(
                "Too Many Redirects:\nThe request was redirected too many times. Please check the URL and try again."
            )
        except requests.exceptions.RequestException as re_error:
            self.display_error(f"An Error Occured: {re_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        weather_description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(
            f"{temperature_celsius:.0f} °C / {temperature_fahrenheit:.0f} °F"
        )

        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id < 232:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id < 321:
            return "🌦️"  # Drizzle
        elif 500 <= weather_id < 531:
            return "🌧️"  # Rain
        elif 600 <= weather_id < 622:
            return "❄️"  # Snow
        elif 700 <= weather_id <= 741:
            return "🌫️"  # Fog
        elif weather_id == 762:
            return "🌋"  # Volcanic Ash
        elif weather_id == 771:
            return "💨"  # Squall
        elif weather_id == 800:
            return "☀️"  # Clear
        elif 801 <= weather_id < 804:
            return "☁️"  # Clouds
        else:
            return "🌈"  # Unknown


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
