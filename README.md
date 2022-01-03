# PySystem-Framework

**PySystem Framework** é um projeto open-source com o intuito de automatizar a criação, desenvolvimento e gerenciamento de elementos do sistema e tarefas de programação.

Dentro do framework temos 5 pacotes até então:

- PySystem
- PyProject
- PyDocs
- PyFiles
- PyEnvironment

O pacote **PySystem** é utilizado para interagir com o sistema. Entre suas principais funções é criar novos comandos e aprimorar comandos já existentes do Windows, e também conseguir diversas informações do sistema de forma simples e ter a possibilidade de gravar em um arquigo LOG, JSON, XML, SQL, YAML, CSV, entre outros.

O pacote **PyProject** visa automatizar o processo de criação de projetos. Quando vamos criar projetos em qualquer linguagens, principalmente utilizando algum framework da mesma, geralmente temos um padrão de diretórios e arquivos (alguns obrigatórios, outros opcionais). Com isso, o PyProject automatiza a criação desses diretórios e arquivos, acrscenta o conteúdo padrão de cada arquivo e separa o que pode ser uma estrutura simples, recomendada e pesada, que pode ser configurado com seu CLI.

O pacote **PyDocs** visa armazenar a documentação de vários elementos do Python e suas biliotecas, seja para utilizar em sua aplicação ou apenas para ter a documentação consigo. Essa documentação de tal elemento pode ser gravado em arquivos HTML, Markdown, RTF, entre outros, para ser lido tranquilamente, tanto por um humano quanto por um script.

O pacote **PyFiles** automatiza a criação de arquivos padrões que normalmente são encontrados em alguns projetos, como package.json, gitignore, entre outros.

Por fim, o **PyEnvironment** trata-se de um pacote, onde terá um CLI (Command-Line Interface) que poderá ajudar a preparar um ambiente de programação. Terá opção para instalação de IDEs, linguagens, entre outros recursos, bem como terá bibliotecas para instalação dos mesmos.