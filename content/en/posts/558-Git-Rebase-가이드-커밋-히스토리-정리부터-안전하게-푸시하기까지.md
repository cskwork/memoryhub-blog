---
title: "Git Rebase guide - from organizing commit history to pushing safely"
date: 2025-04-22T18:27:33+09:00
slug: "558-Git-Rebase-가이드-커밋-히스토리-정리부터-안전하게-푸시하기까지"
original_url: "https://memoryhub.tistory.com/558"
tistory_id: 558
draft: false
categories: ["Dev Ops"]
tags: ["Git"]
---

## 1. Git Rebase Concept

`git rebase` is a core Git operation that readjusts the commit sequence of a specific branch on top of a different base commit. In this process, existing commits are regenerated as new commits to form a linear history.

**Core functions:**

- **History optimization:** Consolidates granulated commits into semantic units (`squash`, `fixup`), modifies commit messages (`reword`), reorders commits, etc., systematizing local commit history.
- **Branch synchronization:** Rebases the working branch to the latest state of the base branch (e.g., `main`, `develop`), keeping the codebase current and minimizing the complexity of future merge conflicts.

## 2. Technical advantages of using Rebase

- **Linear history structure:** Applies commits sequentially without the merge commits created by `git merge`, forming an intuitive and traceable history.
- **Improved code review efficiency:** Commits reconstructed into logical units allow reviewers to clearly understand the intent and impact of changes.
- **Incremental conflict resolution:** Periodic synchronization with the base branch distributes large conflict risks and resolves them in manageable units.

## 3. Practical application scenarios and implementation methods

### A. Branch synchronization (`git rebase <base_branch>`)

```
# 1. Switch to working branch
git checkout feature

# 2. Get latest state of base branch
git fetch origin main

# 3. Rebase working branch commits on top of origin/main
git rebase origin/main

# If conflicts occur, resolve them and continue
# git rebase --continue
```

### B. Refine commit history (`git rebase -i <base>`)

Through interactive rebase, you can edit the history after the `<base>` commit.

- **Ways to specify base:**

  - `HEAD~N`: Starting from N commits before the current position
  - `<commit-id>`: After a specific commit ID
  - `<branch_name>`: After a specific branch's split point
- **Key commands in interactive interface:**

  ```
    pick a1b2c3d feat: initial feature implementation
    pick e4f5g6h fix: minor bug fix (WIP)
    pick i7j8k9l feat: additional feature implementation

    # Command options:
    # p, pick <commit> = use commit
    # r, reword <commit> = use commit, modify message
    # e, edit <commit> = use commit, stop for amending
    # s, squash <commit> = combine with previous, merge messages
    # f, fixup <commit> = combine with previous, discard message
    # d, drop <commit> = remove commit
    # other options...
  ```
- **Advanced rebase example: Combining recent 3 commits**

  1. Run command: `git rebase -i HEAD~3`
  2. Modify in editor:

     ```
      pick a1b2c3d main feature implementation
      squash e4f5g6h partial fix 1
      fixup i7j8k9l partial fix 2
     ```
  3. Save and finalize combined commit message
  4. Result: three commits optimized into a single semantic commit

## 4. Rebase conflict resolution process

1. **Identify conflict point:** Git marks the rebase interruption point and conflicting files.
2. **Resolve conflicts:** Modify areas in conflicted files marked with markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. **Stage changes:** Register resolved files with `git add <resolved_file>`.
4. **Continue rebase:** Resume the process with `git rebase --continue`.

**Alternative options:**

- `git rebase --skip`: Ignore changes from current conflicting commit and proceed to next
- `git rebase --abort`: Cancel entire rebase and return to original state

## 5. Core principles of Rebase

> **Golden rule: Never rebase commits that have already been pushed to the shared repository and are shared among developers.**

- **Risk:** Rebase discards existing commits and creates new ones. If other developers are working based on the original commits, force-pushing the rebased history will lose their working foundation, causing serious history inconsistencies and work loss.
- **Safe application scope:**

  - Local commits not yet pushed to remote repository
  - Personal dedicated branches (where you're certain other developers aren't using as a base)

## 6. Safe pushing strategy after rebase (`--force-with-lease`)

When history is restructured through rebase, normal `git push` is rejected. This is a remote repository history protection mechanism.

- **Common error:** Running `git pull` merges the remote's old history with the local's reconstructed history, creating unnecessary merge commits.
- **Optimal solution: `git push --force-with-lease <remote> <branch>`**

  - A safer approach than `--force`, verifying that the remote branch matches the last synchronized state.
  - Stops pushing if other developers' commits have been added, preventing work loss.
  - Updates history only if the remote state matches expectations.

    ```
    git push --force-with-lease origin feature-branch
    ```
- **Cautions:** When applying to shared branches, prior team communication is essential, and other developers must afterwards synchronize their local with `git fetch origin` and `git reset --hard origin/feature-branch`.

## 7. Recovery mechanism (`git reflog`)

If rebase errors or unintended results occur, you can recover to the previous state using `git reflog`.

- `reflog` preserves HEAD position change history.
- Use `git reflog` to identify commit hashes before rebase.
- Recover to previous state with `git reset --hard <commit-hash>` (be careful as current work is lost).

## 8. Comparative analysis of Rebase and Merge

| Characteristic | git rebase | git merge |
| --- | --- | --- |
| History structure | Linear, refined history (commits regenerated) | Branch splitting/merging explicitly shown (merge commit created) |
| Commit identifier | New hash generated | Original commit hash retained |
| Shared branch application | Strictly forbidden | Can be safely applied |
| Conflict management | May occur per commit (multiple resolutions needed) | Unified resolution at single merge point |
| Primary use cases | Local history optimization, working branch synchronization | Integrating completed features to main branch |

The optimal strategy may differ depending on team workflow and project characteristics. If you prefer linear history management, rebase is suitable; if explicit preservation of branch history is important, merge is better. Generally, a hybrid approach is effective: refine history within working branches using rebase, and apply merge with `--no-ff` option when integrating into main branch.

## Conclusion

`git rebase` is a powerful tool for history management and codebase synchronization, but improper application can cause serious collaboration problems. Adhering to the principle of never rebasing shared history and using `--force-with-lease` as a safeguard when pushing rebased branches is essential. Following these principles and best practices enables clean and traceable history management through rebase.
