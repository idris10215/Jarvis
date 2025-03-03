# Jarvis - Personal Voice Assistant

Jarvis is a simple voice assistant built using Python that can open websites, perform Google searches, and respond to voice commands.

## Features
✅ Wake word activation ("Jarvis")  
✅ Open common websites (Google, YouTube, Facebook, Instagram, LinkedIn)  
✅ Perform Google searches via voice input  
✅ Exit the assistant by saying "exit" or "stop"  
✅ Text-to-speech (TTS) responses  
✅ Error handling for better user experience  

## Installation
### Prerequisites
Ensure you have Python installed (version 3.6 or later). You also need the following Python libraries:

```bash
pip install SpeechRecognition pyttsx3 webbrowser
```

### Clone the Repository
```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

## Usage
Run the script using:
```bash
python jarvis.py
```

### How to Use
1. Run the script.
2. Say **"Jarvis"** to activate.
3. Give a command such as:
   - "Open Google"
   - "Search for Python tutorials"
   - "Exit" (to stop the assistant)

## Code Overview
- **speech_recognition**: Captures and processes voice input.
- **pyttsx3**: Provides text-to-speech functionality.
- **webbrowser**: Opens specified URLs in the default browser.

## Contributing
Contributions are welcome! If you have ideas for improvements or additional features, feel free to fork the repository and submit a pull request.

---
🚀 Feel free to contribute and enhance the assistant!

