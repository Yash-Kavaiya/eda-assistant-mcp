#!/usr/bin/env python3
"""
Test suite for EDA Assistant MCP tools
"""

import pytest
import tempfile
import os
from pathlib import Path
from server import (
    read_text_file,
    read_csv_file,
    list_files_in_directory,
    get_file_info
)


class TestFileOperationTools:
    """Test file operation tools"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
        
        # Create test files
        self.test_txt_file = self.temp_path / "test.txt"
        self.test_txt_file.write_text("Hello, World!\nThis is a test file.\nLine 3")
        
        self.test_csv_file = self.temp_path / "test.csv"
        self.test_csv_file.write_text(
            "name,age,city\nAlice,25,New York\nBob,30,Los Angeles\nCharlie,35,Chicago"
        )
        
        self.empty_file = self.temp_path / "empty.txt"
        self.empty_file.write_text("")
    
    def teardown_method(self):
        """Clean up test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_read_text_file_success(self):
        """Test successful text file reading"""
        result = read_text_file(str(self.test_txt_file))
        
        assert "File successfully read!" in result
        assert "Hello, World!" in result
        assert "This is a test file." in result
        assert "Line 3" in result
        assert "3" in result  # Line count
        assert "utf-8" in result  # Encoding
    
    def test_read_text_file_nonexistent(self):
        """Test reading non-existent file"""
        result = read_text_file("/nonexistent/file.txt")
        
        assert "Error: File '/nonexistent/file.txt' does not exist." in result
    
    def test_read_text_file_directory(self):
        """Test reading directory instead of file"""
        result = read_text_file(str(self.temp_dir))
        
        assert f"Error: '{self.temp_dir}' is not a file." in result
    
    def test_read_csv_file_success(self):
        """Test successful CSV file reading"""
        result = read_csv_file(str(self.test_csv_file))
        
        assert "CSV File Successfully Loaded!" in result
        assert "3 rows × 3 columns" in result
        assert "name: object" in result
        assert "age: int64" in result
        assert "city: object" in result
        assert "Alice" in result
        assert "Bob" in result
        assert "Charlie" in result
    
    def test_read_csv_file_preview_rows(self):
        """Test CSV file reading with custom preview rows"""
        result = read_csv_file(str(self.test_csv_file), preview_rows=2)
        
        assert "CSV File Successfully Loaded!" in result
        assert "Alice" in result
        assert "Bob" in result
        # Charlie should not be in preview with only 2 rows
        lines = result.split('\n')
        preview_section = False
        charlie_in_preview = False
        for line in lines:
            if "Data Preview" in line:
                preview_section = True
            elif preview_section and "Charlie" in line:
                charlie_in_preview = True
                break
            elif "Numeric Columns Summary" in line:
                break
        assert not charlie_in_preview
    
    def test_read_csv_file_nonexistent(self):
        """Test reading non-existent CSV file"""
        result = read_csv_file("/nonexistent/file.csv")
        
        assert "Error: File '/nonexistent/file.csv' does not exist." in result
    
    def test_list_files_in_directory_success(self):
        """Test successful directory listing"""
        result = list_files_in_directory(str(self.temp_dir))
        
        assert f"Files in directory: {self.temp_path.absolute()}" in result
        assert "Found 3 file(s)" in result
        assert "test.txt" in result
        assert "test.csv" in result
        assert "empty.txt" in result
    
    def test_list_files_in_directory_with_extension(self):
        """Test directory listing with extension filter"""
        result = list_files_in_directory(str(self.temp_dir), ".txt")
        
        assert "(filtered by extension: .txt)" in result
        assert "Found 2 file(s)" in result
        assert "test.txt" in result
        assert "empty.txt" in result
        assert "test.csv" not in result
    
    def test_list_files_in_directory_nonexistent(self):
        """Test listing non-existent directory"""
        result = list_files_in_directory("/nonexistent/directory")
        
        assert "Error: Directory '/nonexistent/directory' does not exist." in result
    
    def test_list_files_in_directory_file(self):
        """Test listing file instead of directory"""
        result = list_files_in_directory(str(self.test_txt_file))
        
        assert f"Error: '{self.test_txt_file}' is not a directory." in result
    
    def test_get_file_info_success(self):
        """Test successful file info retrieval"""
        result = get_file_info(str(self.test_txt_file))
        
        assert f"File Information: {self.test_txt_file.name}" in result
        assert f"Full Path: {self.test_txt_file.absolute()}" in result
        assert "File Name: test.txt" in result
        assert "Extension: .txt" in result
        assert "File Type: Text file" in result
        assert "Size:" in result
        assert "Created:" in result
        assert "Modified:" in result
    
    def test_get_file_info_csv(self):
        """Test file info for CSV file"""
        result = get_file_info(str(self.test_csv_file))
        
        assert "Extension: .csv" in result
        assert "File Type: CSV (Comma-Separated Values)" in result
    
    def test_get_file_info_nonexistent(self):
        """Test file info for non-existent file"""
        result = get_file_info("/nonexistent/file.txt")
        
        assert "Error: File '/nonexistent/file.txt' does not exist." in result
    
    def test_get_file_info_directory(self):
        """Test file info for directory"""
        result = get_file_info(str(self.temp_dir))
        
        assert f"Error: '{self.temp_dir}' is not a file." in result


class TestFileToolsIntegration:
    """Test integration scenarios for file tools"""
    
    def setup_method(self):
        """Set up integration test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
        
        # Create a more complex CSV for testing
        self.complex_csv = self.temp_path / "complex.csv"
        csv_content = """product_id,product_name,category,price,stock_quantity,last_updated
1,"Laptop Pro",Electronics,1299.99,15,2024-01-15
2,"Coffee Maker","Home & Kitchen",89.99,23,2024-01-14
3,"Running Shoes",Sports,129.99,8,2024-01-13
4,"Book: Python Programming",Books,45.50,12,2024-01-12
5,"Wireless Headphones",Electronics,199.99,0,2024-01-11"""
        self.complex_csv.write_text(csv_content)
    
    def teardown_method(self):
        """Clean up integration test fixtures"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_comprehensive_csv_analysis(self):
        """Test comprehensive CSV analysis workflow"""
        # First, list files to find CSV
        list_result = list_files_in_directory(str(self.temp_dir), ".csv")
        assert "complex.csv" in list_result
        
        # Get file info
        info_result = get_file_info(str(self.complex_csv))
        assert "CSV (Comma-Separated Values)" in info_result
        
        # Read and analyze CSV
        csv_result = read_csv_file(str(self.complex_csv))
        assert "5 rows × 6 columns" in csv_result
        assert "product_id: int64" in csv_result
        assert "price: float64" in csv_result
        assert "Laptop Pro" in csv_result
        assert "Wireless Headphones" in csv_result
        
        # Check numeric summary is included
        assert "Numeric Columns Summary:" in csv_result
    
    def test_workflow_with_missing_data(self):
        """Test workflow with missing data in CSV"""
        csv_with_missing = self.temp_path / "missing_data.csv"
        csv_content = """name,age,salary,department
Alice,25,50000,Engineering
Bob,,60000,Marketing
Charlie,35,,Engineering
Diana,28,55000,
Eve,32,62000,Marketing"""
        csv_with_missing.write_text(csv_content)
        
        result = read_csv_file(str(csv_with_missing))
        
        # Should detect missing values
        assert "Missing:" in result
        # Should show percentages for missing data
        assert "%" in result
        # Should handle mixed data types appropriately
        assert "age:" in result
        assert "salary:" in result


if __name__ == "__main__":
    pytest.main([__file__])