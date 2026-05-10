import cadquery as cq



#import dxf
bicep_2d=cq.importers.importDXF("assets/svg/dxf_derivatives/bicep_mirror.dxf")

# # Bicep emoji
# bicep = (
#     cq.Workplane("XY")
#     .importDXF("svg/bicep.dxf")
#     .extrude(3.0)  # 3mm extrusion
# )
# cq.exporters.export(bicep, "bicep_test.stl")
# print("Bicep STL exported")

# # Flame emoji
# flame = (
#     cq.Workplane("XY")
#     .importDXF("svg/flame.dxf")
#     .extrude(3.0)
# )
bicep_3d = cq.Workplane("XY").add(bicep_2d).extrude(3.0)
# cq.exporters.export(bicep_3d, "bicep_test.stl")
# print("Bicep STL exported")