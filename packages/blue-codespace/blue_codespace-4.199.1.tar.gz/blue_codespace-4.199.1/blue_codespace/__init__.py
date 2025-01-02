NAME = "blue_codespace"

ICON = "🌀"

DESCRIPTION = f"{ICON} a github codespaces terraform."

VERSION = "4.199.1"

REPO_NAME = "blue-codespace"

MARQUEE = (
    "https://github.com/kamangir/assets/raw/main/blue-codespace/marquee.png?raw=true"
)

ALIAS = "@codespace"


def fullname() -> str:
    return f"{NAME}-{VERSION}"
