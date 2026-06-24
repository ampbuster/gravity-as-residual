#!/usr/bin/env python3
"""
inline_to_unicode.py - Convert simple inline LaTeX math to Unicode for better
GitHub rendering.

User's principle: "use unicode for inline, and latex if not"

Strategy:
- If an inline math expression ($...$) can be FULLY expressed in Unicode,
  convert it to Unicode.
- Otherwise, leave it as LaTeX.

Display math ($$...$$) is left alone.
Complex LaTeX (\\text{}, \\rm, \\frac, multi-char subscripts, ...) is left alone.
"""
import re
import sys
import os


# ============================================================
# UNSAFE commands (cannot be cleanly converted to Unicode)
# ============================================================
UNSAFE_COMMANDS = {
    # Text/font commands
    'text', 'rm', 'bf', 'it', 'emph', 'upshape', 'slshape', 'scshape',
    'mathbf', 'mathcal', 'mathrm', 'mathit', 'mathfrak', 'mathsf', 'mathtt',
    'mathnormal', 'boldsymbol',
    # Math operators (functions)
    'frac', 'sqrt', 'sum', 'int', 'prod', 'coprod', 'oint', 'iint', 'iiint',
    'bigcup', 'bigcap', 'bigvee', 'bigwedge', 'bigsqcup', 'bigoplus', 'bigotimes', 'biguplus',
    'binom', 'tbinom', 'dbinom',
    # Layout
    'over', 'choose', 'atop', 'overwithdelims', 'atopwithdelims',
    'left', 'right', 'begin', 'end', 'tag', 'label', 'ref', 'cite', 'bibliography',
    'array', 'matrix', 'pmatrix', 'bmatrix', 'Bmatrix', 'vmatrix', 'Vmatrix',
    'cases', 'aligned', 'align', 'equation', 'gather', 'multline', 'split', 'subarray',
    # Decoration (these have Unicode in some cases but are too specialized)
    'boxed', 'color', 'textcolor', 'colorbox', 'fcolorbox',
    'tilde', 'hat', 'bar', 'vec', 'dot', 'ddot', 'check', 'breve', 'acute', 'grave',
    'overline', 'underline', 'widehat', 'widetilde', 'overbrace', 'underbrace',
    'overrightarrow', 'overleftarrow', 'overleftrightarrow', 'underrightarrow', 'underleftarrow',
    'not', 'cancel', 'bcancel', 'xcancel', 'cancelto', 'sout',
    # Trigonometric/log
    'arcsin', 'arccos', 'arctan', 'arccot', 'arcsec', 'arccsc',
    'sin', 'cos', 'tan', 'cot', 'sec', 'csc',
    'sinh', 'cosh', 'tanh', 'coth', 'csch', 'sech',
    'log', 'ln', 'exp', 'lg',
    # Calculus
    'max', 'min', 'sup', 'inf', 'lim', 'liminf', 'limsup',
    'argmax', 'argmin', 'det', 'tr', 'rank', 'dim', 'ker', 'hom', 'ext', 'tor',
    # Spacing
    'quad', 'qquad', 'enspace', 'thinspace',
    'hfill', 'vfill', 'hspace', 'vspace', 'phantom', 'mathstrut', 'strut', 'mathchoice',
    'hphantom', 'vphantom', 'smash',
    # Size
    'displaystyle', 'textstyle', 'scriptstyle', 'scriptscriptstyle',
    'tiny', 'scriptsize', 'footnotesize', 'small', 'normalsize', 'large', 'Large', 'LARGE', 'huge', 'Huge',
    # Misc
    'stackrel', 'overset', 'underset', 'xleftarrow', 'xrightarrow', 'xmapsto',
    'xRightarrow', 'xLeftrightarrow',
    'centerline', 'par', 'noindent', 'indent', 'hbox', 'mbox', 'fbox', 'framebox', 'makebox',
    'parbox', 'minipage',
    'mathop', 'mathbin', 'mathrel', 'mathord', 'mathopen', 'mathclose', 'mathpunct', 'mathinner',
    'operatorname', 'DeclareMathOperator', 'providecommand', 'newcommand', 'renewcommand',
    'def', 'gdef', 'edef', 'xdef', 'let',
    'input', 'include', 'includegraphics', 'usepackage', 'documentclass',
    'verb', 'verbatim', 'href', 'url', 'hyperref',
}
WORD_UNSAFE_REGEX = re.compile(r'\\(' + '|'.join(re.escape(c) for c in UNSAFE_COMMANDS) + r')\b')
SPECIAL_UNSAFE_REGEX = re.compile(r'\\([,;!: ]|quad|qquad)')


