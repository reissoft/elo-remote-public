# Instalação

## Windows x86_64

Baixe e execute `EloRemote-Setup-x86_64.exe`. O instalador coloca o app em
Arquivos de Programas, cria atalhos e registra a desinstalação no Windows.
Não fecha sessões à força nem abre o app automaticamente sem sua escolha.
A versão instalada mantém as bibliotecas na pasta do app e recebe as próximas
atualizações pelo instalador verificado, após o aplicativo fechar.

A versão portátil continua disponível em `EloRemote-Windows.zip`: extraia em
uma pasta própria e abra `EloRemote.exe`, mantendo os arquivos juntos.
Desde 0.1.81, o app Windows solicita administrador ao abrir. Cancelar não abre
uma interface sem elevação. Não é necessário instalar navegadores para a interface.

Ainda não há assinatura Authenticode: o instalador pode continuar mostrando
aviso de aplicativo não reconhecido no Windows. A assinatura Ed25519 do canal
de atualização verifica integridade, mas não substitui a assinatura Windows.

Desde 0.1.53, o app já usa a sinalização pela Internet, sem importar perfil ou
escolher modo LAN. Inicie o acesso no host e copie o ID. Instalações que antes
usavam somente LAN geram um novo ID público; copie-o novamente no cliente.

O app novo não instala nem utiliza serviço administrativo. A migração tenta
remover o serviço antigo quando estiver sem agentes ativos; acessos em uso são
preservados. Executar elevado não garante controle da tela segura do UAC.

## Linux x86_64

Extraia `EloRemote-Linux-x86_64.tar.gz` em `~/.local/opt/elo-remote` ou em outra
pasta própria. Execute `./EloRemote-Linux-x86_64`. O pacote foi gerado no Ubuntu
24.04 e requer glibc 2.39 ou compatível, sessão gráfica e bibliotecas
X11, OpenGL e PulseAudio/ALSA. No Ubuntu 24.04:

```sh
sudo apt install libpulse0 libasound2t64 libgl1 libx11-6 libxext6 libxrender1 libxrandr2 libxi6 libxcursor1 libxfixes3 xclip
```

Execute como usuário comum, sem `sudo`. O aplicativo não é um pacote `.deb` nem
um AppImage; o atualizador substitui somente o executável portátil.

## O que é preservado

Configurações e convites permanecem no diretório de dados original do app:
`%LOCALAPPDATA%/AlcParsec` no Windows e `~/AlcParsec` no Linux. Credenciais da
conta continuam no cofre do sistema. A atualização não migra nem apaga esses dados.
