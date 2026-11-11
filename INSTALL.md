# Instalação

## Windows x86_64

Extraia `EloRemote-Windows.zip` em uma pasta própria, como
`%LOCALAPPDATA%/Programs/EloRemote`, e abra `EloRemote.exe`. Mantenha juntos os
arquivos do pacote. Não use o arquivo dentro do ZIP nem uma pasta protegida se
quiser atualização automática sem administrador. A partir da versão 0.1.52,
o motor Qt WebEngine acompanha o executável: não é necessário instalar Edge,
WebView2, Chrome ou qualquer outro navegador para abrir a interface.

Desde 0.1.53, o app já usa a sinalização pela Internet, sem importar perfil ou
escolher modo LAN. Inicie o acesso no host e copie o ID. Instalações que antes
usavam somente LAN geram um novo ID público; copie-o novamente no cliente.

## Linux x86_64

Extraia `EloRemote-Linux-x86_64.tar.gz` em `~/.local/opt/elo-remote` ou em outra
pasta própria. Execute `./EloRemote-Linux-x86_64`. O pacote foi gerado no Ubuntu
24.04 e requer glibc 2.39 ou compatível, sessão gráfica e bibliotecas Qt/WebEngine,
X11/XCB, EGL/OpenGL, NSS, DBus, PulseAudio/ALSA. No Ubuntu 24.04:

```sh
sudo apt install libpulse0 libasound2t64 libgl1 libx11-6 libxext6 libxrender1 libxrandr2 libxi6 libxcursor1 libxfixes3 libxcb-cursor0 libxcb-shape0 libxcb-keysyms1 libxcb-icccm4 libnss3 libxkbcommon-x11-0 libegl1 libdbus-1-3 xclip
```

Execute como usuário comum, sem `sudo`. O aplicativo não é um pacote `.deb` nem
um AppImage; o atualizador substitui somente o executável portátil.

## O que é preservado

Configurações e convites permanecem no diretório de dados original do app:
`%LOCALAPPDATA%/AlcParsec` no Windows e `~/AlcParsec` no Linux. Credenciais da
conta continuam no cofre do sistema. A atualização não migra nem apaga esses dados.
