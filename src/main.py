from domain.world import World


def main():
    # Create the world as a 2d numpy array with size 64x64.
    world = World(64, 64)
    # Create an agent in one of the cells.
    world.add_agent(4, 17)
    # Get that agent.
    agent = world.state[4][17]

    print("BEFORE")
    print(agent.x, agent.y)
    print(world.state[4][17])
    print(world.state[5][17])

    agent.move(1, 0, world)

    print("AFTER")
    print(agent.x, agent.y)
    print(world.state[4][17])
    print(world.state[5][17])


if __name__ == "__main__":
    main()
