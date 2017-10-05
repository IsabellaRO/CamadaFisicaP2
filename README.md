# Camada Física -  Projeto 5 - DTMF
Por: Isabella Oliveira e Vitória Camilo (Insper)


## Geração dos tons
Os tons são gerados a partir da soma de duas ondas senoides. A fórmula utilizada foi *sen(wt)* para gerar a onda, onde *w = 2πf*. O arquivo onde os tons são gerados, reproduzidos, e plotados pela primeira vez é o *encoderDTMF.py*.


## Frequências que compõem cada tom 
|             |1209 Hz  |1336 Hz  |1477 Hz  |
|:-----------:|---------|---------|---------|
|**697 Hz**   |1        |2        |3        |
|**770 Hz**   |4        |5        |6        |
|**852 Hz**   |7        |8        |9        |
|**941 Hz**   |*        |0        |#        |


## Tons Gerados e Captados

Nos gráficos abaixo relaciona-se o sinal de tom no decorrer do tempo. Na esquerda estão as soma dos senos das duas frequências utilizadas, e na direita o gráfico do som que foi gravado de um computador que escutava o outro. As visíveis disparidades entre os gráficos correspondem as interferencias presentes em meio a gravação. O arquivo com o código que escuta, grava e plota um novo gráfico é o *decoderDTMF.py*.

| Tom | Primeira plotagem                  |Ondas Captadas               |
|:-----:|-------------------------|----------------------|
|1      | ![1](img/1p.png)        |![1](img/1.png)       |
|2      | ![2](img/2p.png)        |![2](img/2.png)       |
|3      | ![3](img/3p.png)        |![3](img/3.png)       |
|4      | ![4](img/4p.png)        |![4](img/4.png)       |
|5      | ![5](img/5p.png)        |![5](img/5.png)       |
|6      | ![6](img/6p.png)        |![6](img/6.png)       |
|7      | ![7](img/7p.png)        |![7](img/7.png)       |
|8      | ![8](img/8p.png)        |![8](img/8.png)       |
|9      | ![9](img/9p.png)        |![9](img/9.png)       | 
|0      | ![0](img/0p.png)        |![0](img/0.png)       |
|*      | ![*](img/astp.png)  |![*](img/ast.png)    |
|#      | ![#](img/hashp.png)     |![#](img/hash.png) |

## Sinais Enviados e Recebidos

| Tom   | Sinal Enviado       |Sinal Recebido         |
|:-----:|-------------------------|----------------------|
|1      | ![1](img/T1.png)        |![1](img/Fourier1.png)      |
|2      | ![2](img/T2.png)        |![2](img/Fourier2.png)      |
|3      | ![3](img/T3.png)        |![3](img/Fourier3.png)      |
|4      | ![4](img/T4.png)        |![4](img/Fourier4.png)      |
|5      | ![5](img/T5.png)        |![5](img/Fourier5.png)      |
|6      | ![6](img/T6.png)        |![6](img/Fourier6.png)      |
|7      | ![7](img/T7.png)        |![7](img/Fourier7.png)      |
|8      | ![8](img/T8.png)        |![8](img/Fourier8.png)      |
|9      | ![9](img/T9.png)        |![9](img/Fourier9.png)      | 
|0      | ![0](img/t0.png)        |![0](img/Fourier0.png)      |
|*      | ![*](img/Tast.png)  |![*](img/Fourier10.png)   |
|#      | ![#](img/Thash.png)     |![#](img/Fourier11.png)|


## Frequências enviadas e recebidas
As frequências enviadas são recebidas sem discrepância, e seguem de acordo com os valores que compõe cada tom (low, high).

## Tempos utilizados
Os audios transmitidos tem duração de 1 segundo, o mesmo setado na geração dos tons, e os gráficos são gerados para cada 1 segundo recebido, captando, assim, cada audio de tom por completo.