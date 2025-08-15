#!/usr/bin/env python3
"""Tests for dayspan package."""

import pytest
from dayspan import calculate_days, parse_date


def test_calculate_days():
    """Test basic day calculation."""
    # Test single day
    days, _, _ = calculate_days("20250101", "20250101")
    assert days == 1
    
    # Test month
    days, _, _ = calculate_days("20250101", "20250131")
    assert days == 31
    
    # Test leap year
    days, _, _ = calculate_days("20240101", "20241231")
    assert days == 366
    
    # Test non-leap year
    days, _, _ = calculate_days("20250101", "20251231")
    assert days == 365


def test_invalid_dates():
    """Test invalid date handling."""
    with pytest.raises(ValueError):
        calculate_days("20250101", "20241231")  # End before start
    
    with pytest.raises(ValueError):
        calculate_days("2025010", "20251231")  # Wrong format
    
    with pytest.raises(ValueError):
        calculate_days("20250132", "20251231")  # Invalid day


if __name__ == "__main__":
    # Run basic tests without pytest
    print("Running basic tests...")
    
    # Test 1: Single day
    days, _, _ = calculate_days("20250101", "20250101")
    assert days == 1, f"Expected 1, got {days}"
    print("✓ Single day test passed")
    
    # Test 2: Full year
    days, _, _ = calculate_days("20250101", "20251231")
    assert days == 365, f"Expected 365, got {days}"
    print("✓ Full year test passed")
    
    # Test 3: Leap year
    days, _, _ = calculate_days("20240101", "20241231")
    assert days == 366, f"Expected 366, got {days}"
    print("✓ Leap year test passed")
    
    print("\nAll tests passed!")