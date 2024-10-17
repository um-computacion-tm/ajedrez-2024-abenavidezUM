## AJEDREZ   
###### Agustin Benavidez
------------
### CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-abenavidezUM/tree/dev.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-abenavidezUM/tree/dev)

### Maintenability
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-abenavidezUM/maintainability"><img src="https://api.codeclimate.com/v1/badges/628e0630c53cad57ef7a/maintainability" /></a>

### Test Coverage
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-abenavidezUM/test_coverage"><img src="https://api.codeclimate.com/v1/badges/628e0630c53cad57ef7a/test_coverage" /></a>

-------------
## Instalacion del Juego

1) ### Instalar Docker  
```bash
    $ sudo apt install docker
```
2) ### Crear la imagen de Docker con el juego: 
```bash
    $ sudo docker build -t ajedrez-2024-abenavidezum . --no-cache
```
3. ### Correr los test 
```bash
    $ sudo docker run --rm ajedrez-2024-abenavidezum
```
-------------
## Juego
El juego sigue las reglas del ajedrez tradicional que se encuentran aqui:
https://es.wikipedia.org/wiki/Leyes_del_ajedrez

Excepciones: No estan implementadas las condiciones de jaque mate, jaque, ni movimientos especiales.
## Modo de Juego
En la terminal vera reflejado  `1.Move piece`, `2.Draw` y `3.Resign`.
    1- `Move piece`: 
    Con esta primera opcion es con la que se mueven las fichas del tablero. Primero se coloca la posicion inicial y a continuacion la posicion de destino, por ejemplo:
        WHITE TO MOVE (♙)
        Moviendo ♙ de E2 a E4

            A  B  C  D  E  F  G  H
           ------------------------
        8 | ♜  ♞  ♝  ♛  ♚  ♝  ♞  ♜ | 8
        7 | ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟ | 7
        6 | .  .  .  .  .  .  .  . | 6
        5 | .  .  .  .  .  .  .  . | 5
        4 | .  .  .  .  ♙  .  .  . | 4
        3 | .  .  .  .  .  .  .  . | 3
        2 | ♙  ♙  ♙  ♙  .  ♙  ♙  ♙ | 2
        1 | ♖  ♘  ♗  ♕  ♔  ♗  ♘  ♖ | 1
           ------------------------
            A  B  C  D  E  F  G  H

2- `Draw`: Con esta opcion se puede proponer un empate al oponente.

3- `Finish`: Permite terminar el juego.

## Finalizar el Juego
El juego termina cuando alguno de los dos jugadores se queda sin piezas.