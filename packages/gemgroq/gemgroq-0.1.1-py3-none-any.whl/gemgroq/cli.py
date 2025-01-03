"""Command-line interface for Gemgroq configuration."""

import argparse
from .config import setup_keys

def main():
    parser = argparse.ArgumentParser(description='Gemgroq CLI configuration tool')
    parser.add_argument('--setup', action='store_true', help='Set up or update API keys')
    parser.add_argument('--force', action='store_true', help='Force new key setup even if keys exist')
    
    args = parser.parse_args()
    
    if args.setup or args.force:
        setup_keys(force=args.force)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
