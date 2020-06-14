# Uso de CNN para análise do dataset Oregon Wildlife

## Descrição geral ##

O trabalho teve como objetivo realizar a modelagem de um database selecionado. Para isso, foi necessário evidenciar features, saídas, técnicas de processamento e explicações sobre escolhas realizadas.

Foi usado o database Oregon Wildlife, que está disponível no site Kaggle. ![link](https://www.kaggle.com/virtualdvid/oregon-wildlife)

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


## Sobre o código ##
