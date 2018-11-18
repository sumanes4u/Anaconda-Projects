# Kitchen Tile Visualization Program

import turtle

def greeting():

    ''' Displays the program greeting on the screen.'''

    print('This program will display the tile pattern for a selected')
    print('pair of tile colors, tile size, and grout color.\n')
    print('The repeat frequency for the secondary tile color can be selected:')
    print('if skip = 1, secondary tile color placed every other tile,')
    print('if skip = 2, secondary tile color placed every third tile, etc.\n')

def getTileSelections(grout_color_options):

    ''' Returns dictionary of the form,

        {'tile_size':dict, 'color1':str, 'color2':str, 'skip':int, 'grout':str}
        
        where the value of tile_size is a dictionary of the form
        {'tile_length': value, 'tile_width': value},

        color1 and color2 are the selected primary and secondary color code
        strings in hexadecimal format, skip is an integer indicating the
        number of primary colors that occur for every secondary color, and
        grout contains the selected grout color.
    '''

    # init
    empty_set = set()
    hex_digits = {'0','1','2','3','4','5','6','7','8','9',
                  'A','B','C','D','E','F','a','b','c','d','e','f'}

    # prompt user for tile size (length and width)
    tile_length = int(input('Enter tile length (1-4 inches): '))
    while tile_length <1 or tile_length > 4:
        tile_length = int(input('INVALID SIZE SELECTED - please re-enter: \n'))

    tile_width = int(input('Enter tile width (1-4 inches): '))
    while tile_width < 1 or tile_width > 4:
        tile_width = int(input('INVALID SIZE SELECTED - please re-enter: \n'))
    
    # prompt user for primary tile color
    color1 = input('Enter primary tile color (6-digit RGB): ')
    while (len(color1) != 6) or \
          (set(color1) - hex_digits != empty_set):
        color1 = input('INVALID RGB color, please re-enter: ')

    # prompt user for secondary tile color
    color2 = input('Enter secondary tile color (6-digit RGB): ')
    while (len(color2) != 6) or \
          (set(color2) - hex_digits != empty_set):
        color2 = input('INVALID RGB color, please re-enter: ')

    # prompt user for skip pattern for colors
    skip = int(input('Enter frequency of secondary tile color (1-10): '))
    while (skip < 1 or skip > 10):
        skip = int(input('INVALID - Please enter 1,2,3,etc. '))
        
    # prompt user for grout color
    grout = input('Enter grout color (white, gray, brown or black): ')
    while (grout not in grout_color_options):
        grout = input('INVALID grout color selection, please re-enter: ')

    # prepend hash sign to indicate RGB string
    color1 = '#' + color1
    color2 = '#' + color2

    # create dictionary of selections
    selections = {'tile_size':{'length':tile_length, 'width':tile_width},
                  'primary_color':color1, 'secondary_color':color2, 
                  'tile_skip':skip, 'grout_color':grout}
    
    return selections

def layoutTiles(window, selections, tile_area, scaling):

    ''' Displays the tiles in the window starting with the top and working
        towards the bottom of the window. This function requires that the
        coordinate (0,0) be set as the top corner of the window.
    '''

    # set background color (as grout color)
    window.bgcolor(selections['grout_color'])

    # get selected tile size
    tile_size = selections['tile_size']

    # get turtle
    the_turtle = turtle.getturtle()

    # scale size of tiles for display
    scaled_length = scaling * tile_size['length']
    scaled_width = scaling * tile_size['width']

    # scale grout spacing 
    tile_spacing =  6

    # create tile shape
    turtle.register_shape('tileshape', 
                          ((0,0), (0, scaled_length),
                           (scaled_width, scaled_length), (scaled_width, 0)))

    # set turtle attributes
    the_turtle.setheading(0)
    the_turtle.shape('tileshape')
    the_turtle.hideturtle()
    the_turtle.penup()

    # place first tile at upper left corner
    loc_first_tile = (-10, tile_area['height'] + 10)
    the_turtle.setposition(loc_first_tile)

    # init first tile color and counters
    first_tile_color = 'primary_color'
    skip_counter = selections['tile_skip']
    row_counter = 1

    terminate_layout = False
    while not terminate_layout:
        
        # check if current row of tiles before right edge of window
        if the_turtle.xcor()< tile_area['width']:
            
            # check if need to switch to secondary tile color
            if skip_counter == 0:
                the_turtle.color(selections['secondary_color'])
                skip_counter = selections['tile_skip']
            else:
                the_turtle.color(selections['primary_color'])
                skip_counter = skip_counter - 1

            # place current tile color at current turtle location
            the_turtle.stamp()

            # move turtle to next tile location of current row
            the_turtle.forward(scaled_length + tile_spacing)

        # check if current row of tiles at bottom edge of window
        elif the_turtle.ycor() > 0:
            
            the_turtle.setposition(loc_first_tile[0],
                                   loc_first_tile[1]- row_counter *
                                   scaled_width - row_counter * tile_spacing)
            
            row_counter = row_counter + 1
        else:
            terminate_layout = True

# ---- main

# init
tile_area = {'width': 660, 'height': 440}
grout_color_selection = {'white', 'gray', 'brown', 'black'}
scaling = 20

# program greeting
greeting()

# get tile selection and layout details
selections = getTileSelections(grout_color_selection)

# set window size
turtle.setup(tile_area['width'], tile_area['height'])

# get reference to turtle window
window = turtle.Screen()

# set window title
window.title('Kitchen Tile Visualization Program')

# set coordinate system
window.setworldcoordinates(0, 0, tile_area['width'], tile_area['height'])
window.mode('world')

# layout tiles in window
layoutTiles(window, selections, tile_area, scaling)

# terminate program when window closed
turtle.exitonclick()

