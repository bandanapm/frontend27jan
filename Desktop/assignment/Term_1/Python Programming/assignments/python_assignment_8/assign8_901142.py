def read_file_data(filename):
    """
    Read all the content of the given file.

    Parameters:
        filename (str): The name of the text file to read.

    Returns:
        str or None: The content of the file as a string, or None if the file is not found.
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


def count_all_words(file_content):
    """
    Count the occurrences of each word in the given file content.

    Parameters:
        file_content (str): The content of the text file as a string.

    Returns:
        dict or None: A dictionary where keys are words, and values are the counts,
                      or None if the file content is None.
    """
    if file_content is None:
        return None

    # Convert all words to lowercase and split the content into individual words
    words = file_content.lower().split()

    # Remove punctuation from each word
    words = [word.strip(",.!?;:'\"()[]{}<>") for word in words]

    # Count word occurrences using a dictionary
    word_freq = {}
    for word in words:
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def display_word_data(word_freq):
    """
    Display the frequency of words in alphabetical order along with the total number of words.

    Parameters:
        word_freq (dict or None): A dictionary where keys are words, and values are the counts,
                                  or None if the file is not found.
    """
    if word_freq is None:
        print("OOPS!, Sorry.\nThe file with the given name doesn't exist!")
    else:
        print("Word with their frequency in the file:")
        print("--------------------------------------")
        for word, count in sorted(word_freq.items()):
            print(f"{word}: {count}")
        print(f"\nTotal word count in the file is: {sum(word_freq.values())}")


def main():
    # Ask the user to specify the name of the text file to be read
    filename = input("Enter the name of the text file: ")
    # Parse the file name to lower case to make it case-insensitive
    filename = filename.lower()

    # Read the content inside the file
    file_content = read_file_data(filename)

    # Count the occurrence of the words
    word_freq = count_all_words(file_content)

    # Display word frequencies
    display_word_data(word_freq)


if __name__ == "__main__":
    main()
