-- Author: G4BB3R

-- Fibonacci function with memoization
local fib_cache = {}
local function fib (n)
	if fib_cache[n] then
		return fib_cache[n]
	elseif n <= 1 then
		return n
	end
	local result = fib (n - 1) + fib (n - 2)
	fib_cache[n] = result
	return result
end

local resultado = 0
for i = 1, 1000 do
	local fib_value = fib(i)
	if fib_value > 4000000 then
		break
	elseif fib_value % 2 == 0 then
		resultado = resultado + fib_value
	end
end

print(resultado)