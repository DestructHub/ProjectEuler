-- Author: G4BB3R

local function isPrime (n)
	if n < 2 then
		return false
	elseif n == 2 or n == 3 then
		return true
	else
		for i = 2, n - 1 do
			if n % i == 0 then
				return false
			end
		end
		return true
	end
end

local n     = 0
local prime = nil
for i = 1, 9999999999 do
	if isPrime(i) then
		n = n + 1
	end
	if n == 10001 then
		prime = i
		break
	end
end

print(prime)