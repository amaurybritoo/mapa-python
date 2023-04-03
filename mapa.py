import folium

#crinado o mapa #
mapa = folium.Map(
    location=[-3.082112977195062, -60.023032565518854],
    tiles='open-street-map',  # estilo do mapa
    zoom_start=16
)

#adicionando o marcador no mapa #
folium.Marker(
    [-3.082112977195062, -60.023032565518854],
    popup='<i> </i>',
    tooltip='Clique Aqui'
).add_to(mapa)

#salvando HTML do mapa #
mapa.save(r'.\mapa.html')
