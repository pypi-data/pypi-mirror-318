from pathlib import Path
from codeassistant.functions_core import shell
import pathspec


def get_git_root(directory: Path | str) -> Path:
    directory = Path(directory)

    git_directory = shell(
        ["git", "-C", str(directory), "rev-parse", "--show-toplevel"], silent=True
    )
    return Path(git_directory)


def get_gitignore_path(directory: Path | str) -> Path:
    directory = Path(directory)

    git_root = get_git_root(directory)

    gitignore_path = git_root / ".gitignore"
    assert gitignore_path.exists()
    assert gitignore_path.is_file()

    return gitignore_path


def get_gitignore_contents(
    directory: Path | str,
    remove_comments=True,
    remove_whitespace=True,
    remove_newline=True,
) -> list[str]:
    directory = Path(directory)
    gitignore_path = get_gitignore_path(directory)

    with open(gitignore_path, "r", encoding="utf-8") as f:
        lines: list[str] = f.readlines()

        if remove_comments:
            lines = [x for x in lines if not x.startswith("#")]
        if remove_whitespace:
            lines = [x for x in lines if x != "\n"]
        if remove_newline:
            lines = [x.removesuffix("\n") for x in lines]
    return lines


def get_git_diff(git_directory: Path | str) -> str:
    """git diff --cached (only staged files) in current dir, not from the git repo root.

    TODO make new git repo diff from root method.

    """
    git_directory = Path(git_directory)

    return shell(["git", "-C", str(git_directory), "diff", "--cached"])


def ensure_not_supported_on_windows():
    import platform

    if platform.system() == "Windows":
        raise OSError("Not supported on Windows as we're using grep")


def get_git_merged_branches(git_directory: Path | str, exclude: list) -> list[str]:
    """Get git merged already branches on remote. wont list any remote branches.

    Only works on linux
    """
    ensure_not_supported_on_windows()

    git_directory = Path(git_directory)

    result: str = shell(
        [
            "git",
            "-C",
            git_directory,
            "branch",
            "--merged",
            "|",
            "grep",
            "-Ev",
            '(^\*|^\+|{"|".join(exclude)})',
        ],
        silent=False,
    )

    branches: list[str] = [x.decode("utf-8").strip() for x in result.splitlines()]  # type: ignore
    return branches


def git_remove_branch(git_directory: Path | str, branch: str) -> str:
    """Remove provided branch"""
    git_directory = Path(git_directory)

    if not branch:
        raise TypeError("No branch")

    return shell(
        ["git", "-C", git_directory, "branch", "-d", branch],
        silent=False,
    )


def git_ignored_files(gitignore_path: Path, root_dir: Path) -> list[Path]:
    """
    Return a list of files ignored by the .gitignore file in `gitignore_path`
    under the `root_dir`.
    """
    # Read the .gitignore
    gitignore_text = gitignore_path.read_text(encoding="utf-8")

    # Create a PathSpec from the .gitignore lines
    spec = pathspec.PathSpec.from_lines("gitignore", gitignore_text.splitlines())

    # Collect all files in the directory (recursively)
    all_files = [f for f in root_dir.glob("**/*") if f.is_file()]

    # Filter out files that match the ignore spec
    ignored_files = [
        f for f in all_files if spec.match_file(str(f.relative_to(root_dir)))
    ]

    return ignored_files
