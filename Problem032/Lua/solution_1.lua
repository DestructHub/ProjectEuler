table.find = function (xs, x)
	for _, v in pairs(xs) do
		if x == v then
			return true
		end
	end
	return false
end

local function sort (str)
	local xs = {}
	str:gsub(".",function (c) table.insert(xs, c) end)
	table.sort(xs)
	return table.concat(xs, "")
end

local function get_pandigal_products_sum ()
	local sum = 0
	local xs  = {}
	for x = 1, 9999 do
		for y = 1, 99 do
			local xy = x * y
			if sort(x .. y .. xy) == "123456789" then
				if not table.find(xs, xy) then
					sum = sum + xy
					table.insert(xs, xy)
				end
			end
		end
	end
	return sum
end

print(get_pandigal_products_sum())
