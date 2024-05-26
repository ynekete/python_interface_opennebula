import json, argparse
from OpennebulaProvider import OpennebulaProvider

def main():
    parser = argparse.ArgumentParser(description='Instantiate VM')
    parser.add_argument('template_id', type=int, help='ID OpenNebula template')
    parser.add_argument('vm_name', type=str, help='Name for VM')
    args = parser.parse_args()

    provider = OpennebulaProvider(args.template_id, args.vm_name)
    provider.delete_vm(int(input("Enter VM ID: ")))

main()
