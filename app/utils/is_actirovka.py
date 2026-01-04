import difflib


def is_actirovka(text: str) -> bool:
    if not text:
        return False

    target = "актировка"
    matches = difflib.get_close_matches(
        text.lower(),
        [target],
        n=1,
        cutoff=0.7
    )

    return bool(matches)