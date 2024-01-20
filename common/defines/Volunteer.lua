NDefines.NAI.SEND_VOLUNTEER_EVAL_BASE_DISTANCE = 750.0  -- How far away it will evaluate sending volunteers if not a major power
NDefines.NAI.SEND_VOLUNTEER_EVAL_MAJOER_POWER = 3.5 	-- How willing major powers are to send volunteers.
NDefines.NAI.SEND_VOLUNTEER_EVAL_CONTAINMENT_FACTOR = 0.5 -- How much AI containment factors into its evaluation of sending volunteers.
NDefines.NAI.SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY = 15			-- Added to AI desire to send volunteers if recipent is same ideology (and AI can't declare war on recipient)
NDefines.NAI.SEND_VOLUNTEER_AIDESIRE_SAME_IDEOLOGY_CIVIL_WAR = 5		-- Added to AI desire to send volunteers if recipent is same ideology and they are currently in civil war
NDefines.NDiplomacy.VOLUNTEERS_PER_COUNTRY_ARMY = 0.1			-- Each army unit owned by the source country contributes this amount of volunteers to the limit.
NDefines.NDiplomacy.VOLUNTEERS_RETURN_EQUIPMENT = 1.0			-- Returning volunteers keep this much equipment
NDefines.NDiplomacy.VOLUNTEERS_TRANSFER_SPEED = 2				-- days to transfer a unit to another nation
NDefines.NDiplomacy.VOLUNTEERS_DIVISIONS_REQUIRED = 20			-- This many divisons are required for the country to be able to send volunteers.
NDefines.NDiplomacy.TENSION_VOLUNTEER_FORCE_DIVISION = 0		-- Amount of tension generated for each sent division
NDefines.NCountry.STARTING_COMMAND_POWER = 60.0					-- starting command power for every country
NDefines.NCountry.BASE_MAX_COMMAND_POWER = 999.0					-- base value for maximum command power
NDefines.NCountry.BASE_COMMAND_POWER_GAIN = 1.5	
NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 0.85				-- base value for daily command power gain
NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN = 2
NDefines.NSupply.CAPITAL_INITIAL_SUPPLY_FLOW = 8.0 -- 5.0
NDefines.NSupply.CAPITAL_STARTING_PENALTY_PER_PROVINCE = 0.5 -- 0.5
NDefines.NSupply.CAPITAL_ADDED_PENALTY_PER_PROVINCE = 1.8 -- 1.2
NDefines.NSupply.NODE_INITIAL_SUPPLY_FLOW = 4.0 -- 2.8
NDefines.NSupply.NODE_STARTING_PENALTY_PER_PROVINCE = 0.50 -- 0.50
NDefines.NSupply.NODE_ADDED_PENALTY_PER_PROVINCE = 1.0 -- 0.70
NDefines.NSupply.NAVAL_BASE_INITIAL_SUPPLY_FLOW = 4.0 -- 3.5
NDefines.NSupply.NAVAL_BASE_STARTING_PENALTY_PER_PROVINCE = 0.8 -- 0.8
NDefines.NSupply.NAVAL_BASE_ADDED_PENALTY_PER_PROVINCE = 1.5 --1.0
NDefines.NSupply.RAILWAY_BASE_FLOW = 10.0 -- 10.0
NDefines.NSupply.RAILWAY_FLOW_PER_LEVEL = 10 --5.0
NDefines.NSupply.RAILWAY_FLOW_PENALTY_PER_DAMAGED = 10 -- 5.0
NDefines.NSupply.SUPPLY_FLOW_DROP_REDUCTION_AT_MAX_INFRA = 0.50 -- 0.30
NDefines.NSupply.SUPPLY_HUB_FULL_MOTORIZATION_BONUS = 4.0 -- 2.2
NDefines.NGame.POPULATION_YEARLY_GROWTH_BASE = 0
NDefines.NOperatives.AGENCY_CREATION_FACTORIES = 99999
NDefines.NProduction.DEFAULT_MAX_NAV_FACTORIES_PER_LINE = 20
NDefines.NProduction.CONVOY_MAX_NAV_FACTORIES_PER_LINE = 100
NDefines.NProduction.CAPITAL_SHIP_MAX_NAV_FACTORIES_PER_LINE = 15
NDefines.NProduction.MAX_MIL_FACTORIES_PER_LINE = 500

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 0
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 0
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 0
NDefines.NMilitary.LAND_EQUIPMENT_BASE_COST = 0
NDefines.NMilitary.LAND_EQUIPMENT_RAMP_COST = 0
NDefines.NMilitary.NAVAL_EQUIPMENT_BASE_COST = 0
NDefines.NMilitary.NAVAL_EQUIPMENT_RAMP_COST = 0
NDefines.NMilitary.AIR_EQUIPMENT_BASE_COST = 0
NDefines.NMilitary.AIR_EQUIPMENT_RAMP_COST = 0
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 240			-- how many divisions a corps commander is limited to. 0 = inf, < 0 = blocked
NDefines.NMilitary.CORPS_COMMANDER_ARMIES_CAP = 0	-- how many armies a corps commander is limited to. 0 = inf, < 0 = blocked
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 10			-- how many divisions a field marshall is limited to. 0 = inf, < 0 = blocked
NDefines.NMilitary.FIELD_MARSHAL_ARMIES_CAP = -1				-- how many armies a field marshall is limited to. 0 = inf, < 0 = blocked
NDefines.NMilitary.GARRISON_ORDER_ARMY_CAP_FACTOR = 10.0		-- armies gets increased cap when they are garrisoned

NDefines.NBuildings.INFRASTRUCTURE_RESOURCE_BONUS = 0.75
NDefines.NBuildings.MAX_BUILDING_LEVELS = 35
NDefines.NBuildings.MAX_SHARED_SLOTS = 50
NDefines.NGame.GAME_SPEED_SECONDS = { 0.5, 0.25, 0.15, 0.1, 0.0 }
NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 1000
NDefines.NGame.LAG_DAYS_FOR_PAUSE = 2500
NDefines.NDiplomacy.TENSION_TIME_SCALE_MONTHLY_FACTOR = 0.0
NDefines.NCountry.POPULATION_YEARLY_GROWTH_BASE = 0.0