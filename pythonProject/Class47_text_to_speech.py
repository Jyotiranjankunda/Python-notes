import os

if __name__ == '__main__':
    print("Welcome to PyBot")

    while True:
        s = input("Enter some text : ")
        if s == "quit":
            break

        command = f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');\""
        os.system(command)
