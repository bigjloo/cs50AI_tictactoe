import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids : name
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    # open file - 2nd argument (sys.argv[1])
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        # read file
        reader = csv.DictReader(f)
        #for each row in reader, create an object w key = id and value = object {name, birth, movies} 
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            # add name from people.csv if not in names dictionary. key name, value id
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                # else if name exist, add id to name (actors can have more than 1 ID)
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    # if more than 2 arguments when run program ie python degrees.py small large
    if len(sys.argv) > 2:
        # print error msg
        sys.exit("Usage: python degrees.py [directory]")
    #else using the 2nd argument as directory
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    # runs load_data function from above 
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """ 
    # TODO
    # start source
    start = Node(state = source, parent = None, action = None)
    
    #initialize frontier as queue since we using breath first search
    frontier = QueueFrontier()
    
    #add the source to the frontier
    frontier.add(start)

    #initialize explored set
    explored_set = set()

    #loop to check nodes in frontier and expand
    while True:
        if frontier.empty():
            raise Exception("frontier is empty, no solution")
        node = frontier.remove()
        explored_set.add(node)
        for action, state in neighbors_for_person(node.state):
            if not frontier.contains_state(state) and state not in explored_set:
                child = Node(state = state, parent = node, action = action)
                if child.state == target:
                    path = []
                    movies = []
                    persons = []
                    while child.parent is not None:
                        #movie_set.add((child.action, child.state))
                        movies.append(child.action)
                        persons.append(child.state)
                        child = child.parent
                    movies.reverse()
                    persons.reverse()
                    for index, movie in enumerate(movies):
                        path.append((movie,persons[index]))
                    return path
                frontier.add(child)

            


    """
    the stars are the nodes in the tree.
    the movies that the stars are connected are the edges that connect the nodes
    use breath first search to go through to find shortest path

    start with a frontier that contains initial state (source id)
    start with empty explored set (to find path cost)
    repeat:
        if frontier is empty there is no solution
        remove node (star id) from the frontier
        if node (star id) === target id, return solution
        add node to explored set
        else expand node (movies) add nodes to frontier

    own:
    find movies of source star.
    *add movie to path ???
    create nodes of actors in those movies and add to frontier
    check if nodes === target
        if true, return length of path
        else, add nodes to explored set
    expand movies, create nodes of actors in the movies of previous star nodes
    repeat from *

    steps:
    1. create Node class with state, parent,action properties
    2. create QueueFrontier class with 
        init - initialize as an empty list
        add - add node to frontier
        contains_state - checks each node in frontier if contain target 
        empty - checks if frontier is empty (cant expand more nodes = no solution)
        remove - remove a node from the frontier
    
    initialize frontier to start
        start = Node(state= start, parent=none, action=none)
        frontier = queuefrontier()
        frontier.add(start)
    
    initialize empty explored set
        explored = set() ** we use set so that each entry is a unique value

    loop until solution is found or all nodes explored
        while True:
            if frontier.empty():
                raise Exception("no solution")
            #remove node from frontier
                node=  frontier.remove()
            #add 1 to explored 
                explored += 1
            #check if node is the goal, true: we loop through the parent (previous node )and append to action and cells
                if node.state == self.goal (node.star_id == target.id):
                    #backtrack to find what actions we took to get to this goal by loop through the parent and adding to action
                    #loop until parent = None which is our initial state
                    actions = [] (edge/movie)
                    cells = []
                    while node.parent is not None:
                        actions.append(node.action)
                        cells.append(node.state)
                        node = node.parent
                    actions.reverse()
                    cells.reverse()
                    self.solution = (actions,cells)
                    return
            #if node is not the goal, add to explored set
            explored.add(node.state) ***what do we put in the state of the node - person.id?
            #add neighbors to the frontier - new connections to the explored node
            for action,state, in self.neighbours(node.state):
                if not frontier.contains_state(state) and state not in self.explored
                    child = Node(state=state, parent = node, action = action)
                    frontier.add(child)
    """
  
    raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    # why do we need to include a set inside the list ??? ***
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """

    # add new nodes (neighbours) returns movie/person linked to current star
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
