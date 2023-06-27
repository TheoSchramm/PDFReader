# __🎙️ PDF Reader__
- Leitor de PDF que utilizando a biblioteca Tkinter, cria uma interface gráfica de usuário responsiva junto com a biblioteca PyPDF2 para manipular arquivos PDF. Para converter texto em fala é usado da API de Texto-para-Fala (gTTS) do Google e a biblioteca OS para salvar e reproduzir o áudio.

<p align="center">
  <img src="/img_exemplo.png?raw=true "Exemplo")" />
</p>

# __📌 Dependências__
1. [Python](https://www.python.org/downloads/)
2. Bibliotecas PyPDF2 & gTTS

# __🤔 Como utilizar?__
Para selecione o arquivo PDF a ser convertido, clique no botão superior esquerdo e navegue até o arquivo desejado. Em seguida, selecione o idioma da narração e clique no botão para iniciar a narração. Se você quiser habilitar a narração lenta, marque a caixa de Narração lenta antes de clicar para narrar. Durante a narração, uma barra de progresso será exibida na janela para mostrar o progresso da conversão caso o PDF seja muito grande.

Se o número de páginas no PDF for maior que o limite definido na variável "pag_limit" (50 páginas), uma mensagem de erro será exibida informando que o limite foi ultrapassado. Sinta-se a vontade para aumentar o limite caso necessário.

Uma vez que a narração tenha sido concluída, o áudio será salvo no mesmo diretório do script.
