# Predictive Video Call

The Predictive Video Call application is a cutting-edge solution designed to revolutionize the way we conduct video calls. By integrating Qt for the user interface, Python for backend processing, and OpenCV for face detection, this application not only facilitates video communication but also enhances it by providing real-time face position tracking. The project aims to offer a more interactive and engaging video calling experience.

## Key Features

- **Real-Time Face Detection**: Utilizes OpenCV to detect and display the position of the face during the call, enhancing user interaction.
- **Interactive UI**: Built with Qt, the application boasts a user-friendly interface with buttons to start and end calls, and a display field for face position.
- **Cross-Platform**: Compatible with various operating systems thanks to the use of Qt and Python, ensuring a wide range of device support.

## Getting Started

Follow these instructions to get the Predictive Video Call application up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Qt 5.x
- OpenCV-Python package
- A C++ compiler (for Qt)

### Installing

1. **Clone the repository**:
    ```bash
    git clone https://github.com/johnasatryan/PredictiveVideoCall.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd PredictiveVideoCall
    ```

3. **Install Python dependencies** (ensure pip is installed):
    ```bash
    pip install -r requirements.txt
    ```

4. **Build the Qt application**:
    - Open the project in Qt Creator and build the project, or use the command line:
        ```bash
        qmake && make
        ```

### Running the Application

- Launch the application from Qt Creator or from the command line after building:
    ```bash
    ./PredictiveVideoCall
    ```

## Built With

- [Qt](https://www.qt.io/) - The GUI framework used.
- [Python](https://www.python.org/) - Backend programming language.
- [OpenCV](https://opencv.org/) - Used for real-time face detection.

## Contributing

Contributions to improve Predictive Video Call are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used as inspiration.
- The Qt Community for their comprehensive documentation.
- The OpenCV team for making computer vision accessible to the masses.
