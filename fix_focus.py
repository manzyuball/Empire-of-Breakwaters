import re

focus_file = r"c:\Users\kaner\Documents\Paradox Interactive\Hearts of Iron IV\mod\Empire of Breakwaters\common\national_focus\CHI_focus.txt"

with open(focus_file, "r", encoding="utf-8") as f:
    text = f.read()

mapping = {
    # Phase 1
    "CHI_start_influence": (40, 0, "", "GFX_focus_SOV_the_marxist_leninist_party"),
    "CHI_secure_the_coast": (-4, 1, "CHI_start_influence", "GFX_focus_SOV_the_road_of_life"),
    "CHI_influence_factions": (0, 1, "CHI_start_influence", "GFX_goal_generic_demand_territory"),
    "CHI_political_fund": (4, 1, "CHI_start_influence", "GFX_SOV_war_economy_ccp_2d_sov_compatibility"),
    
    "CHI_order_prepare": (-15, 1, "CHI_influence_factions", "GFX_focus_SOV_the_right_opposition"),
    "CHI_paris_prepare": (0, 1, "CHI_influence_factions", "GFX_focus_SOV_the_path_of_marxism_leninism"),
    "CHI_moscow_prepare": (15, 1, "CHI_influence_factions", "GFX_focus_SOV_stalins_cult_of_personality"),
    
    "CHI_industrial_nexus": (-3, 1, "CHI_order_prepare", "GFX_focus_SOV_heavy_industry"),
    "CHI_urban_propaganda": (-3, 1, "CHI_paris_prepare", "GFX_focus_SOV_military_purge"),
    "CHI_workers_strike": (3, 1, "CHI_paris_prepare", "GFX_focus_SOV_military_purge"),
    
    "CHI_control_the_rural": (0, 1, "CHI_moscow_prepare", "GFX_focus_SOV_merge_plants"),
    "CHI_peasant_uprising": (-3, 1, "CHI_moscow_prepare", "GFX_focus_SOV_behead_the_snake"),
    "CHI_local_militia": (3, 1, "CHI_moscow_prepare", "GFX_focus_SOV_assassinate_trotsky"),
    
    "CHI_faction_assassination": (-5, 2, "CHI_influence_factions", "GFX_focus_SOV_purge_bukharinists"),
    "CHI_faction_cooperation": (0, 2, "CHI_influence_factions", "GFX_focus_SOV_the_center_ccp_2d_sov_compatibility"),
    "CHI_fund_accumulation": (5, 2, "CHI_influence_factions", "GFX_SOV_war_economy_ccp_2d_sov_compatibility"),
    
    "CHI_arms_import": (-2, 3, "CHI_influence_factions", "GFX_focus_SOV_foreign_experts"),
    "CHI_the_reckoning_close": (0, 3, "CHI_influence_factions", "GFX_focus_SOV_the_antifascist_bloc"),
    "CHI_final_preparation": (2, 3, "CHI_influence_factions", "GFX_focus_SOV_strengthen_the_mobilization_plan"),
    
    # Route A
    "CHI_A_civil_war": (0, 4, "CHI_order_prepare", "GFX_focus_SOV_the_anti_soviet_trotskyist_center"),
    "CHI_A_request_angloJP": (-2, 1, "CHI_A_civil_war", "GFX_focus_SOV_the_antifascist_bloc"),
    "CHI_A_fight_alone": (2, 1, "CHI_A_civil_war", "GFX_focus_SOV_defense_industry"),
    "CHI_A_new_order": (0, 2, "CHI_A_civil_war", "GFX_focus_SOV_centralize_power"),
    "CHI_A_approach_allies": (-3, 1, "CHI_A_new_order", "GFX_focus_SOV_foreign_policy"),
    "CHI_A_coastal_negotiation": (-1, 1, "CHI_A_approach_allies", "GFX_focus_SOV_the_road_of_life"),
    "CHI_A_manchuria_talks": (1, 1, "CHI_A_approach_allies", "GFX_focus_SOV_eastern_development"),
    "CHI_A_full_sovereignty": (0, 1, "CHI_A_coastal_negotiation", "GFX_goal_generic_national_unity"),
    "CHI_A_export_economy": (3, 1, "CHI_A_new_order", "GFX_SOV_war_economy_ccp_2d_sov_compatibility"),
    "CHI_A_labor_concentration": (-1, 1, "CHI_A_export_economy", "GFX_focus_SOV_heavy_industry"),
    "CHI_A_industrial_expansion": (1, 1, "CHI_A_export_economy", "GFX_focus_SOV_development_of_tankograd"),
    "CHI_A_trade_dominance": (0, 1, "CHI_A_industrial_expansion", "GFX_goal_generic_trade"),
    "CHI_A_suppress_left": (0, 1, "CHI_A_new_order", "GFX_focus_SOV_military_purge"),
    "CHI_A_labor_control_law": (-1, 1, "CHI_A_suppress_left", "GFX_goal_generic_suppress_resistance"),
    "CHI_A_secret_police": (1, 1, "CHI_A_suppress_left", "GFX_focus_SOV_nkvd_primacy"),
    "CHI_A_iron_stability": (0, 1, "CHI_A_secret_police", "GFX_focus_SOV_stalins_cult_of_personality"),
    "CHI_A_modernize_army": (-2, 2, "CHI_A_new_order", "GFX_focus_SOV_military_reorganization"),
    "CHI_A_naval_buildup": (2, 2, "CHI_A_new_order", "GFX_focus_SOV_expand_the_red_fleet"),
    
    # Route B
    "CHI_B_revolution": (0, 4, "CHI_paris_prepare", "GFX_focus_SOV_the_workers_dictatorship"),
    "CHI_B_urban_blitz": (-2, 1, "CHI_B_revolution", "GFX_goal_generic_attack_allies"),
    "CHI_B_peoples_government": (2, 1, "CHI_B_revolution", "GFX_focus_SOV_soviet_democracy"),
    "CHI_B_urban_network": (0, 2, "CHI_B_revolution", "GFX_focus_SOV_heavy_industry"),
    "CHI_B_maximize_industry": (-3, 1, "CHI_B_urban_network", "GFX_focus_SOV_the_third_five_year_plan"),
    "CHI_B_central_zone_full": (0, 1, "CHI_B_maximize_industry", "GFX_focus_SOV_merge_plants"),
    "CHI_B_workers_paradise": (0, 1, "CHI_B_central_zone_full", "GFX_goal_generic_construct_civ_factory"),
    "CHI_B_rural_neglect": (3, 1, "CHI_B_urban_network", "GFX_focus_SOV_collectivization_process"),
    "CHI_B_crush_rural_economy": (-1, 1, "CHI_B_rural_neglect", "GFX_focus_SOV_secure_the_administration"),
    "CHI_B_anti_guerrilla": (1, 1, "CHI_B_rural_neglect", "GFX_focus_SOV_behead_the_snake"),
    "CHI_B_total_urban_control": (0, 1, "CHI_B_anti_guerrilla", "GFX_focus_SOV_centralize_power"),
    "CHI_B_elite_divisions": (0, 1, "CHI_B_urban_network", "GFX_focus_SOV_military_reorganization"),
    "CHI_B_fourth_inter_solidarity": (-1, 1, "CHI_B_elite_divisions", "GFX_focus_SOV_the_antifascist_bloc"),
    "CHI_B_coastal_liberation_plan": (1, 1, "CHI_B_elite_divisions", "GFX_focus_SOV_the_road_of_life"),
    "CHI_B_break_the_coast": (0, 1, "CHI_B_coastal_liberation_plan", "GFX_focus_SOV_naval_infantry"),
    "CHI_B_world_revolution_east": (0, 1, "CHI_B_fourth_inter_solidarity", "GFX_focus_SOV_the_comintern"),
    "CHI_B_industrial_army": (-2, 2, "CHI_B_urban_network", "GFX_focus_SOV_development_of_tankograd"),
    "CHI_B_red_navy": (2, 2, "CHI_B_urban_network", "GFX_focus_SOV_expand_the_red_fleet"),
    
    # Route C
    "CHI_C_uprising": (0, 4, "CHI_moscow_prepare", "GFX_focus_SOV_the_marxist_leninist_party"),
    "CHI_C_surround_cities": (-2, 1, "CHI_C_uprising", "GFX_goal_generic_attack_allies"),
    "CHI_C_peoples_victory": (2, 1, "CHI_C_uprising", "GFX_focus_SOV_stalins_cult_of_personality"),
    "CHI_C_trap_paris": (-1, 2, "CHI_C_uprising", "GFX_focus_SOV_purge_bukharinists"),
    "CHI_C_tolerate_paris": (1, 2, "CHI_C_uprising", "GFX_focus_SOV_the_antifascist_bloc"),
    "CHI_C_land_reform": (0, 1, "CHI_C_trap_paris", "GFX_focus_SOV_collectivization_process"),
    "CHI_C_rural_revival": (-2, 1, "CHI_C_land_reform", "GFX_goal_generic_construct_civ_factory"),
    "CHI_C_collective_farming": (0, 1, "CHI_C_rural_revival", "GFX_focus_SOV_collectivization_process"),
    "CHI_C_rural_industry": (2, 1, "CHI_C_land_reform", "GFX_focus_SOV_heavy_industry"),
    "CHI_C_peoples_army": (0, 1, "CHI_C_tolerate_paris", "GFX_focus_SOV_military_reorganization"),
    "CHI_C_soviet_equipment": (-2, 1, "CHI_C_peoples_army", "GFX_focus_SOV_foreign_experts"),
    "CHI_C_mass_assault_doctrine": (2, 1, "CHI_C_peoples_army", "GFX_goal_generic_army_motorized"),
    "CHI_C_urban_siege_tactics": (0, 1, "CHI_C_mass_assault_doctrine", "GFX_focus_SOV_military_engineering_university"),
    "CHI_C_soviet_alliance": (0, 1, "CHI_C_soviet_equipment", "GFX_focus_SOV_the_comintern"),
    "CHI_C_soviet_advisors": (1, 1, "CHI_C_soviet_equipment", "GFX_focus_SOV_foreign_experts"),
    "CHI_C_coastal_peoples_war": (0, 2, "CHI_C_land_reform", "GFX_focus_SOV_the_road_of_life"),
    "CHI_C_manchuria_joint_op": (0, 2, "CHI_C_peoples_army", "GFX_focus_SOV_eastern_development"),
    "CHI_C_peoples_republic": (0, 1, "CHI_C_coastal_peoples_war", "GFX_focus_SOV_soviet_democracy"),
    "CHI_C_self_reliance": (-2, 1, "CHI_C_peoples_republic", "GFX_SOV_war_economy_ccp_2d_sov_compatibility"),
    "CHI_C_red_navy": (2, 1, "CHI_C_peoples_republic", "GFX_focus_SOV_expand_the_red_fleet"),
    
    # Unification
    "CHI_unite_china": (40, 25, "", "GFX_goal_generic_national_unity"),
    "CHI_deal_with_warlords": (0, 1, "CHI_unite_china", "GFX_focus_SOV_centralize_power"),
    "CHI_crush_warlords": (-2, 1, "CHI_deal_with_warlords", "GFX_goal_generic_major_war"),
    "CHI_integrate_warlords": (2, 1, "CHI_deal_with_warlords", "GFX_focus_SOV_the_antifascist_bloc"),
    "CHI_claim_tibet": (-1, 1, "CHI_crush_warlords", "GFX_goal_generic_demand_territory"),
    "CHI_claim_sinkiang": (1, 1, "CHI_integrate_warlords", "GFX_goal_generic_demand_territory"),
    "CHI_expel_foreign_powers": (0, 2, "CHI_deal_with_warlords", "GFX_focus_SOV_military_purge"),
    "CHI_demand_macau": (-2, 1, "CHI_expel_foreign_powers", "GFX_focus_SOV_the_road_of_life"),
    "CHI_demand_kwangchow": (2, 1, "CHI_expel_foreign_powers", "GFX_focus_SOV_naval_infantry"),
    "CHI_final_victory": (0, 1, "CHI_demand_macau", "GFX_focus_SOV_stalins_cult_of_personality"),
}

