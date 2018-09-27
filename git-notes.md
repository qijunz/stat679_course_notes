## GitHub Notes

### Tips:
- Git is designed for version control, not for data storage.
- Github use `vim` as the default editor.
- Use short massage to readme and commit contents.
- To force to generate a new line, end the line with **2 spaces**.

### Git Commands:
- `git init` will initialize a new repo, and create the `.git/` directory.
- `git add` will add new edits to **staging area** (git now tracking thses files, called **tracked files**)
- `git diff` will show any difference between working files (staging area right now, working tree) and intermediate working files (new changes in files)
    * `git diff --staged` showing the difference between staging area and last commit (by `git add` command)
- `git commit` taking the snapshot (kind like the last step, keep history in git repo?)
    * `commit` command is tracking the changes.
    * option `-a` in `git commit` is adding all changes in tracked files to the commit.
- `git show` showing last commit, title, and paragraph.
    * could select specific commit and show only his commit.
    * Also will show the information including email address.
- `git log` using "less" to view git history
    * `--pretty=oneline`, the first line have a special role, must be short.
- `git checkout --<file>` is to discard changes in working directory.
- `.git/` folder has all snapshots of the repo.

### Working with others
- `git clone` when there is nothing, to start a work (with others).
- `git merge` to handle conflicts (two people making changes in the local computer with the same "pulled" repo, and commit to the central GitHub).
- `git remote`
    * `git remote -v`
    * `git remote add origin`
    * `git branch`
    * `git push origin master` (git push where and what)


