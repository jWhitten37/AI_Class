def create_container(container_type):
    match container_type:
        case 'list':
            return []
        case 'dict':
            return {}
        case 'set':
            return set()
        case 'tuple':
            return ()
        case _:
            print("Invalid choice. Please choose either list, dict, set, or tuple.")

def access_item(item, container):
    match container:
        case list():
            return container[item]
        case dict():
            return container.get(item)
        case set():
            return item in container
        case tuple():
            return container[item]
        case _:
            print('Invalid choices.')

def add_item(item, container, position=None):
    match container:
        case list():
            if position != None:
                container.insert(position, item)
                return container
            else:
                container.append(item)
                return container
        case dict():
            if type(item) is tuple:
                container[item[0]] = item[1]
                return container
            else:
                container[item] = None
                return container
        case set():
            container.add(item)
            return container
        case tuple():
            if position != None:
                new_tuple = list(container)
                new_tuple.insert(position, item)
                return tuple(new_tuple)
            else:
                new_tuple = list(container)
                new_tuple.append(item)
                return tuple(new_tuple)
        case _:
            print('Invalid item to add.')
            
def remove_item(item, container, multi=True):
    match container:
        case list():
            if multi:
                for x in container:
                    if x == item:
                        container.remove(x)
                return container
            else:
                container.remove(item)
                return container
        case dict():
            container.pop(item)
            return container
        case set():
            container.remove(item)
            return container
        case tuple():
            if multi:
                new_tuple = list(container)
                for x in new_tuple:
                    if x == item:
                        new_tuple.remove(x)
                return tuple(new_tuple)
            else:
                new_tuple = list(container)
                new_tuple.remove(item)
                return tuple(new_tuple)
        case _:
            print('Invalid item to remove.')

def update_item(orig_item, new_item, container, multi=True):
    match container:
        case list():
            if multi:
                for x in container:
                    if x == orig_item:
                        item_index = container.index(x)
                        container[item_index] = new_item
            else:
                item_index = container.index(orig_item)
                container[item_index] = new_item
            return container
        case dict():
            if type(new_item) is tuple:
                container[new_item[0]] = container.pop(orig_item)
                container[new_item[0]] = new_item[1]
                return container
            else:
                container[orig_item] = new_item
                return container
        case set():
            new_set = list(container)
            new_set[new_set.index(orig_item)] = new_item
            return set(new_set)
        case tuple():
            if multi:
                new_tuple = list(container)
                for x in new_tuple:
                    if x == orig_item:
                        new_tuple[new_tuple.index[x]] = new_item
            else:
                change