# ============================================================
# CONVERTABLE commands (have Unicode equivalents)
# ============================================================
GREEK_LOWER = {
    'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ', 'epsilon': 'ε',
    'varepsilon': 'ε', 'zeta': 'ζ', 'eta': 'η', 'theta': 'θ', 'vartheta': 'ϑ',
    'iota': 'ι', 'kappa': 'κ', 'lambda': 'λ', 'mu': 'μ', 'nu': 'ν',
    'xi': 'ξ', 'omicron': 'ο', 'pi': 'π', 'varpi': 'ϖ', 'rho': 'ρ',
    'varrho': 'ϱ', 'sigma': 'σ', 'varsigma': 'ς', 'tau': 'τ', 'upsilon': 'υ',
    'phi': 'φ', 'varphi': 'ϕ', 'chi': 'χ', 'psi': 'ψ', 'omega': 'ω',
}
GREEK_UPPER = {
    'Alpha': 'Α', 'Beta': 'Β', 'Gamma': 'Γ', 'Delta': 'Δ', 'Epsilon': 'Ε',
    'Zeta': 'Ζ', 'Eta': 'Η', 'Theta': 'Θ', 'Iota': 'Ι', 'Kappa': 'Κ',
    'Lambda': 'Λ', 'Mu': 'Μ', 'Nu': 'Ν', 'Xi': 'Ξ', 'Omicron': 'Ο',
    'Pi': 'Π', 'Rho': 'Ρ', 'Sigma': 'Σ', 'Tau': 'Τ', 'Upsilon': 'Υ',
    'Phi': 'Φ', 'Chi': 'Χ', 'Psi': 'Ψ', 'Omega': 'Ω',
}
BLACKBOARD = {'Z': 'ℤ', 'N': 'ℕ', 'R': 'ℝ', 'C': 'ℂ', 'Q': 'ℚ', 'P': 'ℙ', 'E': '𝔼', 'F': '𝔽'}
OPERATORS = {
    r'\times': '×', r'\cdot': '·', r'\div': '÷', r'\pm': '±', r'\mp': '∓',
    r'\ast': '∗', r'\star': '⋆', r'\circ': '∘', r'\bullet': '•',
    r'\to': '→', r'\rightarrow': '→', r'\Rightarrow': '⇒',
    r'\Leftarrow': '⇐', r'\Leftrightarrow': '⇔',
    r'\mapsto': '↦',
    r'\partial': '∂', r'\nabla': '∇', r'\infty': '∞',
    r'\propto': '∝', r'\equiv': '≡', r'\sim': '∼', r'\simeq': '≃',
    r'\approx': '≈', r'\cong': '≅', r'\neq': '≠', r'\ne': '≠',
    r'\le': '≤', r'\leq': '≤', r'\ge': '≥', r'\geq': '≥',
    r'\ll': '≪', r'\gg': '≫',
    r'\in': '∈', r'\ni': '∋', r'\notin': '∉',
    r'\subset': '⊂', r'\supset': '⊃', r'\subseteq': '⊆', r'\supseteq': '⊇',
    r'\cup': '∪', r'\cap': '∩',
    r'\forall': '∀', r'\exists': '∃',
    r'\therefore': '∴', r'\because': '∵',
    r'\angle': '∠', r'\triangle': '△', r'\square': '□',
    r'\hbar': 'ℏ', r'\ell': 'ℓ', r'\Re': 'ℜ', r'\Im': 'ℑ',
}

CONVERTABLE = {}
CONVERTABLE.update({f'\\{k}': v for k, v in GREEK_LOWER.items()})
CONVERTABLE.update({f'\\{k}': v for k, v in GREEK_UPPER.items()})
CONVERTABLE.update(OPERATORS)

# Sort by length descending
SORTED_CONVERTABLE = sorted(CONVERTABLE.items(), key=lambda x: -len(x[0]))

