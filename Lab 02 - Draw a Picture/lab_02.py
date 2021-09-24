import arcade


arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.DARK_BLUE)

# Get ready to draw
arcade.start_render()
arcade.draw_rectangle_filled(400, 0, 100, 750, arcade.csscolor.BLACK) #building 1
arcade.draw_rectangle_filled(375,345,27,27, arcade.csscolor.YELLOW) #building 1 window
arcade.draw_rectangle_filled(375,300,27,27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(375,255,27,27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(375,210,27,27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(375, 165, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(375, 120, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 345, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 300, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 255, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 210, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 165, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(425, 120, 27, 27, arcade.csscolor.YELLOW)


arcade.draw_rectangle_filled(300, 0, 75, 750, arcade.csscolor.DARK_GREY)  #building 2
arcade.draw_rectangle_filled(280, 345, 27, 27, arcade.csscolor.YELLOW)   #building 2 window start
arcade.draw_rectangle_filled(280, 300, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(280, 255, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(280, 210, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(280, 165, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(280, 120, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 345, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 300, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 255, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 210, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 165, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(320, 120, 27, 27, arcade.csscolor.YELLOW)


arcade.draw_rectangle_filled(220, 0, 100, 600, arcade.csscolor.BLACK) #building 3
arcade.draw_rectangle_filled(190, 260, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 215, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 170, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 125, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(240, 260, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(240, 215, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(240, 170, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(240, 125, 27, 27, arcade.csscolor.YELLOW)


arcade.draw_rectangle_filled(100, 0, 75, 750, arcade.csscolor.DARK_GREY) #building 4
arcade.draw_rectangle_filled(82, 345, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(120, 345, 27, 27, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(82, 300, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(82, 255, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(82, 210, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(82, 165, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(120, 300, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(120, 255, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(120, 210, 20, 30, arcade.csscolor.YELLOW)
arcade.draw_ellipse_filled(120, 165, 20, 30, arcade.csscolor.YELLOW)

arcade.draw_rectangle_filled(470, 0, 100, 500, arcade.csscolor.DARK_GREY) #building 5
arcade.draw_line(505, 230, 435, 230, arcade.color.YELLOW, 15)
arcade.draw_line(505, 200, 435, 200, arcade.color.YELLOW, 15)
arcade.draw_line(505, 170, 435, 170, arcade.color.YELLOW, 15)
arcade.draw_line(505, 140, 435, 140, arcade.color.YELLOW, 15)
arcade.draw_line(505, 110, 435, 110, arcade.color.YELLOW, 15)
arcade.draw_line(505, 80, 435, 80, arcade.color.YELLOW, 15)

arcade.draw_rectangle_filled(0, 0, 140, 600, arcade.csscolor.BLACK) #building 6
arcade.draw_triangle_filled(10, 290, 60, 290, 35, 240, arcade.csscolor.YELLOW)
arcade.draw_triangle_filled(10, 190, 60, 190, 35, 240, arcade.csscolor.YELLOW)

arcade.draw_rectangle_filled(150, 0, 100, 500, arcade.csscolor.GRAY) #building 7
arcade.draw_line(105, 230, 190, 230, arcade.color.YELLOW, 15)
arcade.draw_line(105, 185, 190, 185, arcade.color.YELLOW, 15)
arcade.draw_line(105, 140, 190, 140, arcade.color.YELLOW, 15)

arcade.draw_arc_filled(200, 500, 35, 90, arcade.csscolor.WHITE, 90, 270) #moon
arcade.finish_render()
arcade.run()