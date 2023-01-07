import sys

import pygame

from BT import BT
from button import Button

pygame.init()
clock = pygame.time.Clock()
main_win = pygame.display.set_mode((1200, 720))
pygame.display.set_caption('Liquid level measurement system')
water_tank = pygame.image.load('assets/tan5.png')
BG = pygame.image.load("assets/Background3.png")
bt = BT()
global liquid_level

DISCONNECTED = "disconnected"
CONNECT = "connected"
GREEN = "Green"
RED = "Red"


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Domelen.ttf", size)


async def measure_button_declaration():
    MEASURE_MOUSE_POS = pygame.mouse.get_pos()

    MEASURE_1 = Button(image=None, pos=(950, 460), text_input="Send 1", font=get_font(25),
                       base_color="White",
                       hovering_color="Green")
    MEASURE_0 = Button(image=None, pos=(1100, 460), text_input="Send 0", font=get_font(25),
                       base_color="White",
                       hovering_color="Green")
    MEASURE_CALIBRATE = Button(image=None, pos=(80, 650), text_input="Calibrate", font=get_font(25),
                               base_color="White",
                               hovering_color="Green")
    MEASURE_BACK = Button(image=None, pos=(1150, 680), text_input="BACK", font=get_font(20),
                          base_color="White",
                          hovering_color="Green")
    MEASURE_READ = Button(image=None, pos=(750, 460), text_input="READ", font=get_font(20),
                          base_color="White",
                          hovering_color="Green")

    MEASURE_BACK.changeColor(MEASURE_MOUSE_POS)
    MEASURE_1.changeColor(MEASURE_MOUSE_POS)
    MEASURE_0.changeColor(MEASURE_MOUSE_POS)
    MEASURE_CALIBRATE.changeColor(MEASURE_MOUSE_POS)
    MEASURE_READ.changeColor(MEASURE_MOUSE_POS)

    MEASURE_BACK.update(main_win)
    MEASURE_1.update(main_win)
    MEASURE_0.update(main_win)
    MEASURE_CALIBRATE.update(main_win)
    MEASURE_READ.update(main_win)

    return MEASURE_0, MEASURE_1, MEASURE_READ, MEASURE_CALIBRATE, MEASURE_BACK, MEASURE_MOUSE_POS


