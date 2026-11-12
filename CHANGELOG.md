# Notas de versão

## 0.1.59

- Corrigida falha OpenProcess/Acesso negado ao autenticar o serviço Windows.
- Autenticação baseada no PID real do pipe e na configuração protegida do SCM, sem consultar a imagem do processo System.
- Falha do serviço opcional deixa o host disponível no modo normal, com aviso, sem encerrar o motor.
- Serviço compatível por protocolo, cache de motores assinados e atualização em caminho novo sem substituir executável em uso.

## 0.1.58

- Corrigido o alinhamento do menu lateral: Conta, Ocultar na bandeja, Licença e Sair usam o mesmo alinhamento à esquerda, fonte e espaçamento interno.

## 0.1.57

- Nova identidade Elo Remote em grafite e verde jade, com logo de elos conectados.
- Tela inicial unificada com computadores salvos, conexão rápida por ID e painel deste computador.
- Ação Conectar em cada cartão e menus individuais para renomear e remover computadores.
- Preferências de transmissão e conexão reunidas nas configurações; permissões continuam disponíveis no painel do host.
- Cliente web 0.1.57 com a mesma identidade, layout responsivo e controles da sessão preservados.
- Histórico, IDs, conta, licença e atualização automática preservados. Sem mudança de protocolo nem reinício dos servidores.

## 0.1.56

- Corrigida a instalação do serviço Windows que falhava com “Python int too large to convert to C long”.
- Máscara de permissões corrigida e validada com a API real do Windows em arquivo temporário.

## 0.1.55

- Interface desktop nativa em Windows e Linux, sem WebView, Qt ou Chromium.
- Tema escuro, cores, organização das telas e cartões preservados.
- Licença offline, idiomas, conta, convites por link/QR, arquivos, notificações e atualização integrados à interface nativa.
- Serviço Windows opcional, instalado pelo usuário nas configurações, para suporte a janelas elevadas e telas protegidas.
- Input normal dos jogos continua local; helper privilegiado só entra quando necessário.
- Protocolo de conexão preservado, sem atualização dos servidores.

## 0.1.54

- Notificações compatíveis com Qt, sem dependência de WinForms/.NET.
- Avisos mais compactos, com fundo sólido e sem contorno desenhado.
- Disponibilidade consultada também para computadores adicionados por ID.
- Indicador “Em uso” informa ocupação sem bloquear vagas restantes.

## 0.1.53

- Modo LAN e configuração manual removidos da interface; Internet pronta no primeiro uso.
- Cadastro automático de identidade sem compartilhar chave administrativa.
- IDs e configurações de hosts já configurados preservados.
- Um único atalho de ajuda para conexão direta.
- Mensagem específica para ID inexistente, sem manter a tentativa indefinidamente.

## 0.1.52

- Windows com Qt WebEngine embutido, sem depender de Edge/WebView2 ou navegador instalado.
- Inicialização da interface validada antes de restaurar o acesso remoto.
- Mensagem nativa e diagnóstico local se a interface não abrir.
- Licença em nove idiomas, aceite explícito no primeiro uso e link permanente.

## 0.1.45

- Identidade visual Dar Play nos aplicativos.
- Verificação e download automáticos de atualizações assinadas.
- Instalação ao encerrar e opção de reiniciar para atualizar.
- Backup da versão anterior e restauração se a verificação de inicialização falhar.
- Pacotes Windows/Linux e links permanentes na release `last`.
