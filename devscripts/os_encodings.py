#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys as _sys
import locale as _locale

_locale_enc = _locale.getpreferredencoding()

if _sys.stdout.encoding == None:
    # Pipe! Assume is a pipe to a file
    stdout = _locale_enc
else:
    stdout = _sys.stdout.encoding
    
if _sys.stderr.encoding == None:
    stderr = _locale_enc
else:
    stderr = _sys.stderr.encoding
    
if _sys.stdin.encoding == None:
    stdin = _locale_enc
else:
    stdin = _sys.stdin.encoding

argv = _locale_enc

subprocess = _locale_enc
