from pynput import keyboard
import pygame
import os
import sys

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Load song
try:
    song_path = os.path.join(os.path.dirname(__file__), "song.mp3")
    song = pygame.mixer.Sound(song_path)
except pygame.error:
    print("⚠️ Error: 'song.mp3' not found or not playable.")
    sys.exit(1)

print("🎧 Welcome to the Button Check Script!")
print("🔘 Press any key to play the sound.")
print("❌ Press 'q' to quit.")

def on_press(key):
    """Handle key press event."""
    if key == keyboard.Key.f11:
        print("✨ EUREKA!!!")
    else:
        song.play()

def on_release(key):
    """Handle key release event."""
    print(f"Key released: {key}")
    if key == keyboard.KeyCode.from_char('q'):
        print("👋 Exiting program.")
        return False
    if key == keyboard.Key.f11:
        print("✨ EUREKA!!!")

# Start listener
if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
