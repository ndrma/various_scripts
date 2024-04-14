When you run this script it will ask for

1. screenshot number
2. columns number

it will then take the amount of screenshots in the vertical moving from the center of the bbox (you can change that as well as the borders, see the commented code) and click hold and drag all the way until it runs out of scrolling to do, or out of screenshots to take.
Then it will make the same steps downward so that you have a similar starting point for the second column, where it will do this process again, etc until all the screenshots are done.

This is a very "manual" script, you won't be able to run it headless but it will cover quite some ground. I suggest adding some overlap in the horizontal movement.

At the end it runs ImageMagick to create a collage of the screenshots per column, so you end up with vertical slices.
