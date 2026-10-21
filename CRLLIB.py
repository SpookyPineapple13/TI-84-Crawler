import random

class Player:
    def __init__(self):
        self.hp = 10
        self.mry = 0
        self.mode = "ground"

    def move_op(self, q):
        global enemy
        inte = input("")
        q_txt, q_ans, g_h, b_h = q

        if inte == "s": 
            enemy.show_stat(True)
            scr.buf[5] = "Player"
            scr.buf[6] = "HP: " + str(self.hp)
            scr.buf[7] = "Morrays: " + str(self.mry) 
            scr.buf[8] = "Mode: " + self.mode
            scr.ref(); input()
            scr.clr(); enemy.show_stat()
            return False
            
        elif inte == "m":
            enemy.show_stat()
            scr.buf[6], scr.buf[7], scr.buf[8] = "1 - ground", "2 - air", "3 - crouch"
            scr.ref()
            inte = input("Mode: ")
            if inte == "1": self.mode = "ground"
            elif inte == "2": self.mode = "air"
            elif inte == "3": self.mode = "crouch"
            else: 
                scr.clr(); enemy.show_stat()
                scr.buf[8] = "Invalid mode"
                scr.ref(); input()
            scr.clr(); enemy.show_stat()
            return False
        
        if inte == str(q_ans): g_h()
        else: b_h()
        return True

class GameScreen:
    def __init__(self):
        self.buf = [""] * 9

    def write_line(self, n, txt):
        if 0 <= n < 9: self.buf[n] = txt
    
    def clr(self):
        for i in range(9): self.buf[i] = ""

    def ref(self):
        print("\x1b[2J\x1b[H", end="") 
        for line in self.buf: print(line)

class Monster:
    def __init__(self, t):
        self.t = t 
        if t == 0:
            self.name, self.mode, self.hp, self.a_special = "Goblin", "ground", 8, 3
        elif t == 1:
            self.name, self.mode, self.hp, self.a_special = "DigiBat", "air", 6, 2
        elif t == 2:
            self.name, self.mode, self.hp, self.a_special = "Gelatin Cube", "crouch", 12, 4
        
        self.mry = 5
        self.alive = True
        self.a_basic = 1

    def basic(self):
        global player
        player.hp -= self.a_basic
        scr.buf[8] = "wrong"; scr.ref(); input()

    def basic_solve(self):
        global player
        if player.mode == self.mode: 
            self.hp -= self.a_basic
            if self.hp <= 0: self.death()
        scr.buf[8] = "correct"; scr.ref(); input()

    def special(self):
        global player
        player.hp -= self.a_basic 
        scr.buf[8] = "blast"; scr.ref(); input()

    def parry(self):
        self.hp -= self.a_special
        if self.hp <= 0: self.death()
        scr.buf[8] = "parry"; scr.ref(); input()

    def death(self):
        global player
        self.alive = False
        player.mry += self.mry
        scr.buf[8] = "Monster killed"; scr.ref(); input()

    def show_stat(self, d=False):
        scr.buf[0] = self.name
        scr.buf[1] = "HP: " + str(self.hp)
        if d: scr.buf[2] = "Mode: " + self.mode

    def move_op(self):
        self.show_stat()
        if random.random() <= 0.2:
            if self.t == 0:
                c = random.choice([("2 * 2", 4), ("4 * 8", 32), ("12 * 0.5", 6), ("13 + (-)80", -67)])
                return (c[0], c[1], self.basic_solve if c[1]==-67 else self.parry, self.basic if c[1]==-67 else self.special)
            elif self.t == 1:
                c = random.choice([("-3 * 8", -24), ("-12 * -11", 132)])
                return (c[0], c[1], self.parry, self.special)
            elif self.t == 2:
                c = random.choice([("4^3/2", 8), ("8^2/3", 4), ("9^3/2", 27), ("16^1/2", 4)])
                return (c[0], c[1], self.parry, self.special)
        return None
    
    def get_basic(self):
        if self.t == 0:
            t1, t2 = random.randint(1, 100), random.randint(1, 100)
            return (str(t1) + "+" + str(t2), t1 + t2, self.basic_solve, self.basic)
        elif self.t == 1:
            t1, t2 = random.randint(1, 100), random.randint(1, 100)
            return (str(t1) + "-" + str(t2), t1 - t2, self.basic_solve, self.basic)
        elif self.t == 2:
            if random.random() < 0.5:
                n = random.randint(2, 12)
                return (str(n) + "^2", n * n, self.basic_solve, self.basic)
            else:
                n = random.randint(2, 6)
                return (str(n) + "^3", n * n * n, self.basic_solve, self.basic)

scr = GameScreen()
player = Player()
enemy = Monster(random.choice([0, 1, 2]))
