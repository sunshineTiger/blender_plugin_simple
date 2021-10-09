#插件信息
bl_info = {
    #这将作为主条目显示在附加组件菜单中"""
    'name': 'shader library',
    #定义脚本所属的组"""
    'category': '3D View', 
    #作者姓名"""
    'author': 'zh', 
    #说明可以在何处找到新功能"""
    'location': 'View 3D > Tool Shelf ', 
    #这个简短的文本帮助用户在阅读插件列表时决定他是否需要插件"""
    'description': '',
    #脚本版本"""
    'version': (1, 0 , 0),  
    #运行脚本所需的最低 Blender 版本"""
    'blender': (2, 80, 0),
    #显示支持级别（默认为COMMUNITY）"""
    "support" :  "COMMUNITY" ,        
    'warning': '',
}
import bpy
from bpy.types import Panel, Operator,Header,Menu

class SharderMainPanel(Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='Shader Library' 
    
    def draw(self,context):
        layout=self.layout
        row=layout.row()
        row.label(text = 'Select a shader to be added')
        row.operator('shader.diamond_operator')
        
class SHADER_OT_DIAMOND(Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"
    
    def execute(self,context):
        material_diamond = bpy.data.materials.new(name= "Diamond")
        material_diamond.use_nodes = True
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        material_output=material_diamond.node_tree.nodes.get('Material Output')
        material_output.location=(400,0)
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass') 
        glass1_node.location = (-600,0)
        glass1_node.label = "glass1_node"
        glass1_node.inputs[0].default_value = (1, 0, 0, 1) 
        glass1_node.inputs[1].default_value = 0
        glass1_node.inputs[2].default_value = 1.450
        
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass') 
        glass2_node.location = (-600,-150)
        glass2_node.label = "glass2_node"
        glass2_node.inputs[0].default_value = (0, 1, 0, 1) 
        glass2_node.inputs[1].default_value = 0
        glass2_node.inputs[2].default_value = 1.450
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass') 
        glass3_node.location = (-600,-300)
        glass3_node.label = "glass3_node"
        glass3_node.inputs[0].default_value = (0, 0, 1, 1) 
        glass3_node.inputs[1].default_value = 0
        glass3_node.inputs[2].default_value = 1.450 

        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader') 
        add1_node.location = (-400,-50)
        add1_node.label = "Add 1"
        add1_node.hide = True
        add1_node.select = False
        
        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader') 
        add2_node.location = (-100,0)
        add2_node.label = "Add 2"
        add2_node.hide = True
        add2_node.select = False
        
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass') 
        glass4_node.location = (-150,-150)
        glass4_node.label = "glass4_node"
        glass4_node.inputs[0].default_value = (1, 1, 1, 1) 
        glass4_node.inputs[1].default_value = 0
        glass4_node.inputs[2].default_value = 1.450 
        glass4_node.select = False 

        mix1_node =material_diamond.node_tree.nodes.new('ShaderNodeMixShader') 
        mix1_node.label = "mix1_node"
        mix1_node.location = (200,0)
        mix1_node.select = False
        
        material_diamond.node_tree.links.new(glass1_node.outputs[0],add1_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass2_node.outputs[0],add1_node.inputs[1])
        
        material_diamond.node_tree.links.new(add1_node.outputs[0],add2_node.inputs[0])
        
        material_diamond.node_tree.links.new(glass3_node.outputs[0],add2_node.inputs[1])
 
        material_diamond.node_tree.links.new(add2_node.outputs[0],mix1_node.inputs[1])
        
        material_diamond.node_tree.links.new(glass4_node.outputs[0],mix1_node.inputs[2])
        
        material_diamond.node_tree.links.new(mix1_node.outputs[0],material_output.inputs[0])

        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}

classes=[SHADER_OT_DIAMOND,SharderMainPanel]

def register():
    #bpy.utils.register_class(SHADER_OT_DIAMOND)
   # bpy.utils.register_class(SharderMainPanel)
    for cls in classes:
        bpy.utils.register_class(cls)
   
def unregister():
   # bpy.utils.unregister_class(SHADER_OT_DIAMOND)
    #bpy.utils.unregister_class(SharderMainPanel)
    for cls in classes:
        bpy.utils.unregister_class(cls)
   
    
if __name__=="__main__":
    register()