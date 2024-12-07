import whisper
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Create a file selection dialog
def select_file():
    # Ensure the root Tkinter window doesn't show
    root = Tk()
    root.withdraw()  # Hide the root window
    root.update()  # Prevent the window from freezing
    # Open file dialog
    file_path = askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.ogg *.mp3 *.wav *.opus")]
    )
    root.destroy()  # Clean up the Tkinter root window
    print("Selected file:")
    print(file_path)
    return file_path

# Let the user select a file
file_name = select_file()

if not file_name:
    print("No file selected. Exiting...")
else:
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the selected audio file
    result = model.transcribe(file_name)

    # Print the transcribed text
    print(result["text"])
