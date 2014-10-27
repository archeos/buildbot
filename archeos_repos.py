# These repos are checked in archeos_sources.py for modifications on ALL branches
all_branch_repos = {'archeos-manual': 'git://github.com/archeos/archeos-manual.git',
         'archeos-meta': 'git://github.com/archeos/archeos-meta.git',
         'archeos-desktop': 'git://github.com/archeos/archeos-desktop.git'
         }

# These repos are checked in archeos_sources.py for modification only on branch master
master_repos = {'cloudcompare-archeos': 'git://git@github.com:archeos/cloudcompare-archeos.git'}

# this dict must contain all repos
all_repos = dict(all_branch_repos.items() + master_repos.items())

