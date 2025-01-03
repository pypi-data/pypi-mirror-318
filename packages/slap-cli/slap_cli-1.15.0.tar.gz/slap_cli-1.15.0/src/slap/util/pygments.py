import typing as t


def toml_highlight(toml_data: dict[str, t.Any] | str) -> str:
    import pygments
    import pygments.formatters
    import pygments.lexers
    import tomli_w

    if not isinstance(toml_data, str):
        toml_data = tomli_w.dumps(toml_data)
    return pygments.highlight(
        toml_data, pygments.lexers.get_lexer_by_name("toml"), pygments.formatters.get_formatter_by_name("terminal")
    )
