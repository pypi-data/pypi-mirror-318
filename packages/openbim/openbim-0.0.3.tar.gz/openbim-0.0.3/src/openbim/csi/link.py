#===----------------------------------------------------------------------===#
#
#         STAIRLab -- STructural Artificial Intelligence Laboratory
#
#===----------------------------------------------------------------------===#
#
import numpy as np
from .utility import UnimplementedInstance, find_row, find_rows


def _orient(xi, xj, deg):
    # Calculate the direction vector of the link element
    # Where a is the node number of node i, b is the node number of node j, and degree is the user-specified local axis
    # ------------------------------------------------------------------------------
    d_x, d_y, d_z = e_x = xj - xi

    # Local 1-axis points from node I to node J
    l_x = np.array([d_x, d_y, d_z])
    # Global z-axis
    g_z = np.array([0, 0, 1])

    # In SAP2000, if the link is vertical, the local y-axis is the same as the
    # global x-axis, and the local z-axis can be obtained by crossing the local
    # x-axis with the local y-axis
    if d_x == 0 and d_y == 0:
        l_y = np.array([1, 0, 0])
        l_z = np.cross(l_x, l_y)

    # In other cases, the plane formed by the local x-axis and the local y-axis
    # is a vertical plane (i.e., the normal vector is horizontal), and the
    # local z-axis can be obtained by crossing the local x-axis with the global
    # z-axis
    else:
        l_z = np.cross(l_x, g_z)

    # The local axis may also be rotated using the Rodrigues' rotation formula
    angle = deg / 180 * np.pi
    l_z_rot = l_z * np.cos(angle) + np.cross(l_x, l_z) * np.sin(angle)
    # The rotated local y-axis can be obtained by crossing the rotated local z-axis with the local x-axis
    l_y_rot = np.cross(l_z_rot, l_x)
    # Finally, return the normalized local y-axis
    return l_y_rot / np.linalg.norm(l_y_rot)


_link_tables = {
    "Linear              " : "LINK PROPERTY DEFINITIONS 02 - LINEAR",
    "??                  " : "LINK PROPERTY DEFINITIONS 03 - MULTILINEAR",
    "Damper - Exponential" : "LINK PROPERTY DEFINITIONS 04 - DAMPER",
    "???                 " : "LINK PROPERTY DEFINITIONS 05 - GAP",
    "????                " : "LINK PROPERTY DEFINITIONS 06 - HOOK",
    "?????               " : "LINK PROPERTY DEFINITIONS 07 - RUBBER ISOLATOR",
    "??????              " : "LINK PROPERTY DEFINITIONS 08 - SLIDING ISOLATOR",
    "Plastic (Wen)"        : "LINK PROPERTY DEFINITIONS 10 - PLASTIC (WEN)",
    "???????             " : "LINK PROPERTY DEFINITIONS 11 - MULTILINEAR PLASTIC",
}

def create_links(csi, model, library, config):
    log = []


    for link in csi.get("CONNECTIVITY - LINK",[]):
        nodes = (link["JointI"], link["JointJ"])

        assign = find_row(csi["LINK PROPERTY ASSIGNMENTS"],
                          Link=link["Link"])

        if assign["LinkJoints"] == "SingleJoint":

            props = find_row(csi["LINK PROPERTY DEFINITIONS 01 - GENERAL"],
                             Link=assign["LinkProp"])

            if props["LinkType"] != "Linear":
                log.append(UnimplementedInstance(f"Joint.SingleJoint.LinkType={props['LinkType']}", assign))

            # TODO: Implement soil springs
            props = find_rows(csi["LINK PROPERTY DEFINITIONS 02 - LINEAR"],
                             Link=assign["LinkProp"])

            flags = tuple(1 if find_row(props, DOF=f"{dof[0]}{'XYZ'.find(dof[1])+1}") and config["dofs"][dof] else 0 for dof in config["dofs"])

            model.fix(nodes[0], flags)

            continue

        elif assign["LinkJoints"] != "TwoJoint":
            log.append(UnimplementedInstance(f"Joint.{assign['LinkJoints']}", assign))
            continue

        #
        # Get mats and dofs
        #
        mats = tuple(library["link_materials"][assign["LinkProp"]].values())
        dofs = tuple(library["link_materials"][assign["LinkProp"]].keys())
        dofs = tuple(["U1", "U2", "U3", "R1", "R2", "R3"].index(i)+1 for i in dofs)



        #
        # Get axes
        #
        axes   = find_row(csi.get("LINK LOCAL AXES ASSIGNMENTS 1 - TYPICAL",[]),
                          Link=link["Link"])

        if not axes:
            orient_vector = None

        elif axes["AdvanceAxes"]:

            axes = find_row(csi.get("LINK LOCAL AXES ASSIGNMENTS 2 - ADVANCED",[]),
                          Link=link["Link"])

            orient_vector = (
                    axes["AxVecX"], axes["AxVecY"], axes["AxVecZ"],
                    axes["PlVecX"], axes["PlVecY"], axes["PlVecZ"],
            )

        else:
            xi = np.array(model.nodeCoord(nodes[0]))
            xj = np.array(model.nodeCoord(nodes[1]))
            orient_vector = tuple(_orient(xi, xj, axes["Angle"]))


        #
        # Create the link
        #
        if orient_vector is not None:
            model.element("TwoNodeLink", None,
                      nodes,
                      mat=mats,
                      dir=dofs,
                      orient=orient_vector
                      )
        else:
            model.element("TwoNodeLink", None,
                      nodes,
                      mat=mats,
                      dir=dofs
                      )

    return log

