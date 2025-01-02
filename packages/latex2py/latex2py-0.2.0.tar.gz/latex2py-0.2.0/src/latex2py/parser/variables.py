import re
from .config import Config
from .parse import parse_latex_with_config as sympy_parse_latex


def number_to_base(n: int, b: int) -> list[int]:
  """Convert a number to a given base.
  
  See: https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
  """
  if n < 0:
    raise ValueError("Number must be positive.")
  if n == 0:
    return [0]
  digits = []
  while n:
    digits.append(int(n % b))
    n //= b
  return digits[::-1]


def number_to_base_string(n: int, L: int = 3) -> str:
  """Convert a number to a unique string.
  
  To do this, we convert the number to base 26 and then map the digits to the
  letters of the alphabet. The resulting string will be unique for every number
  up to 26^L, where L is the number of digits.

  The "Zx" prefix is added since it is unlikely it will conflict with another
  identifier, and is similar to the `0x` prefix for hexadecimal numbers.
  """
  if n < 0:
    raise ValueError("Number must be positive.")
  if n >= 26 ** L:
    raise ValueError(f"Number must be less than {26 ** L}.")
  digits = number_to_base(n, 26)
  padded = [0] * max(0, (L - len(digits))) + digits
  return "Zx" + "".join([chr(ord("A") + d) for d in padded])


def parse_latex(expr: str, strict: bool = False, config: Config = Config()) -> str:
  """Parse a LaTeX expression while respecting identifiers.
  
  Due to the limitations of SymPy, we need to temporarily remove identifiers,
  parse, and then substitute them back in.

  https://docs.sympy.org/latest/modules/parsing.html#mathrm-latex-parsing-functions-reference
  """
  if expr.strip() == "":
    raise ValueError("This expression is empty!")

  # Find all identifiers in the expression. An identifier is an alphanumeric
  # variable name that must start with a letter or an underscore, or a forward
  # slash in the case of latex commands.
  identifier_or_command_pattern = re.compile(r"([\\a-zA-Z_][a-zA-Z0-9\._]*)")

  # Add a \ before any identifier.
  expr = re.sub(identifier_or_command_pattern, r"\\\1", expr)

  matches = re.findall(identifier_or_command_pattern, expr)

  mapping = {}
  for i, m in enumerate(matches):
    # Don't map special LaTeX commands.
    if m.startswith("\\\\"):
      continue

    # Don't map any single slashes detected as identifiers.
    if len(m) == 1:
      continue

    # Map the identifier to a unique string.
    if m not in mapping:
      mapping[m] = number_to_base_string(i)

    # Match the identifier only if it isn't preceded by a backslash (LaTeX command)
    # or followed by a word character (part of a larger identifier).
    pattern_not_part_of_larger = rf"(?<!\\)({re.escape(m)})(?![\w]+)"
    expr = re.sub(pattern_not_part_of_larger, re.escape(f"\\{mapping[m]}"), expr)

  print("MAPPING:", mapping)
  print("MAPPED:", expr)

  # The line above will add an extra \ before LaTeX commands, which we need to remove.
  expr = expr.replace("\\\\", "\\")
  print("EXPRESSION:", expr)
  expr = sympy_parse_latex(expr, config=config, strict=strict)
  print("PARSED:", expr)

  # Unmap the identifiers to add the . back in where they were.
  for k, v in mapping.items():
    expr = expr.replace(v, k)

  expr = expr.replace("\\", "")
  return expr
