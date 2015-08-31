-- Author: G4BB3R

local function isPalindrome (x)
	return tonumber(string.reverse(x)) == x
end

local largest = 0
for a = 1, 999 do
	for b = 1, 999 do
		if a * b > largest and isPalindrome(a * b) then
			largest = a * b
		end
	end
end

print(largest)