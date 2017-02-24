RHEL6-LINSEE_clang:
  pkg.installed:
    - pkgs:
      - clang.x86_64
      - clang-devel.x86_64

RHEL6-LINSEE_clang_lib_1:
  file.managed:
    - name: /usr/lib64/llvm/libclang.so.backup
    - source: /usr/lib64/llvm/libclang.so
    - mode: 644

RHEL6-LINSEE_clang_lib_2:
  file.managed:
    - name: /usr/lib64/llvm/libclang.so
    - source: salt://linsee-rhel6/files/libclang.so
    - mode: 644
    
RHEL6-LINSEE_clang_lib_3:
  file.managed:
    - name: /usr/lib64/llvm/libLLVM-3.7.so
    - source: salt://linsee-rhel6/files/libLLVM-3.7.so
    - mode: 644
