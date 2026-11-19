# Coal Haul changelog

Version numbers: every push to git adds 1 to the last number (0.1.0 → 0.1.1 → … → 0.1.10 → 0.1.100). The middle number changes only when we decide on a big step. 1.0.0 is the first release.

Saves remember the version they were made with. In multiplayer, players must be on the same version: a player on another version is turned away and asked to reload the page.

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
