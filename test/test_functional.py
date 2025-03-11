import pytest
import inspect
import importlib
import re
from test.TestUtils import TestUtils
from library_management_system import *  # Import all functions directly

@pytest.fixture
def test_obj():
    return TestUtils()

@pytest.fixture
def sample_books():
    """Sample books for testing"""
    return initialize_data()[0]  # First element is books

@pytest.fixture
def sample_new_arrivals():
    """Sample new arrivals for testing"""
    return initialize_data()[1]  # Second element is new_arrivals

def test_variable_naming(test_obj):
    """Test that the required variable names are used in the solution"""
    try:
        # Import the module
        try:
            module = importlib.import_module("solution")
        except ImportError:
            # Try alternative module name
            try:
                module = importlib.import_module("library_management_system")
            except ImportError:
                raise ImportError("Could not import solution module. Make sure it's named 'solution.py' or 'library_management_system.py'")

        # Check initialize_data function returns properly named variables
        init_source = inspect.getsource(module.initialize_data)
        
        # Check for return statement with the expected variable names
        assert "return books, new_arrivals" in init_source, "initialize_data() must return variables named 'books' and 'new_arrivals'"
        
        # Check that the main function uses the required variable names
        main_source = inspect.getsource(module.main)
        
        # Check for proper variable assignment from initialize_data
        assert re.search(r"books,\s*new_arrivals\s*=\s*initialize_data\(\)", main_source), "main() must assign initialize_data() return values to variables named 'books' and 'new_arrivals'"
        
        # Check list comprehension functions use the right parameter names
        assert "def filter_by_genre(books, genre)" in inspect.getsource(module), "filter_by_genre() must use parameter names 'books' and 'genre'"
        assert "def filter_by_availability(books, available" in inspect.getsource(module), "filter_by_availability() must use parameter name 'books'"
        assert "def filter_by_decade(books, decade)" in inspect.getsource(module), "filter_by_decade() must use parameter names 'books' and 'decade'"
        assert "def filter_by_keyword(books, keyword)" in inspect.getsource(module), "filter_by_keyword() must use parameter names 'books' and 'keyword'"
        
        # For transformation functions
        assert "def transform_titles(books, case" in inspect.getsource(module), "transform_titles() must use parameter names 'books' and 'case'"
        assert "def generate_citations(books)" in inspect.getsource(module), "generate_citations() must use parameter name 'books'"
        assert "def get_book_availability(books)" in inspect.getsource(module), "get_book_availability() must use parameter name 'books'"
        
        # For statistical functions
        assert "def calculate_genre_counts(books)" in inspect.getsource(module), "calculate_genre_counts() must use parameter name 'books'"
        assert "def calculate_average_popularity(books)" in inspect.getsource(module), "calculate_average_popularity() must use parameter name 'books'"
        
        # For integrating new arrivals
        integrate_source = inspect.getsource(module.integrate_new_arrivals)
        assert "def integrate_new_arrivals(books, new_arrivals)" in integrate_source, "integrate_new_arrivals() must use parameter names 'books' and 'new_arrivals'"
        
        # Check predefined books exist with right IDs
        assert '"B001"' in init_source, "initialize_data() must contain book with ID 'B001'"
        assert '"B002"' in init_source, "initialize_data() must contain book with ID 'B002'"
        assert '"B003"' in init_source, "initialize_data() must contain book with ID 'B003'"
        assert '"B004"' in init_source, "initialize_data() must contain book with ID 'B004'"
        assert '"B005"' in init_source, "initialize_data() must contain book with ID 'B005'"
        
        # Check new arrivals
        assert '"N001"' in init_source, "initialize_data() must contain new arrival with ID 'N001'"
        assert '"N002"' in init_source, "initialize_data() must contain new arrival with ID 'N002'"
        
        test_obj.yakshaAssert("TestVariableNaming", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestVariableNaming", False, "functional")
        pytest.fail(f"Variable naming test failed: {str(e)}")

def test_list_comprehension_filtering(test_obj, sample_books):
    """Test list comprehension filtering operations"""
    try:
        # Test filter_by_genre
        fiction_books = filter_by_genre(sample_books, "fiction")
        assert all(book["genre"] == "fiction" for book in fiction_books), "All filtered books should be fiction genre"
        
        # Test filter_by_availability
        available_books = filter_by_availability(sample_books, True)
        assert all(book["available"] for book in available_books), "All filtered books should be available"
        
        # Test filter_by_decade
        decade_2010_books = filter_by_decade(sample_books, 2010)
        assert all(book["publication_year"] // 10 * 10 == 2010 for book in decade_2010_books), "All filtered books should be from 2010s"
        
        # Test filter_by_keyword
        python_books = filter_by_keyword(sample_books, "Python")
        assert all("python" in book["title"].lower() or "python" in book["author"].lower() for book in python_books), "All filtered books should contain keyword 'Python'"
        
        test_obj.yakshaAssert("TestListComprehensionFiltering", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestListComprehensionFiltering", False, "functional")
        pytest.fail(f"List comprehension filtering test failed: {str(e)}")

def test_list_comprehension_transformation(test_obj, sample_books):
    """Test list comprehension transformation operations"""
    try:
        # Test transform_titles
        uppercase_titles = transform_titles(sample_books, "upper")
        assert all(title.isupper() for title in uppercase_titles), "All titles should be uppercase"
        
        lowercase_titles = transform_titles(sample_books, "lower")
        assert all(title.islower() for title in lowercase_titles), "All titles should be lowercase"
        
        # Test generate_citations
        citations = generate_citations(sample_books)
        for i, book in enumerate(sample_books):
            citation = citations[i]
            assert book["author"] in citation, "Citation should contain author"
            assert str(book["publication_year"]) in citation, "Citation should contain publication year"
            assert book["title"] in citation, "Citation should contain title"
        
        # Test get_book_availability
        availability_list = get_book_availability(sample_books)
        for i, book in enumerate(sample_books):
            item = availability_list[i]
            assert book["title"] in item, "Item should contain book title"
            assert ("Available" in item) == book["available"], "Item should correctly indicate availability"
            assert ("On Loan" in item) == (not book["available"]), "Item should correctly indicate loan status"
        
        test_obj.yakshaAssert("TestListComprehensionTransformation", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestListComprehensionTransformation", False, "functional")
        pytest.fail(f"List comprehension transformation test failed: {str(e)}")

def test_list_comprehension_statistics(test_obj, sample_books):
    """Test list comprehension statistics operations"""
    try:
        # Test calculate_genre_counts
        genre_counts = calculate_genre_counts(sample_books)
        
        # Check all genres are included
        required_genres = ["fiction", "non-fiction", "reference", "children", "biography"]
        for genre in required_genres:
            assert genre in genre_counts, f"Genre counts should include '{genre}'"
        
        # Verify counts
        for genre, count in genre_counts.items():
            actual_count = len([book for book in sample_books if book["genre"] == genre])
            assert count == actual_count, f"Genre count for '{genre}' should be {actual_count}"
        
        # Test calculate_average_popularity
        avg_popularity = calculate_average_popularity(sample_books)
        expected_avg = round(sum(book["popularity_score"] for book in sample_books) / len(sample_books), 2)
        assert avg_popularity == expected_avg, f"Average popularity should be {expected_avg}"
        
        test_obj.yakshaAssert("TestListComprehensionStatistics", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestListComprehensionStatistics", False, "functional")
        pytest.fail(f"List comprehension statistics test failed: {str(e)}")

def test_list_comprehension_integration(test_obj, sample_books, sample_new_arrivals):
    """Test list comprehension integration operations"""
    try:
        # Test integrate_new_arrivals
        integrated_books = integrate_new_arrivals(sample_books, sample_new_arrivals)
        
        # Check that the integrated list has the right size
        assert len(integrated_books) == len(sample_books) + len(sample_new_arrivals), "Integrated list should contain all books"
        
        # Check that new arrivals have the "section" field
        new_arrival_ids = [book["id"] for book in sample_new_arrivals]
        for book in integrated_books:
            if book["id"] in new_arrival_ids:
                assert "section" in book, f"New arrival {book['id']} should have 'section' field"
                assert book["section"] == "New", f"New arrival {book['id']} should have section 'New'"
        
        # Check that original books do not have the "section" field
        original_book_ids = [book["id"] for book in sample_books]
        for book in integrated_books:
            if book["id"] in original_book_ids:
                assert "section" not in book, f"Original book {book['id']} should not have 'section' field"
        
        test_obj.yakshaAssert("TestListComprehensionIntegration", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestListComprehensionIntegration", False, "functional")
        pytest.fail(f"List comprehension integration test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])