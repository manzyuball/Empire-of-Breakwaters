import re
import math

focus_file = r"c:\Users\kaner\Documents\Paradox Interactive\Hearts of Iron IV\mod\Empire of Breakwaters\common\national_focus\CHI_focus_backup.txt"
out_file = r"c:\Users\kaner\Documents\Paradox Interactive\Hearts of Iron IV\mod\Empire of Breakwaters\common\national_focus\CHI_focus.txt"

with open(focus_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all focuses and their prerequisites
focuses = []
idx = 0
while True:
    start = text.find("focus = {", idx)
    if start == -1: break
    
    # find end
    brace_level = 0
    in_str = False
    offset = text.find("{", start)
    end = -1
    for i in range(offset, len(text)):
        c = text[i]
        if c == '"' and text[i-1] != '\\': in_str = not in_str
        elif not in_str:
            if c == '{': brace_level += 1
            elif c == '}':
                brace_level -= 1
                if brace_level == 0:
                    end = i
                    break
    if end == -1: break
    
    block = text[start:end+1]
    id_m = re.search(r'id\s*=\s*(\w+)', block)
    if id_m:
        fid = id_m.group(1)
        # Find prerequisites
        prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*(\w+)', block)
        focuses.append({'id': fid, 'prereqs': prereqs, 'block': block, 'start': start, 'end': end})
    
    idx = end + 1

# 2. Build Tree & Assign Layout
children_map = {f['id']: [] for f in focuses}
roots = []

for f in focuses:
    if not f['prereqs']:
        roots.append(f['id'])
    else:
        # Just use the first prereq as the layout parent
        parent = f['prereqs'][0]
        if parent in children_map:
            children_map[parent].append(f['id'])

layout = {}
# DFS to assign positions
def layout_tree(node_id, x_offset, parent_id):
    children = children_map.get(node_id, [])
    
    if parent_id is None:
        layout[node_id] = {'x': x_offset, 'y': 0, 'rel': ''}
    else:
        # Position relative to parent
        layout[node_id] = {'x': x_offset, 'y': 1, 'rel': parent_id}
        
    num_children = len(children)
    if num_children == 0:
        return
        
    # Spread children
    spacing = 2
    if num_children == 1:
        layout_tree(children[0], 0, node_id)
    elif num_children == 2:
        layout_tree(children[0], -spacing, node_id)
        layout_tree(children[1], spacing, node_id)
    elif num_children == 3:
        layout_tree(children[0], -spacing * 2, node_id)
        layout_tree(children[1], 0, node_id)
        layout_tree(children[2], spacing * 2, node_id)
    else:
        start_x = -spacing * (num_children - 1) // 2
        for i, child_id in enumerate(children):
            layout_tree(child_id, start_x + (i * spacing), node_id)

# Roots should be spaced out
root_spacing = 30
start_root_x = 25
for i, r in enumerate(roots):
    layout_tree(r, start_root_x + (i * root_spacing), None)

# Vanilla GFX Assignment logic
gf_map = [
    ("army", "GFX_focus_SOV_military_reorganization"),
    ("navy", "GFX_focus_SOV_expand_the_red_fleet"),
    ("air", "GFX_focus_SOV_air_force"),
    ("industry", "GFX_focus_SOV_heavy_industry"),
    ("factory", "GFX_focus_SOV_merge_plants"),
    ("rural", "GFX_focus_SOV_collectivization_process"),
    ("urban", "GFX_focus_SOV_urban_blitz"),
    ("police", "GFX_focus_SOV_nkvd_primacy"),
    ("civil_war", "GFX_focus_SOV_the_anti_soviet_trotskyist_center"),
    ("order", "GFX_focus_SOV_centralize_power"),
    ("paris", "GFX_focus_SOV_the_path_of_marxism_leninism"),
    ("moscow", "GFX_focus_SOV_stalins_cult_of_personality"),
    ("_A_", "GFX_focus_SOV_the_right_opposition"),
    ("_B_", "GFX_focus_SOV_the_workers_dictatorship"),
    ("_C_", "GFX_focus_SOV_the_marxist_leninist_party"),
    ("unite", "GFX_goal_generic_national_unity"),
    ("demand", "GFX_goal_generic_demand_territory")
]

def get_gfx(fid):
    for key, gfx in gf_map:
        if key.lower() in fid.lower():
            return gfx
    return "GFX_focus_SOV_the_antifascist_bloc"

# 3. Apply changes and create new text
new_text = ""
last_end = 0

for f in focuses:
    new_text += text[last_end:f['start']]
    
    block = f['block']
    fid = f['id']
    
    # Remove old layout
    block = re.sub(r'^\s*x\s*=\s*[^\n]*\n', '', block, flags=re.MULTILINE)
    block = re.sub(r'^\s*y\s*=\s*[^\n]*\n', '', block, flags=re.MULTILINE)
    block = re.sub(r'^\s*icon\s*=\s*[^\n]*\n', '', block, flags=re.MULTILINE)
    block = re.sub(r'^\s*relative_position_id\s*=\s*[^\n]*\n', '', block, flags=re.MULTILINE)
    
    l = layout.get(fid, {'x': 0, 'y': 1, 'rel': ''})
    icon = get_gfx(fid)
    
    new_props = f"\n\t\ticon = {icon}\n\t\tx = {l['x']}\n\t\ty = {l['y']}\n"
    if l['rel']:
        new_props += f"\t\trelative_position_id = {l['rel']}\n"
        
    block = re.sub(r'(id\s*=\s*'+fid+r')', r'\1' + new_props, block)
    
    new_text += block
    last_end = f['end'] + 1

new_text += text[last_end:]

with open(out_file, "w", encoding="utf-8") as f2:
    f2.write(new_text)

print("Dynamic layout applied successfully.")
