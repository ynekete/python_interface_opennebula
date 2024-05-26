import ansible_runner

runner = ansible_runner.run(private_data_dir='/home/u/my_project/ping', playbook='/home/u/my_project/ping/test.yml')

print(runner)
