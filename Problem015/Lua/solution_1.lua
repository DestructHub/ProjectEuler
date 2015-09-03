-- Author: G4BB3R

local function fat (n)
	return n <= 1 and 1 or n * fat(n - 1)
end

print(fat(40) / fat(20) ^ 2)