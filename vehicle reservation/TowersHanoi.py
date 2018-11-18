# Towers of Hanoi Program

from turtle import *
import time


def getNumDisks():
    """Returns number of disks requested by user."""

    num_disks = int(input('Enter the number of disks(2-8): '))

    while num_disks < 2 or num_disks > 8:
        print ('Must select between 2 and 8 disks')
        num_disks = int(input('Enter the number of disks (2-8): '))
        
    return num_disks


def displayPegs(peg_locs):
    """Displays peg images at peg_locs."""
    
    # retrieve and register peg image
    peg_image = 'Peg.gif'
    register_shape(peg_image)

    # set vertical offset
    offset = 65

    # create temp peg-shaped turtle
    temp = Turtle()
    temp.penup()
    temp.shape(peg_image)
    
    # stamp three images of peg-shaped turtle
    for loc in peg_locs:
        temp.setposition(loc[0], loc[1] + offset)
        temp.stamp()
    

def getDiskImages(num):
    """Returns a list of disk image file names for num requested.

       Disk images in order from largest to smallest image.
    """

    # init empty images list
    images = []

    # init first image file name
    disk_image = 'Disk-1.gif'
    
    # create all disk images
    for k in range(0,num):
        images = ['Disk-' + str(k+1) + '.gif'] + images

    return images


def registerDiskImages(images):
    """Registers disk image file names provided in images."""

    for image in images:
        register_shape(image)


def newPeg(image_file):
    """Returns a new turtle with peg shape in image_file."""

    peg = Turtle()
    peg.hideturtle()
    peg.shape(image_file)
    
    return peg


def newDisk(image_file):
    """Returns a new turtle with disk shape in image_file."""

    disk = Turtle()
    disk.penup()
    disk.hideturtle()
    disk.shape(image_file)
    
    return disk


def createDisks(images):
    """Returns a list of disk shape turtles for each image in images.

       Disks ordered by image size from largest to smallest.
    """

    # init empty list of disks for all three pegs
    disks = [[], [], []]

    # create disks with all disks on first peg
    for k in range(0, len(images)):
        
        disks[0].append(newDisk(images[k]))
        disks[1].append(None)
        disks[2].append(None)

    return disks
    

def calcDiskLocations(num_disks, peg_locs, separation):
    """Returns the calculated locations of all disks for all three pegs.

       Locations in order from largest (bottom) disk to smallest, with
       decreasing separation for smaller disks.
    """

    # init
    saved_separation = separation
    all_disk_locations = []
    
    # caculate locations of disks for all three pegs
    for peg in range(0, 3):
        
        disk_locs = []

        for k in range(0, num_disks):
            
            xloc = peg_locs[peg][0]
            yloc = int(peg_locs[peg][1] + k * separation)

            disk_locs.append((xloc, yloc))
            separation = separation * 0.95

        all_disk_locations.append(disk_locs)
        separation = saved_separation
        
    return all_disk_locations


def placeDisksOnStartPeg(start_peg, disks, locations):
    """Places and displays all disks on start peg in turtle graphics."""

    for k in (range(0, len(disks[start_peg]))):
        disks[start_peg][k].setposition(locations[start_peg][k])


def makeDisksVisible(start_peg, disks):
    """Makes visible all disk-shaped turtles on start_peg."""

    for k in range(0,len(disks[start_peg])):
        disks[start_peg][k].showturtle()


def removeTopDisk(peg, disks):
    """Returns the top disk of disks currently on peg."""
    
    # init k to top-most position of disks on peg
    k = len(disks[peg]) - 1
    found = False
    
    # find top-most position with disk in place
    while k >= 0 and not found:
        
        if disks[peg][k] != None:
             disk = disks[peg][k]
             disks[peg][k] = None
             found = True
        else:
            k = k - 1
            
    return disk
        

def placeTopDisk(disk, peg, disks, disk_locations):
    """Places disk on top of disks currently on peg."""

    # init k to bottom-most position of disks on peg
    k = 0
    found = False
    
    # assign disk to bottom-most position of peg with no disk
    while k < len(disk_locations[peg]) and not found:

        if disks[peg][k] == None:
            
            disks[peg][k] = disk
            found = True
        else:
            k = k + 1
             
    return disk


def getNextAvailDiskLoc(peg, disks, disk_locations):
    """Returns location for next disk on peg."""

    # init k to bottom-most position of disks on peg
    k = 0
    found = False
    
    # get bottom-most location of peg with no disk
    while k < len(disks[peg]) and not found:
        
        if disks[peg][k] == None:
            loc = disk_locations[peg][k]
            found = True
        else:
            k = k + 1
            
    return loc
       

def moveDisk(from_peg, to_peg, disks, disk_locations):
    """Moves disk on top of from_peg to top of to_peg."""
    
    # get disk on top of from_peg
    disk = removeTopDisk(from_peg, disks)

    # get available loc for new disk on to_peg
    new_loc = getNextAvailDiskLoc(to_peg, disks, disk_locations)

    # move disk image
    disk.goto(new_loc)

    # add disk to to_peg list of disks
    placeTopDisk(disk, to_peg, disks, disk_locations)
   
    
def towers(start_peg, dest_peg, spare_peg, num_disks, disks, disk_locations):
    """Begins the problem solving process."""
        
    if num_disks == 1:
        moveDisk(start_peg, dest_peg, disks, disk_locations)
        time.sleep(.5)
        
    else:
        towers(start_peg, spare_peg, dest_peg, num_disks - 1,
               disks, disk_locations)
        
        moveDisk(start_peg, dest_peg, disks, disk_locations)
        towers(spare_peg, dest_peg, start_peg, num_disks - 1,
               disks, disk_locations)
   
# ---- main

# program welcome
print('This program solves the Towers of Hanoi for up to eight disks')

# init turtle screen
setup(800, 600)

# init display parameters
peg_locations = ((-150, -50), (0,-50), (150,-50))
disk_separation = 24

# initpeg numbers
peg_A = 0
peg_B = 1
peg_C = 2

# get number of disks
num_disks = getNumDisks()
print()

# display pegs
displayPegs(peg_locations)

# create and register disk images
disk_images = getDiskImages(num_disks)
registerDiskImages(disk_images)

# calc locations for all disks
disk_locs = calcDiskLocations(num_disks, peg_locations, disk_separation)

# create and position number of disks requested
disks = createDisks(disk_images)

# place all disks on start peg
placeDisksOnStartPeg(peg_A, disks, disk_locs)

# make all disks visible    
makeDisksVisible(peg_A, disks)

# delay
time.sleep(2)
               
# start movement of disks
towers(peg_A, peg_C, peg_B, num_disks, disks, disk_locs)

# exit turtle screen
print('\nDone - Click screen to quit')
exitonclick()
            
