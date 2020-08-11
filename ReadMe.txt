Arquivo criado no curso de OO

Exemplo de comandos para ser utilizados para ver o funcionamento da classe


vingadores = Filme("Vingadores",2018,160)
TDEM = Filme("Todo mundo em panico",2020,120)
VF = Filme("Velozes e furioso",2016,120)

atlanta = Serie("Atlanta",2018,2)
demolidor = Serie("demolidor",2018,5)

atlanta.dar_like()
VF.dar_like()
vingadores.dar_like()
TDEM.dar_like()
vingadores.dar_like()
TDEM.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores,atlanta, demolidor, TDEM]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist:{len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)