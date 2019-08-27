# Assigning values to variables
mv_population, mv_size = 74728, 11.995
mv_density = mv_population / mv_size
print(mv_density)

# Assignment operators
mv_population += 4000 - 600
mv_density = mv_population / mv_size
print(mv_density)

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------


# Data types
print(type(4))
print(type(4.0))
print(int(49.7))  # Converts to integer
print(float(2 + 1))  # Converts to float

# Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them
# together we can see the difference between the mathematically correct answer and the one that Python creates.

print(.1 + .1 + .1 == .3)  # This is false due to the approximation that Python applies


