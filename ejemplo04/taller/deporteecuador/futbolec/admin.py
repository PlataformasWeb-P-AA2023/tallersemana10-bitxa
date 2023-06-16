from django.contrib import admin
from futbolec.models import Equipo, Jugador, Campeonato, CampeonatoEquipos

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas',  'twitter_username')
    search_fields = ('nombre', 'siglas', 'twitter_username')

admin.site.register(Equipo, EquipoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'posicion_campo', 'equipo')

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato', 'nombre_auspiciante')

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display = ('year', 'equipo', 'campeonato')
    search_fields = ('year', 'equipo', 'campeonato')

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
