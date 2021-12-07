fish = [4,5,3,2,3,3,2,4,2,1,2,4,5,2,2,2,4,1,1,1,5,1,1,2,5,2,1,1,4,4,5,5,1,2,1,1,5,3,5,2,4,3,2,4,5,3,2,1,4,1,3,1,2,4,1,1,4,1,4,2,5,1,4,3,5,2,4,5,4,2,2,5,1,1,2,4,1,4,4,1,1,3,1,2,3,2,5,5,1,1,5,2,4,2,2,4,1,1,1,4,2,2,3,1,2,4,5,4,5,4,2,3,1,4,1,3,1,2,3,3,2,4,3,3,3,1,4,2,3,4,2,1,5,4,2,4,4,3,2,1,5,3,1,4,1,1,5,4,2,4,2,2,4,4,4,1,4,2,4,1,1,3,5,1,5,5,1,3,2,2,3,5,3,1,1,4,4,1,3,3,3,5,1,1,2,5,5,5,2,4,1,5,1,2,1,1,1,4,3,1,5,2,3,1,3,1,4,1,3,5,4,5,1,3,4,2,1,5,1,3,4,5,5,2,1,2,1,1,1,4,3,1,4,2,3,1,3,5,1,4,5,3,1,3,3,2,2,1,5,5,4,3,2,1,5,1,3,1,3,5,1,1,2,1,1,1,5,2,1,1,3,2,1,5,5,5,1,1,5,1,4,1,5,4,2,4,5,2,4,3,2,5,4,1,1,2,4,3,2,1]
# fish = [3,4,3,1,2]

### The original idea was to use a dictionary to figure out how many babies are born over a certain number of days to
### a certain age fish, but the nested loops were computationally inefficient

# fish_sim = {
#     1:0,
#     2:0,
#     3:0,
#     4:0,
#     5:0,
# }

# for key in fish_sim.keys():
#     print(key)
#     fish_life = [key]
#     for i in range(256):
#         for j in range(len(fish_life)):
#             if fish_life[j] == 0:
#                 fish_life.append(9)
#                 fish_life[j] = 7
#         fish_life = [age - 1 for age in fish_life]
#     # fish_sim[key] = len(fish_life)
#     fish_sim[key] = fish_life

# print(fish_sim)

# fish_final = sum([fish_sim[i] for i in fish])          
# print(fish_final)

### Track the number of fish of each age and just update off that

fish_count = {}
for i in set(fish):
    fish_count[i] = fish.count(i)
    
for i in range(256):
    fish_copy = {k: 0 for k in range(9)}
    for key in fish_count.keys():
        if key == 0:
            fish_copy[8] += fish_count[key]
            fish_copy[6] += fish_count[key]
        else:
            fish_copy[key-1] += fish_count[key]
    fish_count = fish_copy.copy()
print(sum(fish_count.values()))
            

