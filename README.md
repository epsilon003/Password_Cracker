# 🔐 Smart Password Cracker

> A Python-based ethical password cracker that supports **SHA-256**, **SHA-1**, **MD5**, and even **mixed hash dumps** using smart detection.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

---

## 📦 Features

- 🔍 Supports **dictionary attacks**
- 🧠 **SmartCracker** auto-detects hash type
- ✅ Cracks **SHA256**, **SHA1**, **MD5** hashes
- 🧾 Saves cracked results to `results.csv`
- 🌈 Beautiful CLI output using [`rich`](https://github.com/Textualize/rich)
- 🔐 Ethical usage only (legal disclaimer below)

---

## 🗂️ Project Structure

```
password-cracker/
├── main.py
├── cracker/
│   ├── base.py
│   ├── sha256cracker.py
│   ├── sha1cracker.py
│   ├── md5cracker.py
│   └── smartcracker.py
├── cracker/
│   ├── wordlist.txt
│   └── hashes.txt
├── utils/
│   └── output.py
├── results.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

```bash
# 1. Clone the repo
git clone https://github.com/epsilon003/password-cracker.git
cd password-cracker

# 2. Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python main.py --hashfile data/hashes.txt --wordlist data/wordlist.txt --hashalgo smart --save
```

### 🔧 Arguments

| Flag          | Description                                      |
|---------------|--------------------------------------------------|
| `--hashfile`  | File containing password hashes (1 per line)     |
| `--wordlist`  | Dictionary file to attempt cracking with         |
| `--hashalgo`  | One of: `sha256`, `sha1`, `md5`, or `smart`      |
| `--save`      | Optional. Saves output to `results.csv`          |

---

## 🧪 Sample Test

Create a `wordlist.txt`:

```
123456
password
admin
welcome
qwerty
```

And `hashes.txt` with mixed hashes:

```
8d969eef6ecad3c29a3a629280e686cff8fab2d3c5fba025ae3001fddc8f7fdd
5f4dcc3b5aa765d61d8327deb882cf99
5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
```

Then run:

```bash
python main.py --hashfile hashes_custom.txt --wordlist wordlist.txt --hashalgo smart --save
```

✅ Output:
```
🔍 Cracking 3 hashes using SMART...

✅ Cracked Passwords:
<hash> → <plaintext>

💾 Results saved to results.csv
```

---

## 📄 License

MIT License © 2025 [Abhimantr Singh](https://github.com/epsilon003)

---

## ⚠️ Legal Disclaimer

> This tool is built strictly for **ethical research and educational purposes only**. Do **not** use it against systems you don’t own or have permission to test. The author is not responsible for any misuse or illegal activity.

---

## 📬 Contact

Have feedback, questions, or suggestions?
- Email: abhimantrsingh@gmail.com