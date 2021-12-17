import bpy
import os

# Makes sure nothing is selected
for obj in bpy.context.selected_objects:
    obj.select_set(False)


for collection in bpy.data.collections:
   for obj in collection.all_objects:
      # Start selecting
      bpy.data.objects[obj.name].select_set(True)
      current_state = bpy.data.objects[obj.name].select_get()


      # Makes export path and other data
      blend_file_path = bpy.data.filepath
      directory = os.path.dirname('/tmp/testing/')
      target_file = os.path.join(directory, obj.name + '.obj')

      # Exports the obj and mtl
      bpy.ops.export_scene.obj(filepath=target_file, check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl", use_selection=True, use_animation=False, use_mesh_modifiers=True, use_edges=True, use_smooth_groups=False, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=True, use_nurbs=False, use_vertex_groups=False, use_blen_objects=True, group_by_object=False, group_by_material=True, keep_vertex_order=False, global_scale=1, path_mode='AUTO')

      # Deselects was selected
      bpy.data.objects[obj.name].select_set(False)