# Unicode sub/super digits
SUB = {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'}
SUP = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}
SUB_LET = {'a':'ₐ','e':'ₑ','h':'ₕ','i':'ᵢ','j':'ⱼ','k':'ₖ','l':'ₗ','m':'ₘ','n':'ₙ','o':'ₒ','p':'ₚ','r':'ᵣ','s':'ₛ','t':'ₜ','u':'ᵤ','v':'ᵥ','x':'ₓ'}
SUP_LET = {'a':'ᵃ','b':'ᵇ','c':'ᶜ','d':'ᵈ','e':'ᵉ','f':'ᶠ','g':'ᵍ','h':'ʰ','i':'ⁱ','j':'ʲ','k':'ᵏ','l':'ˡ','m':'ᵐ','n':'ⁿ','o':'ᵒ','p':'ᵖ','r':'ʳ','s':'ˢ','t':'ᵗ','u':'ᵘ','v':'ᵛ','w':'ʷ','x':'ˣ','y':'ʸ','z':'ᶻ'}


def is_safe_for_unicode(inner: str) -> bool:
    """Check if an inline math expression can be FULLY converted to Unicode."""
    if not inner.strip():
        return False
    if WORD_UNSAFE_REGEX.search(inner):
        return False
    if SPECIAL_UNSAFE_REGEX.search(inner):
        return False
    
    # Multi-char subscripts: only allow digit content (optionally with -) or single letter
    for m in re.finditer(r'_\{([^{}]+)\}', inner):
        content = m.group(1)
        if content.isdigit():
            continue
        if content.startswith('-') and content[1:].isdigit():
            continue
        if len(content) == 1 and (content.isalpha() or content in GREEK_LOWER):
            continue
        return False
    
    # Multi-char superscripts: allow digits, minus, plus (up to 3 chars for ^{-NN})
    for m in re.finditer(r'\^\{([^{}]+)\}', inner):
        content = m.group(1)
        if len(content) > 3:
            return False
        if not all(c.isdigit() or c in '-+' for c in content):
            return False
    
    # All LaTeX commands should be in CONVERTABLE
    for m in re.finditer(r'\\[a-zA-Z]+', inner):
        cmd = m.group(0)
        if cmd not in CONVERTABLE and cmd != '\\mathbb':
            return False
    
    # Multi-char subscripts without braces: _DE - unsafe
    if re.search(r'(?<!_)_[a-zA-Z][a-zA-Z0-9]+(?!\w)', inner):
        return False
    # Multi-char superscripts without braces: ^ab - unsafe
    if re.search(r'(?<!\^)\^[a-zA-Z][a-zA-Z0-9]+(?!\w)', inner):
        return False
    
    return True


def convert_single_symbols(inner: str) -> str:
    """Convert LaTeX to Unicode in the expression."""
    result = inner
    
    def bbm_replace(m):
        letter = m.group(1)
        sub = m.group(2) or ''
        if letter not in BLACKBOARD:
            return m.group(0)
        uni = BLACKBOARD[letter]
        if sub:
            if sub.isdigit():
                return uni + ''.join(SUB.get(d, d) for d in sub)
            elif sub.startswith('-') and sub[1:].isdigit():
                return uni + '₋' + ''.join(SUB.get(d, d) for d in sub[1:])
            elif len(sub) == 1 and sub in SUB_LET:
                return uni + SUB_LET[sub]
        return uni
    
    result = re.sub(r'\\mathbb\{([A-Z])\}(?:_\{?([^{}\s]+?)\}?)?', bbm_replace, result)
    
    # Greek letters and operators
    for latex, uni in SORTED_CONVERTABLE:
        result = re.sub(re.escape(latex) + r'(?![a-zA-Z])', uni, result)
    
    # Subscripts
    def sub_replace(m):
        content = m.group(1) or m.group(2)
        if not content:
            return m.group(0)
        if content.isdigit():
            return ''.join(SUB.get(d, d) for d in content)
        if content.startswith('-') and content[1:].isdigit():
            return '₋' + ''.join(SUB.get(d, d) for d in content[1:])
        if len(content) == 1 and content in SUB_LET:
            return SUB_LET[content]
        return m.group(0)
    result = re.sub(r'_\{([0-9a-zA-Z-]+)\}|_([0-9a-zA-Z-])', sub_replace, result)
    
    # Superscripts
    def sup_replace(m):
        content = m.group(1) or m.group(2)
        if not content:
            return m.group(0)
        if content.isdigit():
            return ''.join(SUP.get(d, d) for d in content)
        if content.startswith('-') and content[1:].isdigit():
            return '⁻' + ''.join(SUP.get(d, d) for d in content[1:])
        if len(content) == 1 and content in SUP_LET:
            return SUP_LET[content]
        return m.group(0)
    result = re.sub(r'\^\{([0-9a-zA-Z+-]+)\}|\^([0-9a-zA-Z+-])', sup_replace, result)
    
    return result


