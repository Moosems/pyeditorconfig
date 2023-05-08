from sys import path as sys_path

sys_path.insert(0, "../pyeditorconfig")

from pyeditorconfig import get_config # noqa: E402


def test_get_config() -> None:
    assert get_config(__file__) == {
        "indent_style": "space",
        "indent_size": "4",
        "max_line_length": "100",
        "end_of_line": "lf",
        "charset": "utf-8",
        "trim_trailing_whitespace": "true",
        "insert_final_newline": "true",
    }
