#RANDOM INTERIOR BLOCKING
#by Bunny Ash
#https://neko-glitch.myportfolio.com
#-----------------------------------------------------------

import bpy
import random

#Clear the scene entirely
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

#Add a random amount of random cubes
for i in range(random.randint(2, 8)):
    
    bpy.ops.mesh.primitive_cube_add(
        location=(random.uniform(-1, 1), random.uniform(-1, 1), 0),
        scale=(random.uniform(-1, 1), random.uniform(-1, 1), 0.1)
    )

#Join all the cubes
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()
    
#Set render resolution to 16:9
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

#Create a new material
mat = bpy.data.materials.new("Material")

#Set the material color
mat.diffuse_color = (1, 1, 1, 1)

#Append the material to the object
bpy.context.object.data.materials.append(mat)

#Set render engine to EEVEE
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

#Enable Freestyle
bpy.context.scene.render.use_freestyle = True

#Get active View Layer
freestyle_settings = bpy.context.window.view_layer.freestyle_settings

#Get active Line Set
lineset = freestyle_settings.linesets.active

#Enable the necessary edge types
lineset.select_silhouette = False
lineset.select_crease = False
lineset.select_border = False
lineset.select_edge_mark = False
lineset.select_contour = True
lineset.select_external_contour = False
lineset.select_material_boundary = False

#Add a camera
bpy.ops.object.camera_add(
    location=(0, 0, 10), rotation=(0, 0, 0), scale=(1, 1, 1)
    )

#Change background color
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)