def get_provider_info():
    return {
        "package-name": "airflow-airflow-provider",
        "name": "Airflow Ansible Provider",
        "description": "Run Ansible Playbook as Airflow Task",
        "connection-types": [
            {
                "hook-class-name": "airflow_ansible_provider.hooks.AnsibleHook",
                "connection-type": "ansible",
            },
            {
                "hook-class-name": "airflow_ansible_provider.hooks.GitHook",
                "connection-type": "git",
            },
        ],
        "versions": ["0.0.1"],
    }
