#!/usr/bin/env python3
"""Command-line interface for dayspan."""

import sys
import argparse
from .calculator import calculate_days
from dayspan import __version__


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog='dayspan',
        description='Calculate days between two dates (inclusive)',
        epilog='Example: dayspan 20250101 20251231'
    )
    
    parser.add_argument(
        'start_date',
        help='Start date in YYYYMMDD format'
    )
    
    parser.add_argument(
        'end_date',
        help='End date in YYYYMMDD format'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )

    args = parser.parse_args()
    
    try:
        days, start_formatted, end_formatted = calculate_days(args.start_date, args.end_date)
        
        if args.verbose:
            print(f"Start date: {start_formatted}")
            print(f"End date: {end_formatted}")
            print(f"Days from {start_formatted} to {end_formatted} (inclusive): {days} days")
        else:
            print(f"{days} days (from {start_formatted} to {end_formatted}, inclusive)")
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
