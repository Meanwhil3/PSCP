"""ChristmasTree"""

def main(layer, tree):
    """ChristmasTree"""
    glass = (layer*2)-1
    glass_per_layer = 1
    for _ in range(layer):
        print((("*"*glass_per_layer).center(glass)))
        glass_per_layer += 2
    for _ in range(tree):
        print((("-"*3).center(glass)))
main(int(input()), int(input()))
