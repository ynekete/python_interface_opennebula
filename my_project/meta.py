import json, argparse
from OpennebulaProvider import OpennebulaProvider

def main():

    parser = argparse.ArgumentParser(description='Control VMs')
    parser.add_argument('action', type=str, choices=['instantiate', 'poweroff-hard', 'terminate-hard', 'resume', 'ssh-key', 'run-task'], help='usage: python3 meta.py action [-args]') # Позиционный параметр

    #Опциональные параметры
    parser.add_argument('-i', '--id', type=int, help='Virtual machine ID')
    parser.add_argument('-n', '--name', type=str, help='Virtual machine name')
    parser.add_argument('-t', '--template', type=int, help='Template ID')
    args = parser.parse_args()

    if args.action == 'instantiate':
        provider = OpennebulaProvider()
        provider.instantiate_vm(args.template, args.name)

    elif args.action == 'terminate-hard':
        provider = OpennebulaProvider()
        provider.terminate_hard(args.name)

    elif args.action == 'poweroff-hard':
        provider = OpennebulaProvider()
        provider.poweroff_hard(args.name)

    elif args.action == 'resume':
        provider = OpennebulaProvider()
        provider.resume(args.name)

    elif args.action == 'ssh-key':
        provider = OpennebulaProvider()
        provider.ssh_key_forwarding(args.name)

    elif args.action == 'run-task':
        provider = OpennebulaProvider()
        provider.run_anible_task()

main()
