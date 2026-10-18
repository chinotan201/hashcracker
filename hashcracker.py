import hashlib

def hash_cracker(hash_to_crack, wordlist, algorithm="md5"):
    try:
        hash_func = getattr(hashlib, algorithm)
    except AttributeError:
        print(f"Algorithm {algorithm} not supported.")
        return None

    with open(wordlist, "r", encoding="utf-8") as f:
        for word in f:
            word = word.strip()
            hashed_word = hash_func(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"[+] Match found: {word}")
                return word
    print("[-] No match found.")
    return None

if __name__ == "__main__":
    target_hash = "5d41402abc4b2a76b9719d911017c592"  # md5("hello")
    wordlist_file = "wordlist.txt"
    hash_cracker(target_hash, wordlist_file, "md5")
