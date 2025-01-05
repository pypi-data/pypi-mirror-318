from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown

def show_help():
    console = Console()

    help_text = """

Welcome to the BugScanX help documentation! This script offers a suite of tools designed to simplify your security tasks. Below is a detailed explanation of each feature.

## Features Overview

1. **HOST SCANNER (Option 1)**
   - Scan hosts from a provided TXT file in a highly customizable manner.
   - Features include selecting specific ports and methods such as direct, SSL, proxy, and UDP.
   - In direct mode, you can use various HTTP methods like GET, HEAD, PATCH, and more.
   - Utilizes multithreading to efficiently scan multiple hosts.

2. **SUB SCANNER (Option 2)**
   - Designed for beginners to scan hosts from a TXT file with minimal inputs.
   - Simply select a file using an interactive file manager and start the scan.

3. **CIDR SCANNER (Option 3)**
   - Scans IP addresses from a provided CIDR range.
   - Similar to Option 2, but tailored for CIDR input instead of TXT files.

4. **SUBFINDER (Option 4)**
   - Find subdomains of a given domain using advanced enumeration techniques.
   - Helpful for expanding the scope of your reconnaissance.

5. **IP LOOKUP (Option 5)**
   - Perform a reverse IP lookup to discover domains and subdomains hosted on a specific IP address.
   - Supports CIDR input to analyze multiple IP addresses at once.

6. **TxT TOOLKIT (Option 6)**
   - A versatile set of tools for working with TXT files.
   - Includes functionalities such as splitting large TXT files, merging multiple files, and more.

7. **OPEN PORT (Option 7)**
   - Checks for open ports on a target host, revealing potential entry points for further analysis.
   - Provides insights into active services and their configurations.

8. **DNS RECORDS (Option 8)**
   - Retrieves DNS records for a given domain, including A, MX, CNAME, TXT, and more.
   - Valuable for gathering domain configuration details and identifying potential misconfigurations.

9. **OSINT (Option 9)**
   - Conduct Open Source Intelligence gathering to collect publicly available data on a target.
   - Supports various techniques to maximize the scope of information collected.

10. **HELP MENU (Option 10)**
    - Displays this help documentation anytime for guidance on using the script.

11. **EXIT (Option 11)**
    - Exit the script gracefully.

## How to Use

1. Run the script in your terminal: `bugscanx`.
2. Follow the interactive menu prompts to select the desired feature.
3. Input the required parameters (e.g., file paths, domains, IP addresses) when prompted.
4. View the results directly in your terminal.

## Additional Resources

- **Contact**: For support or inquiries, connect with us on Telegram  https://t.me/BugScanX

    """

    markdown = Markdown(help_text)
    main_panel = Panel(markdown, title="\U0001F41B BugScanX Help Menu", border_style="bold green", expand=True)

    additional_info = """
Thank you for choosing BugScanX!

Stay updated with the latest releases and features by following our Telegram  https://t.me/BugScanX
    """
    additional_panel = Panel(Text(additional_info), border_style="bold blue", expand=True)

    console.print(main_panel)
    console.print(additional_panel)
