from archeos_repos import repos, master_repos
from buildbot.changes.gitpoller import GitPoller

sources = []

# To add sources with other settings add other loops
for name, url in repos.iteritems():
    sources.append(GitPoller(
        url,
        workdir='/home/builder/buildbot/gitpoller/' + name + '/',
        branches=True,
        pollinterval=300))

for name, url in master_repos.iteritems():
    sources.append(GitPoller(
        url,
        workdir='/home/builder/buildbot/gitpoller/' + name + '/',
        branches=['master'],
        pollinterval=300))
