#!/usr/bin/env python3
"""Core module for calculating days between dates."""

from datetime import datetime


def parse_date(date_str):
    """
    Parse date string in YYYYMMDD format.
    
    Args:
        date_str (str): Date in YYYYMMDD format
        
    Returns:
        datetime: Parsed datetime object
        
    Raises:
        ValueError: If date format is invalid
    """
    if not date_str or len(date_str) != 8:
        raise ValueError(f"Invalid date format: '{date_str}'. Expected YYYYMMDD format.")
    
    try:
        year = int(date_str[0:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])
        return datetime(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: '{date_str}'. {str(e)}")


def calculate_days(start_date_str, end_date_str):
    """
    Calculate days between two dates (inclusive).
    
    Args:
        start_date_str (str): Start date in YYYYMMDD format
        end_date_str (str): End date in YYYYMMDD format
        
    Returns:
        tuple: (days_count, start_date, end_date) where dates are formatted strings
        
    Raises:
        ValueError: If date format is invalid or end date is before start date
    """
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    
    if end_date < start_date:
        raise ValueError(f"End date ({end_date_str}) must be after or equal to start date ({start_date_str})")
    
    # Calculate difference and add 1 to include both dates
    days_difference = (end_date - start_date).days + 1
    
    # Format dates for display
    start_formatted = start_date.strftime("%Y-%m-%d")
    end_formatted = end_date.strftime("%Y-%m-%d")
    
    return days_difference, start_formatted, end_formatted