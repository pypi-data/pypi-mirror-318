import pytest
from whoisquery import WhoisQuery
from unittest.mock import patch

# Sample WHOIS output for testing
SAMPLE_WHOIS_OUTPUT = """
Domain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.example-registrar.com
Registrar URL: http://www.example-registrar.com
Updated Date: 2022-08-14T07:01:31Z
Creation Date: 1995-08-14T04:00:00Z
Registrar Registration Expiration Date: 2023-08-13T04:00:00Z
Registrar: Example Registrar, Inc.
Registrar IANA ID: 1234
Registrar Abuse Contact Email: abuse@example-registrar.com
Registrar Abuse Contact Phone: +1.1234567890
Domain Status: clientTransferProhibited
Name Server: NS1.EXAMPLE.COM
Name Server: NS2.EXAMPLE.COM
DNSSEC: signedDelegation

# whois.example-registrar.com
Domain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.example-registrar.com
Creation Date: 1995-08-14T04:00:00Z
Updated Date: 2022-08-14T07:01:31Z
"""

class TestWhoisQuery:
    def setup_method(self):
        self.domain = "example.com"
        self.whois = WhoisQuery(self.domain)

    def test_init(self):
        """Test initialization of WhoisQuery class"""
        assert self.whois.domain == self.domain

    @patch('subprocess.run')
    def test_execute_whois_success(self, mock_run):
        """Test successful WHOIS query execution"""
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = SAMPLE_WHOIS_OUTPUT
        
        output = self.whois.execute_whois()
        assert output == SAMPLE_WHOIS_OUTPUT
        mock_run.assert_called_once_with(
            ["whois", self.domain],
            stdout=-1,  # subprocess.PIPE
            stderr=-1,  # subprocess.PIPE
            text=True
        )

    @patch('subprocess.run')
    def test_execute_whois_failure(self, mock_run):
        """Test WHOIS query execution failure"""
        mock_run.return_value.returncode = 1
        mock_run.return_value.stderr = "Error: Connection failed"
        
        with pytest.raises(Exception) as exc_info:
            self.whois.execute_whois()
        assert "Error executing whois" in str(exc_info.value)

    def test_extract_whois_server(self):
        """Test WHOIS server extraction"""
        server = self.whois.extract_whois_server(SAMPLE_WHOIS_OUTPUT)
        assert server == "whois.example-registrar.com"

    def test_parse_output(self):
        """Test WHOIS output parsing"""
        parsed_data = self.whois.parse_output(SAMPLE_WHOIS_OUTPUT)
        
        assert parsed_data["name"] == "example.com"
        assert parsed_data["created"] == "1995-08-14T04:00:00Z"
        assert parsed_data["changed"] == "2022-08-14T07:01:31Z"
        assert parsed_data["nameservers"] == ["NS1.EXAMPLE.COM", "NS2.EXAMPLE.COM"]
        assert parsed_data["dnssec"] == "signedDelegation"
        assert parsed_data["registrar"]["id"] == "1234"
        assert parsed_data["registrar"]["email"] == "abuse@example-registrar.com"
        assert parsed_data["registrar"]["phone"] == "+1.1234567890" 