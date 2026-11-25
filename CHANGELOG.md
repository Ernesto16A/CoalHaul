# Coal Haul changelog

Version numbers: every push to git adds 1 to the last number (0.1.0 → 0.1.1 → … → 0.1.10 → 0.1.100). The middle number changes only when we decide on a big step. 1.0.0 is the first release.

Saves remember the version they were made with. In multiplayer, players must be on the same version: a player on another version is turned away and asked to reload the page.

## 0.1.29 · 25 Nov 2026
- Demolishing a building no longer deletes what lay on its room floor: those items stay on the ground where they lay, in the now empty lot (the start kit's pump and hoses in the garage house, for example). Its bulk store is still emptied, and its yard sign still goes. Vehicles stored in the garage stay stored and come out of the new garage.
- The crusher's rock unloading place is now a grate like the power plant's (same place and size), with the rock it holds seen in its hopper.
- Unloading goes before a pipe: a rig unloading somewhere (a grate, a pad) while part of it is under a pipe unloads first, and the pipe does not pour during that press of Space. Once it is empty: let go of Space and press it again to load from the pipe (the game says so).
- Fix: a hose on a water pump can be taken off again. Right-click the pump (one hose at a time), either end of the pump, the hose's end on a tank or its end lying on the ground: the whole hose goes into your hands. The pump's ends are also easier to point at.
- The crusher loads by two pipes behind the building instead of its loading pad and the S/G lever (both are gone): a GRAVEL pipe from the building's back wall and a SAND pipe from a housing standing free in the yard (2 squares in from the back wall, on a concrete footing), each spout 5 squares from its housing. A rig under both spouts at once loads nothing and the player is told to move under just one. Icon and text switches for both pipes are in the crusher's upgrade window. The crusher and quarry shop texts now say their vehicles appear beside the building.
- The iron mine loads by a pipe too: an ore pipe instead of its IRON ORE LOADING pad, the same as the quarry's (its colour, 'IRON ORE' lettering, the ore icon, rust-red bits falling while it pours, the two switches in its window). The check covers both.
- The quarry loads like the coal mine: a rock pipe instead of its ROCK LOADING pad. A solid housing on the middle of the building's back wall, the pipe to the middle of the chunk behind it, its spout there (rim green while rock pours, amber with rock to give, grey when empty; grey stones fall while it pours), see-through while a vehicle is under it, 'ROCK' lettering and the rock icon in the spout. Park any cargo space of your rig under the spout and hold Space: 30% of its capacity a second, from the quarry's store. The quarry's window has the two switches (icon, text on the pipe). Before it is built, its site still takes coal on the same spot. Check added.

## 0.1.28 · 25 Nov 2026
- Fix: getting out of a vehicle (or switching its lights) could stop the game step, so the player could no longer move: a vehicle's health was kept in the same field as the crane's hook lamp, and the lamp's on/off overwrote it. Health has a field of its own now, and it is really in the save (it was not), and so is dirt (it was not either).
- A frame error is now shown in a red banner at the top (the version, the error and where it happened, to copy into a report; a click closes it), and the game keeps drawing even when the error is in the game step (the player could not move but nothing said why).

## 0.1.27 · 25 Nov 2026
- Freezes: a mistake in one frame no longer stops the game: the game goes on and says once 'Something went wrong (…)', to be reported. The loops that keep an angle within one turn and the ones along a trailer chain can no longer run forever (an infinite angle or a chain looping on itself used to hang the tab). Looked for after a freeze reported on getting out of the pickup on a rebuilt garage's yard (not reproduced).
- The big map's Build tab, zoomed in, shows the live map under the tools (like the Map tab does), so you see the real ground, roads and yards where you build. A yard picked to be put down shows as a ghost under the mouse: its lot (green where it fits, red where it does not) with its gates, and its buildings' outlines where they would stand, turned with it (R). Zoomed out, the drawn map as before. Check added.

## 0.1.26 · 25 Nov 2026
- Getting into a vehicle sounds new (option G): two clear rising notes, then a short engine blip when the engine can start (no blip with an empty tank or a broken-down vehicle, nor when getting in as a passenger). The old door thud and the five starter cranks are gone; getting out still plays the door and the engine stopping.
- Vehicle health: a new bar under the fuel bar (green, orange under 50%, red under 25%). Every km driven takes 1%; a crash takes 0.25% for each km/h above 5 (a 40 km/h crash: about 9%). At 0% the vehicle breaks down and will not move. In the garage, at the control pad in the house: a stored vehicle shows its health, and its Parts view has Repair (back to 100%, up to 30% of the vehicle's price for a wreck); one broken down on the map can be towed home into a free slot for €100. In the save. Check added.
- The fuel station reworked. Its building is 14 x 10 in the middle chunk (10 across, 14 deep, its door to the front, FUEL on the roof), walk-in, with a control pad in the middle that shows its water, the fuel price and the car wash. A 2 x 8 bay on each long side: the water bay (its small tank container stands in it; any tank container on the yard still counts) and the fuel tank bay (empty, for the fuel tanker to come; the fuel does not run out for now). One pump in the front chunk between the two gates, turned, with a 2 x 2 FUEL square on each side. The shop is gone from the station (no canisters, fuel pickups or fuel trailers sold there), and so are its price board and its VEHICLES area.
- Car wash: across the top half of the station's back chunk (16 x 8), walls along both sides, three brush gantries. Driven through slowly, a vehicle and its trailers lose their dirt; it takes the station's water (about 10 L a pickup, 20 a dump truck, 30 a semi, 10 a trailer, for a whole wash) and €0.50 a litre from your cash; no water or no cash, no wash.
- Dirt (only for looks): vehicles and what they pull get dirty as they drive, fast off the road, slowly on it, a bit faster with a bulk load; it shows as a brown film and mud spatter, and it is in the save.
- An older save: the station's small tank moves into its water bay; what waited on its shelves goes to the shop's aisle shelves.
- Checks: the station's layout, room and pad; dirt and the car wash (water, cash, a trailer too, nothing without water); the older-save move.

## 0.1.25 · 25 Nov 2026
- The shop's inside, as a showroom: 3 counters along its back wall instead of one pad in the middle, each opening its own part of the shop: VEHICLES + TRAILERS (Vehicles and Trailers tabs), ITEMS, and SELL. In front of them, 4 aisle shelves (1 x 5 tiles each, a wide aisle down the middle from the door) where bought items appear, 20 slots as before; the shelves on the side walls are gone. Goal hints name the counters. Check: each counter opens its own part.
- The tank container rule for every yard but a garage: a power plant, lumberyard, sawmill, quarry, iron mine, crusher, factory and foundry also get a small tank container in the corner by their gate when put down (they still start as construction sites). Each works only with water in the tank containers on its yard and drinks it by what it makes, not by time: 1 L for each thing made (a log, a t of rock, iron ore, sand or gravel, a plank, a bar, a crate or pallet), a power plant 1 L for each t of coal it burns. A yard makes only as much as its water allows: a power plant without water gives no power (its window shows its water and says so), a yard without water takes no power and makes nothing (its status says 'idle: no water in its tank'). Older saves give their yards a tank too. Check added.
- Yards that run on water: a coal mine, a shop, a fuel station and a garage placed from the Yards list are built at once and for free (no more construction sites for them). A coal mine, the shop and the fuel station come with a small tank container in their yard, in the corner by the gate, empty. They work only while the tank containers standing on their yard hold water: a coal mine digs only with water and drinks 1 L for each ton, the shop and the fuel station drink 1 L an in-game hour and are closed without water (no shop window, no fuel window, no refuelling, no fuel loading, no canisters filled). More room for water: put another tank container on the yard, or a bigger one. The coal mine's window shows its water. An older save: its sites of these four are finished and each of the three gets its tank container. Goals and How to play follow (the coal mine goal is now: fill its tank with the pump). Checks rewritten for this; the checks give every yard all the water it wants unless a check is about water.
- New game: no hose on the tap any more; 2 short hoses and a water pump lie on the floor of the house instead, beside the player. The water goal and How to play say so.
- New item: water pump (shop, Items, €300, on the NEW PURCHASES pad). 2 x 1 squares with an arrow on top. A hose (any of the 3) goes on each end, IN at the tail of the arrow and OUT at its head, the other end of each on a hatch of any liquid tank, by clicks like the tap's hose. A click on the pump switches it on or off: it moves 20 L/s from the IN tank to the OUT tank (any liquid, only into an empty tank or one with the same liquid, never over full). A middle-click (or R) turns it a quarter at a time, so the arrow points east, south, west or north. Driving a tank away pulls its hose off; with a hose on it the pump cannot be picked up. A light and a label show whether it is pumping. Checks added.
- Tank containers: the rack check now covers them too.
- Fix: an item set down on the floor of the walk-in shop (a crate, any item) was not drawn, so it seemed to go through the floor. It lay there all along and could be taken back. Check added: an item on the floor of every room is drawn.

## 0.1.24 · 25 Nov 2026
- Tank containers for liquids, in the same 3 sizes: small (2x2, 150 L, €3,500), standard (2x4, 400 L, €6,000), large (2x8, 800 L, €10,500). A liquid tank in a container frame: moved with the crane's cables like the others, filled with the hose on any of its hatches, has a hose rack, and on a flatbed of the rig it is emptied with Space (V picks the flatbed it sits on). In the shop with the containers. Checks: on every flatbed, filled at the tap, emptied on a water site's grate.
- Two more shipping containers: small (2x2, one flatbed place: pickup, small flatbed trailer and up; 5 t, €3,000) and large (2x8, four places: the semi flatbed; 20 t, €9,000). The old one (2x4, two places, 10 t, €5,000) stays. All three in the shop, with an updated description (it said they hold nothing). Checks: every container on every flatbed with room for it.
- Saving under a name that a save already has now saves over that save instead of making a second one with the same name (names match whatever the case; with several, the newest one). Check added.
- New start kit: a pickup with a water tank bed (100 L) and a hitch, and a small bulk trailer, both stored in the garage (was a cargo-bed pickup and a small water tanker). The first goals now fill the pickup's own tank at the tap.
- Fixed: inside the shop, the items you bought could not be taken off its shelves. Since the shop became a walk-in room (0.1.23) the game no longer looked at its shelves under the cursor. A click takes an item off a shelf again, a right-click puts what you hold on a free shelf place (or into a crate on it)
- Added to /check: an item bought waits on the shop's shelf, a click takes it and a right-click puts it back

## 0.1.23 · 24 Nov 2026
- Changed: the shop is walked into like the power plant, the garage and the coal mine: its room is drawn where it stands, with no jump, and you walk in and out through its door (entrance tiles inside and out). Its two shelves and the counter stay; walking onto the counter opens the shop
- Removed: the upgrade pad inside the shop, and the shop's storage (its tab was already hidden). An older save is paid for whatever was still in it
- Changed: the desks and chairs are gone from every building (the 9 production buildings and the garage house). In their place a CONTROL pad lies in the middle of each room: walk onto it and the building's window opens, as the shop's counter does; walk off and it closes. The water bill, the platforms and the vehicles' parts are now at the control pad in the house. An older save's desks and chairs are taken away
- Changed: a new player starts in the house just in front of its control pad, so its window does not open at once
- Added to /check: every building's control pad opens its window, and no desk or chair is left
- Added to /check: walking into the shop and out, the counter opening the shop, no upgrade pad; an old save's shop storage paid out

## 0.1.22 · 24 Nov 2026
- Fixed: walking into the house by the back door moved the player to another spot in the room. You now keep your place, as at the front door
- Changed: the name on the ground at a garage's gate is just the owner's name (GARAGE when it has no owner), no longer "…'s garage"
- Fixed: the hose is three clicks: click the hose to pick it up, click the tap to put it on (you hold its end), click the tanker to connect it. A right-click on the tap puts it on too. With the hose on the tap and empty hands, a click on a liquid tank in reach connects it too
- Changed: a new player starts inside the house of their garage, in the middle of the room, facing the front door (a joining player too)
- Cleaned: 67 pieces of code nothing used any more were taken out (old on-foot loading, a factory dropdown that did nothing, old drawing and layout helpers, unused values); the game is about 7 KB smaller
- Changed: the hose goes only on a hatch of a liquid tank (the round lids along its top), not anywhere on the tanker. A bigger tank has several hatches and every one of them takes the hose; the hose stays on the one it was put on, and its reach is measured to that hatch. The hose rack moved to the back of the tank, on the side away from the fill bar, clear of the hatches, the fill bar and the hitch behind it
- Changed: the hose's free end lies where it is left. Right-click with the end in hand puts it down where you point; a right-click on the connected end takes it off the tank and leaves it there; a click on a lying end takes it again. A tank driven out of reach still snaps the hose off: its end stays where the hatch was
- Fixed: after a construction site was finished, a speck of cargo (like 0.000000000001 L of water) stayed on the vehicle, still counted as its cargo. The last crumbs now come off, and a speck left by any unloading is cleared
- Removed: the bed and hitch code of the desk's parts menu (no longer offered there since 0.1.20)
- Cleaned: the last unused values went too: a counter in the multiplayer connection code that nothing read, and spare values inside the self-checks. A scan now finds nothing unused
- Added to /check: a yard touching two power plants takes from the one with the most coal and switches when the other has more
- Added to /check: the hose only on a hatch, every hatch of a several-hatch tank, its end lying where left and after driving off; no cargo left after a site is finished
- Added to /check: walking in and out by the back door, whichever way the garage is turned

## 0.1.21 · 24 Nov 2026
- Changed: the water pad behind the house is gone. The tap is one tile against the back wall of the house, in its right-hand corner, with the hose coiled beside it; park a tank within the hose's reach of it
- Added: a back door in the middle of the back wall of the house, next to the platforms: walk in and out either way. It has the 2 x 1 entrance tiles inside and outside, like the front door; nothing can be put down on them
- Changed: a garage placed from the Yards list by a player who has no finished garage stands ready at once, for free. With a finished one, a new garage is a construction site as before. So demolishing your only working garage lets you place a ready one again
- Added: a hose rack on every water tanker (the liquid bed of a pickup or dump truck, and the liquid tank trailers), at the back end of the tank. Right-click it with a hose in hand to hang the hose on it, click it to take the hose back. The hose travels with the tanker and is kept in saves
- Added to /check: the first garage standing ready, the hose rack

## 0.1.20 · 24 Nov 2026
- Fixed: the hose lying coiled by the tap (the one a new game starts with) could not be picked up. A click on it, left or right, takes it into your hands and off the tap; it lights up when the cursor is on it
- Changed: a fuel tank is no longer mounted by clicking a vehicle with it in hand. It is fitted at the desk in the house, on a stored vehicle, and only from a tank that sits in the house (on its floor or in a crate there): the Fuel tank row lists just the sizes that are there and fit. The tank is used up, costs nothing more, and brings its fuel with it; the old tank goes to the floor of the house
- Changed: the desk in the house no longer changes beds or hitches. The hitch stays an item, mounted on the back of a vehicle by hand
- Added to /check: fitting a tank from the house (none there, on the floor, in a crate)

## 0.1.19 · 24 Nov 2026
- Changed: on foot everything is done with the mouse. Left click uses or opens what is under the cursor (a desk, a sign, a crate's window, the tap, a seat) or picks up an item; with something in hand it uses it (pour a canister, mount a fuel tank, connect the hose). Right click puts what you hold where you point (the ground, a slot, a crate, a shelf, a pallet, a hitch on a vehicle, the hose on the tap) or, empty-handed, takes what you point at into your hands. Middle click turns a barrier, a sign or a desk, in your hands or on the ground (R still works)
- Changed: you carry one thing at a time; the end of the hose counts
- Changed: Space works only in vehicles. Shop and upgrade pads open when you walk onto them (Esc closes; walk off and back on to open again)
- Changed: the hose: right-click the tap to put it on, click the tap to take its end, click a tank to connect; right-click lets go of the end, right-click the tap again takes the hose off
- Changed: on touch, the big button is the hand (✋) on foot, the action button (␣) in a vehicle; R turns a barrier, sign or desk near you
- Added to /check: the hands (one thing at a time, left and right click, crates, turning)

## 0.1.18 · 24 Nov 2026
- Changed: a player starts with the pickup with a cargo bed and the small water tanker both stored in their garage, on foot next to the platforms. A joining player no longer picks a bed
- Added: a first goal, "Bring out your pickup"

## 0.1.17 · 24 Nov 2026
- Changed: the garage is a 4 x 3 chunk yard with the house in the middle. Vehicles and trailers are stored and brought out on platforms (2 at first, up to 8); what is stored is private, and each takes one of your own slots
- Changed: parts, beds and colours are changed on stored vehicles, at the desk in the house. The garage's goods storage is gone: what an older save had in it is paid out
- Added: a water tap behind the house, with hoses of different lengths to connect a tanker or a tank on a bed, and a water bill (the tap is shut at €100 unpaid)
- Changed: the coal mine, the shop and the fuel station start as construction sites too; they need only water (200, 600 and 400 L)
- Changed: a new game starts with a pickup with a hitch, a small water tanker and the shortest hose
- Added: every player has their own garage, at a random free place near the middle of the map and turned at random. Nobody else gets through its gate; the owner can let players in at the desk (Garage tab). A player who comes back to an older map without one is given one
- Added: more garages from the Yards list, as construction sites (300 L of water, 20 t of gravel, 10 planks). Only the owner or the host can demolish a garage
- Fixed: a joining player could be taken for a returning one and start without a pickup
- Added to /check: the garage, the tap, the water sites and the garages of several players

## 0.1.16 · 24 Nov 2026
- Changed: cash is each player's own, no longer one shared pot. Whoever delivers or sells is paid, whoever clicks pays; a new player starts with nothing. The host's game and saves remember what each player has and give it back when they return (an older save's shared pot goes to whoever loads it). /players shows everyone's cash
- Added: pay another player: click a player within your reach, type an amount, Pay. Both are told; a payment the other game does not confirm within 6 seconds comes back. Only in games played with a code
- Changed: € instead of $
- Fixed: the cash bar jumped about while cash was running up or down and pushed the clock around. It shows whole euros, has a fixed width and changes at most 5 times a second
- Changed: the player's name is typed in the colour window (a new game, or joining one as a new player) and nowhere else: gone from Settings, the main menu and /name
- Fixed: the main menu's 3D background stayed away when the game was opened in a hidden window

## 0.1.15 · 24 Nov 2026
- Changed: new construction sites for every building that starts as one. Only the middle chunk is under construction (foundation, materials, a barrier where the walls will stand), with a board on it that lists every material, how much has come in and how much is still to come; it always reads upright. The yard is packed earth with the trucks' tracks from the gate to the unloading place, and becomes the building's asphalt when it is finished
- Changed: every site has an unloading grate behind the building; what has been delivered lies in its hopper, each material in its colour. Logs and planks are still set down on it with the forklift. The finished power plant keeps its grate, the other buildings get their own pads
- Removed: the four building stages, the mud with its puddles, the banner, cones, tower crane and coal pile of the old sites
- Changed: the foundry needs 25 t of sand (was 20)
- Added to /check: on every site a truck delivers on the grate, and the site and the finished yard are drawn

## 0.1.14 · 24 Nov 2026
- Added: every yard that gets power lights all its pillars and gate posts, the pillars a neighbour's corner makes along its wall too, whatever its own main switch says. A power plant's pillars along a wall are lit while both corner switches of that wall are on; its corners and gate go by their switches as before
- Fixed: the power plants after the first had only the main switch; the 4 corner levers and the gate lever are back in every one
- Fixed: the crumbs around the grate of a further power plant, and the pipe of a further coal mine, were wood-coloured; they are coal
- Fixed: walking up-right or down-left did not swing the arms. The swing goes by the distance walked now, the same in every direction, for other players too
- Added to /check: every lever of a second power plant switches that plant only; the pillars lit on powered and unpowered yards; the arm swing in all 8 directions

## 0.1.13 · 24 Nov 2026
- Changed: a power plant gives power only to the yards that touch its wall. Where the two walls meet stands a shared pillar: at a corner of the plant it is live while that corner's switch is on, along a wall while both corner switches of that wall are on. One live pillar is enough; power does not go on from yard to yard. The corner switches work the lamp and the power together, the gate switch only its lamps. In older saves a yard that touches no power plant stands still until one is built against it
- Added: any number of power plants (Yards list), each its own construction site with its own coal, main switch, corner switches, desk, sign and unloading grate, kept in saves and shared in multiplayer. A yard burns the coal of the plant that feeds it; of several, the one with the most coal
- Changed: a plant's control desk lists the yards that touch it, and which switches each still needs; a building without power says why (no plant touches it, its switches are off, the plant is off, out of coal or not built)
- Changed: goals, the arrow, the help and the messages work with any power plant; the /test worlds have four, so every yard that needs power has it
- Changed: where two yards meet there is one pillar across both walls, no L up the neighbour's wall, and no second post where a gate begins right at a neighbour's corner
- Fixed: what had been delivered to a construction site could be missing from the save once that building had been demolished and built again
- Added to /check: power through corner and wall pillars (the plant turned all 4 ways), coal burnt at the right plant, several power plants (site, desk, sign, grate, save, host)

## 0.1.12 · 24 Nov 2026
- Changed: the built power plant has an unloading grate in the ground instead of the painted pad: a concrete collar with yellow and black ends, a steel frame and bars over a hopper, where the stored coal is seen, more of it the fuller the store is. Unloading works as before, in the same place; the construction site keeps its pad
- Changed: in the colour window a click only selects the colour (white ring and tick), and the new Confirm button takes it. The colour picked last time is selected to begin with
- Fixed: the colour window of a new game was hidden behind the main menu's new background
- tools/check.py presses the new Confirm button

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
