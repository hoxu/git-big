# gig, git-in-git

Store big files in the git repository itself, without cloning them when you clone the repository

Like git-annex but without requiring any extra software on the remote git repository (eg. github).

## Synopsis

```
gig add <file|path>   # sha256, hash-object -w, mv+ln
gig fetch [file|path] # fetch given file or all files on path
gig fetch --all       # fetch all files from remote refs/gig/, including old versions
gig push [file|path]
gig push --all        # push all files, including old versions
gig unlock <file>     # change symlink back to file (for editing)
gig lock <file>       # change file back to symlink (reverting changes?)
gig drop <file>       # remove .git/gig/objects/sha256 and .git/refs/gig/sha256
gig fold              # remove .git/gig/objects/sha256
gig unfold            # create .git/gig/objects/sha256
gig cull              # remove .git/refs/gig/sha256 if it exists on remote, --force to remove anyway
gig sync              # fetch all files in HEAD, then push all files in HEAD
gig sync --all        # ditto, but old versions as well
gig detach <file>     # ??? remove .gig/refs/gig/sha256 ?
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
