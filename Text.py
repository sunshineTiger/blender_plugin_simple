#插件信息
bl_info = {
    #这将作为主条目显示在附加组件菜单中"""
    'name': 'Object add',
    #定义脚本所属的组"""
    'category': '3D View', 
    #作者姓名"""
    'author': 'zh', 
    #说明可以在何处找到新功能"""
    'location': 'View 3D > Tool Shelf > CATS', 
    #这个简短的文本帮助用户在阅读插件列表时决定他是否需要插件"""
    'description': '单行解释这个脚本究竟做了什么',
    #脚本版本"""
    'version': (1, 0 , 0),  
    #运行脚本所需的最低 Blender 版本"""
    'blender': (2, 80, 0),
    #显示支持级别（默认为COMMUNITY）"""
    "support" :  "COMMUNITY" ,        
    'warning': '',
}



import bpy

class TestPanel(bpy.types.Panel):
    """ 
    bl_category        面板过滤标签
    bl_context         面板所属的上下文
    bl_description     面板描述
    bl_idname          面板自定义 ID
    bl_label           面板标签
    bl_options         面板类型的选项   DEFAULT_CLOSED        默认关闭，定义面板在创建时是打开还是折叠
                                        HIDE_HEADER           隐藏标题，如果设置为 False，面板会显示一个标题
                                        INSTANCED             实例化面板，此类型的多个面板可用作列表的一部分
                                        HEADER_LAYOUT_EXPAND  展开标题布局，允许标题中的按钮拉伸和收缩以填充整个布局宽度
                                        DRAW_BOX              框样式，带有框小部件主题的显示面板
    bl_order           数字较小的面板默认排列在数字较大的面板之前
    bl_owner_id      
    bl_parent_id       如果设置了这个，面板就会变成子面板
    bl_region_type     面板将用于的区域 类型['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER'中的枚举, 'TOOL_HEADER'], 默认为 'WINDOW'
    bl_space_type      面板将用于的空间 EMPTY 空的。
                                        VIEW_3D 3D 视口，在 3D 环境中操作对象。
                                        IMAGE_EDITOR UV/图像编辑器，查看和编辑图像和 UV 贴图。
                                        NODE_EDITOR 节点编辑器，基于节点的着色和合成工具的编辑器。
                                        SEQUENCE_EDITOR 视频序列器，视频编辑工具。
                                        CLIP_EDITOR 电影剪辑编辑器，运动跟踪工具。
                                        DOPESHEET_EDITOR 摄影表，调整关键帧的时间。
                                        GRAPH_EDITOR 图形编辑器、编辑驱动程序和关键帧插值。
                                        NLA_EDITOR 非线性动画、组合和分层动作。
                                        TEXT_EDITOR 文本编辑器、编辑脚本和文件内文档。
                                        CONSOLE Python 控制台，用于高级编辑和脚本开发的交互式编程控制台。
                                        INFO 信息、操作日志、警告和错误消息。
                                        TOPBAR 顶部栏，屏幕顶部的全局栏，用于每个窗口的全局设置。
                                        STATUSBAR 状态栏，屏幕底部的全局栏，用于显示一般状态信息。
                                        OUTLINER 大纲图、场景图概览和所有可用数据块。
                                        PROPERTIES 属性，编辑活动对象和相关数据块的属性。
                                        FILE_BROWSER 文件浏览器，浏览文件和资产。
                                        SPREADSHEET 电子表格，探索表格中的几何数据。
                                        PREFERENCES 首选项，编辑持久配置设置
                                        
    """  
    
    """
    Blender面板中界面组件是通过UILayout进行组织的. 其主要属性如下:
        row() 定义横向子布局.
        column() 定义竖向子布局.
        split() 按比例拆分行
        column_flow() 定义多列的竖向子布局(根据列,计算行数, 然后按逐列摆放组件)
        box() 定义有外框的竖向子布局
        menu_pie() 饼状菜单
        operator() 放置调用操作器的按钮
        prop() 展示RNA,并把它放在布局中
        label() 显示标签
        separator() 分隔元素
    """
    
    
    
    bl_label = "test panel"#面板标签
    bl_idname="pt_testpanel"#面板自定义 ID
    bl_space_type='VIEW_3D'#
    bl_region_type='UI'
    bl_category='My first addon'
    
    def draw(self,context):
        layout=self.layout
        layout.scale_y = 1.4 
        row=layout.row()
        row.label(text='Add an object',icon='EMPTY_AXIS')
        row=layout.row()
        row.operator("mesh.primitive_cube_add",icon='CUBE') 
        row.operator("mesh.primitive_uv_sphere_add",icon='SPHERE' )
        
        
        
class TestPanelA(bpy.types.Panel):
    bl_label = "test panel A"
    bl_idname = "pt_panel_a"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My first addon'
    bl_parent_id = "pt_testpanel"
    
    def draw(self,context):
        layout=self.layout
        obj = context.object
        row=layout.row()
        row.label(text="Select an option to scale your object",icon="FONT_DATA")
        row=layout.row()
        row.operator("transform.resize")
        layout.scale_y = 1.4 
        col=layout.column()
        col.prop(obj,"scale")
                
class TestPanelB(bpy.types.Panel):
    bl_label = "test panel B"
    bl_idname = "pt_panel_b"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My first addon'   
    bl_parent_id = "pt_testpanel"
    
    def draw(self,context):
        layout=self.layout
        layout.scale_y = 1.4 
        row=layout.row()
        row.label(text="this is panel b",icon="ERROR")
        
class TestPanelC(bpy.types.Panel):
    bl_label = "test panel C"
    bl_idname = "pt_panel_C"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My first addon'   
    bl_parent_id = "pt_testpanel"
    
    def draw(self,context):
        layout=self.layout
        layout.scale_y = 1.4 
        row=layout.row()
        row.label(text="select a special option",icon="COLOR_BLUE")
        row=layout.row()
        row.operator("object.shade_smooth",icon="MOD_SMOOTH",text="Set Smooth shading")
        row=layout.row()
        row.operator("object.shade_flat",icon="MOD_SMOOTH",text="Set Flat shading")
        row=layout.row()
        row.operator("object.subdivision_set",icon="MOD_SMOOTH",text="Set Subdivision shading")
        row=layout.row()
        row.operator("object.modifier_add")
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(TestPanelA)
    bpy.utils.register_class(TestPanelB)
    bpy.utils.register_class(TestPanelC)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(TestPanelA)
    bpy.utils.unregister_class(TestPanelB)
    bpy.utils.unregister_class(TestPanelC)
    
if __name__=="__main__":
    register()