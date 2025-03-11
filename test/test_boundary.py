import pytest
from test.TestUtils import TestUtils
from library_management_system import *  # Import all functions directly

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Consolidated test for boundary scenarios"""
    try:
        # Test with empty book list
        empty_books = []
        
        # Test empty list filtering
        filtered_genre = filter_by_genre(empty_books, "fiction")
        assert filtered_genre == [], "Filtering empty list by genre should return empty list"
        
        filtered_available = filter_by_availability(empty_books, True)
        assert filtered_available == [], "Filtering empty list by availability should return empty list"
        
        filtered_decade = filter_by_decade(empty_books, 2010)
        assert filtered_decade == [], "Filtering empty list by decade should return empty list"
        
        filtered_keyword = filter_by_keyword(empty_books, "Python")
        assert filtered_keyword == [], "Filtering empty list by keyword should return empty list"
        
        # Test empty list transformations
        transformed_titles = transform_titles(empty_books, "upper")
        assert transformed_titles == [], "Transforming titles on empty list should return empty list"
        
        citations = generate_citations(empty_books)
        assert citations == [], "Generating citations on empty list should return empty list"
        
        availability = get_book_availability(empty_books)
        assert availability == [], "Getting availability on empty list should return empty list"
        
        # Test empty list statistics
        genre_counts = calculate_genre_counts(empty_books)
        for genre, count in genre_counts.items():
            assert count == 0, f"Genre count for '{genre}' should be 0 on empty list"
        
        avg_popularity = calculate_average_popularity(empty_books)
        assert avg_popularity == 0.0, "Average popularity should be 0.0 on empty list"
        
        # Test edge cases with real data
        books, new_arrivals = initialize_data()
        
        # Test single item lists
        single_book = [books[0]]
        
        # Single book filtering
        filtered = filter_by_genre(single_book, single_book[0]["genre"])
        assert len(filtered) == 1, "Filtering should find the single matching book"
        
        filtered = filter_by_genre(single_book, "not-a-real-genre")
        assert len(filtered) == 0, "Filtering should return empty list when no matches"
        
        # Test publication year edge cases
        # Find earliest and latest years
        years = [book["publication_year"] for book in books]
        earliest = min(years)
        latest = max(years)
        
        # Test earliest decade
        earliest_decade = (earliest // 10) * 10
        earliest_decade_books = filter_by_decade(books, earliest_decade)
        assert all(book["publication_year"] // 10 * 10 == earliest_decade for book in earliest_decade_books), f"All books should be from {earliest_decade}s"
        
        # Test latest decade
        latest_decade = (latest // 10) * 10
        latest_decade_books = filter_by_decade(books, latest_decade)
        assert all(book["publication_year"] // 10 * 10 == latest_decade for book in latest_decade_books), f"All books should be from {latest_decade}s"
        
        # Test non-existent decade
        non_existent_decade = 1900  # Assuming no books from 1900s
        non_existent_books = filter_by_decade(books, non_existent_decade)
        assert len(non_existent_books) == 0, f"No books should be found for decade {non_existent_decade}"
        
        # Test rating boundary values
        min_rating = min(book["popularity_score"] for book in books)
        max_rating = max(book["popularity_score"] for book in books)
        
        # Test integration with empty lists
        integrated = integrate_new_arrivals([], [])
        assert integrated == [], "Integrating empty lists should result in empty list"
        
        integrated = integrate_new_arrivals([], new_arrivals)
        assert len(integrated) == len(new_arrivals), "Integrating empty with new_arrivals should equal new_arrivals length"
        
        integrated = integrate_new_arrivals(books, [])
        assert len(integrated) == len(books), "Integrating books with empty list should equal books length"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

def test_edge_case_filtering(test_obj):
    """Test filtering with edge case inputs"""
    try:
        books, _ = initialize_data()
        
        # Test case sensitivity in keyword filtering
        uppercase_keyword = "PYTHON"
        lowercase_keyword = "python"
        
        uppercase_results = filter_by_keyword(books, uppercase_keyword)
        lowercase_results = filter_by_keyword(books, lowercase_keyword)
        
        assert len(uppercase_results) == len(lowercase_results), "Keyword filtering should be case-insensitive"
        assert set(book["id"] for book in uppercase_results) == set(book["id"] for book in lowercase_results), "Same books should be found regardless of case"
        
        # Test partial word matching
        partial_keyword = "Py"  # Should match "Python"
        partial_results = filter_by_keyword(books, partial_keyword)
        full_results = filter_by_keyword(books, "Python")
        
        assert partial_results == full_results, "Partial keywords should match containing words"
        
        # Test empty string keyword
        empty_keyword_results = filter_by_keyword(books, "")
        assert len(empty_keyword_results) == len(books), "Empty keyword should match all books"
        
        # Test single character inputs
        for case in ["upper", "lower", "title"]:
            titles = transform_titles(books, case)
            assert len(titles) == len(books), f"Should transform all titles for case '{case}'"
        
        # Test invalid case parameter
        invalid_case_titles = transform_titles(books, "invalid_case")
        original_titles = [book["title"] for book in books]
        assert invalid_case_titles == original_titles, "Invalid case should return original titles"
        
        test_obj.yakshaAssert("TestEdgeCaseFiltering", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
        pytest.fail(f"Edge case filtering test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])