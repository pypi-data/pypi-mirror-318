"""Command-line interface for Gemgroq configuration."""

import sys
import argparse
from .config import setup_keys

def main():
    parser = argparse.ArgumentParser(description='Gemgroq CLI configuration tool')
    parser.add_argument('--setup', action='store_true', help='Set up or update API keys')
    parser.add_argument('--force', action='store_true', help='Force new key setup even if keys exist')
    
    args = parser.parse_args()
    
    try:
        if args.setup or args.force:
            setup_keys(force=args.force)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print("\nSetup cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
