# Word Counter

A simple Python 3.13 command-line text analyzer. It counts words (including common apostrophe- and hyphen-joined words), all characters including whitespace, non-whitespace characters, sentence-ending punctuation groups, and non-empty paragraphs separated by blank lines. Unicode letters are supported.

## Usage

Analyze inline text:

```powershell
python word_counter.py --text "Hello there. How are you?"
```

Read a UTF-8 text file:

```powershell
python word_counter.py --file "C:\path\to\notes.txt"
```

Or pipe text through standard input:

```powershell
Get-Content .\notes.txt -Raw | python word_counter.py
```

When run in a terminal without an option, paste/type text and finish input with **Ctrl+Z**, then **Enter** on Windows. Files are read-only and must be regular UTF-8 text files. Sentence boundaries are counted from `.`, `!`, or `?` punctuation; abbreviations are not language-model disambiguated.

## Test

```powershell
python -m unittest -v
```
