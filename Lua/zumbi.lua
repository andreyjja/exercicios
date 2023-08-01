local inimigo = require("entidade/inimigo")
local player = require("entidade/player")
local zumbi = {}

function zumbi.novo()
    local instancia = inimigo.novo(50, zumbi)
    instancia.comer_celebro = true
    instancia.explodir = false

    function instancia:atacar(player_instancia )
        
        if self == nil then
            print("esse zumbi esta morto")
        elseif self.explodir then
            print("zumbi explodiu D:")
            player_instancia:matar ()
            return nil
        else
            print("zumbi deu uma mordida " .. player_instancia.nome .. (" !"))
            player_instancia:atacado(self.forca)
            return instancia
        end
    end
    return instancia
end
    function zumbi.novo_bomb()
    local zumbi = zumbi.novo()
    zumbi.comer_celebro = false
    zumbi.explodir = true
    return zumbi
end


return zumbi