import win32gui, win32con


def RGB(r, g, b):
    r = r & 0xFF
    g = g & 0xFF
    b = b & 0xFF
    return (b << 16) | (g << 8) | r


def display():
    foreground = win32gui.GetForegroundWindow()
    dc = win32gui.GetWindowDC(foreground)
    pirate_win = win32gui.FindWindow(None, "The Legend of Pirates Online [BETA]")
    pirate_dc = win32gui.GetWindowDC(pirate_win)
    win32gui.BitBlt(dc, 40, 753, 440-40, 953-753, pirate_dc, 40, 753, win32con.SRCCOPY)
    win32gui.ReleaseDC(foreground, dc)
    win32gui.ReleaseDC(pirate_win, pirate_dc)


if __name__ == "__main__":
    while True:
        display()
