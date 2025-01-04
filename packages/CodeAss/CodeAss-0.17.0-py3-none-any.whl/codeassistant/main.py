from pathlib import Path
from time import sleep
import click
from codeassistant.click_args import arg_directory
from codeassistant.functions_cmds import generate_commit_msg
from codeassistant.functions_git import (
    get_git_diff,
    get_gitignore_contents,
    get_git_merged_branches,
    git_remove_branch,
)
from codeassistant.functions_core import shell, timer
from codeassistant.variables import (
    OPTION_NO_ADD_HELP,
    OPTION_GIT_DIRECTORY_HELP,
    PROMPT_EXTRA_PROMPT_HELP,
    PROMPT_GENERATE_COMMIT_MESSAGE,
    PROMPT_GENERATE_COMMIT_MESSAGE_HELP,
)

# TODO add this command:  tree --gitignore -pugf to give tree with permissions and user, group


@click.group(context_settings={"show_default": True})
def cli():
    """CodeAssistant CLI"""
    pass


@cli.command()
@click.option(
    "-d",
    "--directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    default=".",
    required=False,
    # help="Path to git repoistory, can be a subdir in repoistory as well.",
)
@click.option(
    "-p",
    "--prompt",
    type=str,
    required=False,
    default=PROMPT_GENERATE_COMMIT_MESSAGE,
    help="Prompt to AI model. Context (git diff and/or others) will be added as well.",
)
@click.option(
    "-e",
    "--extra",
    "extra_prompt",
    type=str,
    required=False,
    default="",
    help=PROMPT_EXTRA_PROMPT_HELP,
)
@click.option(
    "-na",
    "--no-add",
    "no_add",
    type=bool,
    required=False,
    is_flag=True,
    default=False,
    help=OPTION_NO_ADD_HELP,
)
@click.option(
    "-y",
    "--yes",
    type=bool,
    is_flag=True,
    required=False,
    default=False,
    help="Do not prompt for push",
)
@click.option(
    "--pipeline-delay",
    "pipeline_delay",
    type=int,
    required=False,
    default=2,
    help="How long we wait before running glab ci view",
)
@timer
def commit(
    directory: Path,
    prompt: str,
    no_add: bool,
    yes: bool,
    extra_prompt: str,
    pipeline_delay: int,
):
    """Commits with generated a commit message and pushes to remote.

    Can cancel any time with CTRL+C.
    """
    if not no_add:
        shell(["git", "add" "."], raise_error=True, check_returncode=True)

    msg = generate_commit_msg(directory, prompt, extra_prompt=extra_prompt)
    if not yes:
        input("Proceed with commit? (ctrl+c to cancel)")

    shell(["git", "commit", "-m", msg], raise_error=True, silent=False)

    if not yes:
        input("Proceed with push? (ctrl+c to cancel)")
    shell(["git", "push"], silent=False)
    shell(["git", "status"], silent=False)

    if not yes:
        input("Proceed with viewing gitlab pipeline? (ctrl+c to cancel)")
    for i in range(pipeline_delay):
        print(f"Waiting {pipeline_delay-i}s", end="\r")
        sleep(pipeline_delay)
    click.echo()
    shell(["glab ci view"], silent=False)


@cli.command()
@click.option(
    "-d",
    "--directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    default=".",
    required=False,
)
@click.option(
    "-p",
    "--prompt",
    type=str,
    required=False,
    default=PROMPT_GENERATE_COMMIT_MESSAGE,
    help=PROMPT_GENERATE_COMMIT_MESSAGE_HELP,
)
@click.option(
    "-e",
    "--extra",
    "extra_prompt",
    type=str,
    required=False,
    default="",
    help=PROMPT_EXTRA_PROMPT_HELP,
)
@timer
def msg(directory: Path, prompt: str, extra_prompt: str):
    """Generates a commit message based on git diff"""
    generate_commit_msg(directory, prompt, extra_prompt=extra_prompt)


@cli.command()
@click.option(
    "-d",
    "--directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    default=".",
    required=False,
    help=OPTION_GIT_DIRECTORY_HELP,
)
@timer
def diff(directory: Path):
    """Run the diff command used internally"""
    diff: str = get_git_diff(directory)

    click.echo(diff, color=True)


