"""
CipherSafe Episodes (episodes.py)
---------------------------------
Encapsulates mission-level metadata for the CipherSafe storyline.
Each episode defines its title, cipher type, learning objectives, and narrative overview.
"""

class Episode:
    """Represents one narrative mission episode."""
    def __init__(self, number, title, cipher_used, threat_level, objective, summary):
        self.number = number
        self.title = title
        self.cipher_used = cipher_used
        self.threat_level = threat_level
        self.objective = objective
        self.summary = summary
        self.completed = False

    def details(self):
        """Return formatted mission info."""
        return (
            f"Episode {self.number}: {self.title}\n"
            f"Cipher Used: {self.cipher_used}\n"
            f"Threat Level: {self.threat_level}\n"
            f"Objective: {self.objective}\n"
            f"Summary: {self.summary}\n"
            f"Status: {'COMPLETED' if self.completed else 'IN PROGRESS'}\n"
        )


class EpisodeManager:
    """Manages all storyline episodes and their progress."""
    def __init__(self):
        self.episodes = self._load_episodes()
        self.current_episode = 0

    def _load_episodes(self):
        """Define all episodes and their core narrative data."""
        return [
            Episode(1, "Silent Footsteps in Neo-Berlin", "Vigenère", "Low",
                    "Establish secure HQ communication.", 
                    "ZOE begins mission setup using the Vigenère cipher."),
            Episode(2, "Echo in the Circuits", "Vigenère", "Medium",
                    "Investigate possible mole and cipher breach.", 
                    "HQ detects irregular encrypted patterns linked to INZA."),
            Episode(3, "Shadows Split", "Vernam OTP", "High",
                    "Transmit high-risk intelligence to HQ.", 
                    "ZOE switches to one-time pad encryption for critical secrets."),
            Episode(4, "Betrayal at Checkpoint 47", "Vernam OTP + Steganography", "Critical",
                    "Extract intel and expose traitor hiding within communications network.",
                    "Messages now hidden inside images to evade AI detection."),
            Episode(5, "Operation Black Dawn", "Vernam OTP + Steganography", "Maximum",
                    "Neutralize INZA’s quantum command systems.",
                    "Final mission — destroy enemy communication core.")
        ]

    def get_episode(self, number):
        """Return an episode by number."""
        for ep in self.episodes:
            if ep.number == number:
                return ep
        return None

    def mark_completed(self, number):
        """Mark an episode as completed."""
        episode = self.get_episode(number)
        if episode:
            episode.completed = True
            return True
        return False

    def show_progress(self):
        """Display all episode completion states."""
        report_lines = []
        for ep in self.episodes:
            status = "✓ Completed" if ep.completed else "→ Pending"
            report_lines.append(f"{ep.number}. {ep.title} [{status}]")
        print("\n".join(report_lines))

    def unlock_next(self):
        """
        Unlocks the next uncompleted episode, returns it for continuation.
        """
        for ep in self.episodes:
            if not ep.completed:
                return ep
        return None


if __name__ == "__main__":
    manager = EpisodeManager()
    print("=== CipherSafe Episode Overview ===")
    manager.show_progress()
    next_ep = manager.unlock_next()
    print("\nNext Episode:\n", next_ep.details())
