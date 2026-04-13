# TaskQuest

## Em TaskQuest você irá se aventurar por missões criadas para o seu herói no intuito de evoluir ele com xp e assim poder derrotar o grande vilão da história, PROCASTINATOR!! Embarque nessa aventura agora!

### Como começar?

#### Instalação

##### A instalação é muito simples, se estiver no windows e já estiver na pasta do /taskquest rode no terminal powershell ou cmd:

```
./setup.bat
```

##### Se estiver no linux rode no terminal bash:

```
source setup.sh
```

##### Após a instalação vamos iniciar o programa:

```
python run.py
```

##### Com o programa iniciado podemos entrar no nosso navegador no link http://127.0.0.1:5000/

##### O que podemos fazer no TaskQuest?

- Criar um herói.
- Logar com um herói já criado.
- Voltarmos para o menu a qualquer momento.
- Na nossa dashboard, ou o nosso Mural de Missões é onde temos os status do nosso herói logado:
  - Nome do herói, qual level ele está, quanto de xp ele tem no momento e quantas moedas de ouro ele tem.
- No nosso Mural de Missões também podemos criar uma missão no botão "Nova Missão" Logo abaixo dos status do nosso herói, quando clicamos neste botão uma tela aparece pedindo para darmos um título para a missão, uma descrição, quanto de xp ela nos recompensará e quanto de ouro ela nos recompensará também(ouro e xp são limitados a 100), depois de preencher podemos clicar em "Publicar no Mural".
  - Missão publicada, ela aparece na coluna "Mural de Missões", lá nós podemos ver todas nossas missões criadas, uma missão tem 3 estados:
    1. "Mural de Missões" - Pendente
    2. "Andamento" - Em progresso
    3. "Concluídas" - Completas
  - Uma missão pode ser deletada tanto na coluna "Mural de Missões", quanto na coluna "Andamento" clicando no botão vermelho e com um "X" na célula da missão, mas não na coluna "Concluídas"
- Podemos ver os detalhes de uma missão clicando no botão azul com o ícone de estrela na célula da missão, nas colunas "Mural de Missões" e "Andamento" é possível alterar os dados da missão, mas na coluna "Concluídas" aparece somente os dados e não é possível alterá-los.
- Para que o herói progrida na missão ele vai clicar sempre no botão verde com ícone de joinha na célula da missão, ela começa na coluna "Mural de Missões", depois passa para a coluna "Andamento" e por fim para a coluna "Concluídas" onde se encontra o nosso chefe final o PROCASTINATOR.
- Para derrotar o PROCASTINATOR precisamos de terminar as missões e assim que a missão finaliza aparece uma tela com um ponteiro que quanto mais perto do vermelho ele estiver mais dano você dará no chefão, sendo o dano calculado assim:
  - O ponteiro vai de 0 a 10
  - dano = level do herói X valor do ponteiro X missões já terminadas
- O chefão final vai tomando dano a cada missão finalizada e temos uma progressão, cada missão nos dá xp e quando chegamos a 100 evoluímos um level e assim damos mais dano, até que a vida do PROCASTINATOR chega ao fim e ganhamos dele, aparecendo uma tela de vitória e um botão para começarmos uma nova jornada no mundo de TaskQuest!!
- OBS: Não se esqueça você pode jogar com muitos heróis, é só criar

## Futuro

- Lojinha para o herói gastar suas moedas, com poções de força ou de xp.
