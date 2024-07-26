# Migração dos Bancos de Dados

### Passos anteriores ao dia da migração

- [ ] SolicitarLUN de 100GB para estender o /u01
- [ ] Estender o volume /u01 com o disco de 100GB

  Identificar a partição

      lsblk

  Criar a partição

      fdisk -u -p /dev/xvdh <<EOF
      n
      p
      1

      w
      EOF


      
