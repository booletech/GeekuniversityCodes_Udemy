import os
import re


def remove_bracket_content(text):
    return re.sub(r'\[.*?\]', '', text)


def split_text(text, length=4000):
    return [text[i:i + length] for i in range(0, len(text), length)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_parts(text):
    cleaned_text = remove_bracket_content(text)
    parts = split_text(cleaned_text)

    for i, part in enumerate(parts, 1):
        clear_screen()
        print(f"Parte {i}:\n{part}\n")
        if i != len(parts):
            answer = input("Deseja continuar para a próxima parte? (s/n) ").lower()
            if answer != 's':
                break


# Teste
texto_original = """Detecting language using up to the first 30 seconds. Use `--language` to specify the language
Detected language: Portuguese
[00:00.000 --> 00:12.560]  Muito bem. Pessoal, todo mundo me ouvindo aí, todo mundo me vendo, ouvindo.
[00:12.560 --> 00:29.600]  Beleza. Bom, pessoal, vamos lá. Eu já vi que o pessoal está mandando e-mail, tá?
[00:29.600 --> 00:37.440]  Eu preciso começar a organizar isso aí. E eu tô vendo que tem bastante gente aí que tá me mandando
[00:37.440 --> 00:49.160]  falar conosco, tá? Então, eu vou fazer o seguinte, tá? Como assim, muitos assim, alguns estão me
[00:49.160 --> 00:55.200]  questionando sobre o TCC, que nem eu já tinha falado primeiro de aula, né? Ah, inclusive no falo
[00:55.200 --> 01:04.640]  conosco. Se vocês olharem no falo conosco, eu anexei as nossas três aulas. Inclusive, a de hoje
[01:04.640 --> 01:12.160]  já está lá disponível, tá? Então, já tá lá disponível no falo conosco. Então, quando você
[01:12.160 --> 01:19.160]  fala conosco, tá lá três arquivos anexados, certo? E vamos fazer o seguinte, pessoal. Vamos
[01:20.000 --> 01:27.040]  concentrar os temas, ou seja, que vocês vão estar mandando os temas para mim. Vamos concentrar
[01:27.040 --> 01:34.040]  os temas. Se possível, no falo conosco, no falo com o professor, tá? Eu já vi lá hoje lá que tem
[01:34.040 --> 01:40.240]  oito mensagens lá. Então, amanhã de manhã, amanhã cedinho, eu já vou procurar responder. Eu vou
[01:40.240 --> 01:48.000]  começar a planilhar esses temas. Só vou pedir a gentileza. Quem for falar que, olha, que o meu
[01:48.000 --> 01:56.920]  professor tem cinco pessoas, por favor, no falo conosco, coloca lá o nome e o registro de aluno
[01:56.920 --> 02:03.400]  de cada um, tá? Coloca o nome e registro de aluno de cada um para eu poder planilhar, para eu ter uma
[02:03.400 --> 02:10.040]  ideia aí, ter uma ideia da quantidade de trabalho e dos temas para eu já começar a dar os feedbacks,
[02:10.040 --> 02:17.640]  certo? Então, vamos procurar, vamos concentrar tudo no falo conosco, que aí amanhã, amanhã já
[02:17.640 --> 02:24.280]  vai começar a acessar e respondendo aos poucos. É rápido. Pode ser, pessoal. Beleza ou não?
[02:30.400 --> 02:40.080]  Beleza, beleza. Pode ser sim. Como eu tinha comentado na última aula, né, o fim de semana a gente
[02:40.080 --> 02:50.560]  fecha o fim de semana. No fim do trimestre, a gente fecha aí os temas até a parte de
[02:50.560 --> 02:57.240]  fundamentação teórica, tá? Para vocês ir no final do semestre, a composição do artigo, do
[02:57.240 --> 03:08.840]  pitch e do artigo, do pitch e do slide, certo? Então, aí na próxima aula já vou dar uma
[03:08.840 --> 03:16.880]  mensagem sobre esse assunto. Eu preciso, eu vou postar de novo no Fale com o Professor, eu
[03:16.880 --> 03:23.680]  preciso que vocês me mandem os temas com o nome do grupo. Quem já mandou mensagem Fale com o
[03:23.680 --> 03:33.240]  Professor, manda de novo, tá? Com o nome do grupo para que eu possa o quê? Para que eu possa planilhar
[03:33.240 --> 03:44.360]  os temas e já começar a nossa ação de validação e criar o cronograma de entrega do outro trabalho,
[03:44.360 --> 03:52.200]  entendeu? Que é o trabalho conclusão de curso de vocês, pessoal. Beleza? Bom, meu objetivo hoje,
[03:52.200 --> 04:02.560]  trabalho conclusão de curso, pessoal, é um trabalho de pesquisa, certo? Como ele é um trabalho de
[04:02.560 --> 04:10.520]  pesquisa. Pesquisar pessoal não é só simplesmente ir lá abrir o Google e procurar, não. A pesquisa
[04:10.520 --> 04:18.760]  científica, pesquisa tecnológica, ela possui alguns ritos, né? Possui alguns dogmas, mas como assim?
[04:18.760 --> 04:28.480]  Quando você faz, quando você tem um tempo curto para você realizar pesquisa de material, aí vem
[04:28.480 --> 04:35.400]  a pergunta, como que eu faço, para que eu tenha resposta certa, eu tenho que fazer a pergunta certa,
[04:35.400 --> 04:43.280]  ou seja, se eu pesquiso o material, como, se eu pesquiso, como que eu faço essa pesquisa? Que
[04:43.280 --> 04:48.040]  tipo de questionamento que eu faço? Por que é importante isso? Ah, mas eu vou procurar tudo sobre
[04:48.040 --> 04:57.240]  esse assunto. Não, eu tenho que ser algo focado de maneira que eu seja direto, de maneira que a minha
[04:57.240 --> 05:06.680]  pesquisa seja otimizada, certo? Quando a gente fala de metodologia científica, pessoal, a metodologia
[05:06.680 --> 05:15.880]  científica, ela advém do método, mas que seria o método? O conjunto de procedimentos necessário
[05:15.880 --> 05:23.240]  para atingir o meu objetivo, certo? Então, a metodologia, ela adivém o quê? Ela adivém do conjunto
[05:23.400 --> 05:35.560]  de procedimentos, ou seja, ela adivém do método. Método para quê? Para adquirir ciência.
[05:40.440 --> 05:50.400]  Pessoal, ciência é conhecimento. Então, quando eu falo método, quando eu falo o método científico,
[05:50.880 --> 05:58.480]  quando você está estudando, quando você está apresentando um problema, e a partir desse problema,
[05:58.480 --> 06:05.120]  você está apresentando a solução, você está gerando o quê? Você está gerando conhecimento e
[06:05.120 --> 06:15.480]  você está aplicando o método científico, certo? E assim, pessoal, tudo que temos, tudo que temos em
[06:15.800 --> 06:23.400]  ciência e tecnologia hoje, em algum momento foi um problema, foi um problema gerado, foi um problema
[06:23.400 --> 06:33.000]  que foi necessário realizar a sua solução, certo? Se você tem uma internet de boa comunicação,
[06:33.000 --> 06:41.320]  em algum momento ela foi necessária na Primeira, na Segunda Guerra Mundial. Se você tem materiais,
[06:41.400 --> 06:47.080]  você tem materiais mais leves, você tem o que denominamos hoje o grupo dos biomateriais,
[06:47.080 --> 06:54.840]  e em algum momento ele foi utilizado na corrida espacial, certo? Então, tudo o que a gente tem
[06:54.840 --> 07:03.960]  hoje, ele surgiu para a solução do problema, e essa solução desse problema criou-se conhecimento
[07:04.040 --> 07:09.560]  ou se um produto que ele é aplicado no comércio mundial, certo? Então,
[07:11.320 --> 07:19.080]  o método científico, ele está relacionado ao quê? Está relacionado à forma como você irá
[07:19.080 --> 07:32.200]  pesquisar, como você irá atacar um assunto, certo? A ciência, ela é classificada em dois grupos,
[07:32.920 --> 07:43.480]  que é o que denominamos as ciências formais, que é que estudam ideias, e as ciências factuais que
[07:43.480 --> 07:56.120]  estudam objetos, coisas e processos. As ciências formais, pessoal, ela tem um perfil mais parecido
[07:56.120 --> 08:05.880]  com a estrutura de engenharia, né? Ou seja, o estudo lógico, o estudo matemático. As ciências
[08:05.880 --> 08:14.200]  factuais, elas são divididas em dois grupos, que são os naturais e os sociais, né? Dos grupos
[08:14.200 --> 08:23.160]  naturais, enxergamos aí as ciências naturais e as ciências aplicadas, física, química,
[08:23.240 --> 08:36.040]  psicologia, agronomia, certo? Dentro as ciências sociais já entra direito, sociologia, antropologia,
[08:36.040 --> 08:45.800]  economia, política, psicologia, psicopedagogia, certo? E assim sucessivamente, certo? E assim,
[08:45.800 --> 08:57.560]  estudar conceitos sociais, você criar modelos de estudo para conceitos sociais é muito mais
[08:57.560 --> 09:10.520]  difícil do que ciências formais e factuais naturais. Por quê? Porque a gente consegue quantificar,
[09:10.520 --> 09:23.880]  quando você consegue quantificar um fenômeno, é mais fácil você interpretar e você reproduzir.
[09:23.880 --> 09:29.080]  E agora, quando você tem um fenômeno que você não possui essa quantificação, mas como assim?
[09:29.080 --> 09:37.080]  Ah, por exemplo, eu vou fazer uma pesquisa, eu vou fazer uma pesquisa sobre gosto por refrigerante,
[09:37.160 --> 09:43.720]  uma escala de zero a dez, quanto que você gosta de refrigerante? Ah, mas eu gosto mais ou menos,
[09:43.720 --> 09:51.400]  é cinco, né? Aí outra pessoa fala, não, eu gosto muito, é dez, só que aí é assim, é aquela história,
[09:51.400 --> 09:59.080]  nem sempre lá o dez, o dez dele é assim, não, mas será que ele gosta muito mesmo? Ou ele sempre
[09:59.080 --> 10:08.360]  fala, eu gosto, é dez aí, acabou, entendeu? Então, estudar fenômenos sociais é muito mais difícil
[10:08.360 --> 10:16.120]  do que estudar fenômenos naturais e ciências lógicas e matemáticas, certo? Então assim,
[10:16.120 --> 10:29.000]  o conhecimento científico adquirido na pesquisa, na geração do trabalho tecnológico, ele sempre
[10:29.000 --> 10:43.640]  ele adivém da solução de problemas, que é o que denominamos aí de pesquisa aplicada, e de explicações,
[10:43.640 --> 10:52.600]  descrição, testes, que ele adivém o que? Da pesquisa pura, certo? Então, no fim, as duas,
[10:52.600 --> 11:05.080]  no fim, as duas, elas vão chegar no mesmo objetivo, né? Então, nosso objetivo é atender
[11:05.080 --> 11:10.480]  a sociedade, então nosso objetivo é atender a sociedade, então seja de forma direta com a
[11:10.480 --> 11:16.200]  pesquisa aplicada, seja de forma indireta com a pesquisa fundamental, a partir da pesquisa fundamental,
[11:16.200 --> 11:25.480]  você vai gerar produtos e subsídios que vai chegar na pesquisa aplicada, certo? Então, de uma forma,
[11:25.480 --> 11:34.120]  um resumo para nós aqui, né? O método, que é o conjunto de etapas, a metodologia, que é o estudo
[11:34.120 --> 11:42.360]  crítico desses métodos, ou seja, o que é mais adequado para resolver o problema, a ciência, que
[11:42.360 --> 11:48.560]  é a adivém, o conjunto conhecimento, ou seja, criador, domínio saber, e a pesquisa, que ela,
[11:48.560 --> 11:58.960]  basicamente, seria o que? Seria a investigação, certo? Quando a gente fala do método científico,
[12:00.160 --> 12:06.240]  quando a gente fala do método científico, basicamente, a gente quer
[12:07.000 --> 12:21.200]  pesquisar, ou seja, você quer explicar o fenômeno, você quer, desculpa, você quer explicar o
[12:21.200 --> 12:30.040]  fenômeno, você quer criar uma ferramenta de aquisição e construção do conhecimento,
[12:30.040 --> 12:40.040]  você quer reproduzir um fenômeno, ou você quer validar algo que você observou, certo? Então,
[12:40.040 --> 12:46.240]  assim, basicamente, você tem isso também direcionado para o nosso trabalho, para o nosso trabalho de
[12:46.240 --> 12:53.840]  conclusão de curso, né? Você quer explicar um fenômeno, você quer explicar o fenômeno, ou você
[12:53.880 --> 13:00.440]  quer reproduzir, ou então você quer validar o modelo que você criou, certo? Então, isso vai
[13:00.440 --> 13:13.800]  encontrar o quê? Com o nosso modelo de pesquisa tecnológica, certo? Dentro da parte de pesquisas,
[13:14.520 --> 13:34.680]  nós temos o conceito de indução e dedução, certo? Existe algo que você é induzido,
[13:34.680 --> 13:42.280]  existe algo que você deduz, certo? Então, assim, eles são, a diferença entre elas são bem sutis,
[13:42.280 --> 13:50.160]  ou seja, né? O processo de indução, por que eu preciso disso? Porque, assim, para você estudar
[13:50.160 --> 13:56.840]  fenômenos, mesmo os fenômenos tecnológicos, ou seja, um dispositivo, equipamento que você
[13:56.840 --> 14:03.720]  implementar, você precisa ter a dedução e você precisa ter a indução, certo? Quando a gente fala,
[14:03.720 --> 14:21.200]  da indução, basicamente, a gente parte de dados particulares para uma verdade geral ou universal,
[14:21.200 --> 14:29.520]  certo? Então, vamos assim, isso é o que denominamos indução, vou dar um exemplo aí, né? A lei, assim,
[14:29.520 --> 14:35.160]  é a primeira vez de homem, é a primeira vez de homem, R é igual a U dividido por I,
[14:35.160 --> 14:56.720]  pronto. Então, assim, eu tinha dois volts, um ampere, três volts, um ampere e meio, quatro volts,
[14:56.800 --> 15:04.080]  dois amperes, cinco volts, dois amperes e meio. Então, a partir de dados particulares,
[15:04.080 --> 15:13.000]  eu consegui induzir que a lei de homem é igual a V dividida por I, certo? Então, ou seja, eu parti
[15:13.000 --> 15:27.400]  de dados particulares para uma verdade geral ou universal, certo? E assim, via de regra, assim,
[15:27.400 --> 15:34.360]  o método inidutivo, ele é empírico. Pessoal, o que é empírico, para vocês entenderem? Empírico
[15:34.360 --> 15:43.960]  é o famoso tentativa e erro, mas tentativa e erro. Eu não tenho, eu não tenho, eu não tinha
[15:43.960 --> 15:52.120]  uma expressão matemática, eu comecei a fazer o teste, ó, um volt, meia ampere, dois volts,
[15:52.120 --> 15:58.120]  um ampere, três volts, um ampere e meio, quatro volts, até chegou o momento, bom, então,
[15:58.120 --> 16:03.800]  teoricamente, então, teoricamente, quando eu tenho aqui, quando eu aplicar dez volts,
[16:03.800 --> 16:08.040]  eu tenho que ter cinco amperes, aí eu vou lá e meço cinco amperes, então, beleza, então,
[16:08.040 --> 16:17.920]  eu consegui estabelecer o modelo. Ele é lógico e ele é intuitivo, certo? Então, método inidutivo,
[16:17.920 --> 16:24.720]  eu passo de dados particulares para uma verdade geral, certo? Então, assim, algumas, né,
[16:24.960 --> 16:31.840]  geralmente é aplicado em observações fenômenos, relação entre eles, generalização de uma
[16:31.840 --> 16:40.160]  relação, certo? Então, um exemplo aqui, um trocadilho, certo? Observe-se que Pedro,
[16:40.160 --> 16:47.640]  João, Pedro, José e João são mortais, ponto. Verifica se a relação entre ser homem e ser mortal
[16:47.640 --> 16:55.800]  generaliza dizendo que todos os homens são mortais, então, Pedro é mortal, o homem Pedro, Pedro é
[16:55.800 --> 17:05.080]  mortal, José é mortal, João é mortal, todos eles são homens, ou seja, né, se Pedro, José e João
[17:05.080 --> 17:14.400]  são mortais e os três são homens, então significa o quê? Significa que todos os homens eles são
[17:14.520 --> 17:24.800]  mortais, certo? Então, assim, alguns exemplos de pesquisas que nós conhecemos hoje de forma
[17:24.800 --> 17:34.280]  indutiva, a lei da gravidade de Newton, a equação do pelo de Galileu-Galileu, a primeira, segunda,
[17:34.280 --> 17:43.640]  a lei de Newton, as pesquisas estatísticas, elas induzem, elas são indutivas, pesquisas
[17:43.640 --> 17:55.400]  epidemiológicas, os testes com remédios vacinas e as pesquisas agropecuárias, certo? Método
[17:55.400 --> 18:10.120]  dedutivo, né, o método dedutivo, basicamente, você vem de enunciados ou teorias universais
[18:10.120 --> 18:21.080]  e transforma em teorias particulares, diferente da indução, a partir da teoria, a partir de dados
[18:21.080 --> 18:30.640]  particulares, você chega a uma verdade universal, certo? E assim, a dedução é uma argumentação que
[18:30.640 --> 18:39.160]  ela torna explícita verdades particulares dentro de escopos universais, vou dar um exemplo aqui,
[18:39.160 --> 18:53.560]  é, todo mamífero tem um coração, ponto, então, ou seja, uma lei geral, né? Todos os cães são
[18:53.560 --> 19:00.160]  mamíferos, então, continua sendo geral, então, agora, eu tornei um dado particular, então, logo,
[19:00.160 --> 19:08.280]  todos os cães, eles têm coração, ou seja, a dedução, eu parti de algo geral para um conceito
[19:08.280 --> 19:17.800]  específico, a indução, eu parti de algo específico para um conceito geral, uma visão geral, certo?
[19:19.080 --> 19:28.320]  Alguns exemplos de pesquisa, né, de argumento dedutivo, a luneta astronômica de Galileo Galilei,
[19:28.320 --> 19:36.880]  o para-raios de Benjamin Franklin, a pilha de Alessandro Volta, a lâmpada de Thomas Alva Edson,
[19:36.960 --> 19:45.480]  a teoria da relatividade de Einstein, Albert Einstein, as ondas de rádio de Heinrich R. Hertz,
[19:45.480 --> 19:58.080]  e todas as pesquisas teóricas, certo? Então, resumidamente, indução e dedução, ambas
[19:58.400 --> 20:06.440]  em precisas, premissas, o dedutivo, premissas verdadeiras, invariávelmente a conclusões
[20:06.440 --> 20:14.680]  verdadeiras, o indutivo, premissas verdadeiras conduzem a conclusões prováveis, né, tanto é
[20:14.680 --> 20:23.320]  que ele destaca bem o dedutivo e o indutivo, certo? Pessoal, até aqui, beleza? Tudo tranquilo aí?
[20:24.120 --> 20:34.400]  Todo mundo esperto aí, ou não? Alex, Aline, Anderson, Antônio, Carolina, Fabio, Hélio Araújo,
[20:34.400 --> 20:42.800]  João Paulo, Larissa, Leandro, Jesus, Marcos, Melki, Reginaldo, Alesson e Daniel Gomes,
[20:43.320 --> 20:56.040]  todo mundo esperto aqui, né? Todo mundo esperto. Bom, então, a gente viu aí método científico,
[20:58.040 --> 21:07.200]  método científico, indução, dedução, certo? Agora, sim, a parte de pesquisa. Pessoal,
[21:07.400 --> 21:16.760]  como eu falei, primeira coisa, primeira frase que eu falei hoje, né? Pesquisar não é ir lá,
[21:16.760 --> 21:22.040]  colocar no Google. Você pode colocar no Google, você pode achar um monte de porcaria lá, entendeu?
[21:22.040 --> 21:31.200]  Mas, assim, o pesquisar, pessoal, é a forma como você irá questionar, certo? Então, assim,
[21:31.680 --> 21:39.880]  aquisição de novos conhecimentos, realidade empírica, mas o pesquisar, ele está relacionado
[21:39.880 --> 21:52.080]  ao questionar, está relacionado a você escrever ou descrever, certo? Explicar, se você quer explicar,
[21:52.080 --> 21:58.800]  se você quer explicar um fenômeno, você precisa da parte pesquisa mais teórica, se você quer
[21:58.800 --> 22:04.600]  explicar um fenômeno, você precisa da parte de pesquisa aplicada, entendeu? Então, assim,
[22:04.600 --> 22:12.360]  se você quer atender o mercado, se você quer resolver problemas, então, em função do seu trabalho,
[22:12.360 --> 22:19.960]  em função da sua meta, é que você irá realizar a pergunta correta, certo?
[22:19.960 --> 22:39.240]  Como que é caracterizada a pesquisa, pessoal? A pesquisa científica, ela tem o início
[22:39.240 --> 22:51.560]  e ela tem o término, né? Pesquisa, ela tem o objetivo de melhorar a qualidade de vida, certo?
[22:51.560 --> 23:03.360]  Então, assim, uma técnica, um processo construtivo, uma substituição de equipamento,
[23:03.560 --> 23:09.920]  uma substituição de equipamento vai gerar o quê? Você vai gerar uma otimização no processo,
[23:09.920 --> 23:17.920]  você vai gerar um ambiente mais seguro para um profissional da área, para o seu funcionário,
[23:17.920 --> 23:24.240]  você vai gerar mais lucros para o seu cliente. Então, tudo isso está relacionado ao quê?
[23:24.240 --> 23:30.560]  A melhoria de qualidade de vida. E assim, basicamente, a pesquisa científica é dividida
[23:30.560 --> 23:44.480]  em dois grupos, né? A pesquisa básica ou fundamental, ela tem, o principal objetivo dela,
[23:44.480 --> 23:59.120]  gerar conhecimento, ciência, certo? Esses conhecimentos, eles são aplicados, eles são aplicados
[23:59.120 --> 24:07.000]  para pesquisas aplicadas ou tecnológicas. Então, de forma indireta, você está vindo para cá, certo?
[24:10.000 --> 24:21.760]  Já a pesquisa aplicada, ela já vem o quê? Ela já vem conhecimentos básicos para gerar produtos,
[24:22.760 --> 24:34.000]  gerar processos ou gerar mais conhecimento, certo? Então, assim, esta modalidade, ela já possui o
[24:34.000 --> 24:43.200]  quê? Já possui uma ação imediata, ou seja, eu preciso criar um produto e esse produto eu já preciso
[24:43.200 --> 24:50.680]  lançar no mercado, então já é uma pesquisa imediata. Agora, a pesquisa básica e fundamental,
[24:50.720 --> 24:57.560]  ela é mais morosa, então você já vai criar o quê? Um conceito, você vai criar uma ferramenta que
[24:57.560 --> 25:06.760]  lá na frente ele será aplicado nesta modalidade, certo? Então, por que é que é importante, né?
[25:06.760 --> 25:13.000]  Por que é que é importante saber o tipo da pesquisa que você vai aplicar no seu trabalho?
[25:13.000 --> 25:22.400]  Por que é assim? Para saber o quê? Para saber fazer a pergunta correta, certo? Se eu fizer a
[25:22.400 --> 25:29.760]  pergunta correta, eu consigo fazer a pesquisa correta, consequentemente eu perco o quê? Menos
[25:29.760 --> 25:37.760]  tempo e eu consigo emitir resultados de formas mais rápidas, certo? Então, assim, como que elas
[25:37.760 --> 25:47.400]  são classificadas as pesquisas científicas, né? Quanto à finalidade, básica ou fundamental,
[25:47.400 --> 26:00.560]  ou aplicada? Quanto ao objetivo? Você vai explorar o fenômeno, você vai descrever um fenômeno ou
[26:00.560 --> 26:12.240]  você vai explicar um fenômeno, certo? Quanto aos procedimentos, a fonte material, você vai
[26:12.240 --> 26:24.000]  utilizar pesquisa bibliográfica, você vai utilizar pesquisa documental, que são pesquisas
[26:25.000 --> 26:31.120]  instantâneas, ou você vai fazer o que a gente denomina o trabalho de campo, certo?
[26:33.120 --> 26:39.960]  Quanto à natureza dos seus dados? Se você vai ser uma pesquisa qualitativa, você vai ser uma
[26:39.960 --> 26:50.880]  pesquisa quantitativa e é o local de realização. Você vai fazer a sua aplicação em campo direto ou
[26:50.880 --> 27:02.280]  você irá realizar a sua reprodução em laboratório, certo? Então, assim, quanto ao objetivo?
[27:03.680 --> 27:16.280]  Explorar, descrever ou explicar? Quanto às fontes que você utilizará? Levantamento de campo,
[27:16.280 --> 27:25.160]  pesquisa laboratório, pesquisa bibliográfica. E quanto ao procedimento para a coleta das pesquisas?
[27:25.160 --> 27:41.560]  Nós temos pesquisa experimental, ex post facto, levantamento, estudo de caso, pesquisação,
[27:41.560 --> 27:51.960]  pesquisa bibliográfica ou pesquisa documental, certo? O que é cada um, pessoal? A pesquisa
[27:51.960 --> 28:02.680]  exploratória, você quer, o próprio nome já diz, ou seja, você quer explorar determinado fenômeno,
[28:02.680 --> 28:14.040]  certo? E assim, você quer explorar ele e recuperar informações disponíveis. Via de regra é feita
[28:14.040 --> 28:19.840]  através de devotamento bibliográfico, entrevistas profissionais da área, visites, instituições,
[28:19.840 --> 28:30.040]  empresas, websites, etc. Então, quero explorar o fenômeno. Ele já existe, ele já tem uma teoria
[28:30.040 --> 28:39.600]  visualizada, você quer explorar mais essa teoria, certo? A pesquisa descriptiva, você vai fazer um
[28:39.600 --> 28:47.640]  levantamento dos principais componentes de um fenômeno, certo? E você vai fazer o quê? O
[28:47.640 --> 29:02.920]  levantamento ou as observações sistemáticas. Já a pesquisa, já a pesquisa explicativa, o próprio
[29:02.920 --> 29:08.480]  nome já diz o porquê, certo? Por que que isso, por que que esse fenômeno acontece dessa maneira,
[29:08.480 --> 29:16.960]  certo? Então, assim, você vai explorar, ou seja, o fenômeno já existe, você vai descrever, então
[29:16.960 --> 29:22.920]  você vai pegar alguns elementos básicos e você vai tentar explicar, certo? E tudo isso, pessoal,
[29:22.920 --> 29:29.880]  assim, todos esses três protópios eu posso aplicar, posso aplicar na área tecnológica, né?
[29:29.880 --> 29:37.880]  Se você tem um problema na sua instalação elétrica, então você precisa, assim, descrever o que está
[29:37.880 --> 29:43.600]  acontecendo, você precisa explicar por que está acontecendo isso, você precisa explorar. Então,
[29:43.600 --> 29:47.040]  tudo isso é válido para a área o quê? Para a área tecnológica.
[29:55.040 --> 30:10.360]  Os tipos de pesquisa quanto ao forma ou local, né? O levantamento de campo, ou seja, eu vou para
[30:10.360 --> 30:17.960]  campo, eu vou aplicar isso, vou aplicar isso direto na minha empresa, certo? Vou aplicar
[30:17.960 --> 30:25.840]  isso direto na minha empresa e eu faço o quê? Uma observação direta e o que a gente diz aí,
[30:25.840 --> 30:36.360]  o próprio nome diz aí, levantamento de campo, certo? Posso trabalhar o que a gente diz em laboratório,
[30:36.360 --> 30:39.720]  quando a gente trabalha, quando a gente fala trabalho laboratório, pessoal,
[30:42.200 --> 30:52.120]  existem alguns tópicos, alguns temas que a gente consegue fazer a reprodução via simulação
[30:52.120 --> 30:59.960]  computacional, certo? Então, a própria simulação computacional, ela já é caracterizada como um
[30:59.960 --> 31:10.520]  ambiente laboratório. Por quê? Porque quando você, eu vou dar um exemplo, teste de software
[31:10.520 --> 31:19.240]  antes de você soltar ele para aplicação, certo? Quando você cria um ambiente virtual e você não
[31:19.240 --> 31:24.080]  linka o seu software com a sua aplicação, que eu estou executando ele somente aqui nesse ambiente
[31:24.080 --> 31:29.600]  virtual, eu estou executando ele em laboratório, certo? Então, laboratório necessariamente, você
[31:29.600 --> 31:36.080]  existe um laboratório que você pode reproduzir todos os fenômenos em determinado processo ou
[31:36.080 --> 31:43.200]  você também pode realizar o quê? Realizar o que denominamos de simulação computacional, certo? Então,
[31:43.200 --> 31:54.800]  basicamente, você ia interferir de forma artificial e você criaria estímulos externos
[31:54.800 --> 32:06.560]  e cenários de forma simular uma possível situação, certo? A ideia é que na pesquisa de campo,
[32:06.640 --> 32:14.160]  você tenta esclarecer um padrão, certo? E descrever e realizar uma análise e uma reprodução desse
[32:14.160 --> 32:27.920]  evento, certo? Quanto a parte da pesquisa, tá? Aí entra a coleta dos dados. Lembre-se, pessoal,
[32:27.920 --> 32:35.680]  que eu trabalho com o Cruzão do Curso e vocês, não existe, não é só uma montagem, ela tem que ter
[32:35.760 --> 32:44.240]  uma pesquisa, ela deve ter um levantamento de dados, você deve tratar esses dados e apresentar o
[32:44.240 --> 32:51.200]  quê? Apresentar uma solução, uma conclusão com base nos dados que você coletou, certo? Então,
[32:51.200 --> 32:56.560]  é importante que o trabalho vocês tenham esse trabalho, o Cruzão do Curso, que vocês tenham
[32:56.560 --> 33:03.920]  realmente esse contexto científico, certo? Coleta dos dados.
[33:06.080 --> 33:15.120]  Eu não preciso chegar ao resultado final do TCC1 somente no 2, sim, você não precisa, vamos lá.
[33:15.120 --> 33:25.440]  Ali, seria o pré-projeto e o resultado do projeto, sim. Você define o problema, a metodologia e
[33:25.440 --> 33:31.120]  o resultado esperado, e no 2 você vai apresentar todos os resultados e fazer o questionamento,
[33:31.120 --> 33:39.040]  perfeito? Então, TCC1 você já vai apresentar o problema, você já vai ter uma ideia da parte
[33:39.040 --> 33:47.280]  de fundamentação teórica e você já terá uma metodologia para cumprir. No TCC2 você já cumprirá
[33:47.280 --> 33:56.400]  a metodologia e apresentará os resultados, certo? Perfeito, pessoal? Então, vocês já sabem que nessa
[33:56.400 --> 34:08.000]  primeira etapa vocês deverão ter a ideia em mente como que vocês vão atacar e como que vocês vão
[34:08.000 --> 34:15.440]  pegar esses dados para análise, entendeu? Etape número 1. Etape 2, desenvolver, apresentar o
[34:15.440 --> 34:23.280]  resultado, concluir, finalizar e sair para o abraço. E fazer nada, não se esqueça, semana que vem a gente
[34:23.280 --> 34:35.520]  tem aula de nada, certo? Pesquisa bibliográfica, basicamente, você se baseia o quê? Basicamente,
[34:35.520 --> 34:46.640]  você se baseia na bibliografia que ela já existe, certo? Ou seja, livros, catálogos, artigos,
[34:46.640 --> 34:53.120]  data sheet, então, ou seja, você já tem material técnico para você embasar o seu trabalho,
[34:53.120 --> 35:04.960]  isso é o que denominamos de pesquisa bibliográfica, né? Pesquisa experimental é a famosa pesquisa
[35:04.960 --> 35:10.960]  bibliográfica, é quando você faz o quê? Você vai lá, faz o levantamento, né? Você faz o
[35:10.960 --> 35:18.960]  levantamento de campo e tenta reproduzir com base nesses dados, certo? Então, isso aí é o que seria o
[35:18.960 --> 35:24.320]  processo de, o exemplo seria o processo de indução que eu falei para vocês, certo?
[35:24.320 --> 35:39.120]  O que que é a pesquisa ex post facto, ou seja, a partir depois do fato? Essa pesquisa é assim,
[35:39.120 --> 35:47.920]  ela é empírica, certo? Basicamente é assim, você tem uma ação, certo? Você tem uma situação antes,
[35:48.320 --> 35:57.760]  você provoca uma manifestação, você manipula e você faz a verificação após essa manipulação,
[35:57.760 --> 36:06.640]  certo? Ou seja, você relaciona variável antes de você aplicar e após você aplicar, certo? Então,
[36:06.640 --> 36:15.520]  você é o que denominamos de pesquisa ex post facto, ou seja, depois do determinado facto, ou seja,
[36:16.160 --> 36:25.040]  manipulou alguma variável e você quer verificar antes dessa manipulação e após manipulação. Eu
[36:25.040 --> 36:34.720]  vou dar um exemplo, vai. Eu vou falar, eu vou fazer o experimento da lei de homem. Eu vou aplicar,
[36:34.720 --> 36:40.720]  fazer o experimento da lei de homem exatamente a 20 graus Celsius, então ele sempre vai dar lá,
[36:41.040 --> 36:47.280]  ele sempre vai dar lá um valor lá x lá, depende lá, 10 ohms, 15 ohms, 20 ohms, depende do resistor.
[36:47.280 --> 36:57.520]  O que acontece? Eu vou pegar este resistor e eu vou submeter ele a um pico de temperatura e eu
[36:57.520 --> 37:05.440]  vou verificar, vou realizar um novo experimento e verificar que tipo de alteração que ele sofreu
[37:05.680 --> 37:11.840]  e após a alteração da temperatura. Então, antes do fato de aumento da temperatura,
[37:11.840 --> 37:27.600]  depois do fato do aumento da temperatura, certo? A coleta de dados que seria o levantamento de campo,
[37:28.320 --> 37:38.880]  certo? Ou seja, basicamente você vai explorar e descrever, certo? Então, você vai selecionar,
[37:38.880 --> 37:46.960]  vai fazer, selecionar uma amostra e você vai verificar se vai questionar, vai selecionar uma
[37:46.960 --> 37:54.560]  amostra, você vai aplicar, vai aplicar alguma operação, vai registrar, irá registrar esses
[37:54.560 --> 38:02.400]  dados e utilizar o uso de ferramentas estatísticas, certo? Então, o levantamento de campo,
[38:03.520 --> 38:10.560]  você tem a possibilidade que você tenha possibilidade de levantar os dados reais e
[38:10.560 --> 38:17.040]  esses dados reais você consegue que a partir desses dados reais você consegue criar e tentar
[38:17.040 --> 38:28.240]  usar os dados de um modelo, certo? O estudo de caso. Pessoal, este, eu vou até trocar a cor aqui,
[38:28.240 --> 38:43.520]  tá? Este aqui, ele é exatamente o trabalho de vocês, tá? É um estudo aprofundado e exaustivo
[38:43.600 --> 38:54.720]  ou poucos objetos de maneira a permitir o seu conhecimento amplo e detalhado. Ele é adequado
[38:54.720 --> 39:02.640]  para explorar situações da vida real, levantamento de campo, descrever a situação no contexto que
[39:02.640 --> 39:10.480]  está sendo feita determinada investigação e explicar as variáveis causais de determinado
[39:10.560 --> 39:18.000]  situação muito complexa. Então, o estudo de caso é onde você, ele tem um perfil muito mais
[39:18.000 --> 39:25.200]  adequado para o nosso curso, certo? Basicamente, você vai pegar algo que está acontecendo,
[39:25.200 --> 39:31.600]  algo que você quer melhorar e você vai aplicar, vai permitir aplicar o seu conhecimento e vai
[39:31.680 --> 39:37.840]  aplicar a resposta de maneira que de maneira você atingir o seu objetivo, certo?
[39:42.400 --> 39:57.520]  Pesquisa documental. Pesquisa documental, pessoal, é assim, pesquisa bibliográfica já existe alguém
[39:58.320 --> 40:07.120]  realizou esse trabalho de levantamento de campo e buscou material e produziu material acadêmico e
[40:07.120 --> 40:13.840]  tecnológico, certo? A pesquisa documental é quando você vai lá e faz a consulta ao material,
[40:14.640 --> 40:23.440]  como a gente costuma dizer, in natura. Como assim? Eu fui contratado por uma empresa
[40:24.400 --> 40:34.720]  familiar, ponto. Nessa empresa familiar eu preciso verificar como que está a produção, ponto.
[40:34.720 --> 40:46.080]  Eu pergunto para o dono da empresa, onde está a planilha de o que entra no material,
[40:46.800 --> 40:54.400]  que produz, que é desperdiçado? Está ali. Aí eu vou perguntar, ali é onde? Está naquela mesa,
[40:54.400 --> 41:03.360]  na gaveta número um. É um pendrive? Não. É um disquete? Não. É um bolo de papel? Sim, é um bolo
[41:03.360 --> 41:15.440]  de papel de material, ou seja, são impressos, manuscritos, registros audiovisuais, sonores,
[41:15.440 --> 41:23.680]  imagens sem modificações, certo? Então, ou seja, são materiais que eu costumo dizer assim,
[41:23.680 --> 41:33.360]  são materiais que se encontram em natura. E a partir desses materiais eu tenho que construir
[41:33.360 --> 41:44.800]  tudo isso e fazer toda a montagem do meu modelo de interpretação de dados. E assim, não só,
[41:45.040 --> 41:55.920]  de dados, de números, mas você tem lá registros, prontuários, fotografias, obras originais,
[41:56.880 --> 42:03.520]  no caso aí da NR-10, que ela obriga que você tenha lá a ficha da atualização de treinamento,
[42:03.520 --> 42:10.480]  inspeção de todos os equipamentos, é algo que, independente de eletrônico, você deve ter aí a
[42:10.480 --> 42:18.960]  presença do documento impresso, entendeu? Então, é assim, esses tipos de material aqui destacamos
[42:18.960 --> 42:31.120]  como pesquisa documental. Pesquisação. Pesquisação, tipo pesquisa social, com base empírica,
[42:33.040 --> 42:39.760]  que é concebida e realizada em estreita associação com ação e resolução de... Professor, conforme
[42:39.760 --> 42:52.640]  o TCC, o número de páginas é máxima de 15 a 25 páginas pode passar. Então, é assim, conversado
[42:52.640 --> 43:03.760]  com o nosso diretor acadêmico e o coordenador de curso, o TCC de vocês será artigo, ponto,
[43:03.760 --> 43:29.600]  10 a 12 páginas. Então, o TCC de vocês será artigo de 10 a 12 páginas, certo? Sim. E, assim, será artigo de 10 a 12 páginas.
[43:33.760 --> 43:54.000]  Ok. Então, assim, a gente vai trabalhar de 10 a 12 páginas. Por que, pessoal? Porque esse é o formato
[43:54.000 --> 44:07.760]  dos congressos acadêmicos, certo? Então, vocês vão fixe de 10 a 12 páginas. Vamos manter dentro
[44:07.760 --> 44:19.040]  desse, certo? Vamos trabalhar de 10 a 12 páginas. Se vocês quiserem, por exemplo, ele fala de 15 a 25,
[44:20.000 --> 44:28.560]  se vocês quiserem pegar o artigo, se vocês quiserem pegar o artigo e considerar as 12 páginas de
[44:28.560 --> 44:35.360]  elemento textual e as demais páginas como anexo, não tem problema, mas vamos trabalhar, vamos tentar
[44:35.360 --> 44:47.760]  trabalhar dentro das 10 a 12 páginas, certo? Fábio, beleza? Então, pessoal, pesquisação, basicamente,
[44:47.760 --> 44:54.400]  ele está associado, o quê? Ele está associado a um problema coletivo, representação de situação.
[44:54.400 --> 45:03.280]  Então, assim, a pesquisação é muito mais o jeitão de uma pesquisa eleitoral, certo? Então,
[45:03.280 --> 45:09.840]  pesquisação, ele está muito relacionado à pesquisa eleitoral. Olha, antes do debate, fulano tinha
[45:09.840 --> 45:23.920]  10% após o debate, baixou, aumentou seu score, entendeu? E aqui a gente tem um resumo, tá? Uma
[45:23.920 --> 45:31.960]  síntese, esse material já está com falho com o professor, tá? Então, os níveis de pesquisa,
[45:31.960 --> 45:40.520]  explorar, descrever, explicar, o tipo de conhecimento, como, o quê, por quê, os objetivos
[45:40.520 --> 45:55.080]  para cada um, certo? E os tipos de modalidade, explorar, estou de caso, descrever, levantamento,
[45:55.080 --> 46:05.800]  atitudes, cresce, etc. Explicar, experimental é quase experimental, certo? Bom, pessoal,
[46:07.320 --> 46:21.400]  para fecharmos, tarefa de vocês, fale com o professor, nome dos integrantes dos grupos e tema,
[46:22.280 --> 46:30.760]  e aí, a partir desses mensagens, fale conosco, eu vou planilhar tudo, eu vou planilhar e já vou
[46:30.760 --> 46:43.400]  fazer um checklist de todos os temas, tá? Como a própria Aline, ela comentou aqui no início,
[46:43.880 --> 46:52.520]  ela comentou aqui um pouquinho antes do termo da aula, TCC1 é a escolha do tema, a fundamentação
[46:52.520 --> 46:59.800]  teórica e já o método, TCC2, o desenvolvimento, os resultados e a conclusão, certo? Então,
[47:01.000 --> 47:10.760]  fechamos até cinco integrantes, tá? E precisam que me mandem e falem conosco o tema para eu já
[47:10.760 --> 47:20.520]  iniciar a análise. Pessoal, fechado, fechamos.
[47:20.520 --> 47:43.720]  A primeira entrega mantém para o dia 6, 09. Vamos fazer o seguinte,
[47:43.720 --> 47:59.320]  essas entregas, pessoal, essas entregas serão importantes para eu já verificar um jeitão.
[47:59.320 --> 48:06.200]  Eu não vou atribuir nota, mas eu vou querer dar uma olhada para saber se está ok, se não está ok,
[48:06.200 --> 48:13.480]  se a gente pode manter, se manter até o final do semestre, se a gente faz uma modificação
[48:13.480 --> 48:19.400]  do meio do caminho, certo? Então, uma primeira entrega, bom considerada como obrigatória,
[48:19.400 --> 48:24.680]  mas importante para eu fazer a verificação, mas antes da primeira entrega, eu preciso dos nomes,
[48:24.680 --> 48:34.040]  dos integrantes, eu preciso do tema para eu checar, certo? Você vai escolher, você vai escolher o
[48:34.040 --> 48:42.200]  tema? Não, Carleno, quem vai escolher o tema é você. Quem vai escolher o tema é você, lembre-se que
[48:42.200 --> 48:53.320]  o tema é focado na área de Engenharia Elétrica, beleza? Pessoal, obrigado pela presença de vocês,
[48:53.320 --> 49:06.080]  bom início de semana para todos, continuação do projeto integrador. O Hélio, depende da intensidade
[49:06.080 --> 49:12.720]  de pesquisa no projeto, entendeu? Lembre-se que o TCC não é um projeto, ele é um nível mais
[49:12.720 --> 49:19.760]  aprofundado, certo? Vocês não vão querer manter a linha de projeto, vocês precisam subir um pouco a
[49:19.760 --> 49:31.600]  régua na elaboração do trabalho e conclusão do curso. Bele? Pessoal, obrigado, um abraço a todos,
[49:31.600 --> 49:35.600]  até a próxima semana. Wendell, obrigado, Wendell."""
display_parts(texto_original)
