# Coal Haul changelog

Version numbers: every push to git adds 1 to the last number (0.1.0 → 0.1.1 → … → 0.1.10 → 0.1.100). The middle number changes only when we decide on a big step. 1.0.0 is the first release.

Saves remember the version they were made with. In multiplayer, players must be on the same version: a player on another version is turned away and asked to reload the page.

## 0.1.11 · 24 Nov 2026
- Fixed: walking into a building that is turned (a coal mine set down with R, for example) made the view jump: the camera kept its offset from the player without turning it with the room. The view now stays put however the building is turned
- Added: Settings → General → Saving: how often to autosave (off, every minute, 2, 5 or 10 minutes; every minute as before). Off also means no autosave when the page closes or when you quit to the menu
- Changed: one autosave only: "Before the last autosave" is gone (the old copy is deleted from the browser)
- Changed: the main menu no longer shows a running new game behind it, but a drawn 3D scene of the game: a coal mine with its headframe and pipe pouring coal into a dump truck, the power plant with smoking stacks, a pickup with its trailer driving along the road, the garage, trees and a dusk sky. It fits wide and tall screens, and stands still with "Lighter graphics"
- Added to /check: the autosave setting (with off) and a single autosave in the load list; the menu's 3D background draws
- Added: /test <world> puts a whole test world in place of the map, alone only: /test full (the old map: every building built and switched on along one street, the coal mine full, $100,000), /test haul (the same, and you in a dump truck under the coal mine's pipe, a pickup with a small bulk trailer next to it), /test crane (the same, and the crane kit at the garage). /test alone lists them. Autosave is off from then on, so your saves are untouched: reload the page to get your game back
- Added to /check: each test world sets every building down built along its street with autosave off, and /test haul puts the dump truck under the pipe
- Changed: people are smaller: the player and the other players span one square, arms and hands included (they were 1.4), and fit in a vehicle's seat
- Fixed: the player on foot was drawn on top of a crane's boom; he now walks under it (in the crane's cab he is still drawn on top)
- Added to /check: a person spans one square, and a player on foot is drawn before (under) a crane's boom
- Added to /check: walking into a coal mine turned each of the 4 ways moves neither the player nor the view by more than a normal step

