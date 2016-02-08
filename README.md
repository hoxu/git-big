# git-big

Store big files in the git repository itself, without cloning them when you clone the repository.

Like git-annex but without requiring any extra software on the remote git repository (eg. github).

## Synopsis

```
git big add [file|dir]...   # add file to git-big
git big fetch [file|dir]... # fetch files from remote
git big push [file|dir]...  # push files to remote
git big unlock <file>       # change symlink back to file (for editing)
git big drop <file>         # remove local copy of file
```

## Storage

* .git/gig/objects/sha256
* .git/refs/gig/sha256 -> object store
* remote (folded, culled)

## Tasks

* mv support like in git annex
* hook that removes .git/gig/objects/sha256 when no links to them exist in HEAD

## Pros and cons

Pros:
* large files are put into git object store, so they are under git delta algorithms. Good for modified files, bad for deleting files
* good if you have for example one changing large file, so only one file needs to be in the filesystem at once
* fast cloning
* large files are kept in the same repository
* no need for additional executables on the remote repository

Cons:
* if you have lots of large files that need to exist in filesystem unfolded (eg. a music collection), gig uses twice the size. Consider git annex

## Similar projects

* [git-annex](http://git-annex.branchable.com/)
* [git-fat](https://github.com/jedbrown/git-fat)
* [git-media](https://github.com/alebedev/git-media)
