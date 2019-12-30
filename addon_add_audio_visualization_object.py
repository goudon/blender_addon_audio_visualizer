bl_info = {
    "name": "New Object",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}

import bpy
import os
from bpy.types import (
        Operator,
        Menu,
        Panel,
        PropertyGroup,
        )
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        FloatVectorProperty,
        IntProperty,
        StringProperty,
        PointerProperty,
        )
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
from bpy_extras.io_utils import ImportHelper

### add curve objects

# add circle bpy.ops.curve.primitive_bezier_circle_add(radius=1, enter_editmode=False, location=(0.208499, -0.948106, -2.69302))
# add bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, location=(0.637263, -2.1255, -2.63147))
# bpy.ops.object.editmode_toggle()
# bpy.ops.transform.translate(value=(-0, -0.685215, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

def add_object(self, context):
    scale_x = 1 #self.scale.x
    scale_y = 1 #self.scale.y
    scale_z = 1 #self.scale.z

    print('self :', self)


    verts = [
        Vector((-1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, 1 * scale_y, 0)),
        Vector((1 * scale_x, -1 * scale_y, 0)),
        Vector((-1 * scale_x, -1 * scale_y, 0)),
    ]

    edges = []
    faces = [[0, 1, 2, 3]]

    mesh = bpy.data.meshes.new(name="New Object Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)

class OBJECT_OT_add_object(Operator, AddObjectHelper, ImportHelper):
    """Create a new Curve Audio Visual Object"""
    bl_idname = "mesh.add_object"
    bl_label = "Add Curve Object"
    bl_options = {'REGISTER', 'UNDO'}
    Types = [
        ('Line', "Line", "Construct a Line"),
        ('Circle', "Circle", "Construct a Circle"),
        ]

    filter_glob = StringProperty(
        default='*.mp3;*.aac;*.mp4', options={'HIDDEN'})

    Type : EnumProperty(
            name="Type",
            description="Form of Curve to create",
            items=Types
            )

    Step : IntProperty(
        name="Step",
        default=3,
        min=0, soft_min=0,
        description="Sides"
        )

    Length : FloatProperty(
            name="Length",
            default=1.0,
            min=0.0, soft_min=0.0,
            unit='LENGTH',
            description="Radius"
            )
    Low : FloatProperty(
        name="Low",
        default=1.0,
        min=0.0, soft_min=0.0,
        unit='LENGTH',
        description="Radius"
        )

    High : FloatProperty(
        name="High",
        default=1.0,
        min=0.0, soft_min=0.0,
        unit='LENGTH',
        description="Radius"
        )

    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
        )
        
    # def draw(self, context):
    #     layout = self.layout

    def execute(self, context):

        # filename, extension = os.path.splitext(self.filepath)
        # print('Selected file:', self.filepath)
        # print('File name:', filename)
        # print('File extension:', extension)

        add_object(self, context)

        return {'FINISHED'}

# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add Object",
        icon='PLUGIN')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()




#import bpy
#import math

#bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.delete(True)

#count = 3
#lo = 1000
#hi = 15000
#step = (hi - lo) / count

#for i in range(-count,count):
#    for j in range(-count,count):
#        #object fixed
#        bpy.ops.mesh.primitive_cylinder_add(vertices = 6,location=( math.sqrt(3)*j+(i%2)*math.sqrt(3)/2, 1.5*i, 1))
#        bpy.context.scene.cursor_location = bpy.context.active_object.location
#        bpy.context.scene.cursor_location.z -= 1
#        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
#        bpy.context.active_object.scale.z = 10
#        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

#        #scale changes lock xy
#        bpy.ops.anim.keyframe_insert_menu(type='Scaling')
#        bpy.context.active_object.animation_data.action.fcurves[0].lock = True
#        bpy.context.active_object.animation_data.action.fcurves[1].lock = True
#        #import sound & graph baking
#        bpy.context.area.type = 'GRAPH_EDITOR'
#        #radius(round(math.sqrt(i**2+j**2)))
#        bpy.ops.graph.sound_bake(filepath=r'C:\HOGE.mp3', low = (step*round(math.sqrt(i**2+j**2))), high = (step*(round(math.sqrt(i**2+j**2))+1)))
#        bpy.context.active_object.animation_data.action.fcurves[2].lock = True
#bpy.context.area.type = 'TEXT_EDITOR'