## 0.1.10 · 19 Nov 2026
- Changed: a new game starts on an empty map: no roads and no buildings, only the garage in the top-left corner (chunk 0,0, gate south) with your pickup. You build the rest from the map's Build tab: roads with Roads, buildings with Yards (the power plant and the other production buildings start as construction sites; the shop and the fuel station are built at once). Saved games keep their map
- Changed: the first goal is now "Build a coal mine"; the goals that need the power plant, the fuel station or the shop say to build it first when there is none
- Changed: /check sets every building down where the old start had them for its run (your game is put back afterwards), so every building is still checked
- Added to tools/check.py: a new game starts with only the garage at 0,0 and no roads
- Changed: the Yards tool no longer moves buildings. Its list has one card per kind of building: pick one and click the map to build a new one there (R turns it). Coal mine can always be built, as many as you like; the other kinds can only stand once for now, so their card works only after the one on the map is demolished ("built (one only)"). The separate "New coal mine" card is gone. In a shared game the host refuses to move a building that stands
- Fixed: new coal mines had a thin fence instead of the thick concrete yard walls every other yard has
- Fixed: only the first coal mine got its storage sign. Every coal mine now has one, against the back wall of its yard in line with its pipe (a new game's first mine too; a sign already standing in a saved game stays where it is). Demolishing a building takes its sign away; a new one gets a new sign
- Added to /check: every coal mine has the thick walls and its sign at the back wall in line with its pipe
- Added to /check: the Yards list has one card per kind, the coal mine card builds a new mine and leaves the others where they are, and a standing building cannot be picked or moved
- Fixed: the first coal mine, demolished and placed again with the Yards tool, came back with its building and pipe away from its lot (the building stood on the grass where the mine used to be). Resetting a demolished building also reset its link to its place on the map. A game this happened in comes right when it is loaded again
- Added to /check: the first mine demolished and placed again has its building, lot and pipe together

## 0.1.9 · 19 Nov 2026
- Changed: no storage is global any more: every store belongs to its building. The sawmill's count of sawn planks is the sawmill's own, the garage storage (coal, logs, fuel) is the garage's and the shop storage is the shop's, so a later second copy of a building gets its own. Saves keep the same names, so old saves load unchanged
- Fixed: the garage's storage upgrades (room for 50 → 100 → … of coal, logs, fuel) were not saved or shared with the other players; they are now, like the shop's
- Added to /check: every building's own stores (sawmill planks, garage and shop storage and their room) come back from a save
- Changed: the coal mine is ready for more than one. Every coal mine has its own store, digging, main switch, levels, desk and desk window, pipe and housing, lot (with its own name on the wall: COAL MINE 2) and room (what is put down on its floor stays in it). Each pipe pours from its own mine. A new copy is saved and shared with the other players as a map step, with its stores; old saves have the one mine as before. How a player gets a second mine (what it costs, where) is not decided yet
- Changed: Demolish removes a building for good: its stock, upgrades and whatever lay on its room floor are gone (vehicles and things standing in its lot stay). It no longer goes back to the Yards list to be moved again
- Added: the Yards list (Build tab on the map) has a "New coal mine" card: pick it and click the map to place a new, empty coal mine (as many as you like, wherever there is room; a road to its gate is up to you). A demolished one-of-a-kind building shows as "New power plant", "New garage"… and is placed the same way
- Changed: saves keep every building's place and turn, and every building's stores. Before, places were only rebuilt from the list of map changes, so a step that failed on loading could lose a building
- Changed: in a shared game, a guest who sets a building down or places a new coal mine asks the host: the host checks it against its own map and picks the new mine's name, so two players can never make the same mine or put two buildings on one place. If the place is taken, the guest is told
- Changed: the first goal is now "Get coal from a coal mine" (any coal mine). The arrow that pointed from the player to the next goal is gone; goals will be reworked once every building can have copies
- Changed: at night there is no glow round the player, the other players or a vehicle's cab any more: only headlights, tail and reversing lamps, the lamp over each building's entrance and a crane's work light
- Added to /check: unloading takes only the cargo space selected with V; every building's place and turn is in the save; a demolished mine is gone from the Yards list with its store and room floor; the host refuses a second mine on the same place and never repeats a name; a demolished mine comes back new and empty; a save puts a mine back where it stood without checking the place again
- Changed: /tp knows every coal mine by its own name: /tp mine1, /tp mine2… (the other buildings by their name without spaces: /tp powerplant, /tp garage). Each coal mine's desk window shows its name
- Changed: in a shared game a guest's map message waits for the host: "Asking the host…", then "placed" or "demolished" once the host has done it, or why not
- Changed: the dark coal dust on the ground under the spout is drawn at every coal mine (it was only at the first)
- Added to /check: /tp mine1 and /tp mine2 go to each mine's door and the desk window shows its name; a guest hears "placed" only once the host has placed it
- Added: test panel: "Add a coal mine" puts a new coal mine on the nearest free place. The start map has no free place, so it takes up the roads on the nearest place that has only roads on it
- Added to /check: a second coal mine is added and drawn; each mine digs into its own store; a pipe pours from its own mine; its room, main switch and desk are its own; what lies on its floor stays in its room; it is saved with its place and stores

## 0.1.8 · 19 Nov 2026
- Fixed: the crane's cables over a container on a flatbed (a dump truck's bed or a flatbed trailer) could take the truck or trailer under it instead of the container. They chose by distance to each thing's reference point (a truck's rear axle often lies right under its container). Now the cables take what is on top first (a container on a flatbed, a vehicle on a ramp deck, an attachment on a pallet or a bed), then the nearest by its middle. The yellow mark shows the same choice
- Fixed: a crane could lift a truck with a container still on its flatbed. Now it says to unload the flatbed first
- Added to /check: the cables over a container on every kind of flatbed take the container
- Fixed: a load filled slowly (a truck waiting at the mine while it digs) stopped at 4.99 t of 5: the game called a load full within 0.01 t of full and took nothing more. Loads now fill to exactly their capacity, and every bit the mine digs while you hold Space goes onto the truck. The same for loading logs, rock, iron ore, sand, gravel and fuel, from the garage storage, and for the crusher's and foundry's stores
- Changed: the coal mine has no loading pad any more: a pipe runs out of the middle of the building's back wall to the middle of the chunk behind it, and ends in a round spout showing the coal icon. Park so a cargo space is under the spout and hold Space: coal pours into whichever of your rig's cargo spaces is under it, the truck's own bed or a trailer (no need to select it with V). The spout's rim is green while coal pours, amber when the mine has coal to give, grey when it is empty. The crane's bulk container loads under it too. The other loading pads (quarry, iron mine, crusher) stay as they are for now
- Changed: G empties only the selected part of the rig (V selects it): the truck itself, or one trailer. Its cargo, the items in its slots and the pallets on its flatbed (and, for the truck, on its forks) are gone; the rest of the rig keeps its load. Before, G emptied the whole rig
- Added to /check: G empties only the selected truck or trailer
- Changed: the coal pipe is redrawn: it comes out of a 1 x 2 steel housing on the middle of the mine's back wall (part of the building, so it is solid: you and vehicles stop against it), with the drive motor on its lid and hazard stripes on its face. The chute is round with a shine, bolted in lengths with fittings, and ends in a hooded spout
- Changed: the small trailers (bulk, log, fuel, flatbed, liquid tanker) are the size of the pickup's bed: 2.4 units long and 2 wide (they were 3 x 1.8), with a slightly shorter drawbar, so a pickup and its trailer look like a pair and a pallet fills the small flatbed trailer like it fills the pickup's flatbed. Their loads are unchanged. The small ramp trailer keeps its 3-unit deck so an ATV or a forklift still fits on it; only its width changed
- Changed: the label on the coal pipe: small dark COAL lettering between the last two fittings before the spout, read along the pipe; however the mine is turned it never reads upside down
- Added: the coal mine's control desk has two switches for the pipe, green when on and red when off: "Show icon on pipe" (off, the spout's mouth is the dark inside of the hood) and "Show text on pipe". Saved with the game and shared with the other players
- Changed: the coal pipe turns see-through (it fades to about a third) while a vehicle or trailer is under any part of it, so you can see what you drive, and fades back when it leaves
- Added to /check: under the coal pipe only the cargo space under the spout is loaded, and nothing loads with no cargo space under it
- Changed: at night the nine buildings no longer glow all over: outside, only a warm lamp over the entrance lights the ground in front of the door; inside, the room is always fully lit
- Changed: vehicle lamps at the back are on every unit: with the lights on, the truck and each trailer it pulls show red tail lamps (not only the last trailer); backing up, all of them show white reversing lamps. A truck's back that a semi-trailer lies over shows none. Reversing lamps now only glow, like tail lamps: only the headlights throw a beam
- Added to /check: every vehicle kind's head, tail and reversing lamps, and the lamps at every back with a trailer on its hitch
- Changed: the coal mine desk's first screen shows the coal in store in figures (12.7 / 50 t) with the bar under it across the whole screen, without the coal icon
- Changed: the coal mine desk's second screen: the rails are split into 10 sections, one per tenth of a ton, and the coal cart stands in the section of the first decimal of the coal in store (12.7 t: the 8th section). It steps along as the mine digs and reaches the end as each ton is done; it stands still when the mine is off or full
- Changed: the control desks no longer have a switch. Every desk window shows the building's status instead, with a lamp (green running, amber on but idle or without power, red off) and a note that the main lever on the room's back wall switches it. The goal hints no longer send you to the desk to switch a building on
- Added to /check: every vehicle that carries coal fills to exactly its capacity, from a full mine (at 60, 144 and uneven frames a second) and from an empty mine digging while it waits

