# Elo Remote

**Seu PC pode ficar em casa. Seus jogos vão com você.**

Este repositório distribui os aplicativos e as notas de versão do Elo Remote.
O código-fonte do aplicativo é mantido separadamente.

## Baixar a última versão estável

- [Windows x86_64 — ZIP](https://github.com/reissoft/elo-remote-public/releases/download/last/EloRemote-Windows.zip)
- [Linux x86_64 — tar.gz](https://github.com/reissoft/elo-remote-public/releases/download/last/EloRemote-Linux-x86_64.tar.gz)
- [Histórico de versões](https://github.com/reissoft/elo-remote-public/releases)
- [Site e cliente web](https://eloremote.site/)

A release **last** é permanente: os links acima continuam iguais quando sai uma
nova versão. Cada lançamento também é preservado em uma release `vX.Y.Z`.

Extraia o pacote em uma pasta de seu usuário e abra o executável. No Linux,
preserve a permissão de execução (`chmod +x EloRemote-Linux-x86_64` se necessário).
O pacote Linux é compilado no Ubuntu 24.04 x86_64 (glibc 2.39) e precisa de um
ambiente gráfico e das bibliotecas de sistema descritas em [Instalação](INSTALL.md).
O host é Windows; Linux funciona como cliente.

## Atualizações

A partir de 0.1.45, o app verifica e baixa atualizações automaticamente e instala
ao encerrar. É possível desativar isso ou verificar manualmente em Configurações.
Uma sessão em andamento não é interrompida para atualizar. A primeira instalação
de uma versão com atualizador é manual para quem usa uma versão mais antiga.

O manifesto `update.json` possui assinatura Ed25519 e os pacotes têm SHA-256.
A chave **pública** usada para verificar releases está em `update-public-key.json`.
A chave privada de publicação nunca é distribuída. Os pacotes incluem os avisos
e os fontes correspondentes do libjuice; consulte também
[Avisos de terceiros](THIRD_PARTY_NOTICES.md).

Suporte e informações: [eloremote.site/contato](https://eloremote.site/contato/).
