import argparse
from cracker.sha256cracker import SHA256Cracker
from cracker.md5cracker import MD5Cracker
from cracker.sha1cracker import SHA1Cracker
from cracker.smartcracker import SmartCracker
from utils.output import print_result, save_result

# Supported hash algorithms and their corresponding cracker classes
HASH_TYPES = {
    'sha256': SHA256Cracker,
    'md5': MD5Cracker,
    'sha1': SHA1Cracker,
    'smart': SmartCracker    
}

def load_file(file_path):
    """Reads a file and returns a list of stripped lines (non-empty)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        exit(1)

def main():
    # Command-line interface
    parser = argparse.ArgumentParser(
        description="Ethical Password Cracking - Dictionary Attack Tool"
    )
    parser.add_argument("--hashfile", required=True, help="Path to file containing password hashes")
    parser.add_argument("--wordlist", required=True, help="Path to dictionary wordlist file")
    parser.add_argument("--hashalgo", required=True, choices=HASH_TYPES.keys(),help="Hash algorithm to use: sha256, md5, sha1 or smart")
    parser.add_argument("--save", action='store_true', help="Save cracked results to results.csv")

    args = parser.parse_args()

    # Load data
    hashes = load_file(args.hashfile)
    wordlist = load_file(args.wordlist)

    # Initialize the appropriate cracker class
    cracker_class = HASH_TYPES[args.hashalgo]
    cracker = cracker_class(hashes, wordlist)

    print(f"\n🔍 Cracking {len(hashes)} hashes using {args.hashalgo.upper()}...\n")
    results = cracker.crack()

    # Display and optionally save results
    print_result(results)

    if args.save:
        save_result(results)
        print("\n💾 Results saved to results.csv")

if __name__ == "__main__":
    main()
