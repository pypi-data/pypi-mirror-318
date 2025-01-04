import pathlib
import subprocess

def main() -> None:
    """
    Clean out jj metadata from a git repository.

    jj tracks _changes_ as _commits_. Any time you make and edit and run the `jj` command,
    jj will _automatically_ commit those edits to the underlying git repo. That means
    if you make lots of edits and run `jj` in between, you will end up with lots of git
    commits that are dangling. But to keep these commits from being removed (so that you can undo
    all operations), jj will create git references in the `.git/refs/jj/keep/` folder.

    If you look at your repository with `jj log`, everything looks nice. jj does not show these
    dangling commits. But, if you look at it with `tig --all`, you will see a giant nest of branched off
    dangling commits.

    This script removes all of the refs jj puts in `.git/refs/jj/keep` _except_ for the ones that refer to
    a jj head. This keeps your `tig --all` view much saner, and you can then run `git prune` to remove the
    commits from the reposiotry all together.

    All of this makes it easer to switch back and forth between jj and git, which is necessary when you
    are using jj locally to work on git repositories within a git team...

    Currently, the script is not configuration **at all**. It assumes that it is called from the root directory
    of a colocated jj/git repository and that the jj command exists.
    """

    GIT_DIR = pathlib.Path(".git")
                        

    cmd = ['jj', 'log', '--no-graph', '-T' 'commit_id++"\n"', '-r']
    heads = subprocess.check_output( cmd + [ 'heads(all())'] ).decode().split()
    all = subprocess.check_output( cmd + ['all()~root()'] ).decode().split()

    to_remove = filter( lambda id: id not in heads, all)

    for file in (GIT_DIR/"refs/jj/keep").glob("*"):
        if file.stem not in heads:
            print(f"REMOVING {file}")
            file.unlink()
        else:
            print(f"keeping {file}")



