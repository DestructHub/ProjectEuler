-- Author: G4BB3R
-- 1386, arrumar D:

local num_str = string.format("%.0f", tostring(math.pow(2, 1000)))
local sum = 0
for i = 1, num_str:len() do
	local x = tonumber(string.sub(num_str, i, i))
	sum = sum + x
end
print(sum)