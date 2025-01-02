import pytest
from whoisquery.cli import main
from unittest.mock import patch
import json

class TestCLI:
    @patch('whoisquery.core.WhoisQuery.get_whois_data')
    def test_cli_basic_output(self, mock_get_whois):
        """Test basic CLI output"""
        mock_data = {"name": "example.com", "created": "2020-01-01"}
        mock_get_whois.return_value = mock_data
        
        with patch('sys.argv', ['whoisquery', '-d', 'example.com']):
            assert main() == 0


    @patch('whoisquery.core.WhoisQuery.get_whois_data')
    def test_cli_error_handling(self, mock_get_whois):
        """Test CLI error handling"""
        mock_data = {
            "name": "example.com",
            "error": "Test error",
            "registered": False,
            "raw_whois": None
        }
        mock_get_whois.return_value = mock_data
        
        with patch('sys.argv', ['whoisquery', '-d', 'example.com']):
            with patch('builtins.print') as mock_print:
                assert main() == 1
                mock_print.assert_called_once_with(json.dumps(mock_data, indent=2)) 
