"""
Single responsibility principle(a.k.a Separation of concerns).
A class should have on primary responsibility and should not take any other responsibilities.
"""


# Example
class Journal:
    def __init__(self):
        self.count = 0
        self.entries = []

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(self):
        return "\n".join(self.entries)

    # Example breaking the Single responsibility principle will be by adding
    # persistence handling to this object
    # def save_to_file(self):
    #     """Saves the entries to a file """
    #
    # def load_from_file(self):
    #     """Loads the entries from a file """
    #
    # def load_from_uri(self, link):
    #     """Loads entries from an uri"""


# The appropriate way would be to create a separate class which will handle the persistance of objects
# as per below
class PersistenceHandler:
    @staticmethod
    def save_to_file(text):
        """Saves the entries to a file """
        with open("temp.txt", "a+") as file_handler:
            file_handler.write(text)

    @staticmethod
    def load_from_file():
        """Loads the entries from a file """

    @staticmethod
    def load_from_uri(link):
        """Loads entries from an uri"""


if __name__ == '__main__':
    journal = Journal()
    journal.add_entry("Test")
    journal.add_entry("Test2")
    journal.add_entry("Test3")
    print(journal)
    # Saving to a file will be done though this separate class
    PersistenceHandler.save_to_file(str(journal))
