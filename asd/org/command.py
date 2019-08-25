def main():
    import argparse
    from argparse import RawTextHelpFormatter
    from . import org
    helpMode = '''-a: move all files with keys to specific dir(dest)
All keys must exist to move the file.
-o: move all files with keys to specific dir(dst)
at least one key must exist to move the file'''

    helpKeys = 'The keywords to look for in the file names'
    helpDest = 'The Name Of The Folder into which the files\nto be moved'

    parser = argparse.ArgumentParser(prog = 'organize files in folders',formatter_class=RawTextHelpFormatter)
    parser.add_argument('mode',help = helpMode,choices = ['all','one'])
    parser.add_argument('dest',type = str,help = helpDest)
    parser.add_argument('keys',nargs = '+',type = str,help = helpKeys)
    a   = parser.parse_args()
    org.Org(a.mode,a.dest,a.keys)
main()




