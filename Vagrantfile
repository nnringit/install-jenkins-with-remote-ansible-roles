
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-20.04"

  config.vm.synced_folder ".", "/vagrant", disabled: false, type: 'rsync'

  config.vm.provision 'ansible', run: 'always', type: :ansible_local do |ansible|
    ansible.galaxy_role_file = 'requirements.yml' # ansible-galaxy command will be executed within the guest VM and pull the roles into roles folder
    ansible.playbook = 'playbook.yml'
  end

  config.vm.network "forwarded_port", guest: 8080, host: 8080

end

