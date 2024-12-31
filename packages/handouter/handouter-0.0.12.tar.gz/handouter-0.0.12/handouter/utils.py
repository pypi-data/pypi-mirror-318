import os

from pecheny_utils import escape_latex

RESERVED_WORDS = [
    "image",
    "for_question",
    "columns",
    "rows",
    "resize_image",
    "font_size",
    "font_family",
    "no_center",
    "raw_tex",
    "color",
    "handouts_per_team",
]


def read_file(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        contents = f.read()
    return contents


def write_file(filepath, contents):
    with open(filepath, "w", encoding="utf8") as f:
        f.write(contents)


def replace_ext(filepath, new_ext):
    if not new_ext.startswith("."):
        new_ext = "." + new_ext
    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)
    base, _ = os.path.splitext(basename)
    return os.path.join(dirname, base + new_ext)


def wrap_val(key, val):
    if key in ("columns", "rows", "no_center", "color", "handouts_per_team"):
        return int(val.strip())
    if key in ("resize_image", "font_size"):
        return float(val.strip())
    return val.strip()


def parse_handouts(contents):
    blocks = contents.split("\n---\n")
    result = []
    for block_ in blocks:
        block = block_.strip()
        block_dict = {}
        text = []
        lines = block.split("\n")
        for line in lines:
            sp = line.split(":", 1)
            if sp[0] in RESERVED_WORDS:
                block_dict[sp[0]] = wrap_val(sp[0], sp[1])
            elif line.strip():
                text.append(line.strip())
        if text:
            block_dict["text"] = "\n".join(text).strip()
            if not block_dict.get("raw_tex"):
                block_dict["text"] = escape_latex(block_dict["text"])
        result.append(block_dict)
    return result
