import pygame

def play(audio_file):
    """
    Play an audio file using pygame with a simple function call.
    :param audio_file: Path to the audio file (e.g., .mp3, .wav).
    """
    try:
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load the audio file
        pygame.mixer.music.load(audio_file)

        # Play the audio file
        pygame.mixer.music.play()

        # Keep the program running until the music stops
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Avoid busy-waiting
    except Exception as e:
        print(f"Error playing audio file: {e}")
