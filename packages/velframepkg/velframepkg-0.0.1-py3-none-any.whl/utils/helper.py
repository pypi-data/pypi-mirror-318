# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import object
import squish
from typing import Any, Dict, List, Union


def get_object(obj_ref: dict, lookup_error_message: str, timeout: int = 0, needs_to_be_accessible: bool = True) -> Any:
    """Gets an AUT object.

    Parameters
    ----------
    obj_ref: The reference to the object. e.g.: {"type": "QWidget", "name": "EasterEgg"}
    lookup_error_message: A message for the LookupError if the object is not found.
    timeout: The time, in milliseconds, to wait for the object before raising a LookupError
    needs_to_be_accessible: True if the object needs to exist, be visible and enabled.

    Returns
    -------
    An AUT object.
    """
    try:
        if needs_to_be_accessible:
            return squish.waitForObject(obj_ref, timeout)
        else:
            return squish.waitForObjectExists(obj_ref, timeout)
    except LookupError:
        raise LookupError(f"{lookup_error_message} (Timeout: {timeout/1000} s)")


ObjectRef = Dict[str, Union[str, int]]


def get_all_objects(obj_ref: ObjectRef) -> List[Any]:
    """Gets all the objects that match the given object reference.

    Given a structure like:

    A ---> B --> C
       |
       --> B --> C

    If you call
    `squish.findAllObjects({"container": {"type": "B"}, "type": "C"})`,
    it will return a list with only one C object instead of returning
    the two C objects that match the object reference. ¯⧵(°_°)/¯
    For some reason, it only returns the objects inside the first container
    it finds.
    To fix this, we have this function which, in the scenario above, would
    return a list with the two C objects.

    Parameters
    ----------
    obj_ref: The reference to the object. e.g.: {"type": "QWidget", "name": "Tab"}

    Returns
    -------
    A list of AUT objects.
    """
    container = obj_ref.get("container", None)

    if container:
        container_refs = __get_all_objects_refs(container)

        all_objects = []
        for container_ref in container_refs:
            obj_ref_with_container_ref = obj_ref.copy()
            obj_ref_with_container_ref["container"] = container_ref

            all_objects.extend(squish.findAllObjects(obj_ref_with_container_ref))

        return all_objects
    else:
        return squish.findAllObjects(obj_ref)


def __get_all_objects_refs(obj_ref: ObjectRef, get_container_refs: bool = True) -> List[ObjectRef]:
    """Gets all the object references with occurrences that match the given object reference.

    Given a structure like:

    A ---> B --> C
       |
       --> B --> C

    and an object reference like:
    {"container": {"type": "B"}, "type": "C"}

    this function would return a list with two object references like this:
    [
        {"container": {"type": "B", "occurrence": 1}, "type": "C", "occurrence": 1},
        {"container": {"type": "B", "occurrence": 2}, "type": "C", "occurrence": 1}
    ]

    Parameters
    ----------
    obj_ref: The reference to the object. e.g.: {"type": "QWidget", "name": "Tab"}
    get_container_refs: Whether or not to get all the references of the containers.
        Should probably be False when called from outside this function.

    Returns
    -------
    A list of object references.
    """
    container = obj_ref.get("container", None)

    if container and get_container_refs:
        container_refs = __get_all_objects_refs(container)

        obj_refs = []
        for container_ref in container_refs:
            obj_ref_with_container_ref = obj_ref.copy()
            obj_ref_with_container_ref["container"] = container_ref

            obj_refs_with_container_ref_list = __get_all_objects_refs(
                obj_ref_with_container_ref, get_container_refs=False
            )

            obj_refs.extend(obj_refs_with_container_ref_list)

        return obj_refs
    else:
        if "occurrence" in obj_ref:
            return [obj_ref]

        num_obj_refs = len(squish.findAllObjects(obj_ref))

        obj_refs = []
        for i in range(1, num_obj_refs + 1):
            obj_ref_with_occurrence = obj_ref.copy()
            obj_ref_with_occurrence["occurrence"] = i
            obj_refs.append(obj_ref_with_occurrence)

        return obj_refs


