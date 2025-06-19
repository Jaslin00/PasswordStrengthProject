import itertools

def generate_variants(base_words):
    common_suffixes = ['123', '@123', '2024', '2025', '!']
    variants = set()

    for word in base_words:
        variants.add(word.lower())
        variants.add(word.upper())
        variants.add(word.capitalize())

        for suffix in common_suffixes:
            variants.add(word + suffix)
            variants.add(word.capitalize() + suffix)

    for combo in itertools.permutations(base_words, 2):
        variants.add(''.join(combo))

    return list(variants)

def main():
    print("Enter words (e.g. name, birth year, pet name):")
    user_input = input("> ")
    words = user_input.split()

    wordlist = generate_variants(words)

    with open("custom_wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"\n✅ Wordlist generated with {len(wordlist)} entries in 'custom_wordlist.txt'.")

if __name__ == "__main__":
    main()