## 0.1.7 · 19 Nov 2026
- Added: /check in the chat checks the whole game: every building (built, walked into and out of, main switch thrown, desk window opened), every vehicle kind (put down and driven), every trailer and item, a coal run from the mine to the power plant, every window, every settings tab and a save written and read back. It reads the game's own lists, so whatever is added to them is checked from then on. Alone, your game is put back exactly as it was afterwards; with other players here, only the checks that change nothing run
- Added: /checklist in the chat opens a window with everything /check checks (191 checks today, by group: tap a group to see them), read from the same lists, and the things it does not check yet, so the check can be extended. It changes nothing in the game; a button runs /check
- Added: tools/check.py runs the same check in a test browser before every push, and loads every save kept in tools/saves/ (one per version, so a change that breaks old saves is caught)

## 0.1.6 · 19 Nov 2026
- Changed: every building is 14 x 14 squares like the power plant and the coal mine: the lumberyard, sawmill, quarry, iron mine, crusher, factory and foundry, and their construction sites. Each grew towards its back, over the spot where its (hidden) readout board stood
- Changed: their roofs are laid out for the square shape: same look and materials, the skylights, vents, ducts, cyclones, chimneys and the rest spread over the whole roof
- Changed: you walk in and out of all of them as in the power plant: one entrance in the middle of the front wall, the room drawn on the map, things can be put down on the floor. Their shelves, boards and upgrade / control pads are gone; anything that lay on a shelf is put on the room's floor
- Added: a control desk and chair in each. Space on the desk opens the building's window (the factory and foundry: Control panel and Upgrades tabs). Screen 1 shows the main store, screen 2 a lamp: green running, amber on but no power, red off
- Added: each has one main switch (2 squares) in the middle of its back wall, as in the coal mine: it is the building's on/off switch. The power plant keeps its 6 levers and yard lamps
- Changed: each room has its own floor, painted as one piece in the building's material (boards, stone flags, tiles or concrete)
- Fixed: the grass and the ground of the lots showed a checkerboard of slightly different squares, one per map tile; they are now one even colour
- Changed: the Settings page is split into tabs: General (your name, camera), Sound, Display, Controls (touch and the list of controls) and Keys. It opens on the tab you last used
- Changed: the 9 sound sliders are now 3: Vehicles and work (engines, machines, loading and unloading, horn and reversing beeper), Game (money, buttons and doors, goals, chat) and World and music (wind, birds, crickets, music), under the main volume and Mute all. Settings from before keep the loudest of their old sliders in each group

