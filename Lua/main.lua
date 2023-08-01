

local player = require("entidade/player") 
local pocao = require("entidade/pocao")
local zumbi = require("entidade/zumbi")
-- instancias das classes criadas
-- objetos
local player1 = player.novo("Victor")
local player2 = player.novo("Leo")

local zumbi1 = zumbi.novo()
local zumbi2 = zumbi.novo()
local zumbi3 = zumbi.novo_bomb()

--inventario
player1:obter_pocao(pocao.novo())
player2:obter_pocao(pocao.novo())

assert(#player1.pocoes == 1)
assert(#player2.pocoes == 1)

-- zumbi atacam os players
zumbi1:atacar(player1 )
zumbi1:atacar(player1 )
player1:usarpocao ()
zumbi1:atacar(player1 )
zumbi1:atacar(player1 )
player1:usarpocao ()
zumbi1:atacar(player1 )
zumbi1:atacar(player1 )

zumbi3:atacar(player2 )
