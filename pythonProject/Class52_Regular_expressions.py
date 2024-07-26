'''
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs
'''
import re

text = '''JavaScript (JS) is a lightweight interpreted (or just-in-time compiled) programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative (e.g. functional programming) styles.
The standards for JavaScript are the ECMAScript Language Specification (ECMA-262) and the ECMAScript Internationalization API specification (ECMA-402). As soon as one browser implements a feature, we try to document it. This means that cases where some proposals for new ECMAScript features have already been implemented in browsers, documentation and examples in MDN articles may use some of those new features. Most of the time, this happens between the stages 3 and 4, and is usually before the spec is officially published.'''

pattern = r"[A-Za-z]+Script"  # r"" is a raw string, i.e, it take the string as it is given. i.e, if we write \n, then it will print \n, not a new line.

# search - prints only the first match
match = re.search(pattern, text)
print(match)

# for printing all the matches
matches = re.finditer(pattern, text)
for m in matches:
    print(m.span())  # span() tells the range of index in which the pattern is found (in the form of tuple)
    print(text[m.span()[0] : m.span()[1]])

# findall method
matches = re.findall(pattern, text)
print(matches)

# Difference between finditer and findall
# finditer Returns an iterator yielding match objects, while findall Returns a list of all non-overlapping matches in the string.,

