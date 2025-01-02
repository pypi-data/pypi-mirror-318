import argparse
import json
from .core import WhoisQuery

def main():
    """Command-line interface for WhoisQuery."""
    parser = argparse.ArgumentParser(description="Perform WHOIS lookups and parse the results.")
    parser.add_argument("-d", "--domain", required=True, help="The domain to query WHOIS information for.")
    args = parser.parse_args()

    whois = WhoisQuery(args.domain)
    data = whois.get_whois_data()
    
    if "error" in data:
        print(json.dumps(data, indent=2))
    else:
        print(data)
    
    return 0 if "error" not in data else 1

if __name__ == "__main__":
    exit(main()) 