# alt-branch-matching 

Alt Branch Matching is a command-line tool designed for comparing package versions across different branches of the Alt Linux repository ecosystem. Built specifically for Alt Linux developers and system administrators, this utility provides fast, accurate comparisons between branches such as p10, p11, and Sisyphus.

# Project launch

## Docker
1.  `git clone https://github.com/Tor344/alt-branch-matching.git`
2.  `cd alt-branch-matching`
3.  `docker build -f container/Containerfile -t alt-branch-matching .`
4.  `docker run --rm -it alt-branch-matching your_branch1 your_branch2
`

## Podman
1.  `git clone https://github.com/Tor344/alt-branch-matching.git`
2.  `cd alt-branch-matching`
3.  `podman run --rm -it alt-branch-matching`
4.  `podman run --rm -it alt-branch-matching  your_branch1 your_branch2`

## ALT linux 
1.  `git clone https://github.com/Tor344/alt-branch-matching.git`
2.  `cd alt-branch-matching`
3.  `su -`
4.  `apt-get update`
5.  `apt-get install -y git python3 python3-module-click python3-module-requests python3-module-tabulate python3-module-rpm`
6.  `python3 -m cli.main your_branch1 your_branch2`