## 0.1.5 · 19 Nov 2026
- Changed: the coal mine is rebuilt like the power plant: 14 x 14 squares, centred in its lot, with one entrance in the middle and a walk-in room you see into
- Changed: new coal mine roof (winding-engine house, headframe with its ropes, coal bunker) and floor (dark concrete, coal dust, tread plates, hazard stripes)
- Added: the coal mine's main switch in the middle of its back wall; off, it digs no coal
- Added: the coal mine's own control desk and chair. Space on the desk opens the mine's window (coal store, switch, upgrades); its screens show the coal store and a coal cart running while it digs
- Changed: a new game starts with the coal mine switched off and empty. New first goal: switch the coal mine on. Older saves keep their mine digging
- Changed: the horn is a truck air horn that sounds as long as H (or the horn button) is held, and other players hear it, quieter the farther away
- Changed: the squares in reach show inside rooms while you hold an item, as outdoors
- Fixed: passengers could use the horn and the lights; a passenger getting out turned the lights off

## 0.1.4 · 18 Nov 2026
- Changed: you walk in and out of the power plant. The room is drawn over the building with the map all round it, the camera stays on you and there is no jump at the door; other players see the roof from outside and each other inside
- Changed: the power plant room is emptied, with a new concrete floor and one entrance in the middle of the south wall, marked by entrance tiles inside and out
- Added: 6 levers on the power plant's back wall: 4 for the yard's corner pillars, 1 for the 2 gate pillars and the main power lever, which turns everything off. Click one in reach to throw it. They follow the building when it is turned
- Added: lamps on the power plant yard's pillars, lit by their levers while the plant gives power (for testing)
- Added: a control desk (2 x 1) and a chair you can carry and put down. The chair sits in the middle of the desk's long side when put down against it. Space on the desk opens the power plant's window, and the desk lights up when Space would open it. Its 2 screens show the coal store and the yard's lamps (green on, amber no power, red off)
- Added: icons for 14 cargoes, used on pads, in load readouts and on signs
- Added: signs you can carry: a bar sign and a number sign, $60 each in the shop. A sign shows the chosen cargo's store in the yard it stands in (on a site: what has come in), and an out-of-order icon outside any yard. Space on a sign picks what it shows. Every yard starts with one bar sign by its gate
- Changed: items can be put down on the power plant's floor (not on the entrance or the levers); cones, barriers and the desk block you there as outdoors
- Changed: other players' names only show while they are on foot
- Fixed: things inside the power plant could not be picked up
- Fixed: stepping out of the power plant and straight back in was blocked
- Fixed: the power plant's roof went missing after zooming inside; two reach rings showed inside
- Fixed: the player could walk partly into the power plant's walls in the corners

