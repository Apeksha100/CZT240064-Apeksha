def count_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            words = file.read().split()
            word_count = len(words)

        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}")
        print("Word count written to", output_file)

    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
count_words("input.txt", "output.txt")
