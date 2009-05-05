import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

def main():
    """not functional at this time -> do it by find and replace
    
    find '_sources' replace by 'sources'
    find '_static' replace by 'static'
    """
    to_change = ['_sources', '_static']
    include_file_ext = ['html', 'js']
    for f in os.listdir(ROOT):
        if os.path.isdir(f):
            if f in to_change:
                shutil.move(os.path.join(ROOT, f), os.path.join(ROOT, f[1:]))
        else:
            print f

if __name__ == '__main__':
    main()