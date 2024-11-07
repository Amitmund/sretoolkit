## Quick notes on GIT

### What does the `git config` do?
`git config` command is a convenient way to set configuratoin for your local repository.


### Understanding HEAD:
A `head` is the last commit object of a branch. For all repository, there will always be a default head, referred to as `master` or now `main`.  When you create a new branch, it will have its own head. When you switch to a new branch, the head will change to the last commit of that branch. When you commit the head will move to the new commit. When you merge, the head will move to the new commit that is the result of the merge. There will always be a default head referred to as “master”
or now “main” (as per GitHub) but there is no restriction to the count of heads.

- To checkout to 1 commit before the last commit, we use: `git checkout HEAD~1`
- To uncommit the last 3 commits without losing the changes: `git reset HEAD~3`. Later we can verifu the changes and update manually.
- To uncommit the last 3 commits and also remove the changes: `git reset --hard HEAD~3`. This will remove the all the changes.
- To look into the changes made in the last 3 commit: `git diff HEAD~3`
- To revert the last 3 commits: `git revert --no-commit HEAD~3...HEAD`

### Conflict:
- When you try to merge two branches, if there are changes in the same line.
- When A file is deleted in one branch but has been modified in the other.





