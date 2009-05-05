import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def main():
    to_change = ['_sources', '_static']
    for f in os.listdir(ROOT):
        if os.path.isdir(f) and f in to_change:
            print f

if __name__ == '__main__':
    main()