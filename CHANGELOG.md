# Notas de versão

## 0.1.82

- Abrir o app mantém a janela visível. A ida para a bandeja passa a depender de ação do usuário; a restauração do host permanece.
- Novo instalador Windows NSIS, com app em Arquivos de Programas, atalhos e desinstalação que preserva dados do usuário.
- A versão instalada mantém bibliotecas na pasta de instalação, sem extrair o app inteiro para uma pasta temporária em cada abertura.
- Atualizações da versão instalada usam o instalador verificado; as versões portáteis mantêm seu canal compatível.
- Isola a consulta de dispositivos de áudio em um processo com timeout. Falha nessa consulta não encerra a interface.
- Registra PID, etapas de inicialização, pilha segura de exceções e arquivo de falha nativa por processo.
- O motivo do encerramento relatado após interface.ready continua sob investigação. Sem certificado Authenticode configurado, o instalador ainda pode apresentar aviso de confiança do Windows.

## 0.1.81

- O aplicativo Windows pede administrador ao abrir. Cancelar não abre uma interface sem elevação.
- Remove a preparação e o uso do serviço administrativo. Captura, entrada e monitor virtual passam a operar no próprio app elevado.
- Remove a seção de serviço de Configurações. Novas instalações não criam serviços.
- Na migração, remove o serviço antigo somente quando não há agentes ativos e o estado pode ser confirmado; sessões em uso são preservadas.
- Mantém a atualização automática compatível com versões anteriores e a proteção contra instâncias duplicadas.

## 0.1.80

- Remove o botão Instalar/atualizar serviço. Ao abrir o app Windows, verifica automaticamente instalação e inicialização do serviço administrativo.
- Pede administrador somente quando necessário; mantém serviços compatíveis em execução e preserva serviços com sessões ativas.
- Impede outra instância da interface para o mesmo usuário/sessão. Abrir novamente restaura a janela existente.
- Impede um segundo motor host independente. Mantém as conexões de cliente com computadores diferentes.
- Encerra os filhos e descendentes dos motores no Windows ao fechar o app, inclusive se o processo inicial já tiver terminado.
- Processos de versões anteriores já abertos são preservados até seu encerramento normal.

## 0.1.79

- A janela de arquivos mostra somente os lados com transferência disponível. Ter o host ligado não faz aparecer uma opção de envio sem conexão.
- Sem transferência disponível, mostra apenas uma orientação, sem cartões ou botões desabilitados.

## 0.1.78

- Arquivos recebidos pela transferência simples gratuita são salvos automaticamente em Downloads, sem perguntar a pasta.
- Mostra uma notificação discreta com nome e barra de progresso durante o recebimento, sem abrir a janela de arquivos.
- Respeita a pasta Downloads configurada para o usuário e preserva arquivos com o mesmo nome.
- A janela de transferência mostra apenas host ou cliente conforme as conexões em uso. Mostra os dois somente se ambos estiverem ativos.
- Mantém a permissão de arquivos do host e o fluxo avançado de pastas e retomada do Pro.

## 0.1.77

- Impede que a perda da saída de console do Windows (`OSError: Invalid argument`) derrube o motor de acesso remoto.
- Protege as mensagens de diagnóstico e de encerramento contra falhas de escrita, preservando o log em arquivo quando disponível.
- Mantém as mensagens de comunicação local quando a saída funciona normalmente.

## 0.1.76

- Remove as abas de acessos da janela principal. Com mais de um acesso aberto, leve o mouse ao topo da imagem remota e clique no ícone de troca de acesso.
- O ícone alterna entre os computadores conectados, mostra o próximo nome ao passar o mouse e também aceita Ctrl+Shift+Tab.
- Mantém a imagem atual disponível enquanto a próxima conexão abre e volta a outro acesso se o atual fechar.
- Corrige o envio de comandos em segundo plano: teclado, mouse e gamepad são liberados ao trocar de acesso. O segundo monitor acompanha a troca.
- A troca é local ao cliente, sem mudanças nas VPS ou no serviço Windows.

## 0.1.75

- Oculta o botão Convidados (Pro), mantendo as permissões gerais existentes.

## 0.1.74

- Pro: até oito conexões simultâneas, gerenciadas em abas, com janelas de vídeo independentes e arquivos por sessão.
- Pro: histórico local de acessos recebidos/enviados, horários e duração.
- Pro: permissões persistentes por convidado identificado para controle, arquivos, área de transferência e gamepad, com revogação ao vivo.
- Pro: gravação local explícita do vídeo principal e áudio em MKV, finalizada ao parar/desconectar.
- Sessão única e recursos gratuitos anteriores preservados. Aprovação de acesso e confiança existentes permanecem como antes.
- Sem mudanças nas VPS, backend de contas ou serviço Windows. Monitor virtual permanece experimental.

## 0.1.73

- Aviso imediato ao selecionar monitor virtual ou Somente aplicativo sem Pro, com opção Assinar Pro.
- Compartilhamento de aplicativo passa a exigir Pro no host; convidados continuam sem exigência de assinatura.
- Área de trabalho e monitores físicos permanecem gratuitos.

## 0.1.72

- Integração experimental de monitor virtual no Pro, com resoluções 720p, 1080p e 1440p.
- Usa o serviço EloRemoteHost existente: administrador somente na instalação do driver/atualização do serviço, sem UAC a cada ativação.
- Driver assinado incluído, com preparação explícita pelo Windows; monitor temporário vinculado ao aplicativo.
- Monitores físicos e dois monitores continuam gratuitos. Sem alterações nas VPS.
- Ativação do driver em hardware real permanece pendente para preservar a sessão do operador.

