import os
import sys
import time
import itertools
import threading
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def animate_installation(package):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if package['done']:
            break
        sys.stdout.write(f'\r\033[33m Installing {package["name"]} {c}\033[0m')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')

def install_requirements():
    required_packages = [
        'requests', 'rich', 'colorama', 'pyfiglet', 'loguru',
        'bs4', 'dnspython', 'multithreading', 'prompt_toolkit', 'InquirerPy'
    ]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            package_info = {'name': package, 'done': False}
            t = threading.Thread(target=animate_installation, args=(package_info,))
            t.start()
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            package_info['done'] = True
            t.join()
            print(f"\033[32m Package '{package}' installed successfully.\033[0m")

install_requirements()

from rich.console import Console
from bugscanx.modules.utils.handler import*
from bugscanx.modules.utils.other import banner
from bugscanx.modules.utils.glance import display_message
from bugscanx.modules.utils.utils import clear_screen, text_ascii, get_input, digit_validator
console = Console()

def main_menu():
    install_requirements()
    menu_options = {
        '1': ("HOST SCANNER PRO", run_host_checker, "bold cyan"),
        '2': ("HOST SCANNER", run_sub_scan, "bold blue"),
        '3': ("CIDR SCANNER", run_ip_scan, "bold yellow"),
        '4': ("SUBFINDER", run_sub_finder, "bold magenta"),
        '5': ("IP LOOKUP", run_ip_lookup, "bold cyan"),
        '6': ("TxT TOOLKIT", run_txt_toolkit, "bold magenta"),
        '7': ("OPEN PORT", run_open_port, "bold white"),
        '8': ("DNS RECORDS", run_dns_info, "bold green"),
        '9': ("OSINT", run_osint, "bold blue"),
        '10': ("HELP MENU", run_help_menu, "bold yellow"),
        '11': ("EXIT", lambda: sys.exit(), "bold red")
    }

    while True:
        clear_screen()
        banner()
        display_message()
        for key, (desc, _, color) in menu_options.items():
            if int(key) < 10:
                console.print(f"[{color}] [{key}]  {desc}")
            else:
                console.print(f"[{color}] [{key}] {desc}")

        choice = get_input(prompt="\n Enter your choice", validator=digit_validator)

        if choice in menu_options:
            clear_screen()
            text_ascii(menu_options[choice][0], font="calvin_s", color="bold magenta")
            menu_options[choice][1]()
            if choice != '11':
                console.input("[yellow]\n Press Enter to return to the main menu...")
        else:
            console.print("[bold red]\n Invalid choice. Please select a valid option.")
            console.input("[yellow bold]\n Press Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()