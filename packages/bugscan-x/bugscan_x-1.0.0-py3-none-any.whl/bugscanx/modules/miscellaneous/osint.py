import ssl
import socket
import requests
import concurrent
from rich.table import Table
from bugscanx import get_input
from rich.console import Console
from colorama import Style, init
from requests.exceptions import RequestException

init(autoreset=True)
console = Console()

HTTP_METHODS = ["GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "TRACE", "PATCH"]

def check_http_method(url, method):
    try:
        response = requests.request(method, url, timeout=5)
        headers = {
            "Server": response.headers.get("Server", "N/A"),
            "Connection": response.headers.get("Connection", "N/A"),
            "Content-Type": response.headers.get("Content-Type", "N/A"),
            "Content-Length": response.headers.get("Content-Length", "N/A"),
        }
        return method, response.status_code, headers
    except RequestException as e:
        return method, None, str(e)

def check_http_methods(url):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(check_http_method, url, method) for method in HTTP_METHODS]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results

def format_sni_info(sni_info):
    formatted_info = (
        f" Subject:\n"
        f"  Common Name: {sni_info['subject'].get('commonName', 'N/A')}\n"
        f"  Organization: {sni_info['subject'].get('organizationName', 'N/A')}\n"
        f"  Organizational Unit: {sni_info['subject'].get('organizationalUnitName', 'N/A')}\n"
        f"  Country: {sni_info['subject'].get('countryName', 'N/A')}\n"
        f" Issuer:\n"
        f"  Common Name: {sni_info['issuer'].get('commonName', 'N/A')}\n"
        f"  Organization: {sni_info['issuer'].get('organizationName', 'N/A')}\n"
        f"  Organizational Unit: {sni_info['issuer'].get('organizationalUnitName', 'N/A')}\n"
        f"  Country: {sni_info['issuer'].get('countryName', 'N/A')}\n"
        f" Serial Number: {sni_info['serialNumber']}\n"
    )
    return formatted_info

def get_sni_info(host):
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssl_sock:
                cert = ssl_sock.getpeercert()
                sni_info = {
                    "subject": {key: value for (key, value) in cert["subject"][0]},
                    "issuer": {key: value for (key, value) in cert["issuer"][0]},
                    "serialNumber": cert.get("serialNumber"),
                }
                return sni_info
    except Exception as e:
        return str(e)

def format_sni_info_table(sni_info):
    table = Table(title="SNI Information")

    table.add_column("Field", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="left", style="magenta")

    table.add_row("Subject Common Name", sni_info['subject'].get('commonName', 'N/A'))
    table.add_row("Subject Organization", sni_info['subject'].get('organizationName', 'N/A'))
    table.add_row("Subject Organizational Unit", sni_info['subject'].get('organizationalUnitName', 'N/A'))
    table.add_row("Subject Country", sni_info['subject'].get('countryName', 'N/A'))
    table.add_row("Issuer Common Name", sni_info['issuer'].get('commonName', 'N/A'))
    table.add_row("Issuer Organization", sni_info['issuer'].get('organizationName', 'N/A'))
    table.add_row("Issuer Organizational Unit", sni_info['issuer'].get('organizationalUnitName', 'N/A'))
    table.add_row("Issuer Country", sni_info['issuer'].get('countryName', 'N/A'))
    table.add_row("Serial Number", sni_info['serialNumber'])

    return table

def osint_main():
    host = get_input("\n Enter the host (e.g., example.com)")
    protocol = get_input("\n Enter the protocol (http or https)").lower()
    if protocol not in ["http", "https"]:
        console.print("[red]Invalid protocol. Please enter 'http' or 'https'.[/red]")
        return

    url = f"{protocol}://{host}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        http_methods_future = executor.submit(check_http_methods, url)
        sni_info_future = executor.submit(get_sni_info, host) if protocol == "https" else None

    http_methods_results = http_methods_future.result()
    
    http_table = Table(title="HTTP Methods Information")

    http_table.add_column("HTTP Method", justify="center", style="cyan", no_wrap=True)
    http_table.add_column("Status Code", justify="center", style="magenta")
    http_table.add_column("Server", justify="left", style="green")
    http_table.add_column("Connection", justify="left", style="green")
    http_table.add_column("Content-Type", justify="left", style="green")
    http_table.add_column("Content-Length", justify="left", style="green")

    for method, status_code, headers in http_methods_results:
        if isinstance(headers, dict):
            http_table.add_row(method, str(status_code), headers["Server"], headers["Connection"], headers["Content-Type"], headers["Content-Length"])
        else:
            http_table.add_row(method, str(status_code), headers, "N/A", "N/A", "N/A")

    console.print(http_table)

    if protocol == "https":
        sni_info_result = sni_info_future.result()
        if isinstance(sni_info_result, dict):
            sni_table = format_sni_info_table(sni_info_result)
            console.print(sni_table)
        else:
            console.print(f"[red]Failed to retrieve SNI info: {sni_info_result}[/red]")

    print(Style.RESET_ALL)