def process_inline_math(text: str) -> str:
    """Process inline math $...$ and convert simple ones to Unicode.
    Display math $$...$$ is left alone.
    """
    # Find display math regions to skip
    display_ranges = []
    for m in re.finditer(r'\$\$[^$]+?\$\$', text, re.DOTALL):
        display_ranges.append((m.start(), m.end()))
    
    def is_in_display(pos):
        for s, e in display_ranges:
            if s <= pos < e:
                return True
        return False
    
    # Find all inline math
    result = []
    last_end = 0
    for m in re.finditer(r'(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)', text):
        if is_in_display(m.start()):
            continue
        # Add text before
        result.append(text[last_end:m.start()])
        # Try to convert
        expr = m.group(0)
        inner = m.group(1)
        if is_safe_for_unicode(inner):
            converted = convert_single_symbols(inner)
            result.append(converted)
        else:
            result.append(expr)
        last_end = m.end()
    result.append(text[last_end:])
    return ''.join(result)


# ============================================================
# PROSE conversions (in markdown text, not inside $...$)
# ============================================================
def convert_prose_patterns(text: str) -> str:
    """Convert simple Unicode-friendly patterns in prose (not in $...$)."""
    # Find math regions to skip
    display_ranges = []
    for m in re.finditer(r'\$\$[^$]+?\$\$', text, re.DOTALL):
        display_ranges.append((m.start(), m.end()))
    inline_ranges = []
    for m in re.finditer(r'\$[^$\n]+?\$', text):
        if not any(s <= m.start() < e for s, e in display_ranges):
            inline_ranges.append((m.start(), m.end()))
    # Also skip code blocks
    code_block_ranges = []
    i = 0
    while i < len(text):
        if text[i:i+3] == '```':
            end = text.find('```', i+3)
            if end == -1:
                end = len(text)
            else:
                end += 3
            code_block_ranges.append((i, end))
            i = end
        else:
            i += 1
    # And inline code
    inline_code_ranges = []
    for m in re.finditer(r'`[^`\n]+`', text):
        inline_code_ranges.append((m.start(), m.end()))
    
    def is_protected(pos):
        for s, e in code_block_ranges + inline_code_ranges + inline_ranges + display_ranges:
            if s <= pos < e:
                return True
        return False
    
    result = text
    
    # Convert plain 10^N to Unicode 10ⁿ (only in prose, not in code/math)
    sup_digits = {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}
    
    def repl_10n(m):
        if is_protected(m.start()):
            return m.group(0)
        sign = m.group(1) or ''
        digits = m.group(2)
        if not digits.isdigit():
            return m.group(0)
        uni_sign = ''
        if sign == '-':
            uni_sign = '⁻'
        elif sign == '+':
            uni_sign = '⁺'
        return '10' + uni_sign + ''.join(sup_digits.get(d, d) for d in digits)
    
    result = re.sub(r'10\^([+\-]?)(\d+)', repl_10n, result)
    
    # Convert g_+ -> g₊
    def repl_gplus(m):
        if is_protected(m.start()):
            return m.group(0)
        return 'g₊'
    result = re.sub(r'(?<!\w)g_\+(?!\w)', repl_gplus, result)
    
    return result


def process_file(filepath: str, dry_run=False) -> int:
    with open(filepath) as f:
        content = f.read()
    # First do prose conversions
    new_content = convert_prose_patterns(content)
    # Then do inline math conversions
    new_content = process_inline_math(new_content)
    if new_content != content:
        n = sum(1 for a, b in zip(content.split('$'), new_content.split('$')) if a != b) // 2
        if not dry_run:
            with open(filepath, 'w') as f:
                f.write(new_content)
        print(f'  {filepath}: converted (n={n} math exprs)')
        return n
    return 0






if __name__ == '__main__':
    import sys
    files = sys.argv[1:]
    if not files:
        print('Usage: inline_to_unicode.py <file.md>...')
        sys.exit(1)
    dry_run = '--dry-run' in files
    files = [f for f in files if f != '--dry-run']
    total = 0
    for f in files:
        total += process_file(f, dry_run=dry_run)
    print(f'Total: {total} conversions')
