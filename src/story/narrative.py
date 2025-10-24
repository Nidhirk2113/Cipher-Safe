"""
CipherSafe Narrative Controller (narrative.py)
----------------------------------------------
Manages storyline flow between characters and episodes.
Presents dialogues, mission updates, and learning cues to the player.
"""

from story.characters import AgentZOE, AgentMISATO, INZA
from story.episodes import EpisodeManager
import time

class NarrativeController:
    """
    Drives progression through episodes and dialogue among characters.
    Integrates cryptographic tasks with unfolding missions.
    """

    def __init__(self):
        self.zoe = AgentZOE()
        self.misato = AgentMISATO()
        self.inza = INZA()
        self.episodes = EpisodeManager()

    def _speak(self, character, text, delay=1.5):
        """Simulate dialogue pacing."""
        print(f"{character.codename}: {text}")
        time.sleep(delay)

    def start_prologue(self):
        """Show introductory story context."""
        print("\n=== PROLOGUE ===")
        self._speak(self.misato, "Welcome, Agent ZOE. The network's been compromised.")
        self._speak(self.misato, "Your mission: restore secure channels—before INZA deciphers our systems.")
        self._speak(self.zoe, "Understood. Initiating CipherSafe protocol.")
        self._speak(self.misato, "This will be a dangerous one. Stay encrypted, Ghost.")

    def play_episode(self, number):
        """Play narrative for a specific episode."""
        ep = self.episodes.get_episode(number)
        if not ep:
            print("Invalid episode number.")
            return

        print(f"\n=== Episode {ep.number}: {ep.title} ===")
        self._speak(self.misato, f"Mission objective: {ep.objective}")
        self._speak(self.zoe, "Preparing encryption systems...")
        if "Vigenère" in ep.cipher_used:
            self._speak(self.zoe, "Engaging polyalphabetic cipher channel.")
        if "Vernam" in ep.cipher_used:
            self._speak(self.zoe, "Switching to one-time pads.")
        if "Steganography" in ep.cipher_used:
            self._speak(self.zoe, "Embedding encrypted payload in image file...")

        self._speak(self.inza, "You can't hide in the noise forever, Ghost...")
        self.episodes.mark_completed(ep.number)
        print("\n[Mission Completed]")
        time.sleep(1)

    def continue_story(self):
        """Handle automatic mission progression through all episodes."""
        self.start_prologue()
        while True:
            episode = self.episodes.unlock_next()
            if not episode:
                print("\n=== ALL MISSIONS COMPLETE ===")
                print("INZA neutralized. CipherSafe protocol integrity secured.")
                break
            self.play_episode(episode.number)


if __name__ == "__main__":
    story = NarrativeController()
    story.continue_story()
