local player = {}

function player.novo(nome)
    
    local instancia =  {
        vida = 200,
        pocoes = {},
        nome = nome
    }

    function instancia:obter_pocao(pocao)
        table.insert(self.pocoes, pocao)
    end
    
    function instancia:atacado (forca)
        if self:vivo()  then
            self.vida = self.vida - forca
            if not self:vivo() then
                print("apos a mordida, " .. self.nome .. " morreu" )
            else
                print("apos a mordida, " .. self.nome .. " agora tem " .. self.vida .. " vida" )
            
            end
        else
            print (self.nome .. " ja morreu :(")
        end
    end
    function instancia:matar ( )
        if self:vivo() then
            self.vida = 0
        print(self.nome .. " morreu :c")
        else
            print (self.nome .. " ja morreu :(")
    end
end
    
    function instancia:vivo() 
        return self.vida > 0 
    end
    
    function instancia:usarpocao ()
        if #self.pocoes > 0 then
            self.vida = self.vida + self.pocoes[1].vida
            table.remove( self.pocoes, 1)
            print(self.nome .. " uso uma pocao e agora tem " .. self.vida .. " De Vida!!")    
        else
            print(self.nome .. " n tenho pocao")    
        end
    end
    return instancia
end


return player
