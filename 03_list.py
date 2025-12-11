
nums = [1,2,3,4]
nums.append(5)

print(nums)

nums.insert(1, 10)
print(nums)

nums.extend([20,30, 40])
print(nums)

nums.remove(20)

print(nums)

r1 = nums.pop()

del nums[1]

print(nums)

nums.clear()

print(nums)

nums.extend([30, 20, 30, 10, 20, 100, 20])
print(nums)

print(nums.index(20))

print(nums.count(30))

print(nums[len(nums) - 1])

square = [x*x for x in range(6)]
print(square)