class Application:

    def __init__(self):
        self.bt_status = DISCONNECTED
        self.color = RED

    async def connections_button_declaration(self):

        CONNECTIONS_MOUSE_POS = pygame.mouse.get_pos()

        CONNECTIONS_TEXT_STATUS = get_font(15).render(self.bt_status, True, self.color)
        CONNECTIONS_STATUS_POS = CONNECTIONS_TEXT_STATUS.get_rect(center=(236, 10))
        main_win.blit(CONNECTIONS_TEXT_STATUS, CONNECTIONS_STATUS_POS)

        CONNECTIONS_BACK = Button(image=None, pos=(1150, 680), text_input="BACK", font=get_font(20),
                                  base_color="White", hovering_color="Green")
        CONNECTIONS_Conect = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 200), text_input="Connect",
                                    font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        CONNECTIONS_Disconnect = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 350),
                                        text_input="Disconnect", font=get_font(20), base_color="#d7fcd4",
                                        hovering_color="White")

        CONNECTIONS_BACK.changeColor(CONNECTIONS_MOUSE_POS)
        CONNECTIONS_Conect.changeColor(CONNECTIONS_MOUSE_POS)
        CONNECTIONS_Disconnect.changeColor(CONNECTIONS_MOUSE_POS)

        CONNECTIONS_BACK.update(main_win)
        CONNECTIONS_Conect.update(main_win)
        CONNECTIONS_Disconnect.update(main_win)

        return CONNECTIONS_MOUSE_POS, CONNECTIONS_Conect, CONNECTIONS_Disconnect, CONNECTIONS_BACK

    async def measure(self):
        clock.tick(60)
        while True:
            await bt.read()
            # MEASURE_MOUSE_POS = pygame.mouse.get_pos()
            main_win.fill("black")
            # MEASURE_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
            # MEASURE_RECT = MEASURE_TEXT.get_rect(center=(640, 260))
            # main_win.blit(MEASURE_TEXT, MEASURE_RECT)

            MEASURE_TEXT = get_font(15).render("Liquid level = ", True, "White")
            MEASURE_VALUE_LIQUID = get_font(15).render(bt.text, True, "White")

            MEASURE_RECT = MEASURE_TEXT.get_rect(center=(210, 110))
            MEASURE_RECT_LIQUID = MEASURE_VALUE_LIQUID.get_rect(center=(450, 110))

            main_win.blit(MEASURE_TEXT, MEASURE_RECT)
            main_win.blit(MEASURE_VALUE_LIQUID, MEASURE_RECT_LIQUID)

            main_win.blit(water_tank, (20, 40))

            MEASURE_0, MEASURE_1, MEASURE_READ, MEASURE_CALIBRATE, MEASURE_BACK, MEASURE_MOUSE_POS \
                = await measure_button_declaration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MEASURE_BACK.checkForInput(MEASURE_MOUSE_POS):
                        await Application.main_menu(self)
                    if MEASURE_1.checkForInput(MEASURE_MOUSE_POS):
                        bt.write_one()
                    if MEASURE_0.checkForInput(MEASURE_MOUSE_POS):
                        bt.write_zero()
                    if MEASURE_READ.checkForInput(MEASURE_MOUSE_POS):
                        await bt.read()
                    if MEASURE_CALIBRATE.checkForInput(MEASURE_MOUSE_POS):
                        await bt.calibrate()

            pygame.display.update()

    async def description(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            main_win.fill("black")

            OPTIONS_TEXT = get_font(45).render("This is the DESCRIPTION screen.", True, "white")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            main_win.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460),
                                  text_input="BACK", font=get_font(75), base_color="White",
                                  hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(main_win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        await Application.main_menu(self)

            pygame.display.update()

    async def connections(self):
        while True:
            main_win.fill("black")

            CONNECTIONS_TEXT_DEFAULT = get_font(15).render("Connection status: ", True, "White")
            CONNECTIONS_TEXT_DEFAULT_POS = CONNECTIONS_TEXT_DEFAULT.get_rect(center=(100, 10))
            main_win.blit(CONNECTIONS_TEXT_DEFAULT, CONNECTIONS_TEXT_DEFAULT_POS)

            connections_mouse_pos, connections_connect, connections_disconnect, connections_back \
                = await Application.connections_button_declaration(self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if connections_back.checkForInput(connections_mouse_pos):
                        await Application.main_menu(self)
                    if connections_connect.checkForInput(connections_mouse_pos):
                        for i in range(1, 3):
                            try:
                                if bt.bt_serial():
                                    self.bt_status = CONNECT
                                    self.color = GREEN
                                    break
                            except Exception as e:
                                print(e)

                    if connections_disconnect.checkForInput(connections_mouse_pos):
                        try:
                            bt.disconect()
                            self.bt_status = DISCONNECTED
                            self.color = RED
                            break
                        except Exception as e:
                            print(e)

            pygame.display.update()

    async def main_menu(self):
        while True:
            main_win.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(50).render("Liquid level measurement system", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(600, 50))

            MAIN_MENU_BT_TEXT_DEFAULT = get_font(15).render("Bluetooth status: ", True, "White")
            MAIN_MENU_BT_TEXT_DEFAULT_POS = MAIN_MENU_BT_TEXT_DEFAULT.get_rect(center=(950, 10))
            main_win.blit(MAIN_MENU_BT_TEXT_DEFAULT, MAIN_MENU_BT_TEXT_DEFAULT_POS)

            MAIN_MENU_BT_TEXT_STATUS = get_font(15).render(self.bt_status, True, self.color)
            MAIN_MENU_BT_TEXT_STATUS_POS = MAIN_MENU_BT_TEXT_STATUS.get_rect(center=(1100, 10))
            main_win.blit(MAIN_MENU_BT_TEXT_STATUS, MAIN_MENU_BT_TEXT_STATUS_POS)

            MEASUREMENT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 200),
                                        text_input="MEASUREMENT", font=get_font(40), base_color="#d7fcd4",
                                        hovering_color="White")

            DESCRIPTION_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 350),
                                        text_input="DESCRIPTION", font=get_font(40), base_color="#d7fcd4",
                                        hovering_color="White")

            CONNECTIONS_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 500),
                                        text_input="CONNECTIONS", font=get_font(40), base_color="#d7fcd4",
                                        hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(640, 655),
                                 text_input="QUIT", font=get_font(40), base_color="#d7fcd4",
                                 hovering_color="White")

            main_win.blit(MENU_TEXT, MENU_RECT)

            for button in [MEASUREMENT_BUTTON, DESCRIPTION_BUTTON, CONNECTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(main_win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MEASUREMENT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        await Application.measure(self)
                    if DESCRIPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        await Application.description(self)
                    if CONNECTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        await Application.connections(self)
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # main_menu()
