-- Author: G4BB3R

local resultado = 0
for i = 1, 999 do
	if i % 5 == 0 or i % 3 == 0 then
		resultado = resultado + i
	end
end
print(resultado)