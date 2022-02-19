import pyautogui
import time
import pygetwindow
import logging
from random import randint

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

class Start:
    def __init__(self, top, left, width, height):
        logging.info('Starting app!')
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.lure_x = { 'start': (left + 640), 'end': (left + 765) }
        self.lure_y = { 'start': (top + 122), 'end': (top + 150) }
        self.main_target_x = { 'start': (left + 768), 'end': (left + 897) }
        self.main_target_y = { 'start': (top + 217), 'end': (top + 245) }
        
    def r_val(self, start, end):
        return randint(start, end)
    
    def start(self):
        count = 0
        while True:
            # heal = pyautogui.locateOnScreen('images/taoist/greater_heal.png', confidence=0.8, region=(self.left, self.top, self.width, self.height))
            if True:
                if count > 50:
                    logging.info('App obstruido por: ${count}s')
                    count = 0
                else:
                    logging.info('Lurando monstros...')
                    lure_x = Start.r_val(self, start=self.lure_x['start'], end=self.lure_x['end'])
                    lure_y = Start.r_val(self, start=self.lure_y['start'], end=self.lure_y['end'])
                    main_target_x = Start.r_val(self, self.main_target_x['start'], end=self.main_target_x['end'])
                    main_target_y = Start.r_val(self, self.main_target_y['start'], end=self.main_target_y['end'])
                    time_target = Start.r_val(self, 6, 8)
                    pyautogui.click(x=lure_x, y=lure_y, duration=0.5, interval=0.3)
                    time.sleep(time_target)
                    logging.info('Retornando...')
                    pyautogui.click(x=main_target_x, y=main_target_y, duration=0.3)
                    logging.info('Limpando monstros...')
                    time.sleep(time_target * 3)
                    count = 0
            # else:
            #     if count == 0:
            #         logging.info('Refriando cura maior!')
            #         count += 1
            #     elif count == 50:
            #         logging.info('App obstruido!')
            #         count += 1
            #     else:
            #         count += 1
            #         pyautogui.sleep(1)

default_windows = ['Mir4G[1]', 'Mir4G[2]']

class Options:
    def __init__(self, win):
        self.win = win
        
    def auto_setup(self):
        win = pygetwindow.getWindowsWithTitle(self.win[0])[0]
        win.size = (960, 540)
        win.moveTo(0, 0)
        Options.start(self)
    
    def start(self, **kwargs):
        print('1 - Auto setup')
        print('2 - Starting')
        print('0 - Sair')
        start = int(input('Opção: '))
        if start == 1:
            Options.auto_setup(self)
        elif start == 2:
            win = pygetwindow.getWindowsWithTitle(self.win[0])[0]
            left = win.left
            top = win.top
            width = win.width
            height = win.height
            start = Start(top, left, width, height)
            start.start()
        elif start == 0:
            exit()
        else:
            Options.start(self)


opt = Options(default_windows)
opt.start()