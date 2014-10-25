from secret import webauth
from buildbot.status import html
from buildbot.status.web import authz, auth

basic_auth = []
all_auth = []
for k, v in webauth.iteritems():
    basic_auth.append((k, v))
 
authz_cfg=authz.Authz(
    # change any of these to True to enable; see the manual for more
    # options
    auth=auth.BasicAuth(basic_auth),
    gracefulShutdown = True,
    forceBuild = 'auth', # use this to test your slave once it is set up
    forceAllBuilds = True,
    pingBuilder = True,
    stopBuild = True,
    stopAllBuilds = True,
    cancelPendingBuild = True,
)

a1 = html.WebStatus(http_port=8010, authz=authz_cfg)

all_auth.append(a1)
