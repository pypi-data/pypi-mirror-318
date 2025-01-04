import socket
import requests
import threading
from tqdm import tqdm
from pathlib import Path
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed
from bugscanx.modules import *
FILE_WRITE_LOCK = threading.Lock()

def get_hosts_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(Fore.RED + f" Error reading file: {e}")
        return []

def file_manager(start_dir, max_up_levels=None):
    current_dir = Path(start_dir).resolve()
    levels_up = 0

    while True:
        items = list(current_dir.iterdir())
        files = [f for f in items if f.is_file() and f.suffix == '.txt']
        directories = [d for d in items if d.is_dir()]

        if not files and not directories:
            print(Fore.RED + " No .txt files or directories found.")
            return None

        print(Fore.CYAN + f"\n Current Directory: {current_dir}")

        for idx, item in enumerate(directories + files, 1):
            icon = "📂" if item.is_dir() else "📄"
            color = Fore.YELLOW if item.is_dir() else Fore.WHITE
            print(f"  {idx}. {icon} {color}{item.name}")

        print(Fore.LIGHTBLUE_EX + "\n 0. Back to the previous folder")

        selection = get_input(prompt=" Enter the number or filename", validator=not_empty_validator)

        if selection == '0':
            if max_up_levels is not None and levels_up >= max_up_levels:
                print(Fore.RED + " Maximum directory level reached.")
            elif current_dir.parent == current_dir:
                print(Fore.RED + " Already at the root directory.")
            else:
                current_dir = current_dir.parent
                levels_up += 1
            continue

        if selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(directories + files):
                selected_item = (directories + files)[index]
                if selected_item.is_dir():
                    current_dir, levels_up = selected_item, 0
                else:
                    return selected_item
            continue

        file_path = current_dir / selection
        if file_path.is_file() and file_path.suffix == '.txt':
            return file_path

        print(Fore.RED + " Invalid selection. Please try again.")

def get_scan_inputs():
    selected_file = file_manager(Path('.'), max_up_levels=3)
    if not selected_file:
        print(Fore.RED + " No valid file selected.")
        return None, None, None, None

    hosts = get_hosts_from_file(selected_file)
    if not hosts:
        print(Fore.RED + " No valid hosts found in the file.")
        return None, None, None, None
    
    default_output = f"results_{selected_file.name}"

    output_file = get_input(prompt=" Enter output file name", default=default_output, validator=not_empty_validator)
    ports = get_input(prompt=" Enter ports (comma-separated)",default="80", validator=digit_validator)
    port_list = [port.strip() for port in ports.split(',') if port.strip().isdigit()]
    if not port_list:
        print(Fore.RED + " Invalid ports entered.")
        return None, None, None, None

    return hosts, port_list, output_file, 50, "HEAD"

def format_row(code, server, port, ip_address, host, use_colors=True):
    color = lambda text, clr: f"{clr}{text}" if use_colors else text
    return (
        f"{color(code, Fore.GREEN):<4} "
        f"{color(server, Fore.CYAN):<20} "
        f"{color(port, Fore.YELLOW):<5} "
        f"{color(ip_address, Fore.MAGENTA):<15} "
        f"{color(host, Fore.LIGHTBLUE_EX)}"
    ) 

def check_http_response(host, port, method):
    url = f"{'https' if port in ['443', '8443'] else 'http'}://{host}:{port}"
    try:
        response = requests.request(method, url, timeout=SUBSCAN_TIMEOUT, allow_redirects=True)
        if any(exclude in response.headers.get('Location', '') for exclude in EXCLUDE_LOCATIONS):
            return None

        return (
            response.status_code,
            response.headers.get('Server', 'N/A'),
            port,
            socket.gethostbyname(host) if host else 'N/A',
            host
        )
    except (requests.RequestException, socket.gaierror):
        return None

def perform_scan(hosts, ports, output_file, threads, method):
    clear_screen()
    print(Fore.LIGHTGREEN_EX + f" Scanning using HTTP method: {method} on ports {', '.join(ports)}...\n")

    headers = (
        f"{Fore.GREEN}{'Code':<4}  {Fore.CYAN}{'Server':<20}  "
        f"{Fore.YELLOW}{'Port':<5}  {Fore.MAGENTA}{'IP Address':<15}  {Fore.LIGHTBLUE_EX}Host"
    )
    separator = "-" * 65

    with open(output_file, 'w') as file:
        file.write(f"{headers}\n{separator}\n")

    print(headers, separator, sep='\n')

    total_tasks = len(hosts) * len(ports)
    scanned, responded = 0, 0

    pbar = tqdm(total=total_tasks, desc="Progress", position=0, leave=True, unit="host", unit_scale=True)

    def process_result(future):
        nonlocal scanned, responded
        scanned += 1
        result = future.result()
        if result:
            responded += 1
            row = format_row(*result)
            pbar.write(row)
            with FILE_WRITE_LOCK:
                with open(output_file, 'a') as file:
                    file.write(format_row(*result, use_colors=False) + "\n")

        pbar.update(1)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_http_response, host, port, method): (host, port) for host in hosts for port in ports}
        for future in as_completed(futures):
            process_result(future)

    pbar.close()
    print(f"\n\n{Fore.GREEN} Scan completed! {responded}/{scanned} hosts responded.")
    print(f" Results saved to {output_file}.{Style.RESET_ALL}")
