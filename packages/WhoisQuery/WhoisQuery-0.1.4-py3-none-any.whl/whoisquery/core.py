import subprocess
import re

class WhoisQuery:
    """
    A class to perform WHOIS lookups and parse the results.

    Attributes:
        domain (str): The domain name to perform the WHOIS lookup on.
    """

    def __init__(self, domain: str):
        """
        Initializes the WhoisQuery class with the given domain.

        Args:
            domain (str): The domain name to perform the WHOIS lookup on.
        """
        self.domain = domain

    def execute_whois(self):
        """
        Executes the WHOIS command for the domain.

        Returns:
            str: The raw output from the WHOIS command.

        Raises:
            Exception: If the WHOIS command fails or is not available.
        """
        try:
            result = subprocess.run(["whois", self.domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                raise Exception(f"Error executing whois: {result.stderr.strip()}")
            return result.stdout
        except FileNotFoundError:
            raise Exception("The 'whois' command is not available on the system.")

    def extract_whois_server(self, output: str):
        """
        Extracts the WHOIS server from the WHOIS command output.

        Args:
            output (str): The raw output from the WHOIS command.

        Returns:
            str: The WHOIS server.

        Raises:
            Exception: If the WHOIS server is not found in the output.
        """
        match = re.search(r"(?i)^Registrar WHOIS Server:\s*(\S+)", output, re.MULTILINE)
        if match:
            return match.group(1)
        raise Exception("WHOIS server not found in the output.")

    def extract_relevant_section(self, output: str, whois_server: str):
        """
        Extracts the relevant section of the WHOIS output for the given WHOIS server.

        Args:
            output (str): The raw output from the WHOIS command.
            whois_server (str): The WHOIS server.

        Returns:
            str: The relevant section of the WHOIS output.

        Raises:
            Exception: If the relevant section is not found in the output.
        """
        pattern = rf"(?i)# {re.escape(whois_server)}\n(.*)"
        match = re.search(pattern, output, re.DOTALL)
        if match:
            return match.group(1)
        raise Exception(f"Information under WHOIS server {whois_server} not found.")

    def parse_output(self, output: str):
        """
        Parses the WHOIS command output and extracts relevant information.

        Args:
            output (str): The raw output from the WHOIS command.

        Returns:
            dict: A dictionary containing the parsed WHOIS data.
        """
        whois_server = self.extract_whois_server(output)
        relevant_section = self.extract_relevant_section(output, whois_server)

        parsed_data = {
            "name": self.domain,
            "created": None,
            "changed": None,
            "expires": None,
            "dnssec": None,
            "registered": True,
            "status": None,
            "nameservers": [],
            "contacts": {"owner": [], "admin": [], "tech": []},
            "registrar": {"id": None, "name": None, "email": None, "url": None, "phone": None},
            "raw_whois": output.strip()
        }

        for line in output.splitlines():
            line = line.strip()
            if re.match(r"(?i)^creation date:", line):
                parsed_data["created"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^updated date:", line):
                parsed_data["changed"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^registrar registration expiration date:", line):
                parsed_data["expires"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^dnssec:", line):
                parsed_data["dnssec"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^domain status:", line):
                if parsed_data["status"] is None:
                    parsed_data["status"] = []
                parsed_data["status"].append(line.split(":", 1)[-1].strip())
            elif re.match(r"(?i)^name server:", line):
                parsed_data["nameservers"].append(line.split(":", 1)[-1].strip())
            elif re.match(r"(?i)^registrar:", line):
                parsed_data["registrar"]["name"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^registrar iana id:", line):
                parsed_data["registrar"]["id"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^registrar abuse contact email:", line):
                parsed_data["registrar"]["email"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^registrar abuse contact phone:", line):
                parsed_data["registrar"]["phone"] = line.split(":", 1)[-1].strip()
            elif re.match(r"(?i)^registrar url:", line):
                parsed_data["registrar"]["url"] = line.split(":", 1)[-1].strip()

        return parsed_data

    def get_whois_data(self):
        """
        Gets the WHOIS data for the domain.

        Returns:
            dict: A dictionary containing the parsed WHOIS data or error information.
        """
        try:
            raw_output = self.execute_whois()
            return self.parse_output(raw_output)
        except Exception as e:
            return {
                "name": self.domain,
                "error": str(e),
                "registered": False,
                "raw_whois": raw_output if 'raw_output' in locals() else None
            }