class CcWC:

    def __init__(self, file) -> None:
        self.file = file

    def count_bytes(self):
        """
        Counts the number of bytes in the file associated with this object.

        Returns:
            int: The number of bytes in the file.

        Raises:
            FileNotFoundError: If the file cannot be found.
        """
        with open(self.file, 'r') as f:
            return len(f.read())
    
    def count_lines(self):
        """
        Counts the number of lines in the file associated with this object.

        Returns:
            int: The number of lines in the file.

        Raises:
            FileNotFoundError: If the file cannot be found.
        """
        with open(self.file, 'r') as f:
            return len(f.readlines())
        
    def count_words(self):
        """
        Counts the number of words in the file associated with this object.

        Returns:
            int: The number of words in the file.
        """
        with open(self.file, 'r') as f:
            return len(f.read().split())

    def count_chars(self):
        """
        Counts the number of characters in the file associated with this object.

        Returns:
            int: The number of characters in the file.

        Raises:
            FileNotFoundError: If the file cannot be found.
        """
        with open(self.file, 'r') as f:
            return len(f.read())


