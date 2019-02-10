from domain.world import World


def main():
    # Create the world as a 2d numpy array with size 64x64.
    world = World(64, 64)
    # Create an agent in one of the cells.
    world.add_agent(4, 17)
    # Get that agent.
    print(world.state[4][17])
    print(world.agents)
    world.step()
    print(world.state[4][17])
    print(world.agents)


if __name__ == "__main__":
    main()
