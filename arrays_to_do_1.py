import random

#in JavaScript, the Array object has numerous useful methods.
#It does not, however, contain a method that will randomize the order of an array’s elements.
# Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally.
# Do you need to return anything from your function?


def shuffle(arr):
    for i in range(len(arr)):
        rand_index=random.randint(0,len(arr)-1)
        temp=arr[i]
        arr[i]=arr[rand_index]
        arr[rand_index]=temp
    return arr

print(shuffle([1,2,3,4,5,6]))

# Lovely Burbank has a breathtaking view of the Los Angeles skyline.
# Let’s say you are given an array with heights of consecutive buildings,
# starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level,
# behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level.
# Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4].
# As always with challenges, do not use built-in array functions such as unshift().

def skyline_heights(building_heights):
    max_building_height=0
    visible_buildings=[]
    for building_height in building_heights:
        if building_height>max_building_height:
            visible_buildings.append(building_height)
            max_building_height=building_height
    return visible_buildings

print(skyline_heights([1,3,1,3,5]))

# Create a standalone function that accepts two arrays and combines their values sequentially into a new array.
# Extra values from either array should be included afterward.
# Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].

def zip_it(arr1, arr2):
    arr_for_range= arr1 if len(arr1)> len(arr2) else arr2
    new_arr=[]
    for i in range(len(arr_for_range)):
        if i <= (len(arr1))-1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr

print(zip_it([4,15,100],[10,20,30,40]) )