import pytest
from test.TestUtils import TestUtils
from library_management_system import *  # Import all functions directly

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Consolidated test for input validation and error handling"""
    try:
        books, new_arrivals = initialize_data()
        
        # Test with None inputs (first function only)
        functions_to_test = [
            (filter_by_genre, [None, "fiction"]),
            (filter_by_availability, [None, True]),
            (filter_by_decade, [None, 2010]),
            (filter_by_keyword, [None, "Python"]),
            (transform_titles, [None, "upper"]),
            (generate_citations, [None]),
            (get_book_availability, [None]),
            (calculate_genre_counts, [None]),
            (calculate_average_popularity, [None]),
            (integrate_new_arrivals, [None, new_arrivals]),
            (integrate_new_arrivals, [books, None]),
        ]
        
        # Test all functions with None inputs
        for func, args in functions_to_test:
            with pytest.raises(Exception):
                func(*args)
        
        # Test with incorrect parameter types (sample only)
        with pytest.raises(Exception):
            filter_by_genre("not a list", "fiction")
            
        with pytest.raises(Exception):
            filter_by_genre(books, 123)
            
        with pytest.raises(Exception):
            filter_by_availability(books, "not a boolean")
            
        with pytest.raises(Exception):
            filter_by_decade(books, "not an integer")
        
        # Test with malformed books for formatting
        malformed_book = {"id": "M001"}  # Missing required fields
        with pytest.raises(Exception):
            get_formatted_book(malformed_book)
        
        # Test with invalid data_type
        display_data(books, "invalid_type")  # Should not crash
        
        # Test edge cases for filters
        assert filter_by_genre(books, "invalid_genre") == [], "Should return empty list for non-existent genre"
        assert filter_by_decade(books, 1900) == [], "Should return empty list for very old decade"
        
        # Ensure malformed data integration doesn't crash
        malformed_books = [{"id": "M001"}]
        result = integrate_new_arrivals(malformed_books, new_arrivals)
        assert len(result) == len(malformed_books) + len(new_arrivals), "Should handle malformed books gracefully"
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])