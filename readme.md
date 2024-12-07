# Audio to Text Converter 🎙️➡️📜
This project is a simple voice-to-text converter powered by Whisper. It enables you to effortlessly transcribe audio files into text with just a few clicks.

## Features ✨
- Easy to Use: A pop-up window lets you select your audio file.
- Accurate Transcription: Leverages OpenAI's Whisper for high-quality text conversion.
- Standalone Executable: No need to install Python or dependencies—just run the executable!
How It Works 🛠️
## Run the executable file.
A pop-up window will appear, prompting you to select an audio file.
The application will process the audio using Whisper and generate the transcribed text.
How to Create a New Executable 🔧
If you want to create a new version of the executable, follow these steps:

##### Ensure PyInstaller is installed:

```bash
pip install pyinstaller
```
Generate the executable:

```bash
pyinstaller --onefile whisper_try.py
```

The new executable will be located in the dist/ folder. Simply run it to use the application.

### Requirements 📋
To run the project as a Python script, make sure you have:

Python 3.7 or higher installed
Required dependencies:
```bash
pip install -r requirements.txt
```
## Contribution 🤝
Feel free to fork this repository and make improvements! Pull requests are welcome.

## License 📜
This project is licensed under the MIT License.

Let me know if you need further enhancements! 😊







