from ics_image import *
from random import *

def nicer_grey(image_name):
    '''
    nicer_grey(str)--> none
    
    '''
    load_image(image_name)
    all_pix = get_all_pixels()
    
    for row in range(0, get_height()):
        for col in range(0, get_width()):
            pix = all_pix[row][col]
            grey_cal = round((pix[0]*0.213 + pix[1]*0.715 + pix[2]*0.072))
            grey = [grey_cal, grey_cal, grey_cal]
            set_pixel(col, row, grey)
    save_image("{}_grey{}".format(image_name[0:image_name.find(".")],image_name[image_name.find("."):]))
    
    
def rgb_adjust(image_name, colour):
    load_image(image_name)
    
    for row in range(0, get_height()):
        for col in range(0, get_width()):
            pix = get_pixel(col, row)
            for i in range(0,3):
                pix[i] = max(0, min(255, pix[i] + colour[i]))
            set_pixel(col,row,pix)
            
    save_image("{}_adjusted{}".format(image_name[0:image_name.find(".")],image_name[image_name.find("."):]))


def triangles(width,height,num_t,b_col):
    new_image(width, height)
    all_pix = get_all_pixels()

    for row in range(0, height):
        for col in range(0, width):
            set_pixel(col, row, b_col)    

    for i in range(num_t):
        coord = [randint(2,width-3),randint(1,height-2)]
        flip = randint(0,2)
        if not flip == 0:
            num = 1
        else:
            num = -1
        tri_order = [[coord[0],coord[1]+(-1*num)],[coord[0]-1,coord[1]],[coord[0],coord[1]],[coord[0]+1,coord[1]],[coord[0]-2,coord[1]+(1*num)],[coord[0]-1,coord[1]+(1*num)],[coord[0],coord[1]+(1*num)],[coord[0]+1,coord[1]+(1*num)],[coord[0]+2,coord[1]+(1*num)]]     
        for i in range(9):
            if i in [0,2,5,6,7]:
                set_pixel(tri_order[i][0],tri_order[i][1],[0,0,0])
            else:
                set_pixel(tri_order[i][0],tri_order[i][1],[b_col[0]/2,b_col[1]/2,b_col[2]/2])

    save_image("triangles_{}.bmp".format(num_t))


def crop(image_name,crop_a1,crop_a2):
    load_image(image_name)
    all_pix = get_all_pixels()
    x_xn = [min(get_width(),max(crop_a1[0],crop_a2[0])+1),max(0,min(crop_a1[0],crop_a2[0]))]
    y_xn = [min(get_height(),max(crop_a1[1],crop_a2[1])+1),max(0,min(crop_a1[1],crop_a2[1]))]
    new_image(x_xn[0]-x_xn[1],y_xn[0]-y_xn[1])
    for row in range(0, y_xn[0]-y_xn[1]):
        for col in range(0, x_xn[0]-x_xn[1]):
                set_pixel(col,row, all_pix[y_xn[1]+row][x_xn[1]+col])
    save_image("{}_crop{}".format(image_name[0:image_name.find(".")],image_name[image_name.find("."):]))
    

