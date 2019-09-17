def main():
    from . import ctrlf
    import os
    import argparse
    '''start of help msgs'''
    helpMatch  = 'The regex pattern you want to files to match.'
    helpIgnore = 'The regex pattern you want to files NOT to match.'
    helpPath   = 'the root path to start the search -if not specified\
            the current path is used-'
    '''end of help msgs'''
    parser = argparse.ArgumentParser(prog = 'Control-f')

    parser.add_argument('match',type = str,help=helpMatch)
    parser.add_argument('-i','--ignore',help=helpIgnore)
    parser.add_argument('-p','--path', default = None,help=helpPath)

    args = parser.parse_args()
    # if not os.path.isdir(args.path) and args.path!=None :
        # raise IOError('An invalid path has been input.')
    ctrlf.main_class(args.match,args.path,args.ignore)


# main()
