import bpy
import mixamo_rig

actionList=['']
personList=['']

def clearAll():
    # 删除场景中的所有对象
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # 删除场景中的所有材质
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

    # 删除场景中的所有纹理
    for texture in bpy.data.textures:
        bpy.data.textures.remove(texture)

    # 删除场景中的所有图像
    for image in bpy.data.images:
        bpy.data.images.remove(image)

    # 删除场景中的所有动作
    for action in bpy.data.actions:
        bpy.data.actions.remove(action)
        
def createActionFbx(person, action):
    clearAll()

    bpy.ops.import_scene.gltf(filepath="path" + person)
    person_obj = bpy.context.selected_objects[0]

    # 检查是否有外部数据需要解包
    bpy.context.view_layer.objects.active = person_obj
    bpy.ops.file.unpack_all(method='USE_LOCAL')

    # 选中骨骼
    for pose_bone in bpy.context.active_object.pose.bones:
        pose_bone.bone.select = True

    #sheng cheng dongzuo bangding
    bpy.ops.mr.make_rig()

    # 导入动作
    bpy.ops.import_scene.fbx(filepath="path" + action)
    action_object = bpy.context.selected_objects[0]
    bpy.context.scene.mix_source_armature = action_object

    # 选中person
    bpy.context.view_layer.objects.active = person_obj

    # 绑定动作
    bpy.ops.mr.import_anim_to_rig()

    # 删除动作的模型
    bpy.data.objects.remove(action_object)

    # 导出
    if person.find("man") != -1:
        path = "/{}".format("man"+action)
    else:
        path = "/{}".format("woman"+action)
    bpy.context.view_layer.objects.active = person_obj
    bpy.ops.export_scene.fbx(
        filepath=path,  # 设置导出的文件路径
        check_existing=False,  # 检查现有文件
        use_selection=False,  # 只导出所选对象
        object_types = {"ARMATURE", "MESH"}, # 导出哪种类型的对象
        path_mode="COPY",
        embed_textures=True,  #嵌入纹理
        use_mesh_modifiers=True
    )


for p in range(len(personList)):
    for a in range(len(actionList)):
        if p.find(".glb") != -1 and a.find(".fbx") != -1:
            createActionFbx(personList[p], actionList[a])
         