"""
CipherSafe Menu System (menu.py)
--------------------------------
Defines the interactive terminal menu structure used throughout CipherSafe.
Provides reusable menu utilities for navigation, validation, and display.
"""

import os
import sys
import time

class Menu:
    """Simple text-based menu handler."""

    def __init__(self, title, options):
        """
        Initialize a menu screen.

        Args:
            title (str): Menu title displayed at the top.
            options (list[str]): List of selectable options.
        """
        self.title = title
        self.options = options

    def clear(self):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        """Display the formatted menu options."""
        self.clear()
        print("=" * 60)
        print(f"{self.title.center(60)}")
        print("=" * 60)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print("=" * 60)

    def get_choice(self):
        """
        Display menu and capture the user’s choice.

        Returns:
            int: Index of selected menu option.
        """
        while True:
            self.display()
            try:
                choice = int(input("Select an option: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid selection. Try again.")
                    time.sleep(1)
            except ValueError:
                print("Please enter a number.")
                time.sleep(1)

    def pause(self):
        """Pause before returning to previous menu."""
        input("\nPress Enter to continue...")

# Quick menu demo (optional)
if __name__ == "__main__":
    demo_menu = Menu("CipherSafe Demo Menu", ["Encrypt Message", "Decrypt Message", "Exit"])
    choice = demo_menu.get_choice()
    print(f"You selected: {demo_menu.options[choice-1]}")
