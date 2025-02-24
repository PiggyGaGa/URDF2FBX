from urdf_importer.robot_builder import RobotBuilder
import bpy
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='urdf2fbx')
    parser.add_argument('--urdf', type=str, required=True, help='urdf file path')
    parser.add_argument('--merge_duplicate_materials', action="store_true", help='merge duplicate materials or not')
    parser.add_argument('--should_check_material_name', action="store_true", help='With or without name check, Merge materials if they have the same name and same content')
    parser.add_argument('--rename_materials', action="store_true", help='rename materials')
    parser.add_argument('--apply_weld', action="store_true", help='Apply weld modifier')
    parser.add_argument('--unique_name', action="store_true", help='unique name')
    parser.add_argument('--scale_unit', type=float, default=1.0, help='scale unit, unreal engine is 0.01 default')
    parser.add_argument('--fbx', type=str, default='./result.fbx', help='fbx file path to export')


    
    args = parser.parse_args()

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')
    print('import urdf')
    filepath = args.urdf  # urdf file path
    merge_duplicate_materials = args.merge_duplicate_materials  # merge_duplicate_materials
    should_check_material_name = args.should_check_material_name # "With or without name check", "Merge materials if they have the same name and same content"
    rename_materials = args.rename_materials  # rename materials
    apply_weld = args.apply_weld    # Apply weld modifier
    unique_name = args.unique_name     # Each texture has an unique name
    scale_unit = args.scale_unit    # Scale unit (for Unreal Engine is 0.01)
    
    ## build Robot
    urdf_robot_instance = RobotBuilder(filepath, merge_duplicate_materials, should_check_material_name, rename_materials, apply_weld, unique_name, scale_unit)
    
    ## export fbx file
    fbx_file_path = args.fbx
    print('export!!!\n')
    bpy.ops.export_scene.fbx(filepath = fbx_file_path, object_types={"ARMATURE", "MESH"}, mesh_smooth_type="FACE", add_leaf_bones=False)