def dump_children(parent, depth=1000, indent=""):
    if depth < 0:
        return

    for child in object.children(parent):
        object_name = getattr(child, "objectName", None)
        class_name = squish.className(child)

        print("{}{} : {}".format(indent, str(object_name), str(class_name)))

        dump_children(child, depth - 1, indent + "  ")


def walk_children_with_class_filter(parent, allowed_list, depth=1000):
    """Generator to allow lazy evaluation on the children, keeping only interesting ones.

    Parameters
    ----------
    allowed_list: list of object class to follow
    depth: maximum depth to find childs

    Returns
    -------
    list of found objects
    """
    if depth < 0:
        return

    for child in object.children(parent):
        if squish.className(child) not in allowed_list:
            continue
        yield child
        for grandChild in walk_children_with_class_filter(child, allowed_list, depth - 1):
            if squish.className(grandChild) not in allowed_list:
                continue
            yield grandChild


def walk_children(parent, depth=10):
    """Generator to allow lazy evaluation on the children, keeping only interesting ones.

    Parameters
    ----------
    depth: maximum depth to find childs

    Returns
    -------
    list of found objects
    """
    if depth < 0:
        return

    for child in object.children(parent):
        yield child
        if child is not None and str(child) != "<null>" and parent is not None and str(parent) != "<null>":
            for grandChild in walk_children(child, depth - 1):
                yield grandChild


def get_children_of_type(parent, type_name, depth=10):
    return [
        child
        for child in walk_children(parent, depth)
        if child is not None and str(child) != "<null>" and squish.className(child) == type_name
    ]


def get_child_object_name(parent, object_name, depth=10):
    object_name = object_name.lower()

    return [
        child
        for child in walk_children(parent, depth)
        if child is not None
        and str(child) != "<null>"
        and str(getattr(child, "objectName", None)).lower() == object_name
    ]


def get_splitter_conf(parent, total_x: int = 0, total_y: int = 0, depth: int = 5):
    """Retrieve all splitters in a hierarchy with associated absolute indexes. The default value of depth (5) has been
    empirically chosen because the qsplitters are never deeper than 5.

    Parameters
    ----------
    depth: maximum depth to find childs

    Returns
    -------
    children: list of objects
    x_list: list of associated x coordinates
    y_list: list of associated y coordinates
    """
    children = []
    x_list = []
    y_list = []

    for child in object.children(parent):
        # Checks that the child is valid and fully instantiated
        if child is not None and str(child) != "<null>":
            # each child start position is the one of the parent
            child_x = total_x
            child_y = total_y
            if squish.className(child) == "QSplitter":
                children.append(child)
                # compute the QSplitter child start position
                child_x = total_x + child.x
                child_y = total_y + child.y
                x_list.append(child_x)
                y_list.append(child_y)

            if depth:
                l_children, l_x, l_y = get_splitter_conf(child, child_x, child_y, depth - 1)
                children.extend(l_children)
                x_list.extend(l_x)
                y_list.extend(l_y)

    return children, x_list, y_list


def get_children_of_type_avoid_splitter(parent, type_name, depth=10):
    """Retrieve all children in a hierarchy with without following splitter.

    The default value of depth (10) has been empirically chosen because the qsplitters are never deeper than 10.
    """

    children = []
    for child in object.children(parent):
        # Checks that the child is valid and fully instantiated
        if child and str(child) != "<null>":
            if squish.className(child) == type_name:
                children.append(child)
            if squish.className(child) == "QSplitter":
                continue
            if depth:
                children.extend(get_children_of_type(child, type_name, depth - 1))
    return children


def str_to_bool(value):
    test = ["true", "1", "t", "on"]
    return value.lower() in test
