# __🎙️ PDF Reader__
- Leitor de PDF que utiliza a biblioteca Tkinter para criar uma interface gráfica de usuário (GUI) e a biblioteca PyPDF2 para manipular arquivos PDF. Ele também usa a API de Texto-para-Fala (gTTS) do Google para converter texto em fala e a biblioteca OS para salvar e reproduzir o áudio. A biblioteca Threading também é usada para tornar a GUI responsiva durante a conversão PDF para MP3.

<p align="center">
  <img src="/img_exemplo.png?raw=true "Exemplo")" />
</p>

# __📌 Dependências__
1. [Python](https://www.python.org/downloads/)
2. Bibliotecas PyPDF2 & gTTS

# __🤔 Como utilizar?__
Depois de instalar as bibliotecas, você pode rodar o código como qualquer outro script Python. Ele criará uma janela GUI com vários widgets, incluindo um botão para selecionar o arquivo PDF, um botão para iniciar a narração, uma caixa combinada para selecionar o idioma, uma entrada para exibir o caminho do arquivo PDF selecionado e uma caixa de seleção para habilitar a narração lenta.

Para selecionar o arquivo PDF, clique no botão "Selecionar PDF" e navegue até o arquivo desejado. Em seguida, selecione o idioma desejado na caixa combinada e clique no botão "Narrar" para iniciar a narração. Se você quiser habilitar a narração lenta, marque a caixa de seleção "Narração lenta" antes de clicar no botão "Narrar". Durante a narração, uma barra de progresso será exibida na janela para mostrar o progresso da conversão.

Se o número de páginas no PDF for maior que o limite definido na variável "pag_limit" (50 páginas), uma mensagem de erro será exibida informando que o limite foi ultrapassado.

Uma vez que a narração tenha sido concluída, o áudio será salvo com o nome "audio.mp3" no mesmo diretório do script.