## 0.1.71

- Transferência Pro de pastas, incluindo subpastas e diretórios vazios, nos aplicativos para PC atualizados.
- Transferências Pro pausadas podem ser retomadas após reconexão ou reabertura do app, com nova confirmação do destinatário e verificação de integridade.
- Velocidade de envio configurável em 2, 4, 6 ou 8 Mbps, também na transferência simples gratuita.
- Sem atualização das VPS; convidados usam os recursos avançados quando o host tem Pro.

## 0.1.70

- Perfis Pro Jogar, Trabalhar e Celular no host Windows, com preferências salvas automaticamente por conta neste computador.
- Troca de qualidade, FPS e bitrate durante a sessão, sem interromper o acesso.
- Ajustes manuais continuam gratuitos; sem alteração no backend ou nas VPS.

## 0.1.69

- Corrigida a renomeação de computadores no aplicativo Windows/Linux, incluindo os sincronizados pela conta.
- Sem alteração nas VPS ou no backend de contas.

## 0.1.68

- Sincronização automática dos computadores ao entrar na conta Pro, sem botão nem avisos rotineiros.
- A versão web oculta o link Entrar quando a conta está conectada.
- Sincronização em segundo plano, preservando as sessões e os recursos gratuitos.

## 0.1.67

- Sincronização manual dos computadores pela conta Pro no aplicativo e no navegador, sem enviar credenciais ou permissões de acesso.
- Convites Pro com nome, início agendado, validade, limite de tentativas e revogação individual.
- Recursos gratuitos preservados; computadores sincronizados continuam exigindo aprovação por ID.
- Compatível com a sinalização atual, sem atualização das VPS.

## 0.1.66

- Somente aplicativo assume processos já abertos do executável selecionado, no mesmo usuário e sessão do Windows, sem iniciar uma segunda instância.
- Identificação pelo caminho completo e identidade do processo, incluindo processos filhos; desconectar não encerra o aplicativo.
- Atalhos do Windows, troca de aplicativos e abertura do menu Iniciar bloqueados no host; teclas liberadas ao perder o foco.
- Indicador de espera substituído por pontinhos nos clientes nativo e web.
- Sem atualização ou reinício dos servidores.

## 0.1.65

- Menus, dicas e pequenos diálogos transmitidos em PNG sem perda, preservando letras finas e dimensões originais nos clientes Windows/Linux e web.
- H.264 mantido nas janelas principais e maiores; imagens pequenas sem alterações não são recodificadas.
- Capturas incompletas rejeitadas para evitar imagens esticadas.
- Negociação compatível com versões anteriores, sem atualização ou reinício de servidores.

## 0.1.64

- Corrigida a conexão por ID que podia descartar o anúncio de H.264 e área única antes da aprovação e voltar silenciosamente a janelas separadas.
- Capacidades reenviadas após a autorização, nos clientes PC/Linux e web.
- Acrescentados diagnósticos do transporte e do layout efetivamente negociados.
- Testes com aprovação atrasada e sinalização local real; sem atualização ou reinício de servidores.

## 0.1.63

- Todas as janelas do aplicativo reunidas na mesma área em clientes PC/Linux e web atualizados, mantendo suas posições e a ordem de sobreposição.
- Área expandida automaticamente para janelas distantes; espaços entre elas permanecem pretos, sem captura de monitor ou outros aplicativos.
- Menus recebem mouse sem criar outra janela local nem forçar uma troca de foco no host.
- Bordas e barras de título preservadas; coordenadas estáveis durante o arraste e restauração de janelas minimizadas.
- Captura alternativa de menus e diálogos clássicos ajustada para incluir a janela completa.
- Mantidos H.264, áudio, teclado virtual e gamepad, com negociação compatível e sem atualização de servidor.

## 0.1.62

- Modo Somente aplicativo com vídeo H.264 em clientes PC/Linux e web atualizados, usando o encoder do desktop e captura exclusiva das janelas autorizadas.
- Captura configurável a 30 ou 60 FPS, até Full HD por janela; eliminada a conversão para JPEG no novo caminho de vídeo.
- Filas de apenas um quadro por janela e espera assíncrona, sem acumular atraso nem ocupar threads com janelas sem imagem.
- Cliente web mantém uma única área de exibição e alterna para diálogos, preservando a barra superior, teclado virtual, gamepad e áudio.
- Clientes antigos continuam usando o modo JPEG compatível. Sem mudança ou reinício nos servidores.

## 0.1.61

- Reativada a opção Somente aplicativo nas configurações do host Windows, com escolha do executável e argumentos.
- Corrigidas a conexão por ID, a aprovação de acesso, a validade dos convites e a recuperação após falha de captura.
- Cliente web com uma única área de exibição, alternando entre a janela principal e seus diálogos, e barra superior padrão preservada.
- Teclado virtual Unicode, gamepad físico/virtual e áudio do sistema opcionais no modo aplicativo, respeitando as permissões do host.
- Controle virtual neutralizado ao perder foco, desconectar ou deixar de receber comandos.
- Mantida a compatibilidade do protocolo; nenhuma atualização de servidor necessária.

## 0.1.60

- Corrigida a exibição do ID completo no painel deste computador, ajustando a fonte ao espaço disponível.
- Layout validado com IDs reais de 16 caracteres e diferentes escalas de tela.
- Mantidas a compatibilidade do protocolo e as correções do serviço Windows da versão anterior.

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
