"""Problem 1 - File parsing practice."""

import ast
import io
import tokenize


def line_number(input_filename: str, output_filename: str) -> None:
    """Copy a file to another file and prefix each line with its number."""
    try:
        with open(input_filename, "r", encoding="utf-8") as input_file:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                for number, line in enumerate(input_file, start=1):
                    output_file.write(f"{number}. {line}")

    except OSError as error:
        print(f"Error processing file: {error}")
        raise


def _remove_comments_and_empty_lines(code: str) -> str:
    """Remove Python comments and empty lines from source code."""
    tokens = tokenize.generate_tokens(io.StringIO(code).readline)

    without_comments = tokenize.untokenize(
        token
        for token in tokens
        if token.type != tokenize.COMMENT
    )

    lines = [
        line.rstrip()
        for line in without_comments.splitlines()
        if line.strip()
    ]

    return "\n".join(lines) + "\n"


def parse_functions(filename: str) -> tuple:
    """Return information about top-level functions in a Python file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            source = file.read()

        tree = ast.parse(source)
        results = []

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                function_name = node.name
                arguments = ast.unparse(node.args)

                function_code = ast.get_source_segment(source, node)

                if function_code is None:
                    function_code = ""

                function_code = _remove_comments_and_empty_lines(
                    function_code
                )

                results.append(
                    (
                        node.lineno,
                        function_name,
                        arguments,
                        function_code,
                    )
                )

        results.sort(key=lambda item: item[1])

        return tuple(results)

    except (OSError, SyntaxError) as error:
        print(f"Error parsing Python file: {error}")
        raise


def main() -> None:
    """Test Problem 1 functions."""
    filename = "p1_Velazquez_Manuel.py"

    line_number(filename, "p1_numbered.txt")

    functions = parse_functions(filename)

    print("Parsed functions:")
    for function in functions:
        print(function)


if __name__ == "__main__":
    main()