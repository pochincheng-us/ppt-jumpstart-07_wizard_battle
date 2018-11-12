import random
import time

from actors import Wizard, Creature


def print_header():
    app_name = 'Wizard Game App'
    dashes = '-' * (5 + len(app_name) + 5)
    spaces = ' ' * 5
    print("{}".format(dashes))
    print("{}{}{}".format(spaces, app_name, spaces))
    print("{}".format(dashes))
    print('')


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appear from a dark and foggy forest...'.format(
            active_creature.name, active_creature.level
        ))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ').lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('lookaround')
        else:
            print('OK, exiting game...bye!')
            break

        print()


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
