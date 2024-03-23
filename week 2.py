def count_words(sentence):
    """
    Function to count the number of words in a sentence.
    
    Args:
    sentence (str): The input sentence or paragraph.
    
    Returns:
    int: The number of words in the sentence.
    """
    words = sentence.split()  # Split the sentence into words
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    sentence = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if not sentence.strip():
        print("Error: No input provided.")
        return

    word_count = count_words(sentence)
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
