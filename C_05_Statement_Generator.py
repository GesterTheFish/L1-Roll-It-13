def make_statement(statement, decoration):
    """Adds emojis / additional characters to headings."""
    ends = decoration * 3
    print(f"{ends} {statement} {ends}")

# Main routine
make_statement("I love python", "🐍")
make_statement("Round Results", "=")