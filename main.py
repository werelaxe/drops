import model


def main():
    game_model = model.Model()
    game_model.print_model()
    game_model.update()
    game_model.print_model()


if __name__ == '__main__':
    main()
