from archeos_repos import repos
from buildbot.changes.gitpoller import GitPoller

sources = []

# At the moment only one type of source.
# To add sources with other settings add other loops
for name, url in repos.iteritems():
    sources.append(GitPoller(
        url,
        workdir='/home/builder/buildbot/gitpoller/' + name + '/',
        branches=True,
        pollinterval=300))

