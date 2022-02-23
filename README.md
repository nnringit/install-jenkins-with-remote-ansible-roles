
# Install Jenkins CI server using Vagrant and ansible roles from ansible-galaxy community roles on a remote/guest VM

This is to install Jenkins CI server on a ubuntu VM  which gets created using Vagrant and will be provisioned by ansible CM tool which is get installed and configured automatically by the ansible_local vagrant's provisioner

## Pre-Reqs

1. Install Vagrant
2. Install VirtualBox

Run the following single command which performs the following all by vagrant itself for you
1. Downloads ubuntu 20.04 virtual box
2. Provision a Ubuntu VM and bootstraps with ansible install and its setup
3. Pull down Ansible roles from ansible-galaxy.com 
4. Runs ansible-playbook which installs Jenkins Server
4. Exposes Jenkins console default port 8080 to host machine 

```sh
vagrant up --provision
```

## Testing Jenkins and a sample job

  Access this Jenkins console URL from a browser and follow the instructions on Jenkins pages to finish the Jenkins Server setup
        http://localhost:8080

Configure a **test** job and check whether the job status is SUCCESS or FAILED

```sh
    python query_jenkins.py
```

## Folder structure 
    
    ├── README.md
    ├── Vagrantfile
    ├── playbook.yml
    ├── query_jenkins.py
    └── requirements.yml

 

