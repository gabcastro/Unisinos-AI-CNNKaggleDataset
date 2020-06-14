# Uso de CNN para análise do dataset Oregon Wildlife

## Descrição geral ##

O trabalho teve como objetivo realizar a modelagem de um database selecionado. Para isso, foi necessário evidenciar features, saídas, técnicas de processamento e explicações sobre escolhas realizadas.

Foi usado o database Oregon Wildlife, que está disponível no site Kaggle. ![link](https://www.kaggle.com/virtualdvid/oregon-wildlife)

## Descrição sobre a base da dados ##

O dataset contém 20 classes, sendo elas divididas em pastas para cada espécie de animal. Dentro delas encontramos o seguindo total para cada uma:

                            Classe | Total de Itens
---------------------------------- | ---------------
0                    bald_eagle    |      735
1                    black_bear    |      708
2                        bobcat    |      690
3                   canada_lynx    |      716
4   columbian_black-tailed_deer    |      735
5                        cougar    |      670
6                        coyote    |      736
7                          deer    |      761
8                           elk    |      660
9                      gray_fox    |      668
10                    gray_wolf    |      730
11              mountain_beaver    |      576
12                       nutria    |      689
13                      raccoon    |      723
14                        raven    |      650
15                      red_fox    |      759
16                     ringtail    |      583
17                    sea_lions    |      725
18                        seals    |      695
19             virginia_opossum    |      728


* Número total realizando um `imread` e `resize`, onde em alguns casos a imagem não foi lida (algumas vezes por ser gif).


## Sobre o código ##