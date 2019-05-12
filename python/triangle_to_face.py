import bpy

def clean():
    all = bpy.context.selectable_objects
    for item in all:
        if(item.type != 'MESH'):
            continue
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.tris_convert_to_quads()
        bpy.ops.object.editmode_toggle()
    

if __name__ == "__main__":
    clean()
