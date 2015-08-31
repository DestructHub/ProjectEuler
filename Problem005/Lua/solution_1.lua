-- Author: G4BB3R
-- Used python solution XD

local i = 1
for k = 1, 20 do
	if i % k > 0 then
		for j = 1, 20 do
			if (i * j) % k == 0 then
				i = i * j
				break
			end
		end
	end
end
print(i)