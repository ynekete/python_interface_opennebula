#file -- OpennebulaProvider.py --
import pyone, ansible_runner, json
global one

one = pyone.OneServer("http://brest-srv.asafonov.local:2633/RPC2", session="oneadmin:CychajBekal3")

class OpennebulaProvider:

    def __init__(self):
        try:
            with open('info.json') as f:
                self.info = json.load(f)
        except:
            self.info = {}

    def instantiate_vm(self, template_id, name):
        self.info[name] = one.template.instantiate(template_id, name)

    def terminate_hard(self, vm_name):
        print(one.vm.action("terminate-hard", self.info[vm_name]))
        self.info.pop(vm_name)

    def poweroff_hard(self, vm_name):
        print(one.vm.action("poweroff-hard", self.info[vm_name]))

    def resume(self, vm_name):
        print(one.vm.action("resume", self.info[vm_name]))

    def ssh_key_forwarding(self, vm_name):
        ssh_key = input("Enter a ssh public key: ")
        vm_context = {
        'TEMPLATE': {
            'CONTEXT': {
                'CONTEXT': 'true',
                'NETWORK': 'yes',
                'SET_HOSTNAME': 'hostname-1',
                'USERNAME': 'u',
                'SSH_PUBLIC_KEY': ssh_key
            },
            'GRAPHICS': {
                    'TYPE': 'SPICE',
                    'LISTEN': '0.0.0.0',
                    'PORT': '5905'
            },
            'FEATURES': {
                    'GUEST_AGENT': 'yes'
            },
          }
        }

        print(one.vm.updateconf(self.info[vm_name], vm_context))

    def run_anible_task(self):
        runner = ansible_runner.run(private_data_dir='/home/u/my_project/ping', playbook='/home/u/my_project/ping/test.yml', )
        print(runner)

    def __del__(self):
        with open('info.json', 'w') as f:
            json.dump(self.info, f)
