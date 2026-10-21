import random
import CRLLIB

def main():
    while True: 
        q = None
        if CRLLIB.enemy is not None: 
            q = CRLLIB.enemy.move_op()
            if q is None: q = CRLLIB.enemy.get_basic() 

        resolved = False
        while not resolved:
            CRLLIB.scr.buf[8] = q[0]
            CRLLIB.scr.ref()
            resolved = CRLLIB.player.move_op(q) 

        if not CRLLIB.enemy.alive: 
            CRLLIB.enemy = CRLLIB.Monster(random.choice([0, 1, 2]))

main()