def show_alike(img1, img2, per):
    load_image(img1)
    all_pix1 = get_all_pixels()    
    load_image(img2)
    all_pix2 = get_all_pixels()
    new_image(min(len(all_pix1[0]),len(all_pix2[0])), min(len(all_pix1),len(all_pix2)))
    
    for row in range(0, get_height()):
        for col in range(0, get_width()):
            pix1 = all_pix1[row][col]
            pix2 = all_pix2[row][col]
            if ((pix2[0] - pix1[0])**2 + (pix2[1] - pix1[1])**2 + (pix2[2] - pix1[2])**2)**0.5 < ((255**2)*3)**0.5 * per:
                avg_pix = [(pix1[0]+pix2[0])//2, (pix1[1]+pix2[1])//2, (pix1[2]+pix2[2])//2]
                set_pixel(col, row, avg_pix)
    show_image()
    save_image("{}_{}.bmp".format(img1[0:img1.find(".")],img2[0:img2.find(".")]))


def encoder(e_str, image_name):
    load_image(image_name)
    e_str += '$'
    alnum_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7','8','9','0','$','.',',','#',"'"]
    l_count = 0
    
    for row in range(0, get_height()):
        for col in range(0, get_width()):
            pix = get_pixel(col, row)
            #Using integer division by 100 the multiplying it by 100 so that when I add the index of the desired letter in the string the colour is barely changed,
            #This makes the encoding of the image a lot more stealthy
            pix[2] = (pix[2]//100)*100 + alnum_list.index(e_str[l_count].lower())
            if l_count < len(e_str)-1:
                l_count += 1
            else:
                l_count = 0
            set_pixel(col,row,pix)    
    save_image("{}_encoded.bmp".format(image_name[0:image_name.find(".")]))
 

def decoder(image_name):
    if "encoded" not in image_name:
        return "INVALID FILE NAME"
    else:
        load_image(image_name)
        d_str = ''
        alnum_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7','8','9','0','$','.',',','#',"'"]
    
        for row in range(0, get_height()):
            for col in range(0, get_width()):
                pix = get_pixel(col, row)
                #By using the '$' character as a sentinel character I can determine that I have reached the end of my sentence and should add a space
                if alnum_list[pix[2]%100] == '$':
                    d_str += '\n'
                #By getting the modulus of the pixel (by 100) of the pixel I can get the index of the desired letter 
                if alnum_list[pix[2]%100] != '$':
                    d_str += (alnum_list[pix[2]%100])
        return d_str 


def grid(image1,num):
    load_image(image1)
    all_pix1 = get_all_pixels()
    #In order to make the image divisble by the desired amount of grid boxes I did the integer division of the width or height (depending on which is smaller) then multiplied
    #it by the number
    width = min(len(all_pix1[0]),len(all_pix1))//num*num
    #Made a list representing each seperate grid box
    order = list(range(1,num+1))
    new_image(width,width)  
    v1 = []
    consec = [0]*num
    ver = 0
    for i in range(0,num):
        random.shuffle(order)
        while ver != -1:
            ver = -1
            random.shuffle(order)            
            for v in range(num):
                #verified that any two rows that were connected had any two grid boxes that seem to form the original image
                if consec[v] == order[v]:
                    ver = 1
                elif ver != 1:
                    ver = -1
        consec = order.copy()
        ver = 1
        for consec1 in range(1,len(order)):
            #Because I am using the shuffled order of a list for the order of my grid boxes I tried to eliminate consecutive numbers 
            #which could contribute to forming the original image
            if order[consec1-1]+1 == order[consec1]:
                order.reverse()        
        #In order to maintain efficiency, not including setting all the pixels in their place, I only looped through the entire image once by 
        #looping through in sections. I accomplished this by manipulating the range with my first for loop.
        for row in range(i*width//num, width//num+width//num*i):
            for i2 in range(0,num):
                #Because I have a list of numbers representing the random order of my grid boxes, I use that list to reorganize each row in the image
                v1.extend(all_pix1[row][(order[i2]-1)*(width//num):order[i2]*width//num])
            all_pix1[row] = v1
            v1 = []
    for row in range(width):
        for col in range(width):
            #I set all the pixels into place
            set_pixel(col, row, all_pix1[row][col])    
    show_image()
    
    
def duo_reverse(image1, image2):
    load_image(image1)
    all_pix1 = get_all_pixels()
    load_image(image2)
    all_pix2 = get_all_pixels()
    width = min(len(all_pix1[0]),len(all_pix2[0]),len(all_pix1),len(all_pix2))//2*2
    new_image(width,width)    
    for row in range(width):
        for col in range(width):
            this_pix1 = all_pix1[row][col]
            this_pix2 = all_pix2[row][col]
            if col > get_width()//2 and row < get_height()//2:
                set_pixel(col, row, this_pix1)
            elif col > get_width()//2 and row > get_height()//2:
                set_pixel(col, row, this_pix2)
            #I reversed the colours of the top left and bottom left portions of the image
            elif col < get_width()//2 and row > get_height()//2:
                this_pix1.reverse()
                set_pixel(col, row, this_pix1)            
            else:
                this_pix2.reverse()
                set_pixel(col, row, this_pix2)
    show_image()

rgb_adjust('lorikeet.bmp',[100,100,100])