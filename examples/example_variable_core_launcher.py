#!/usr/bin/env python

import pylauncher

##
## Emulate the classic launcher, using a one liner
##

pylauncher.ClassicLauncher("corecommandlines",
                           debug="job+task+host+exec+command",
                           cores="file",
                           )

