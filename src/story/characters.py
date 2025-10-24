"""
CipherSafe Character Definitions (characters.py)
------------------------------------------------
Defines main story characters used throughout the CipherSafe narrative.
Each character includes name, role, code name, and personality traits.
"""

class Character:
    """Generic character base class."""
    def __init__(self, name, codename, role, description):
        self.name = name
        self.codename = codename
        self.role = role
        self.description = description

    def profile(self):
        """Return a formatted string of the character’s identity."""
        return (
            f"Name: {self.name}\n"
            f"Codename: {self.codename}\n"
            f"Role: {self.role}\n"
            f"Description: {self.description}\n"
        )

# --- Primary Cast ---

class AgentZOE(Character):
    def __init__(self):
        super().__init__(
            name="Agent ZOE",
            codename="Cipher Ghost",
            role="Field Operative",
            description=(
                "A skilled cryptanalyst turned spy; she seeks unbreakable encryption. "
                "Her mission: protect classified intel from the rogue AI network—INZA."
            )
        )

class AgentMISATO(Character):
    def __init__(self):
        super().__init__(
            name="Agent MISATO",
            codename="Oracle",
            role="HQ Intelligence Handler",
            description=(
                "Veteran cryptographer and intelligence coordinator. "
                "ZOE’s handler at HQ, specializing in cipher operations."
            )
        )

class INZA(Character):
    def __init__(self):
        super().__init__(
            name="INZA",
            codename="Network Phantom",
            role="AI Antagonist",
            description=(
                "A self-aware artificial intelligence built from stolen research. "
                "Now seeks to reveal all government secrets in the name of ‘transparency.’"
            )
        )

if __name__ == "__main__":
    zoe = AgentZOE()
    misato = AgentMISATO()
    inza = INZA()
    print("=== CipherSafe Character Profiles ===")
    for c in [zoe, misato, inza]:
        print(c.profile())