@cli.command()
@arg_directory
@click.option(
    "--type",
    "-t",
    "filetypes",
    multiple=True,
    type=str,
    help="Only adds these filetypes\nExample: -t .cpp -t .h -t .hpp #only c++ related files\nExample: -t .py #only python files",
    default=[],
)
@click.option(
    "--gitignore",
    "-gi",
    "gitignore",
    help="Read contents of .gitignore in root of git repo (finds automatically) and exclude those files as --exclude.",
    type=bool,
    default=True,
)
@click.option(
    "--exclude",
    "-e",
    "exclude",
    multiple=True,
    type=str,
    help="If any of this is part of path, then exclude that file.\n\
        Can be comma separatated a,b,c or multiple -e a -e b.",
    default=[".git", ".dockerignore", ".gitignore", ".env"],
)
@timer
def troubleshoot(directory: Path, exclude: list[str], gitignore: bool, filetypes: list):
    """Prints contents of all files in directory for gpt to consume and help troubleshoot code with.
    adds context in form of other modules or functions as tree, bugs, linting, and other to help
    gpt as much as possible in troubleshooting.
    """

    gitignore_contents: list[str] = get_gitignore_contents(directory)

    files = [
        x
        for x in Path(directory).glob("**/*")
        if x.is_file()
        and not (any([excl in str(x) for excl in gitignore_contents]))
        and not (any([excl in str(x) for excl in exclude]))
    ]

    file = files[0]

    def read_file_content(file) -> list[str]:
        with open(file, "r", encoding="utf8") as f:
            lines = f.readlines()
            # think of these in reverse order. insert 0 will move the first insert 0 to insert 1 etc
            # ############################## Insert filepath into file header ####################################
            lines.insert(0, "\n")
            lines.insert(0, "\n")
            lines.insert(0, "\n")
            lines.insert(0, f"# {file.relative_to(directory)}\n")
            lines.insert(0, "\n")

        return lines

    file_contents = []

    for file in files:
        try:
            file_contents.extend(read_file_content(file))
        except Exception as e:
            print(f"ERROR | {file} | {e}")

    lines = file_contents[0]

    for lines in file_contents:
        print(lines, end="")


@cli.group(help="git commands")
def git():
    pass


@git.command()
@click.option(
    "-d",
    "--directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    default=".",
    required=False,
    help=OPTION_GIT_DIRECTORY_HELP,
)
@click.option(
    "--exclude",
    "-e",
    "exclude",
    multiple=True,
    type=str,
    help="What to exclude, like main, master, prod etc.",
    default=["main", "master", "prod", "production", "stage", "staging"],
)
@click.option(
    "-y",
    "--yes",
    type=bool,
    is_flag=True,
    required=False,
    default=False,
    help="Do not prompt, remove directly",
)
@timer
def del_branches(directory: Path, exclude: list, yes: bool):
    """Remove git merged already branches on remote.

    Can only delete a merged branch (in theory)"""
    branches: list = get_git_merged_branches(directory, exclude)

    if not branches:
        click.echo("No branches to remove")
        exit(0)
    if not yes:
        input("Proceed with removal? (ctrl+c to cancel)")

    for branch in branches:
        git_remove_branch(directory, branch)


@cli.command()
@timer
def upgrade():
    """Upgrade CodeAssistant with pip.

    pip install --upgrade codeass
    """
    shell(["pip", "install", "--upgrade", "codeass"], silent=False)


# def split_into_chunks(lines:list[str], chunk_size_limit_in_bytes = 4096):
#     chunks=[]
#     current_chunk = []
#     current_size = 0

#     # Process the lines
#     for line in lines:
#         line_size = len(line.encode('utf-8'))  # Size of the line in bytes
#         if current_size + line_size > chunk_size_limit_in_bytes:
#             # Print or process the current chunk
#             print("".join(current_chunk))
#             print()
#             print()
#             print("-" * 80)  # Separator for readability
#             print()
#             print()
#             # Start a new chunk
#             chunks.append(current_chunk)
#             current_chunk = []
#             current_size = 0
#         current_chunk.append(line)
#         current_size += line_size

#     # Print any remaining lines in the last chunk
#     if current_chunk:
#         chunks.append(current_chunk)
#         print("".join(current_chunk))
#     return chunks


# chunks=split_into_chunks(file_contents)


# output_directory="chunks"
# output_directory_path=Path(output_directory)
# output_directory_path.mkdir(exist_ok=True, parents=True)


# for i,chunk in enumerate(chunks):
#     print(".",end="")
#     with open(output_directory_path/f"{i}.txt","w",encoding="utf8") as f:
#         f.writelines(chunk)
# print()

if __name__ == "__main__":
    cli()
