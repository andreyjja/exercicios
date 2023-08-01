function exerc_array()
    a = {1, 4, 9, 16, 25, 36, 49, 64, 81}
    for i=1, 10 do
        b = a[i]
        a[i] = 0
        print("Index: [", i,"] -> Antes: ", b, " - Depois:", a[i])
    end
end

function exerc_contador()
    a = 0
    for i=1, 10 do
        print("i:", i,"now(a):", a, "depois:", a + i)
        a = a + i
    end

    print("Resultado Final do A: ", a)
end

--exerc_array()
--exerc_contador()
--                          parte 1 livro
-- string é quando tem um texto = print("me mata")
--number é quando tem um valor um numero 
--boolean é quando é false ou true
-- nill é quando não tem valor
-- local é literalmente local para não criar uma global para o script todo
-- print ("Hello World")

function fact (n) -- faz o calcular o fatorial do numero que colocar

    if n == 0 then
      return 1
    else
      return n * fact(n-1)
    end
  end

 -- print("enter a number:") <-- como isso funciona como ele sabe registra o numero que eu cloquei
 -- a = io.read("*number")         
 -- print(fact( a ))


--dofile("teste.lua") ta fala que carrega sua biblioteca mais como assim 

--print(seila) <-- vai dar nill porque não vai ter nenhum valor antes
--seila = 1 -- uma variavel 
--print(seila) <-- vai ter valor 1 por ter sido criado antes