## 0.1.3 · 18 Nov 2026
- Added: saves work across versions. A save is brought up to date when loaded; damaged parts and things the game no longer has are left out instead of breaking the load
- Added: a save from a newer version loads with a warning and is marked in the save list; if a save cannot be loaded, a new map starts and the save stays untouched
- Fixed: saves from 0.1.1 on the bigger power plant: anything that now stands inside a building is moved just outside its nearest wall

## 0.1.2 · 18 Nov 2026
- Fixed: lag on big screens. The streets were drawn from scratch every frame; they are now painted once into the cached ground and only repainted when a street changes
- Changed: the power plant is 14 x 14 squares, centred on the middle chunk of its lot, with a roof laid out for the square shape; its room inside is 14 x 14 too
- Changed: the buildings' readout boards are hidden for now, while the buildings are reworked
- Added: a players list kept with the save. /players opens a window of everyone who has been on the map, where the host can kick, ban or remove a player
- Fixed: a player who joins again no longer gets another starting pickup; they come back on foot where they left
- Added: other players' names above them, also while they drive, drawn over roofs and in the dark
- Added: hovering a vehicle's seats shows the other players sitting in them

## 0.1.1 · 18 Nov 2026
- Fixed: static in the sound. The looping noise behind the wind, engines and machines clicked every time it went round; it now loops seamlessly
- Changed: wind darker and quieter; door, starter and engine stop with less hiss
- Fixed: lag from sound. Sound settings are only sent to the audio when they change, and sounds at rest are switched off until needed

## 0.1.0 · 18 Nov 2026
Version numbering starts here, with everything built so far:
- Hauling coal and building the chain of buildings, on a top-down map with thick coloured walls on every lot
- Vehicles: truck and semi, dump truck, flatbed, crane (with cab view, tools and feet), forklift; traffic barriers
- Day (15 minutes) and night (5 minutes); lights on L, white reversing lamps, crane hook work light
- Camera views on TAB; minimap with optional coordinates
- Main menu, Esc menu, settings (controls, sound channels, touch), saves with names and pictures in the browser's database
- Multiplayer by 5-letter code, chat with commands
- Sounds, all made by the game's own code (no recordings): an engine for each vehicle (diesels, petrol car, ATV, forklift), engine start and stop, low fuel and out of fuel, bumps and crashes, brakes and air brakes, footsteps, off-road rumble, reversing beeper, horn on H, lights on and off, crane hydraulics and tools, hitching, lifting, winching, dumping, buildings at work, wind, birds, crickets, dusk and dawn, building and demolishing, money, goals, saving, players joining and leaving, quiet music
- PC first, phones supported (joystick where you touch, button arc)
