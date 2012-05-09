import sys, locale, platform

print platform.platform(1, 1)
print platform.python_implementation(), platform.python_version()

e_grave = u'\xe8'
param = sys.argv[1]
sys.stderr.write('Type: ')
inp = raw_input()

encodings = (('locale.getpreferredencoding()', locale.getpreferredencoding()),
             ('sys.stdout.encoding', sys.stdout.encoding),
             ('sys.stdin.encoding', sys.stdin.encoding),
             ('utf8', 'utf8'))
             
for name, encoding in encodings:
    print ''
    print '***', name, ':', encoding
    if encoding:
        print "u'\\xe8'          ", e_grave.encode(encoding, 'replace')
        print 'repr(sys.argv[1])', repr(param.decode(encoding, 'replace'))
        print 'repr(raw_input())', repr(inp.decode(encoding, 'replace'))
        
import os_encodings 
print ''
print '*** os_encodings ***'
print e_grave.encode(os_encodings.stdout), '', \
      param.decode(os_encodings.argv).encode(os_encodings.stdout), \
      repr(param.decode(os_encodings.argv)), '', \
      inp.decode(os_encodings.stdin).encode(os_encodings.stdout), \
      repr(inp.decode(os_encodings.stdin))