def process_focuses(text):
    result = ""
    idx = 0
    while True:
        # Match 'focus = {' or 'shared_focus = {'
        start = text.find("focus = {", idx)
        start_shared = text.find("shared_focus = {", idx)
        
        found_start = -1
        if start != -1 and start_shared != -1:
            found_start = min(start, start_shared)
        else:
            found_start = max(start, start_shared)
            
        if found_start == -1:
            result += text[idx:]
            break
            
        result += text[idx:found_start]
        
        # Count braces to find the end of block
        brace_level = 0
        in_string = False
        end = -1
        offset = text.find("{", found_start)
        
        for i in range(offset, len(text)):
            c = text[i]
            if c == '"' and text[i-1] != '\\':
                in_string = not in_string
            elif not in_string:
                if c == '{':
                    brace_level += 1
                elif c == '}':
                    brace_level -= 1
                    if brace_level == 0:
                        end = i
                        break
        
        if end == -1:
            result += text[found_start:]
            break
            
        focus_block = text[found_start:end+1]
        
        # Check if ID is in mapping
        id_match = re.search(r'id\s*=\s*(\w+)', focus_block)
        if id_match:
            focus_id = id_match.group(1)
            if focus_id in mapping:
                x, y, rel, icon = mapping[focus_id]
                
                # Strip old coords and icon
                focus_block = re.sub(r'^\s*x\s*=\s*[^\n]*\n', '', focus_block, flags=re.MULTILINE)
                focus_block = re.sub(r'^\s*y\s*=\s*[^\n]*\n', '', focus_block, flags=re.MULTILINE)
                focus_block = re.sub(r'^\s*icon\s*=\s*[^\n]*\n', '', focus_block, flags=re.MULTILINE)
                focus_block = re.sub(r'^\s*relative_position_id\s*=\s*[^\n]*\n', '', focus_block, flags=re.MULTILINE)
                
                # Inject new properties right after id
                new_props = f"\n\t\ticon = {icon}\n\t\tx = {x}\n\t\ty = {y}\n"
                if rel:
                    new_props += f"\t\trelative_position_id = {rel}\n"
                    
                focus_block = re.sub(r'(id\s*=\s*'+focus_id+r')', r'\1' + new_props, focus_block)
        
        result += focus_block
        idx = end + 1
        
    return result

new_text = process_focuses(text)

with open(focus_file, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Safely replaced focus tree.")
