# Uso de CNN para análise do dataset Oregon Wildlife

## Descrição geral ##

O trabalho teve como objetivo realizar a modelagem de um database selecionado. Para isso, foi necessário evidenciar features, saídas, técnicas de processamento e explicações sobre escolhas realizadas.

Foi usado o database Oregon Wildlife, que está disponível no site Kaggle. [Wildlife image collection](https://www.kaggle.com/virtualdvid/oregon-wildlife)

## Descrição sobre a base da dados ##

O dataset contém 20 classes, sendo elas divididas em pastas para cada espécie de animal. Dentro delas encontramos o seguindo total para cada uma:

Classe                          | Total de Itens
---------                       | ---------------
bald_eagle                      |      735
black_bear                      |      708
bobcat                          |      690
canada_lynx                     |      716
columbian_black-tailed_deer     |      735
cougar                          |      670
coyote                          |      736
deer                            |      761
elk                             |      660
gray_fox                        |      668
gray_wolf                       |      730
mountain_beaver                 |      576
nutria                          |      689
raccoon                         |      723
raven                           |      650
red_fox                         |      759
ringtail                        |      583
sea_lions                       |      725
seals                           |      695
virginia_opossum                |      728


* Número total realizando um `imread` e `resize`, onde em alguns casos a imagem não foi lida (algumas vezes por ser gif).


## Criando o dataset de fato ##

Foi criado uma classe python para poder realizar esse conversão das images para usar como dataset. Nela foi usado a classe `cv2` proveniente da biblioteca openCV para a leitura das imagens, conversão de BGR para RGB (`BGR2RGB`) e diminuição de escala (`resize`) para 64x64. Após isso o conjunto de imagens lidas é convertido para um numpy array.

A conversão do set de imagens é importante por dois motivos:
- Divisão das imagens entre treino e teste, usando o método `train_test_split`, definindo uma taxa de 15% do set para a parte de teste.
- Criação dos arquivos HDF5 (explicado logo abaixo).

Para criação dos arquivos .h5 basta conter a pasta de imagens dentro do repositório (ex.: oregon_wildlife/folder1) e executar o seguinte comando:

> python -i test_create_dataset.py

Todo o processo é feito por esse .py e os arquivos estarão na raiz após finalizado o processo.

## Modelagem ## 

A modelagem da rede foi realizada no Colab, onde consigo buscar os arquivos .h5 do meu Drive e além disso usar uma GPU para realizar o processamento.

Atualmente a rede consegue detectar alguns casos com uma ótima precisão, mas em outros ainda necessita ajustes.

Todos os detalhes se encontram no próprio notebook.
