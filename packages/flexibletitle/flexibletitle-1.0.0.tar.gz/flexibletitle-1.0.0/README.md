# FlexibleTitle: Flexible Smart Title Case Formatter

FlexibleTitle is a Python library designed to transform strings into flexible title case format while excluding specified words from capitalization. This simple yet powerful tool supports various input styles and offers unmatched flexibility for users with diverse formatting needs.

## Features
- Converts strings to a "flexible" title case format.
- Allows exclusions for specific words (e.g., articles, prepositions).
- Handles exclusions provided as:
  - A single word.
  - A list of words.
  - Multiple words as separate arguments.
- Automatically normalizes exclusions to lowercase for consistency.

---

## Importing the Library
```python
from flexibletitle import FlexibleTitle
```

---

## Basic Usage

### Single Exclusion Word
```python
formatter = FlexibleTitle("the")
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps over the Lazy Dog"
```

### Multiple Exclusions as Separate Arguments
```python
formatter = FlexibleTitle("the", "over", "and")
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps over the Lazy Dog"
```

### Exclusions as a List
```python
formatter = FlexibleTitle(["the", "over", "and"])
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps over the Lazy Dog"
```

---

## Advanced Usage

### Combining Lists and Strings
```python
formatter = FlexibleTitle(["the", "over"], "and")
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps over the Lazy Dog"
```

### Empty Exclusions
If no exclusions are provided, FlexibleTitle behaves like a regular title case converter:

```python
formatter = FlexibleTitle()
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps Over The Lazy Dog"
```

### Dynamic Word Splitting
If exclusions contain multiple words in a single string, they are automatically split:

```python
formatter = FlexibleTitle("the over and")
result = formatter.to_flexible_title_case("the quick brown fox jumps over the lazy dog")
print(result)  # Output: "The Quick Brown Fox Jumps over the Lazy Dog"
```

---

## API Reference

### Class: FlexibleTitle
#### Constructor
```python
FlexibleTitle(*exclusions)
```
- **exclusions** (`str`, `list`, or multiple strings): Words to exclude from capitalization.

#### Method: to_flexible_title_case
```python
to_flexible_title_case(text)
```
- **text** (`str`): The input string to format.
- **Returns**: A string formatted in flexible title case.

---

## Author
- **Name**: Khalid Sulaiman Al-Mulaify
- **Email**: khalidmfy@gmail.com
- **X Account**: [@Python__Task](https://x.com/Python__Task)

---

## License
This project is licensed under the MIT License.

