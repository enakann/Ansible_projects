#!/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define the available arguments/parameters that a user can pass to
    # the module
       module_args = dict(
               target=dict(type='str', required=True)
       )
       result = dict(changed=False )
  
       module=AnsibleModule(
          argument_spec=module_args,
          supports_check_mode=True
       )
       
       if module.check_mode:
          return result

       ping_result = module.run_command('ping -c 1 {}'.format(module.params['target']))
       
       if module.params['target']:
           result['debug']=ping_result
           result['rc']=ping_result[0]
           if result['rc']:
              result['failed']=True
              module.fail_json(msg='Failed to ping',**result)
           else:
              result['changed']=True
              module.exit_json(**result)



def main():
    run_module()


if __name__ == '__main__':
      main()    
       

       


