
# p1_w_pressed = False
# p1_s_pressed = False
# p2_up_pressed = False
# p2_down_pressed = False


class KeyPresses:
    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False

    def up_press(self):
        self.up_pressed = True

    def up_release(self):
        self.up_pressed = False

    def down_press(self):
        self.down_pressed = True

    def down_release(self):
        self.down_pressed = False


    # # p1 W
    # def p1_w_press():
    #     global p1_w_pressed
    #     p1_w_pressed = True
    # def p1_w_release():
    #     global p1_w_pressed
    #     p1_w_pressed = False
    #
    # # p1 S
    # def p1_s_press():
    #     global p1_s_pressed
    #     p1_s_pressed = True
    # def p1_s_release():
    #     global p1_s_pressed
    #     p1_s_pressed = False
    #
    # # p2 UP
    # def p2_up_press():
    #     global p2_up_pressedown
    #     p2_up_pressed = True
    # def p2_up_release():
    #     global p2_up_pressed
    #     p2_up_pressed = False
    #
    # # p2 Down
    # def p2_down_press():
    #     global p2_down_pressed
    #     p2_down_pressed = True
    #
    # def p2_down_release():
    #     global p2_down_pressed
    #     p2_down_pressed = False


