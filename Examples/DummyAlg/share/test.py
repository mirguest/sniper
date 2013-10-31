#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lintao

import sys
sys.setdlopenflags( 0x100 | 0x2 )    # RTLD_GLOBAL | RTLD_NOW

import libSniperMgr
import libSniperPython as sp

mgr = libSniperMgr.SniperMgr()
sp.setProperty("Sniper", "EvtMax", 5)
sp.setProperty("Sniper", "InputSvc", "NONE")
sp.setProperty("Sniper", "LogLevel", 0)
sp.setProperty("Sniper", "Dlls", ["RootWriter", "DummyAlg"])

mgr.configure()

rw = sp.SvcMgr.get("RootWriter", True)
# now to configure the algs and svcs.
d = {"FILE1": "output1.root", "FILE2": "output2.root"}
rw.setProp("Output", d)

dalg = sp.AlgMgr.get("DummyAlg/dalg", True)


# begin to run
mgr.initialize()
mgr.run()
mgr.finalize()
