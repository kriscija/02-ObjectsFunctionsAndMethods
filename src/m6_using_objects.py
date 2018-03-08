"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joe Krisciunas.
"""  # Done

import rosegraphics as rg


def main():
    two_circles()
    circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. 
    """
    # Test your functions by putting calls to them here:


def two_circles():

    point1 = rg.Point(75, 75)
    point2 = rg.Point(125, 125)
    window = rg.RoseWindow()
    circle1 = rg.Circle(point1, 25)
    circle1.fill_color = 'green'

    circle2 = rg.Circle(point2,50)

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    point1 = rg.Point(75, 75)
    point2 = rg.Point(125, 125)
    window = rg.RoseWindow()
    circle1 = rg.Circle(point1, 25)
    circle1.fill_color = 'blue'

    rectangle = rg.Circle(point2, 50)

    circle1.attach_to(window)
    rectangle.attach_to(window)

    print(circle1.outline_thickness)
    print(circle1.fill_color)
    print(circle1.center)
    print(point1.x)
    print(point1.y)

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.center)
    print(point2.x)
    print(point2.y)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    point1 = rg.Point(75, 75)
    point2 = rg.Point(125, 125)
    point3 = rg.Point(200, 200)
    window = rg.RoseWindow()
    line1 = rg.Line(point2, point3)
    line2 = rg.Line(point1, point2)
    line1.thickness = 10
    line1.get_midpoint()
    print(line1.get_midpoint())
    midpoint1 = line1.get_midpoint()
    print(midpoint1.x)
    print(midpoint1.y)

    print(line2.get_midpoint())
    midpoint2 = line2.get_midpoint()
    print(midpoint2.x)
    print(midpoint2.y)
    window.render()
    window.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
