## Xeger is a tool to reverse-engineer a matching pattern for a PCRE-compliant regular expression. 

Xeger was mean to be ran on large amounts of simple regular expressions, not evaluating smaller numbers of complex regular expressions. All of the PCRE functionality used by the regular expression that are being targeted has been included.

The grammar for parsing the Regular Expressions is inspired by [this repo](https://github.com/kean/Regex/blob/main/grammar.ebnf)

## Why use Xeger?

Multiple tools exist already to generate a string that will be matched by a particular regular expression. 
- [Xeger-Legacy](https://github.com/crdoconnor/xeger) - I did not realize this existed until creating Xeger, which is why the Python package must be installed via `xeger-lark`, as this package already has the name `Xeger`.
- [rstr](https://github.com/leapfrogonline/rstr) - Inspired Xeger
- [regexp-examples](https://github.com/tom-lord/regexp-examples) - Ruby-based, unlike others.

The two Python libraries both only support Python regular expressions, which does not support POSIX character classes (`[[:graph:]]`, `[[:print:]]`, etc.). Additionally, the libraries rely on the `re.sre_parse` function or `sre_parse` library, which is deprecated since Python 3.11. Modifications to Xeger should be easier and more apporachable for developers relative to the above, as Xeger parses the regular expressions into an AST, then uses a Visitor pattern to evaluate the AST and build the string.

## Installation

Install Xeger via using Pip, or other Python Package Manager
```
pip install xeger-lark
```

Example Usage:
```
from xeger import Xeger

xeger = Xeger()
result = xeger.generate("test (a|b)\w+|\s*")
print(result)
>>> test a0
```

Xeger also includes functionality to check with a PCRE-compliant engine that the generated string does indeed match the pattern:
```
from xeger import Xeger, XegerRegexNotMatched

xeger = Xeger()
try:
    result = xeger.generate("test (a|b)\w+|\s*", check=True)
    print(result)
except XegerRegexNotMatched as e:
    print(f"Xeger failed to match with the regular expression: {e}")
```

## Shortcomings & Pitfalls
Xeger does not currently support:
- positive / negative lookbehind
- back references
- lazy modifiers
