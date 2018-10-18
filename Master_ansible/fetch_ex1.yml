---
 - name: execersie
   hosts: all
   tasks:
     - name: create file
       file:
           path: /tmp/test_modules.txt
           state: touch
           mode: 0600
     - name: contents
       blockinfile:
           dest: /tmp/test_modules.txt
           block: |
             this is the test file
             and i am from {{ ansible_hostname }}
     - name: scp
       fetch:
         src: /tmp/test_modules.txt
         dest: /tmp/host_{{ inventory_hostname }}
         flat: yes
